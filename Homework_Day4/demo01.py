def km_to_m(distance):
    return distance*1000
def m_to_cm(distance):
    return distance*100
def cm_to_mm(distance):
    return distance*10
def feet_to_inch(distance):
    return distance*12
def inch_to_cm(distance):
    return distance*2.54
def converter(distance, con_type, con_func):
   
    result = con_func(distance)
    print(f"{distance} {con_type} = {result}")

if __name__ == "__main__":

        input = float(input("Enter a distance (number): "))
        conversions = [
            ("kilometers to meters", km_to_m),
            ("meters to centimeters", m_to_cm),
            ("centimeters to millimeters", cm_to_mm),
            ("feets to inches", feet_to_inch),
            ("inches to centimeter", inch_to_cm)
        ]
        print(f"\nPerforming conversions for initial distance of {input}:")
        
        for description, func in conversions:
            converter(input, description, func)
