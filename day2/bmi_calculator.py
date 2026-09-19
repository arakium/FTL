def calculate_bmi(weight, height):
    """Return the BMI rounded to two decimals (weight in kg, height in m)."""
    return round(weight / height**2, 2)


def get_bmi_category(bmi):
    """Return the health category for a BMI value."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obesity"


def cli():
    print("########## BMI Calculator ##########")

    while True:
        weight_unit = input("Weight unit ('kg' or 'lb'): ").lower()
        height_unit = input("Height unit ('m' or 'in'): ").lower()

        if weight_unit not in ("kg", "lb") or height_unit not in ("m", "in"):
            print("Invalid unit. Please try again.")
            continue

        try:
            weight = float(input("Enter your weight: "))
            height = float(input("Enter your height: "))
        except ValueError:
            print("Weight and height must be numbers. Please try again.")
            continue

        if weight <= 0 or height <= 0:
            print("Weight and height must be larger than zero. Please try again.")
            continue

        # Convert to kilograms and meters if needed
        if weight_unit == "lb":
            weight = weight / 2.20462
        if height_unit == "in":
            height = height / 39.3701

        bmi = calculate_bmi(weight, height)
        print(f"Your BMI is {bmi}")
        print(f"Category: {get_bmi_category(bmi)}")
        break


if __name__ == "__main__":
    cli()