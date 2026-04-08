namespace MyApp;

public class Form1 : Form
{
    private TextBox nameBox = new();
    private Button button = new();
    private Label label = new();
    private int count = 0;

    public Form1()
    {
        Text = "My App";  // Window title
        Width = 400;
        Height = 200;

        var promptLabel = new Label() { Text = "Your name:", Left = 10, Top = 15, Width = 80 };
        nameBox  = new TextBox() { Left = 90, Top = 10, Width = 150 };
        button   = new Button()  { Text = "Click me", Left = 10, Top = 50, Width = 100 };
        label    = new Label()   { Left = 10, Top = 90, Width = 350 };

        button.Click += OnButtonClick;  // Subscribe to the click event

        Controls.AddRange([promptLabel, nameBox, button, label]);
    }

    private void OnButtonClick(object? sender, EventArgs e)
    {
        count++;
        label.Text = $"Hello {nameBox.Text}, clicked {count} times";
    }
}