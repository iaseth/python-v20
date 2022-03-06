


class Team():
	def __init__(self, tournament, jo):
		self.tournament = tournament
		self.jo = jo
		self.id = jo["id"]
		self.fn = jo["fn"]
		self.sn = jo["sn"]
		self.abb = jo["abb"]
		self.name = jo["name"]
		self.matches = []

	def __repr__(self):
		return f"Team: {self}"

	def __str__(self):
		return f"{self.fn} ({self.abb})"
