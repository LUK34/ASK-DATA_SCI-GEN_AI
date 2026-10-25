#Method overriding means defining a method in a child class with the same name as one in its parent.
# This lets the child customize inherited behavior.
# For example, a new phone model may offer a better camera than its parent model.

class Galaxy:
    def camera(self):
        print("12MP camera")


class Note(Galaxy):
    def camera(self):
        print("24MP camera")


old_phone = Galaxy()
new_phone = Note()
old_phone.camera()
new_phone.camera()