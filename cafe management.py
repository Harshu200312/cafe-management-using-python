
dict1= {
    "coffee": 100,
    "tea": 50,
    "pasta": 150,
    "pizza": 200,
    "burger": 300
}
print("Welcome to our cafe management system!!!!")
print("Order items that you want -")

def menu():
    print("------ MENU CARD ----------")
    for items,price in dict1.items():
        print(f" {items}: {price} RS")

def main (order,quantity,order_items):
    if order in dict1:
        total_price=(quantity) *dict1[order]
        print(f" You ordered {order}  Quantity={quantity}  price :{total_price} RS")
        order_items.append((order,quantity,total_price))

        return total_price
    
    else:
        print("Sorry that item is not available on menu..")
        return 0

    

def bill():
    order_items=[]
    total_bill=0
    while True:
        menu()
        order=input("What do you want ? : ")
        try:
            quantity = int(input("How many quantities do you want? : "))
            if quantity <= 0:
                print("Please enter a positive number for quantity.")
                continue
        except ValueError:
            print("Please enter a valid number for quantity.")
            continue

        total_bill += main(order,quantity,order_items)
        
        again=input("Do you want to order anything else.(y=Yes,n=No): ").lower()
        if again != "y":
            break
    
    
    print(f"YOU ordered:")

    for items,quantity,price in order_items:
        print(f"-- {items}: No:{quantity} Price :{price} RS")
        
    print(f"Your total bill is : {total_bill}")
    print("===========================")
    print("THANK YOU FOR VISITING !!!!")

bill()
