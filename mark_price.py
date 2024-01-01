# Accept the mark price from the user and calculate the net ammount to pay according to following criteria:
# Marked price            discount
# >10000                  20%
# >7000 and <=10000       15%
# <=7000                  10%
# Solution-

mark_price=float(input("Enter the mark price of the item:"))
if mark_price>10000:
	discount=mark_price*(20/100)
	net_ammount=mark_price-discount
	print(net_ammount)
elif mark_price>7000 and mark_price<=10000:
	discount=mark_price*(15/100)
	net_ammount=mark_price-discount
	print(net_ammount)
else:
	discount=mark_price*(10/100)
	net_ammount=mark_price-discount
	print(net_ammount)