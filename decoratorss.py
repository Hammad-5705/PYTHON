def design(fx):
    def mfx(*args,**kwargs):
        print("\nStarting Function")
        fx(*args,**kwargs)
        print("Ending Function\n\n\n")
    return mfx


@design
def w():
    print("Hello Word")

@design
def sum(a,b):
    print(a+b)


w()
sum(1,4)