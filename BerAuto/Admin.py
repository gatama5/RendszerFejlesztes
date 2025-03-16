
class Admin(User):
    def __init__(self, username, password, level=2):
        super().__init__(username, password, level)