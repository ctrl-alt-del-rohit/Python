cost_price=int(input("Enter the cost of the item: "))
sell_price=int(input("Enter the selling price of the item: "))

if cost_price<sell_price:
    profit=sell_price-cost_price
    print("You've received the profit of:",profit,"Rs")
elif cost_price>sell_price:
    loss=cost_price-sell_price
    print("You've incurred a loss of:",loss,"Rs")
else:
    print("No profit and no loss")