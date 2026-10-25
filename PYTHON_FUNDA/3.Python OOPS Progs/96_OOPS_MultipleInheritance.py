# Python supports inheriting from more than one parent.
# If multiple classes define a method with the same name,
# Python uses its Method Resolution Order to select which method is called.

class A:
    def m1(self):
        print("A - m1")

    def m2(self):
        print("A - m2")


class B:
    def m2(self):
        print("B - m2")

    def m3(self):
        print("B - m3")


class C(A, B):
    def m1(self):
        print("C - m1")


obj = C()
obj.m1()
obj.m2()
obj.m3()
print([cls.__name__ for cls in C.mro()])