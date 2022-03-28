


class Squad:
	def __init__(self, match , jo, team, opposition):
		self.match = match
		self.tournament = match.tournament
		self.jo = jo
		self.team = team
		self.opposition = opposition
		self.captain = self.tournament.players[jo["captain"]] if "captain" in jo else None
		self.wk = self.tournament.players[jo["wk"]] if "wk" in jo else None
		self.members = []
		for player_id in jo["players"]:
			self.members.append(self.tournament.players[player_id])
