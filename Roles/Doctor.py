from Roles.Role import Role
class Doctor (Role):
    def __init__(self, name, role, specialty):
        super().__init__(name, role)
        self.specialty = specialty
    def heal(self, player):
        player.health += 1
        