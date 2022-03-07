


class BatsmanInning:
	def __init__(self, team_inning, jo):
		self.team_inning = team_inning
		self.jo = jo
		self.player = team_inning.tournament.players[jo["id"]]
		self.runs = jo["r"]
		self.balls = jo["b"]
		self.n4 = jo["n4"]
		self.n6 = jo["n6"]
		self.out = True if "out" in jo else False

	def getRunsString(self):
		return self.runs if self.out else f"{self.runs}*"

	def __repr__(self):
		return f"{self.player.fn} {self.getRunsString()} ({self.balls})"

	def __str__(self):
		return f"{self.player.fn:25} {self.getRunsString():4} ({self.balls:2}) [{self.n4:2}x4, {self.n6:2}x6]"
