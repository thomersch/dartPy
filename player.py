class Player(object):
	def __init__(self, playername, score=None):
		self._name = playername
		self._scorelist = []
		self._score = score
		self._initscore = self._score

	def newScore(self, points):
		# do some input checking and conversion, so the program doesn't crash at strange inputs
		if points == "":
			points = 0

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