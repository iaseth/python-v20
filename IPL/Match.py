from .Squad import Squad
from .TeamInning import TeamInning



class Match():
	def __init__(self, season, jo):
		self.season = season
		self.jo = jo
		self.tournament = season.tournament
		self.year = season.year
		self.season_index = len(season.matches)

		self.meta = jo["meta"]
		self.order = self.meta["order"]
		self.team_a = self.tournament.teams[jo["teams"][0]["team"]]
		self.team_b = self.tournament.teams[jo["teams"][1]["team"]]
		self.ground = self.tournament.grounds[self.meta["ground"]]

		if self.meta["outcome"] == "A":
			self.winner = self.team_a
			self.loser = self.team_b
		elif self.meta["outcome"] == "B":
			self.winner = self.team_b
			self.loser = self.team_a
		else:
			self.winner = None
			self.loser = None

		self.squad_a = Squad(self, jo["teams"][0], self.team_a, self.team_b)
		self.squad_b = Squad(self, jo["teams"][1], self.team_b, self.team_a)
		self.squad_a.opposition_squad = self.squad_b
		self.squad_b.opposition_squad = self.squad_a

		a_batted_first = 0 in self.order and self.order[0] == 0
		self.inning_a = TeamInning(self.squad_a, jo["innings"], 0 if a_batted_first else 1)
		self.inning_b = TeamInning(self.squad_b, jo["innings"], 1 if a_batted_first else 0)

		self.first_inning = self.inning_a if a_batted_first else self.inning_b
		self.second_inning = self.inning_b if a_batted_first else self.inning_a
		self.printToConsole()

	def printToConsole(self):
		dashes = "================================================"
		print(dashes)
		print(f"IPL {self.season.year}, Match {self.season_index+1} - {self.team_a.abb} vs {self.team_b.abb}")
		if self.first_inning.happened:
			self.first_inning.printToConsole()
		if self.second_inning.happened:
			self.second_inning.printToConsole()
		print(dashes)

	def __repr__(self):
		return f"Match: {self}"

	def __str__(self):
		return f"IPL {self.year} #{self.season_index+1}"
