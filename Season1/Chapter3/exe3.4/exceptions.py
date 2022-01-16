

class UsernameContainsIllegalCharacter(Exception):
    def __init__(self,arg):
        self._arg = arg

    def __str__(self):
        return f"UserName: {self._arg} Contains Illegal Character"

class UsernameTooShort(Exception):
    def __init__(self,arg):
        self._arg = arg

    def __str__(self):
        return f"UserName: {self._arg} TooS hort"

        
class UsernameTooLong(Exception):
    def __init__(self,arg):
        self._arg = arg

    def __str__(self):
        return f"UserName: {self._arg} TooS Long"

class PasswordMissingCharacter(Exception):
    def __init__(self,arg):
        self._arg = arg

    def __str__(self):
        return f"Password: {self._arg} Missing Character"