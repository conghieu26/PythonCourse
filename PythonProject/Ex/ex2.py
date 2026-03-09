# Exercise 2 Shopping Cart Program


item = input("What item would you like to buy? ")
price = float(input("What is the price? $"))
quantity = int(input("How many would you like? "))
total_price = price * quantity

print(f"You have bought {quantity} {item}")
print(f"The total price is {total_price}")
