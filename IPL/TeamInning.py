from .BatsmanInning import BatsmanInning
from .BowlerInning import BowlerInning



class TeamInning:
	def __init__(self, squad, jo, index):
		self.squad = squad
		self.team = squad.team
		self.match = squad.match
		self.tournament = squad.tournament
		self.happened = False
		self.batting = []
		self.bowling = []
		if index < len(jo):
			self.jo = jo[index]
		else:
			return
		self.runs = self.jo["runs"]
		self.balls = self.jo["balls"]
		self.overs = self.jo["overs"]
		self.wkts = len(self.jo["wickets"])
		self.setupBatting()
		self.setupBowling()
		self.happened = True

	def setupBatting(self):
		for jo in self.jo["batting"]:
			b = BatsmanInning(self, jo)
			self.batting.append(b)

	def setupBowling(self):
		for jo in self.jo["bowling"]:
			b = BowlerInning(self, jo)
			self.bowling.append(b)

	def printToConsole(self):
		dashes = "------------------------------------------------"
		print(dashes)
		print(self)
		print(dashes)
		for b in self.batting:
			print(b)
		print(dashes)
		for b in self.bowling:
			print(b)

	def getRunRate(self):
		return 0 if self.balls is 0 else (self.runs * 6 / self.balls)

	def getRunRateRounded(self):
		return round(self.getRunRate(), 2)

	def __str__(self):
		return f"{self.team.fn:35} {self.runs}-{self.wkts} ({self.overs}) {self.getRunRateRounded()}"
