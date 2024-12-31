# models/usuario_model.py

class Usuario:
    def __init__(self, name, lastname, email, birthday, banned=False):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.birthday = birthday
        self.banned = banned

    def __repr__(self):
        return f"Usuario({self.name}, {self.lastname}, {self.email}, {self.birthday}, {self.banned})"

