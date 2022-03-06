import json
import os

from .Team import Team


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
		self.setupCodes();

	def setupCodes(self):
		self.setupTeams()
		self.setupGrounds()
		self.setupPlayers()

	def setupTeams(self):
		teams_json = self.cj["teams"]
		self.teams = [];
		for index in teams_json:
			team = Team(self, teams_json[index])
			self.teams.append(team)

	def setupGrounds(self):
		pass

	def setupPlayers(self):
		pass

	def doStuff(self):
		self.printArgs()

	def printArgs(self):
		print(self.args)
