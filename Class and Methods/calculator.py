class Calculator :
    brand = 'casio'
    color='black'
    model='991 es'
    def sum(self,a,b):
        return a+b
    def biyog(self,a,b):
        return a-b
    def vaag(self,a,b):
        return a/b
    def ghun(self,a,b):
        return a*b

my_calc = Calculator()
print(my_calc.sum(54,6))