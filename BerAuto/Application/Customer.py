
class Customer(User):
    def __init__(self, username, password, level=0):
        super().__init__(username, password, level)