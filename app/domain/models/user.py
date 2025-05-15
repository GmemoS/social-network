class User:
    __slots__ = ('id', 'username', 'email', 'name')

    def __init__(self, id: str, username: str, email: str, name: str):
        self.id = id
        self.username = username
        self.email = email
        self.name = name
