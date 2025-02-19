from Roles.Role import Role
class Executioner(Role):   
     def __init__(self, name, role, favorite_weapon):
         super().__init__(name, role)
         self.favorite_weapon = favorite_weapon