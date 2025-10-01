#lets create a program where we can search through a list of data, and the modify it after searching
#this will be a product inventory application (like an amazon warehouse or amazon website)
#we will have a list of product ids, prices, names, and stock (quantity on hand)

product_ids = ["P001","P002","P003"]
product_names = ["Laptop","Mouse","Keyboard"]
product_prices = [1200.00,22.95,30.00]
product_stock = [10,50,20]


search_id = input("Please enter a id of the product you wish to lookup ")

#we will just do a simple while true break...you can also create a flag

while True:
    if search_id in product_ids:
        #after searching through the ids we can grab its index and modify anything associated with that id
        index = product_ids.index(search_id)
        print("Your products name is", product_names[index])
        buying_qty = int(input("How many items of this product do you wish to buy? "))
        product_stock[index] = product_stock[index] - buying_qty
        print("Your product stock is", product_stock[index])
        break
    else:
        print("Product was not found")
        search_id = input("Please enter a valid product ID")

print("Here is an updated list of all products and prices")
print("ID  Name  Prices  Stock")

for i in range(len(product_ids)):
    print(product_ids[i],product_names[i],product_prices[i],product_stock[i])