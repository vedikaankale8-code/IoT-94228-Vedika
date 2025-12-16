km_to_m=lambda distance :distance*1000
m_to_cm=lambda distance :distance*100
cm_to_mm=lambda distance :distance*10
feet_to_inch=lambda distance :distance*12
inch_to_cm=lambda distance:distance*2.54

def converter(distance,con_type,con_fun):
    result=con_fun(distance)
    print(f"{con_type}{distance}=result")

if __name__ == "__main__":

        input = float(input("Enter a distance (number): "))
        conversions = [
            ("km to m", km_to_m),
            ("m to cm", m_to_cm),
            ("cm to mm", cm_to_mm),
            ("feets to inche", feet_to_inch),
            ("inche to cm", inch_to_cm)
        ]
        print(f"\nPerforming conversions for initial distance of {input}:")
        
        for description, func in conversions:
            converter(input, description, func)
    
