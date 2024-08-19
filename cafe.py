#i want create a cafe program with at least four products on sale
#then i want to calculate the number of items in stock 
#below is a cafe list and the cafe dictionary
cafe_list = ["Coffee","Donuts","Tea","Cakes","Crossient"]
cafe_stock = { "Coffee": 100,"Donuts": 100,"Tea": 350,"Cakes": 50,"Crossient":100 }
cafe_prices ={"Coffee": 5.00,"Donuts": 2.50,"Tea":2.50, "Cakes": 3.50, "Crossient":3.00}
#below is the calculation for total of stock
stock_total = 0.0
for food in cafe_list:
    stock_total+=cafe_stock[food]*cafe_prices[food]
print(stock_total) 