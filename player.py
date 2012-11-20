class Player(object):
	def __init__(self, playername, score=None):
		self._name = playername
		self._scorelist = []
		self._score = score
		self._initscore = self._score

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

	@property
	def average(self):
		if len(self._scorelist) > 0:
			return float(self._initscore-self._score)/len(self._scorelist)
		else:
			return 0.