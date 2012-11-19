import os, sys
os.system("clear")

LIMIT = 501
PLAYERNUMBER = 2
players = {}

class Player(object):
	def __init__(self, playername, score=None):
		self._name = playername
		self._scorelist = []
		if score == None:
			self._score = LIMIT
		else:
			self._score = score

	def newScore(self, points):
		points = int(points)
		if points <= self._score:
			self._score = self._score-points
			self._scorelist.append(points)
		else:
			self._scorelist.append(0)

		return self._score

	@property
	def scorelist(self):
		return self._scorelist

	@property
	def name(self):
		return self._name

	@property
	def score(self):
		return self._score


for pid in range(PLAYERNUMBER):
	pid = pid+1
	pname = raw_input("Spieler %s Name: " % pid)
	players[pid] = Player(playername=pname)

while(True):
	os.system("clear")
	for p in players.itervalues():
		print "%s: %s\n %s" % (p.name, p.score, p.scorelist)

	for p in players.itervalues():
		points = raw_input("%s Punkte: " % (p.name))
		p.newScore(points)
		os.system("say '%s %s Punkte'" % (p.name, p.score))