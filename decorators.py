def announce(f):
    def wrapper():
        print("The function is about to be run...")
        f()
        print("The function is done with...")
    return wrapper

@announce
def hello():
    print("Hello, world!")

hello()