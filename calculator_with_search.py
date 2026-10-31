import math


def _read_number(prompt):
    while True:
        try:
            number = float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if not math.isfinite(number):
            print("Please enter a finite number.")
            continue

        return number


def _format_number(number):
    if number.is_integer():
        return f"{number:.0f}"
    return str(number)


def basic_calculate():
    """Calculate one basic arithmetic expression and display the result."""
    first_number = _read_number("Enter the first number: ")

    while True:
        operator = input("Choose an operation (+, -, *, /): ").strip()
        if operator in {"+", "-", "*", "/"}:
            break
        print("Please choose +, -, *, or /.")

    second_number = _read_number("Enter the second number: ")

    if operator == "+":
        result = first_number + second_number
    elif operator == "-":
        result = first_number - second_number
    elif operator == "*":
        result = first_number * second_number
    elif operator == "/":
        if second_number == 0:
            print("Cannot divide by zero.")
            return None
        result = first_number / second_number

    print(
        f"{_format_number(first_number)} {operator} "
        f"{_format_number(second_number)} = {_format_number(result)}"
    )
    return result


def solve_for_x():
    print("Solve an equation in the form ax + b = c.")
    a = _read_number("Enter a (the coefficient of x): ")
    b = _read_number("Enter b (the constant on the left): ")
    c = _read_number("Enter c (the right side): ")

    equation = (
        f"{_format_number(a)}x "
        f"{'+' if b >= 0 else '-'} {_format_number(abs(b))} "
        f"= {_format_number(c)}"
    )
    print(f"\nEquation: {equation}")

    if a == 0:
        if b == c:
            print("This equation is true for every value of x (infinitely many solutions).")
        else:
            print("This equation has no solution.")
        return

    right_side = c - b
    solution = right_side / a
    print(f"Subtract {_format_number(b)} from both sides:")
    print(f"{_format_number(a)}x = {_format_number(right_side)}")
    print(f"Divide both sides by {_format_number(a)}:")
    print(f"x = {_format_number(right_side)} / {_format_number(a)}")
    print(f"x = {_format_number(solution)}")


def equation_solver_menu():
    """Show the linear-equation solver menu."""
    while True:
        print("\nEquation Solver")
        print("1. Solve a linear equation (ax + b = c)")
        print("2. Return to the main menu")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            solve_for_x()
        elif choice == "2":
            return
        else:
            print("Please choose 1 or 2.")


def visualize_search():
    """Display an ASCII graph of a linear function over a fixed x range."""
    print("Graph a linear function in the form y = mx + b.")
    slope = _read_number("Enter the slope (m): ")
    intercept = _read_number("Enter the y-intercept (b): ")

    width = 41
    height = 21
    x_values = [-10 + column * 20 / (width - 1) for column in range(width)]
    y_values = [slope * x + intercept for x in x_values]

    if not all(math.isfinite(value) for value in y_values):
        print("These values are too large to graph.")
        return

    y_min = min(min(y_values), 0)
    y_max = max(max(y_values), 0)
    if y_min == y_max:
        y_min, y_max = -1, 1

    def y_to_row(value):
        return round((y_max - value) * (height - 1) / (y_max - y_min))

    graph = [[" " for _ in range(width)] for _ in range(height)]
    x_axis_row = y_to_row(0)
    y_axis_column = width // 2

    for column, value in enumerate(y_values):
        graph[y_to_row(value)][column] = "*"

    for column in range(width):
        if graph[x_axis_row][column] == " ":
            graph[x_axis_row][column] = "-"
    for row in range(height):
        if graph[row][y_axis_column] == " ":
            graph[row][y_axis_column] = "|"
    if graph[x_axis_row][y_axis_column] != "*":
        graph[x_axis_row][y_axis_column] = "+"

    print(
        f"\ny = {_format_number(slope)}x "
        f"{'+' if intercept >= 0 else '-'} {_format_number(abs(intercept))}"
    )
    for row, cells in enumerate(graph):
        y_label = y_max - row * (y_max - y_min) / (height - 1)
        print(f"{y_label:8.2f} |{''.join(cells)}")
    print(f"         x ranges from {x_values[0]:g} to {x_values[-1]:g}")


def main():
    while True:
        print("\nSmart Calculator")
        print("1. Basic calculation")
        print("2. Equation solver")
        print("3. Visualize a linear function")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            basic_calculate()
        elif choice == "2":
            equation_solver_menu()
        elif choice == "3":
            visualize_search()
        elif choice == "4":
            print("Goodbye!")
            return
        else:
            print("Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
