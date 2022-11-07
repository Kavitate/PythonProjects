# Ground Shipping
while True:
  entered_weight = input("Enter total weight (lbs): ")
  weight = float(entered_weight)
  if weight <= 2:
    print("Ground: $" , weight * 1.50 + 20.00)
  elif weight <= 6:
    print("Ground: $" , weight * 3.00 + 20.00)
  elif weight <= 10:
    print("Ground: $" , weight * 4.00 + 20.00)
  elif weight > 10:
    print("Ground: $" , weight * 4.75 + 20.00)
  else:
    print("Error.")

#Ground Shipping Premium
  ground_shipping_premium = 125.00
  print("Ground Shipping Premium: $" , ground_shipping_premium)

# Premium Shipping
  if weight <= 2:
    print("Premium Shipping: $" , weight * 4.50)
  elif weight <= 6:
    print("Premium Shipping: $" , weight * 9.00)
  elif weight <= 10:
    print("Premium Shipping: $" , weight * 12.00)
  elif weight > 10:
    print("Premium Shipping: $" , weight * 14.25)
  else:
    print("Error.")

  input('\nPress ENTER to calcualte again.')
  import os
  os.system('cls' if os.name == 'nt' else "printf '\033c'")
