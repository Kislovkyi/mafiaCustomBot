from Roles.Role import Role
class Commissioner(Role):
    def __init__(self, name, role, jurisdiction):
        super().__init__(name, role)
        self.jurisdiction = jurisdiction
    def check(self, player):
        player.arrested = True
        