import os, sys, locale
os.system("clear")

LIMIT = 501
PLAYERNUMBER = 2
SOUND = True

players = {}
lang = locale.getdefaultlocale()[0][:2]

langStrings = {
	"de" : {
		"player" : "Spieler",
		"name" : "Name",
		"points" : "Punkte"
	},
	"en" : {
		"player" : "player",
		"name" : "name",
		"points" : "points"
	}
}

@property
def isMacOs():
	if os.uname()[0] == "Darwin":
		return True
	else:
		return False

def getLangStr(command):
	return langStrings[lang][command]

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
	pname = raw_input("%s %s %s: " % (getLangStr("player"), pid, getLangStr("name")))
	players[pid] = Player(playername=pname)

while(True):
	os.system("clear")
	for p in players.itervalues():
		print "%s: %s\n %s" % (p.name, p.score, p.scorelist)

	for p in players.itervalues():
		points = raw_input("%s %s: " % (p.name, getLangStr("points")))
		p.newScore(points)
		if isMacOs and SOUND:
			os.system("say '%s %s %s'" % (p.name, p.score, getLangStr("points")))