# BMI Calculator (Primitive Version)

while True:
    try:
        # Ask the user for weight and height
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
    except ValueError:
        # Handle non-numeric input
        print("Weight and height must be numbers. Please try again.")
        continue

    # Validate positive values
    if weight <= 0 or height <= 0:
        print("Weight and height must be larger than zero. Please try again.")
        continue

    # Calculate BMI
    bmi = weight / (height ** 2)

    # Print BMI value
    print(f"Your BMI is {bmi:.2f}")

    # Determine health category
    if bmi < 18.5:
        print("Category: Underweight")
    elif 18.5 <= bmi <= 24.9:
        print("Category: Normal weight")
    elif 25 <= bmi <= 29.9:
        print("Category: Overweight")
    else:
        print("Category: Obesity")

    break
