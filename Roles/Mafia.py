from Roles.Role import Role
class Mafia(Role):
    def __init__(self, name, role):
        super().__init__(name, role)
        self.role_description = "A Mafia member, they have access to powerful abilities and secrets. They are usually seen as brutal and violent."
        self.is_mafia = True