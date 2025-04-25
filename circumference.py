import math

def find_circumference(radius):
    """Returns the circumference of a circle given the radius."""
    return 2 * math.pi * radius

if __name__ == "__main__":
    r = float(input("Enter the radius: "))
    circumference = find_circumference(r)
    print(f"Circumference of the circle is: {circumference:.2f}")
