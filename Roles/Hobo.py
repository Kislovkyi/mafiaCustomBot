from Roles.Role import Role
class Hobo(Role):
    def __init__(self, name, role, favorite_song):
        super().__init__(name, role)
        self.favorite_song = favorite_song
    def sing(self, player):
        player.laugh = True