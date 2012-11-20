import os, sys, locale
from player import Player
os.system("clear")

class Game():

	def __init__(self, limit=501, playernumber=2, sound=True):
		self.limit = limit
		self.playernumber = playernumber
		self.sound = sound

		self.players = {}
		self.positions = []
		self.doPlay = True
		self.lang = locale.getdefaultlocale()[0][:2]

		self.langStrings = {
			"de" : {
				"player" : "Spieler",
				"name" : "Name",
				"points" : "Punkte"
			},
			"en" : {
				"Player" : "player",
				"name" : "name",
				"points" : "points"
			}
		}

	@property
	def isMacOs(self):
		if os.uname()[0] == "Darwin":
			return True
		else:
			return False

	def getLangStr(self, command):
		if not self.lang in self.langStrings:
			self.lang = "en"
		return self.langStrings[self.lang][command]

	def play(self):
		for pid in range(self.playernumber):
			pid = pid+1
			pname = raw_input("%s %s %s: " % (self.getLangStr("player"), pid, self.getLangStr("name")))
			self.players[pid] = Player(playername=pname, score=self.limit)

		while(self.doPlay):
			for p in self.players.itervalues():
				os.system("clear")
				for q in self.players.itervalues():
					print "%s %s\n%s\nAverage: %.2f\n" % (q.name, q.scorelist, q.score, q.average)
				if p.score > 0 and p.score < 180:
					if self.isMacOs and self.sound:
						os.system("say '%s noch %s Punkte'" % (p.name, p.score))
				if p.score > 0:
					points = raw_input("%s points: " % (p.name))
				if p.newScore(points) == 0:
					if len(self.positions) == 0:
						if self.isMacOs and self.sound:
							os.system("say '%s hat gesiegt.'" % (p.name))
					self.positions.append(p)
					if len(self.positions) == self.playernumber:
						self.doPlay = False
						if self.isMacOs and self.sound:
							os.system("say 'Spiel beendet.'")

if __name__ == "__main__":
	g = Game()
	g.play()