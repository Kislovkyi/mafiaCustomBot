from Roles.Role import Role
class Citizen (Role):
    def __init__(self, name, role, favorite_movie):
        super().__init__(name, role)
        self.favorite_movie = favorite_movie
    def vote(self, player):
        player.vote = True
    def nominate(self, player):
        player.nominate = True
    def discuss(self, player):
        player.discuss = True
    def accuse(self, player):
        player.accuse = True
    def defend(self, player):
        player.defend = True
    def investigate(self, player):
        player.investigate = True
    def protect(self, player):
        player.protect = True
    def kill(self, player):
        player.kill = True
    def heal(self, player):
        player.heal = True
    def silence(self, player):
        player.silence = True
    def blackmail(self, player):
        player.blackmail = True
    def frame(self, player):
        player.frame = True
    def haunt(self, player):
        player.haunt = True
    def curse(self, player):
        player.curse