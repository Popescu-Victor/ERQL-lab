use rfd::FileDialog;

fn open_file() -> Option<String> {
    let file = FileDialog::new()
        .add_filter("CSV files", &["csv"])
        .set_title("Select a CSV file")
        .pick_file();

    match file {
        Some(path) => Some(path.display().to_string()),
        None => {
            println!("No file selected");
            None
        }
} }

fn main() {
    let selected_file = open_file();

    match selected_file {
        Some(path) => println!("Selected file: {}", path),
        None => println!("Exiting, no file was chosen."),
    }
}