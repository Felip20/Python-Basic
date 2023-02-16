def greet(fun):

    def wrapper(name):
        print("hello");
        fun(name)
        print("goodbye");
    return wrapper
@greet
def name(name):
    print(name);

name("wathone khant");