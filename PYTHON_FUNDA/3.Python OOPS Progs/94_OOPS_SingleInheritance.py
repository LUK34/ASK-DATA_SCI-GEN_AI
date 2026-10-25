# Inheritance allows a child (subclass) to reuse methods and attributes defined in a parent (base class).
# The syntax class Second(First) means Second inherits from First.
class First:
    def m1(self):
        print("First - m1")

    def m2(self):
        print("First - m2")


class Second(First):
    def m2(self):
        print("Second - m2")

    def m3(self):
        print("Second - m3")


obj = Second()
obj.m1()
obj.m2()
obj.m3()