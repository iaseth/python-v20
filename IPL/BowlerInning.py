


class BowlerInning:
	def __init__(self, team_inning, jo):
		self.team_inning = team_inning
		self.jo = jo
		self.player = team_inning.tournament.players[jo["id"]]
		self.overs = jo["ov"]
		self.runs = jo["r"]
		self.maidens = jo["m"]
		self.dots = jo["d"]
		self.wkts = jo["w"]
		self.wds = jo["wd"]
		self.nbs = jo["nb"]

	def __str__(self):
		return f"{self.player.fn:25} {self.wkts}-{self.runs} ({self.overs})"
