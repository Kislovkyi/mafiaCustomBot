from Mafia import Mafia
class Godfather(Mafia):
    def __init__(self, name, role):
        super().__init__(name, role)
        self.role_description = "The Godfather is the head of the Mafia. They have the ability"