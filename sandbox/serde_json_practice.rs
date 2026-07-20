use serde_json::Value;
use std::fs;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let data = fs::read_to_string("data.json")?;
    let v: Value = serde_json::from_str(&data)?;

    println!("{}", v["name"]);
    if let Some(age) = v["age"].as_u64() {
        println!("Age: {}", age);
    }
    Ok(())
}