def do_something():
    print("Inside the function do something")
    def inner_func():
        print('inside the inner function')
    inner_func()

do_something()

def first_func():
    print("OK?")
    def second_func():
        print("yes I am okey")
    return second_func

first = first_func()
# print(first)
first()
first_func()()