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
		self.team_a = self.tournament.teams[jo["teams"][0]["team"]]
		self.team_b = self.tournament.teams[jo["teams"][1]["team"]]
		self.ground = self.tournament.grounds[self.meta["ground"]]
		self.winner = None
		self.loser = None

	def __repr__(self):
		return f"Match: {self}"

	def __str__(self):
		return f"IPL {self.year} #{self.season_index+1}"
