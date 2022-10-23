class Phone :
    manufactured = 'China'
    def __init__(self,brand,price,color):
        self.brand = brand
        self.price = price
        self.color = color
    def call(self):
        print("ring ring ring")

my_phone = Phone('Iphone',100000,'black')
her_phone = Phone('Samsung',45000,'white')
print(my_phone.brand,her_phone.brand,my_phone.price,her_phone.price)
