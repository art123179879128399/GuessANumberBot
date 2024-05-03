class PlayerData:
    id = 0
    wins = 0
    loses = 0
    tries = 0
    num = 0

    def wins_percentage(self, wins, loses):
        percentage = (wins / (wins + loses)) * 100
        return percentage
    def to_dictionary(self):
        return {"id": self.id, "wins": self.wins, "loses": self.loses, "tries": self.tries}
    
    def from_dictionary(self, dictionary):
        self.id = dictionary["id"]
        self.wins = dictionary["wins"]
        self.tries = dictionary["tries"]
        self.loses = dictionary["loses"]
