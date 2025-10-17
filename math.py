#math.py
try:
  a = float(input("Enter first number: "))
  b = float(input("Enter second number: "))

  print(F"Addition: {a + b}")
  print(F"Substraction:  {a - b}")

except ValueError:
  print("please enter valid number.")
