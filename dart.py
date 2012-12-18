import os, sys, locale
from datetime import datetime
from player import Player
os.system("clear")

class Game():

	def __init__(self, limit=501, playernumber=2, sound=True, logging=True):
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
				"points" : "Punkte",
				"finished" : "Spiel beendet.",
				"won" : "hat gesiegt",
				"avg" : "Durchschnitt",
				"manual": "Ergebnis eingeben als Summe oder als Addition (z.B. 60+50+60).\nKorrektur des letzten Wurfes: #Korrektur#aktueller Wurf"
			},
			"en" : {
				"player" : "Player",
				"name" : "name",
				"points" : "points",
				"finished" : "The game has been finished.",
				"won" : "has won",
				"avg" : "avg.",
				"manual": "Type score as number or an addition (e.g. 60+50+60).\nEdit your last score: #new Value#current score"
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
		# ask for player names
		for pid in range(self.playernumber):
			pid = pid+1
			pname = raw_input("%s %s %s: " % (self.getLangStr("player"), pid, self.getLangStr("name")))
			self.players[pid] = Player(playername=pname, score=self.limit)

		t0 = datetime.now()

		while(self.doPlay):
			for p in self.players.itervalues():
				if p.score > 0:
					os.system("clear")

					print self.getLangStr("manual") + "\n"

					# print score table
					for q in self.players.itervalues():
						print "%s %s\n%s\n%s: %.2f\n" % (q.name, q.scorelist, q.score, self.getLangStr("avg"), q.average)

					# for low points say the score loudly
					if p.score > 0 and p.score <= 180:
						if self.isMacOs and self.sound:
							os.system("say '%s %s %s'" % (p.name, p.score, self.getLangStr("points")))

					# if score is > 0 ask for points
					if p.score > 0:
						points = raw_input("%s %s: " % (p.name, self.getLangStr("points")))
						l = p.newScore(points)

					# has the player reached 0?
					if p.score == 0:
						if len(self.positions) == 0:
							if self.isMacOs and self.sound:
								os.system("say '%s %s.'" % (p.name, self.getLangStr("won")))

						self.positions.append(p)
						if len(self.positions) == self.playernumber - 1:
							self.doPlay = False
							if self.isMacOs and self.sound:
								os.system("say '%s'" % self.getLangStr("finished"))

		t1 = datetime.now()

		for player in self.players.itervalues():
			player.writeLog(t0, t1)

if __name__ == "__main__":
	g = Game()
	g.play()
