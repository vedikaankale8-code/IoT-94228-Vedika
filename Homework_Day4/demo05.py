tons_to_kg = lambda tons: tons * 1000
kg_to_grams = lambda kg: kg * 1000
grams_to_mg = lambda grams: grams * 1000
mg_to_pounds = lambda mg: mg * 2.20462e-6 
   
tonnes_input = float(input("Enter weight in tonnes (e.g., 0.002): "))

kilograms = tons_to_kg(tonnes_input)
grams = kg_to_grams(kilograms)
milligrams = grams_to_mg(grams)
pounds = mg_to_pounds(milligrams)

print(f"\n{tonnes_input} tonnes is equal to:")
print(f"*   {kilograms:} kg")
print(f"*   {grams:} gm")
print(f"*   {milligrams:} mg")
print(f"*   {pounds:} lbs")

