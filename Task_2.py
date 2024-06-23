import turtle

def draw_koch_segment(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        length /= 3.0
        draw_koch_segment(t, length, depth-1)
        t.left(60)
        draw_koch_segment(t, length, depth-1)
        t.right(120)
        draw_koch_segment(t, length, depth-1)
        t.left(60)
        draw_koch_segment(t, length, depth-1)

def draw_koch_snowflake(t, length, depth):
    for _ in range(3):
        draw_koch_segment(t, length, depth)
        t.right(120)

def main():
    try:
        depth = int(input("Enter the recursion level: "))
    except ValueError:
        print("Recursion level must be an integer.")
        return

    # Setup the turtle environment
    window = turtle.Screen()
    window.title("Koch Snowflake")

    t = turtle.Turtle()
    t.speed(0)  # Fastest speed

    # Initial length of the triangle side
    length = 300

    # Position turtle to start drawing
    t.penup()
    t.goto(-length / 2, length / (2 * 3**0.5))
    t.pendown()

    # Draw the Koch snowflake
    draw_koch_snowflake(t, length, depth)

    # Complete drawing
    turtle.done()

if __name__ == "__main__":
    main()
