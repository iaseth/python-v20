


class Ground():
	def __init__(self, tournament, jo):
		self.tournament = tournament
		self.jo = jo
		self.id = jo["id"]
		self.fn = jo["fn"]
		self.sn = jo["sn"]
		self.city = jo["city"]
		self.name = jo["name"]
		self.matches = []

	def __repr__(self):
		return f"Ground: {self}"

	def __str__(self):
		return f"{self.fn} ({self.city})"
