from .Match import Match


class Season():
	def __init__(self, tournament, jo):
		self.tournament = tournament
		self.jo = jo
		self.year = jo["year"]
		self.matches = []
		for jo in self.jo["matches"]:
			match = Match(self, jo)
			self.matches.append(match)
			if len(self.matches) == self.tournament.max_matches:
				break

	def __repr__(self):
		return f"Season: {self}"

	def __str__(self):
		return f"{self.year} ({len(self.matches)} matches)"
