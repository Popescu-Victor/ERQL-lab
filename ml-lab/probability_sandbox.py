from functools import reduce

def probability_any_independent(probabilities):
    return 1 - reduce(lambda acc, p: acc * (1 - p), probabilities, 1.0)


def probability_all_independent(probabilities):
    return reduce(lambda acc, p: acc * p, probabilities, 1.0)


def probability_disjoint(probabilities):
    return sum(probabilities)



events = {
    "click": [0.10, 0.15, 0.20],
    "purchase": [0.03, 0.05],
    "signup": [0.08, 0.12]
}


aggregated = {
    event_type: probability_any_independent(probs)
    for event_type, probs in events.items()
}

print("Per-type probabilities:")
for event_type, prob in aggregated.items():
    print(f"{event_type}: {prob:.4f}")


overall = probability_any_independent(list(aggregated.values()))
print(f"\nOverall probability: {overall:.4f}")