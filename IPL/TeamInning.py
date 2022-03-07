from .BatsmanInning import BatsmanInning
from .BowlerInning import BowlerInning



class TeamInning:
	def __init__(self, squad, jo, index):
		self.squad = squad
		self.team = squad.team
		self.match = squad.match
		self.tournament = squad.tournament
		self.batting = []
		self.bowling = []
		if index < len(jo):
			self.jo = jo[index]
		else:
			return
		self.runs = self.jo["runs"]
		self.overs = self.jo["overs"]
		self.wkts = len(self.jo["wickets"])
		self.setupBatting()
		self.setupBowling()

	def setupBatting(self):
		for jo in self.jo["batting"]:
			b = BatsmanInning(self, jo)
			self.batting.append(b)

	def setupBowling(self):
		for jo in self.jo["bowling"]:
			b = BowlerInning(self, jo)
			self.bowling.append(b)

	def printToConsole(self):
		dashes = "================================================"
		print(dashes)
		print(self)
		print(dashes)
		for b in self.batting:
			print(b)
		print(dashes)
		for b in self.bowling:
			print(b)
		print(dashes)

	def __str__(self):
		return f"{self.team.fn:35} {self.runs}-{self.wkts} ({self.overs})"
