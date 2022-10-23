class Shop :
    cart = []
    def __init__(self,buyer):
        self.buyer = buyer
    def add_to_cart(self,item):
        self.cart.append(item)
    
shopper_1 = Shop('efti')
shopper_1.add_to_cart('tshirt')
print(shopper_1.cart)