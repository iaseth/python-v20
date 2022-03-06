import json
import os

from .Team import Team
from .Ground import Ground
from .Player import Player

from .Season import Season


class IPL():
	def __init__(self, args):
		self.args = args
		self.datadir = args[0] if len(args) else "data"

		self.cj_path = os.path.join(self.datadir, "codes.json")
		self.bj_path = os.path.join(self.datadir, "bundle.json")
		if not os.path.isfile(self.cj_path):
			print(f"Not found: {self.cj_path}")
			return
		if not os.path.isfile(self.bj_path):
			print(f"Not found: {self.bj_path}")
			return
		self.cj = json.load(open(self.cj_path))
		self.bj = json.load(open(self.bj_path))
		self.setupCodes()
		self.setupSeasons()

	def setupCodes(self):
		self.setupTeams()
		self.setupGrounds()
		self.setupPlayers()

	def setupTeams(self):
		teams_json = self.cj["teams"]
		self.teams = {}
		for index in teams_json:
			self.teams[index] = Team(self, teams_json[index])

	def setupGrounds(self):
		grounds_json = self.cj["grounds"]
		self.grounds = {}
		for index in grounds_json:
			self.grounds[index] = Ground(self, grounds_json[index])

	def setupPlayers(self):
		players_json = self.cj["players"]
		self.players = {}
		for index in players_json:
			self.players[index] = Player(self, players_json[index])

	def setupSeasons(self):
		self.seasons = []
		self.matches = []
		for jo in self.bj["seasons"]:
			season = Season(self, jo)
			self.seasons.append(season)

	def printStats(self):
		print(f"IPL Object:")
		print(f"\t---- {len(self.teams)} teams")
		print(f"\t---- {len(self.grounds)} grounds")
		print(f"\t---- {len(self.players)} players")

	def doStuff(self):
		self.printStats()
		pass

	def printArgs(self):
		print(self.args)
