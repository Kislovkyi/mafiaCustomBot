from Roles.Doctor import Doctor
from Roles.Commissioner import Commissioner
from chatBot import ChatBot
class MafiaLogic:
    def __init__(self):
        self.players = []
        self.mafia = []
        self.civilians = []
        self.dead = []
        self.votes = {}
        self.votes_count = 0
