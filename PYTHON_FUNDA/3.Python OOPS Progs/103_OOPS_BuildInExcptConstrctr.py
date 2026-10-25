class InvalidAgeError(Exception):
    pass


class Check:
    @staticmethod
    def can_vote(age):
        if age >= 18:
            print("Person can vote")
        else:
            raise InvalidAgeError("Low Age")


try:
    age = int(input("Enter age : "))
    Check.can_vote(age)
except InvalidAgeError as msg:
    print(f"Exception : {msg}")
except ValueError:
    print("Exception : Please enter a valid integer age")