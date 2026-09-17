def calculate_bmi(weight: float, height: float) -> float:
    """
    Calculate the Body Mass Index (BMI).

    Formula:
        BMI = weight / (height^2)

    Parameters:
        weight (float): Weight in kilograms
        height (float): Height in meters

    Returns:
        float: The calculated BMI value
    """
    return weight / height**2


def get_bmi_category(bmi: float) -> str:
    """
    Determine the BMI category based on the calculated value.

    Categories:
        - Underweight: BMI < 18.5
        - Normal weight: 18.5 <= BMI <= 24.9
        - Overweight: 25 <= BMI <= 29.9
        - Obesity: BMI >= 30

    Parameters:
        bmi (float): The BMI value

    Returns:
        str: The health category as a string
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal weight"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obesity"


def cli():
    """
    Command Line Interface (CLI) for the BMI Calculator.

    - Greets the user with a header.
    - Continuously prompts for weight and height until valid inputs are given.
    - Ensures inputs are numeric and greater than zero.
    - Displays the BMI rounded to two decimal places.
    - Also shows the corresponding health category.
    """
    print(f"{'#'*10} BMI Calculator {'#'*10}")

    while True:
        try:
            # Ask the user for weight and height
            weight = float(input("Enter the weight in kilograms: "))
            height = float(input("Enter the height in meters: "))
        except ValueError:
            # Handle non-numeric input
            print("Weight/height must be numbers. Please try again.")
            continue

        # Validate positive values
        if weight <= 0 or height <= 0:
            print("Weight/height must be larger than zero. Please try again.")
            continue

        # Perform BMI calculation
        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)

        # Display result formatted to 2 decimal places with category
        print(f"Your BMI is {bmi:.2f}")
        print(f"Category: {category}")
        break


if __name__ == "__main__":
    """
    Entry point of the program.
    When the script is run directly, start the CLI.
    """
    cli()
