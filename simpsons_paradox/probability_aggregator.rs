//! prob_aggregator
//!
//! Combines multiple probability estimates into a single consensus using
//! six classical and modern aggregation methods:
//!
//!   1. Arithmetic Mean
//!   2. Geometric Mean
//!   3. Log-Odds Pooling
//!   4. Trimmed Mean  (drops top/bottom 10 %)
//!   5. Extremized Pool (sharpens toward extremes, α = 1.5)
//!   6. Weighted Average (user-supplied or equal weights)
//!
//! Build:  cargo build --release
//! Usage:  ./prob_aggregator [p1 p2 p3 ...]
//!         Run with no args for the built-in demo.

// ── types ────────────────────────────────────────────────────────────────────

/// A single forecaster's estimate, optionally weighted.
#[derive(Debug, Clone, Copy)]
struct Forecast {
    p: f64,
    weight: f64,
}

impl Forecast {
    fn new(p: f64, weight: f64) -> Self {
        assert!((0.0..=1.0).contains(&p), "probability {p} not in [0, 1]");
        assert!(weight > 0.0, "weight must be positive");
        Self { p, weight }
    }
}

// ── helpers ───────────────────────────────────────────────────────────────────

const EPS: f64 = 1e-9;

fn clamp(p: f64) -> f64 {
    p.clamp(EPS, 1.0 - EPS)
}

fn logit(p: f64) -> f64 {
    let q = clamp(p);
    (q / (1.0 - q)).ln()
}

fn sigmoid(x: f64) -> f64 {
    1.0 / (1.0 + (-x).exp())
}

fn probs(forecasts: &[Forecast]) -> Vec<f64> {
    forecasts.iter().map(|f| f.p).collect()
}

// ── aggregation methods ───────────────────────────────────────────────────────

fn arithmetic_mean(forecasts: &[Forecast]) -> f64 {
    let ps = probs(forecasts);
    ps.iter().sum::<f64>() / ps.len() as f64
}

fn geometric_mean(forecasts: &[Forecast]) -> f64 {
    let n = forecasts.len() as f64;
    let log_sum: f64 = forecasts.iter().map(|f| clamp(f.p).ln()).sum();
    (log_sum / n).exp()
}

fn log_odds_pool(forecasts: &[Forecast]) -> f64 {
    let n = forecasts.len() as f64;
    let logit_sum: f64 = forecasts.iter().map(|f| logit(f.p)).sum();
    sigmoid(logit_sum / n)
}

fn trimmed_mean(forecasts: &[Forecast], trim_frac: f64) -> f64 {
    let mut ps = probs(forecasts);
    ps.sort_by(|a, b| a.partial_cmp(b).unwrap());
    let n = ps.len();
    let trim = ((n as f64 * trim_frac) as usize).min(n / 2);
    let slice = &ps[trim..n - trim];
    if slice.is_empty() {
        return arithmetic_mean(forecasts);
    }
    slice.iter().sum::<f64>() / slice.len() as f64
}

fn extremized_pool(forecasts: &[Forecast], alpha: f64) -> f64 {
    let n = forecasts.len() as f64;
    let logit_sum: f64 = forecasts.iter().map(|f| logit(f.p)).sum();
    sigmoid(alpha * logit_sum / n)
}

fn weighted_average(forecasts: &[Forecast]) -> f64 {
    let (sw, sp) = forecasts
        .iter()
        .fold((0.0_f64, 0.0_f64), |(sw, sp), f| (sw + f.weight, sp + f.weight * f.p));
    if sw > 0.0 { sp / sw } else { arithmetic_mean(forecasts) }
}

// ── display ───────────────────────────────────────────────────────────────────

fn bar(p: f64, width: usize) -> String {
    let filled = ((p * width as f64).round() as usize).min(width);
    let s: String = (0..width).map(|i| if i < filled { '#' } else { '.' }).collect();
    format!("[{s}]")
}

fn report(label: &str, p: f64) {
    println!("  {label:<28}  {p:.4}  {}", bar(p, 30));
}

fn median(ps: &[f64]) -> f64 {
    let mut sorted = ps.to_vec();
    sorted.sort_by(|a, b| a.partial_cmp(b).unwrap());
    let n = sorted.len();
    if n % 2 == 1 {
        sorted[n / 2]
    } else {
        (sorted[n / 2 - 1] + sorted[n / 2]) / 2.0
    }
}

// ── main ──────────────────────────────────────────────────────────────────────

fn main() {
    let args: Vec<String> = std::env::args().skip(1).collect();

    let forecasts: Vec<Forecast> = if args.is_empty() {
        // Built-in demo: seven forecasters on the same event
        vec![
            Forecast::new(0.20, 1.0),
            Forecast::new(0.35, 2.0),
            Forecast::new(0.40, 1.5),
            Forecast::new(0.55, 2.0),
            Forecast::new(0.60, 1.0),
            Forecast::new(0.70, 3.0),
            Forecast::new(0.80, 1.5),
        ]
    } else {
        args.iter()
            .map(|s| {
                let p: f64 = s.parse().unwrap_or_else(|_| {
                    eprintln!("Error: '{s}' is not a valid number");
                    std::process::exit(1);
                });
                if !(0.0..=1.0).contains(&p) {
                    eprintln!("Error: '{p}' is not in [0, 1]");
                    std::process::exit(1);
                }
                Forecast::new(p, 1.0)
            })
            .collect()
    };

    // ── print inputs ──────────────────────────────────────────────────────────
    println!("\n=== Probability Aggregator ===\n");
    println!("Input estimates ({} forecasters):", forecasts.len());
    for (i, f) in forecasts.iter().enumerate() {
        println!("  Forecaster {:>2} : {:.4}  (weight {:.1})", i + 1, f.p, f.weight);
    }

    // ── summary stats ─────────────────────────────────────────────────────────
    let ps = probs(&forecasts);
    let mut sorted_ps = ps.clone();
    sorted_ps.sort_by(|a, b| a.partial_cmp(b).unwrap());

    println!();
    println!("  Min    : {:.4}", sorted_ps.first().unwrap());
    println!("  Median : {:.4}", median(&ps));
    println!("  Max    : {:.4}", sorted_ps.last().unwrap());

    // ── aggregation results ───────────────────────────────────────────────────
    println!("\nAggregated probabilities:\n");
    report("Arithmetic Mean",        arithmetic_mean(&forecasts));
    report("Geometric Mean",         geometric_mean(&forecasts));
    report("Log-Odds Pool",          log_odds_pool(&forecasts));
    report("Trimmed Mean (10%)",     trimmed_mean(&forecasts, 0.10));
    report("Extremized (alpha=1.5)", extremized_pool(&forecasts, 1.5));
    report("Weighted Average",       weighted_average(&forecasts));
    println!();
}

// ── unit tests ────────────────────────────────────────────────────────────────

#[cfg(test)]
mod tests {
    use super::*;

    fn fc(ps: &[f64]) -> Vec<Forecast> {
        ps.iter().map(|&p| Forecast::new(p, 1.0)).collect()
    }

    #[test]
    fn arithmetic_mean_symmetric() {
        let f = fc(&[0.2, 0.8]);
        assert!((arithmetic_mean(&f) - 0.5).abs() < 1e-10);
    }

    #[test]
    fn geometric_mean_below_arithmetic() {
        let f = fc(&[0.2, 0.8]);
        assert!(geometric_mean(&f) < arithmetic_mean(&f));
    }

    #[test]
    fn log_odds_pool_symmetric_is_half() {
        let f = fc(&[0.2, 0.8]);
        assert!((log_odds_pool(&f) - 0.5).abs() < 1e-10);
    }

    #[test]
    fn extremized_sharpens() {
        let f = fc(&[0.6, 0.7, 0.8]);
        assert!(extremized_pool(&f, 1.5) > log_odds_pool(&f));
    }

    #[test]
    fn weighted_average_skews_toward_high_weight() {
        let forecasts = vec![
            Forecast::new(0.1, 1.0),
            Forecast::new(0.9, 9.0),
        ];
        let wa = weighted_average(&forecasts);
        let am = arithmetic_mean(&forecasts);
        assert!(wa > am, "wa={wa} should be > am={am}");
    }

    #[test]
    fn trimmed_mean_removes_extremes() {
        let f = fc(&[0.01, 0.5, 0.5, 0.5, 0.5, 0.5, 0.99]);
        let tm = trimmed_mean(&f, 0.10);
        let am = arithmetic_mean(&f);
        assert!((tm - 0.5).abs() <= (am - 0.5).abs() + 1e-10);
    }

    #[test]
    fn clamp_keeps_finite_logit() {
        assert!(logit(EPS).is_finite());
        assert!(logit(1.0 - EPS).is_finite());
    }
}
