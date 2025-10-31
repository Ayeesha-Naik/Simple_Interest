# simple_interest.py
# Program to calculate Simple Interest

def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

try:
    print("=== Simple Interest Calculator ===")
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest: "))
    time = float(input("Enter the time (in years): "))

    interest = calculate_simple_interest(principal, rate, time)

    print("\n--- Results ---")
    print(f"Principal amount: {principal}")
    print(f"Rate of interest: {rate}")
    print(f"Time (in years): {time}")
    print(f"Simple Interest = {interest}")
except ValueError:
    print("Invalid input! Please enter numeric values.")