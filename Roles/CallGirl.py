from Roles.Role import Role
class CallGirl(Role):
     def __init__(self, name, role, favorite_song):
         super().__init__(name, role)
         self.favorite_song = favorite_song