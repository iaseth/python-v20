import json
import os

from .Team import Team
from .Ground import Ground
from .Player import Player

from .Season import Season


class IPL():
	def __init__(self, args):
		self.processProps(args)
		self.setupJsons()
		if not self.json_setup_complete:
			return
		self.setupCodes()
		self.setupSeasons()

	def processProps(self, args):
		self.datadir = "data"
		self.args = args
		self.max_seasons = 0
		self.max_matches = 0
		for arg in args:
			if arg.startswith("-s"):
				self.max_seasons = int(arg[2:])
			elif arg.startswith("-m"):
				self.max_matches = int(arg[2:])
			elif arg.startswith("-"):
				pass
			else:
				self.datadir = arg

	def setupJsons(self):
		self.json_setup_complete = False
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
		self.json_setup_complete = True

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
			self.matches.extend(season.matches)
			if len(self.seasons) == self.max_seasons:
				break

	def printStats(self):
		print(f"IPL Object:")
		print(f"\t---- {len(self.teams)} teams")
		print(f"\t---- {len(self.grounds)} grounds")
		print(f"\t---- {len(self.players)} players")
		print(f"\t---- {len(self.seasons)} seasons")
		print(f"\t---- {len(self.matches)} matches")

	def doStuff(self):
		self.printStats()
		pass

	def printArgs(self):
		print(self.args)
