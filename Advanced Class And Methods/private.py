class User :
    def __init__(self,name,password,phone):
        self.name =name
        self.__password = password
        self.phone = phone
    def __get_password (self):
        return  self.__password
ryan = User('Ryan dai','ABCSd','03980294')
# print(ryan.password)
print(ryan.get_password())