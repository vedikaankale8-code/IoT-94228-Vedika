import geomatry as g

print("1. Area of Circle")
print("2. Area of Rectangle")

choice = int(input("Enter your choice : "))

if choice == 1:
    r = float(input("Enter radius of the circle: "))
    print(f"Area of Circle: {g.area_circle(r)}")

else:
    l = float(input("Enter length of the rectangle: "))
    b = float(input("Enter breadth of the rectangle: "))
    print(f"Area of Rectangle: {g.area_rectangle(l, b)}")


