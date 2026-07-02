use std::io::{self, Write};

mod scripts;

fn main() {
    loop {
        print!(">> ");
        io::stdout().flush().unwrap();

        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();

        let command = input.trim();

        match command {
            "plot" => scripts::plot(),
            "analyze" => scripts::analyze(),
            "convert" => scripts::convert(),
            "exit" | "quit" => {
                println!("Goodbye!");
                break;
            }
            "" => {}
            _ => println!("Unknown command. Type 'help'."),
        }
    }
}