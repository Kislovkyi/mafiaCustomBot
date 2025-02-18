from Commissioner import Commissioner
class CommissionerAssistant(Commissioner):
    def __init__(self, name, role, jurisdiction):
        super().__init__(name, role, jurisdiction)
    def check(self, player):
        player.arrested = True
        print(f"{self.name} has arrested {player.name}!")