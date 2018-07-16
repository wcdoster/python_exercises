stock_dict = {"GM": "General Motors", "CAT": "Caterpiller", "MSFT": "Microsoft", "AAPL": "Apple"}

purchases = [("GM", 100, '5-july-2018', 25),
("CAT", 30, "15-june-2018", 60),
("MSFT", 60, "2-apr-2018", 30),
("AAPL", 20, "4-may-2018", 70),
("AAPL", 30, "5-june-2018", 65)]

purchase_history = []

for purchase in purchases:
    item = (stock_dict[purchase[0]], purchase[1]*purchase[3])
    purchase_history.append(item)

purchase_total = {}

for purchase in purchase_history:
    if purchase[0] not in purchase_total:
        purchase_total[purchase[0]] = purchase[1]
    else:
        purchase_total[purchase[0]] += purchase[1]

print(purchase_history)
print(purchase_total)
