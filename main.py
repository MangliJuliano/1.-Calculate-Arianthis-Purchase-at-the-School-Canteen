price = float(input("Enter the price of the product: "))
money = float(input("Enter the amount of money Arianthis has: "))

if money >= price:
    print("Arianthis can buy the product.")
    print("Change:", money - price)
else:
    print("Arianthis does not have enough money.")
    print("She needs", price - money, "more.")
