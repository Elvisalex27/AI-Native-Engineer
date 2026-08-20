def dictionary_practice ():
    product = {
        "name": "laptop",
        "price": 500000,
        "quantity": 5
    }
    
    print(product["name"]) 
    print(product["price"])

    product["quantity"] = 10
    product["brand"] = "Dell"

    for key,value in product.items():
        print(key , value)


