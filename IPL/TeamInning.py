from .BatsmanInning import BatsmanInning
from .BowlerInning import BowlerInning



class TeamInning:
	def __init__(self, squad, jo, index):
		self.squad = squad
		self.match = squad.match
		self.tournament = squad.tournament
		self.batting = []
		self.bowling = []
		if index < len(jo):
			self.jo = jo[index]
		else:
			return
		self.setupBatting()
		self.setupBowling()

	def setupBatting(self):
		for jo in self.jo["batting"]:
			b = BatsmanInning(self, jo)
			self.batting.append(b)
			print(b)

	def setupBowling(self):
		for jo in self.jo["bowling"]:
			b = BowlerInning(self, jo)
			self.bowling.append(b)
			print(b)
