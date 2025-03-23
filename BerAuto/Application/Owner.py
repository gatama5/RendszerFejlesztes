
class Owner(User):
    def __init__(self, username, password, level=1):
        super().__init__(username, password, level)