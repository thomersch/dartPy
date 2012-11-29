import os, json

class Player(object):
	def __init__(self, playername, score=None):
		self._name = playername
		self._scorelist = []
		self._score = score
		self._initscore = self._score
		self.fileobject = None

	def newScore(self, points):
		# do some input checking and conversion, so the program doesn't crash at strange inputs
		if points == "":
			points = 0

		# correction of scores
		if points.startswith("#"):
			c = points.split("#")
			self.correctLastScore(int(c[1]))
			points = c[2]

		try:
			points = int(points)
		except:
			plist = points.split("+")
			if len(plist) <= 1:
				points = 0
			else:
				points = 0
				for p in plist:
					try:
						points += int(p)
					except:
						points += 0

		if points <= self._score:
			self._score = self._score-points
			self._scorelist.append(points)
		else:
			self._scorelist.append(0)

		return self._score

	def correctLastScore(self, newscore):
		self._score = self._score + self.scorelist[len(self.scorelist)-1] - newscore
		self.scorelist[len(self.scorelist)-1] = newscore

	@property
	def scorelist(self):
		return self._scorelist

	@property
	def name(self):
		return self._name

	@property
	def score(self):
		return self._score

	@property
	def average(self):
		if len(self._scorelist) > 0:
			return float(self._initscore-self._score)/len(self._scorelist)
		else:
			return 0.

	def writeLog(self, t0, t1):
		if not os.path.exists("scores"):
			os.makedirs("scores")
		filename = "%s_%s.dartlog.txt" % (self.name, t0.strftime("%Y-%m-%d-%H-%M"))
		filepath = os.path.join("scores", filename)
		data = {
			"name": self.name,
			"start": t0.strftime("%Y-%m-%d-%H-%M-%S"),
			"stop": t1.strftime("%Y-%m-%d-%H-%M-%S"),
			"scores": self.scorelist,
			"average": self.average
		}

		f = open(filepath, "w")
		f.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))
		f.close()