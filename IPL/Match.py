


class Match():
	def __init__(self, season, jo):
		self.season = season
		self.jo = jo
		self.tournament = season.tournament
		self.year = season.year
		self.seasonIndex = len(season.matches)

	def __repr__(self):
		return f"Match: {self}"

	def __str__(self):
		return f"IPL {self.year} #{self.seasonIndex+1}"
