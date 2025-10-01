#to search through a list in python consists of a series of a looping and or conditional statements
#basically we have to go through a series of steps to figure out what we need to search for
#you can search for both numerical and string types

# groceries = ["apple", "bananas", "grapes"]
# look_up = input("Please enter the name of the grocery item you are looking for ")

# #set some sort of search...so we basically will have to loop through a list and return a boolean as a result and then we can do something with the result

# #in a simple search we can use an if in statement that actually loops in the background, but we do not have to worry about the loop conditions
# if look_up in groceries:
#     print("Grocery item is on the list")

# else:
#     print("Grocery item is not in the list")


#Search through a list that allows me to change a balance

balances = [100.00,500.00,200.00]
find_balance = float(input("Please enter your current balance value "))

if find_balance in balances:
    print("Balance found")
    add_to_balance = float(input("How much money would you like to add to the balance "))
    #we found the balance..but how do we modify it..
    #we can grab its index
    #use the .index() function to find index of a value
    balance_index = balances.index(find_balance)
    balances[balance_index] = balances[balance_index] + add_to_balance
    print(balances)

else:
    print("Balance not found")