class User:
    def __init__(self, password):
        # TODO: Store the password as a private attribute using double underscore (__)
        #       This makes it harder to access from outside the class
        self.__password=password
        pass
    
    def check_password(self, input_password):
        # Return True if input matches stored password
        return input_password == self.__password
    
    def change_password(self, old_password, new_password):
        # TODO: Check if old_password is correct using the check_password method
        # TODO: If old_password is correct, update the private password to new_password and return True
        # TODO: If old_password is incorrect, return False without changing the password

        self.__new_password=new_password
        if self.check_password(old_password)==True:
            self.__password=new_password
            return True
        else:
            return False
