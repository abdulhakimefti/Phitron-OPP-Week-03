class Shopping :
    def __init__(self,customer):
        self.customer = customer
        self.items = []
        self.total = 0
    @staticmethod
    def multiply(x,y):
        return x*y
    def add_to_cart(self,item,price,quality):
        item_total = price*quality
        self.total += item_total
        self.items.append(item)

    def checkout():
        pass

result = Shopping.multiply(12,13)
print(result)