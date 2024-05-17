class PlayerData:
    id = 0
    wins = 0
    loses = 0
    times = 0
    num = 0
    start = False
    max_num = 0

    def wins_percentage(self, wins, loses):
        percentage = (wins / (wins + loses)) * 100
        return percentage
    def to_dictionary(self):
        return {"id": self.id, "wins": self.wins, "loses": self.loses, "times": self.times}
    
    def from_dictionary(self, dictionary):
        self.id = dictionary["id"]
        self.wins = dictionary["wins"]
        self.times = dictionary["times"]
        self.loses = dictionary["loses"]
