class Shopping :
    mall = 'jamuna future park'
    hours= 14
    def __init__(self,customer):
        self.customer = customer
        self.item = []
        self.total=0
        
    @classmethod
    def mallName(cls):
        return cls.mall
    @staticmethod
    def multiply(x,y):
        return x*y
    def add_to_cart(self,item,price,quality):
        item_total = price*quality
        self.total += item_total
        self.items.append(item)

print(Shopping.mallName())