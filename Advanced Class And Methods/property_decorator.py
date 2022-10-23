class User :
    def __init__(self,f_name,l_name):
        self.first = f_name
        self.last = l_name
        self.email = f'{self.first}.{self.last}@user.com'
    @property
    def get_email(self):
        return self.email
    @property
    def full_name(self):
        return f'{self.first} {self.last}'
    @full_name.setter
    def full_name(self,value):
        self.first = value.split(' ')[0]
        self.last = value.split(' ')[1]
    @full_name.deleter
    def full_name(self):
        del self.first
        del self.last

mark  = User('mark','zugerberg')
print(mark.email)
print(mark.get_email)
print(mark.full_name)
del mark.full_name
mark.full_name='marks zug'
# del mark.full_name    
print(mark.full_name)