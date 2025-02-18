from Roles.Role import Role
class Jester(Role):
    def __init__(self, name, role, joke):
        super().__init__(name, role)
        self.joke = joke
    def joke(self, player):
        player.laugh = True