class Test:
    def __init__(self, a):
        self.a = a

    def fun(self):
        print("fun...")

obj = Test(10)
print(obj.a)
obj.fun()