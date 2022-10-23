class Person :
    def __init__(self,name,age,money):
        self.name= name
        self.age =age
        self.money= money
    def __add__(self,other):
        return self.age + other.age
    def __call__(self):
        print (f'My name is {self.name} and my age is {self.age} and i have {self.money} taka')
    def __eq__(self,other):
        return self.age==other.age
    def __len__(self):
        return self.age
alim =  Person('alim',16,560)
dalim = Person ('dalim',17,8473)
print(alim+dalim)
alim()
print(dalim==alim)
print(len(alim))