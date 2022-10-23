def do_somethings(work):
    print("Start Work")
    work()
    print("close work")

def greeting():
    print("Hello everyone")

do_somethings(greeting)