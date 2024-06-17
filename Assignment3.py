import math

def volume_of_cube(side):
    if side <= 0:
        raise ValueError("Side length must be positive")
    return side ** 3
def volume_of_sphere(radius):
    if radius <= 0:
        raise ValueError("Radius must be positive")
    return (4/3) * math.pi * radius ** 3
def volume_of_cylinder(radius,height):
    if radius <=0:
        raise  ValueError("Radius must be positive")
    if height <=0:
        raise  ValueError("Height must be positive")
    return math.pi * radius ** 2 * height
def get_positive_float(prompt):
    while True:
        try:
            value=float(input(prompt))
            if value <=0:
                raise ValueError
            return value
        except ValueError:
            print("Invalid input")
def main():
    while True:
        print("\n Volume Calculator")
        print("-"*20)
        print("1.Cube")
        print("2.Sphere")
        print("3.Cylinder")
        print("4.Exit")

        choice = input("Select any option = ")
        if choice=='1':
            print("\nCube")
            side=get_positive_float("Enter the side = ")
            try:
                volume=volume_of_cube(side)
                print(f"The volume of cube is = {volume:2f}")
            except ValueError as e:
                print(f"Error:{e}")
        elif choice=='2':
            print("\nSphere")
            radius=get_positive_float("Enter the radius = ")
            try:
                volume=volume_of_sphere(radius)
                print(f"The volume of Sphere = {volume:2f}")
            except ValueError as e:
                print(f"Error:{e}")
        elif choice=='3':
            print("\nCylinder")
            radius=get_positive_float("Enter the radius = ")
            height=get_positive_float("Entere the height = ")
            try:
                volume=volume_of_cylinder(radius,height)
                print(f"Volume of Cylinder = {volume:2f}")
            except ValueError as e:
                print(f"Error:{e}")
        elif choice=='4':
            print("Exiting")
            break
        else:
            print("Invalid Choice")
if __name__=="__main__":
    main()