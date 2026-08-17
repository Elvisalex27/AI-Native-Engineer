inventory = {}

def Add_Products():
    Product_name = input("Enter name of product: ")
    product_price = int(input("Enter the price of the product: "))
    product_quantity = int(input("how many do you want: "))
    inventory[Product_name] = {
        "price": product_price,
        "quantity": product_quantity
    }
    print("products successfully added")


def View_products():
    for product,detials in inventory.items():
        print(f"{product}\n price : {detials['price']}\n quantity: {detials['quantity']}")

def Update_Quanity():
    new_product = input("Enter the name of the new product:  ")
    new_quantity = input("Enter the quantity of the new product: ")
    inventory[new_product]["quantity"] = new_quantity
  
def Delete_Product():
    deleted_product = input("Enter the name of the product to ne deleted: ")
   
    if deleted_product in inventory:
        del inventory[deleted_product]
        print(f"{deleted_product} has been removed")
    else:
        print("product deosn't exist")

def Total_Stock_Value():
    total = 0
    for product, detials in inventory.items():
       
        stock_value = detials["price"] * detials["quantity"]
        total += stock_value
    print(f"the total stock value of the inventory is {total}")

while True:
    print("1. Add Product\n2. View Product\n3. Update Quantity\n4.Delete Product\n5. Show Total Stock Value\6. Exit")

    question = input("Choose a number: ")
    if question == "1":
        Add_Products()

    elif question == "2":
        View_products()

    elif question == "3":
        Update_Quanity()

    elif question == "4":
        Delete_Product()

    elif question == "5":
        Total_Stock_Value()

    elif question == "6":
        print("Goodbye")
        break



