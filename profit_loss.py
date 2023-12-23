# Ques) If the cost price and selling price of an item is input through the keyboard, write a program to determine whether the seller has made profit or incurred loss or no profit no loss. also determine how much profit he made or loss he incurred.

cost_price=int(input("Enter the cost price of the item:"))
selling_price=int(input("Enter the selling price of the item:"))

# If selling price is more than cost price - Profit.
if cost_price<selling_price:
	profit=selling_price - cost_price
	print("We have made the profit of:",profit)

# If selling price is less than cost price - Loss.
elif cost_price>selling_price:
	loss=cost_price - selling_price
	print("We have incurred the loss of:",loss)

# If selling price is equal to  cost price - No profit no loss.
else:
	print("We have neither made any profit nor incurred any loss.")
