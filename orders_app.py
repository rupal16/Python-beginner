cart = {}

items_price = {
    "pizza" : {
        "1 large pizza " : 10.99,
        "2 large pizza " : 20.99,
        "3 large pizza " : 29.99,
    },
    "pasta" : {
        "1 large pasta " : 9.5,
        "2 large pastas " : 17.00,
        "3 large pastas " : 27.50,
    }
}

def order_items():

    print("What do  you want to order?\n1) Pizza(s)\n2) Pasta(s)\n3) Go back")

    choice = int(input().strip())

    if choice == 1 :
        order_submenu(items_price['pizza'])

    elif choice == 2 :
        order_submenu(items_price['pasta'])

    else:
        print("\n")

def order_submenu(items):

    global cart

    print("Choose the desired option:")

    keys = list(items.keys())

    for index,key in enumerate(keys):
        print(str(index+1)+") "+key + "\t" + str(items[key]) + " AUD")

    print(str(len(keys)+1) + ") Go back.")

    choice = int(input().strip())

    if choice > 0 and choice <= len(keys):

        if keys[choice-1] in cart.keys():

            cart[keys[choice-1]] = cart[keys[choice-1]] + 1
        
        else:

            cart[keys[choice-1]] = 1

    elif choice == len(keys)+1:

        print("\n")
        return

    else:

        print("Invalid entry. Please try again.")

        order_submenu(items)


def get_item_cost(item):

    global items_price

    if "pizza" in item:

        return items_price["pizza"][item]
    
    else:

        return items_price["pasta"][item]


def get_order_summary():

    global cart

    if len(cart) == 0:

        print("Your shopping cart is empty\n")
        #FCALL
        return

    print('-'*len("Order Summary")+"\n"+"Order Summary\n"+'-'*len("Order Summary")+"\n")

    count = {
        "pizza" : 0,
        "pasta" : 0,
    }

    cost = {
        "pizza" : 0,
        "pasta" : 0,
    }

    for item in cart.keys():

        item_cost = get_item_cost(item)

        item_count = cart[item]

        current_cost = item_cost * item_count

        print("{} * {} pc(s)\t{} AUD".format(item,item_count,current_cost))

        if "pizza" in item:

            count["pizza"] += item_count * int(item[0])
            cost["pizza"] += current_cost
        
        elif "pasta" in item:

            count["pasta"] += item_count * int(item[0])
            cost["pasta"] += current_cost


    if count["pizza"] >= 4 or count["pasta"] >= 4:
        print("\n\n[Additional free items]\n")
    else:
        print("\n")
    
    if count["pizza"] >= 4 and count["pasta"] >= 4:

        free_item_count = min(count["pizza"]/4,count["pasta"]/4)

        print("Choco brownie ice cream \t {}".format(2*free_item_count))
        print("1.5lt Soft drink        \t {}".format(free_item_count))
        print("1 plate bruschetta      \t {}".format(free_item_count))

    else:

        if count["pizza"] > 4:
            print("1.5lt Soft drink        \t {}".format(1))
        if count["pasta"] > 4:
            print("1 plate bruschetta      \t {}".format(1))


    print("-"*len("Order Summary"))
    print("-"*len("Order Summary")+"\n")

    print("Total pizza cost : {} AUD \t {} pcs".format(cost['pizza'],count['pizza']))
    print("Total pasta cost : {} AUD \t {} pcs".format(cost['pasta'],count['pasta']))

    print("-"*len("Order Summary"))
    print("-"*len("Order Summary")+"\n")

    print("Total cost : {} AUD".format(cost["pizza"] + cost["pasta"]))

    print("\n\n")
    #FCALL


def start_app():

    while True:
        print("1. Order Food\n2. View order summary\n3.Quit\n")

        choice = int(input().strip())

        if choice == 1:

            order_items()
        
        elif choice == 2:

            get_order_summary()

        elif choice == 3:

            print("Thank you for using our app")
            break

        else:

            print("Invalid Input")


if __name__ == '__main__':

    print("Welcome to the food ordering app")
    start_app()
