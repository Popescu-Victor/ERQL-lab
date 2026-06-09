// Create event

direction = random(360);
speed = 2;

// Step event

if (random(100) < 5)  // 5% chance each step
{
    direction = random(360);
}

// In a Draw event - bar chart

// Draw 3 bars
draw_set_color(c_blue);
draw_rectangle(100, 200, 140, 200 - 80, false); // bar 1, value 80
draw_rectangle(160, 200, 200, 200 - 50, false); // bar 2, value 50
draw_rectangle(220, 200, 260, 200 - 120, false); // bar 3, value 120

// Labels
draw_set_color(c_black);
draw_text(110, 210, "A");
draw_text(170, 210, "B");
draw_text(230, 210, "C");

// Detect colors:
// In Step event
var pixel_color = draw_getpixel(x, y);

if (pixel_color == c_red)
{
    // do something, e.g. take damage
    hp -= 1;
}
else if (pixel_color == c_blue)
{
    // do something else, e.g. slow down
    speed = 1;
}
else if (pixel_color == c_green)
{
    // e.g. heal
    hp += 1;
}