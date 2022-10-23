class Shopper :
    def __init__(self,name):
        self.name = name
        self.cart = []
    def add_to_cart(self,item,price,quantity):
        self.cart.append({'name':item,'price':price,'quantity':quantity})
    def checkout(self,amount):
        # print(self.cart)
        price = 0
        for item in self.cart:
            price += (item['price']*item['quantity'])
        # print(price)
        if amount<price :
            print(f'please give us more money:{price-amount}')
        elif amount>price:
            price(f'please take back;{amount-price}')


shopping = Shopper('Efti')
shopping.add_to_cart('shirt',1200,3)
shopping.add_to_cart('shoes',2300,4)
shopping.add_to_cart('pant',3900,5)

shopping.checkout(10000)