class InvalidAgeError(Exception):
    pass

class Check:
    def can_vote(age):
        if age >= 18:
            print("Person can vote")
        else:
            err = InvalidAgeError()
            raise err

age = int(input("Enter age : "))
Check.can_vote(age)