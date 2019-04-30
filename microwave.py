"""Dans ce programme je vais créer le programme d'un micro-onde et lui faire une interface graphique. Ce module sera écrit en python en utilisant la POO"""

class Bouton: 
	"""Ce sont les différents boutons sur lequel je devrai clicker poyur effectuer des actions"""
	def __init__(self, nom): 
		self.nom = nom
		self.temps = 12	#c'est le minuteur au début il vaut 0, modif par minuteurBtn

	def __str__(self) : 
		return "je clique sur le bouton " + self.nom

class OnOff(Bouton):	

	def __init__(self, nom) : 
		Bouton.__init__(self, nom)
		self.actif = False
	

	def cuisson(self):
		"""Quand je clique sur ce bouton j'active ou désactive la cuisson"""
		if self.actif : 
			self.actif = False
		else : 
			if self.temps > 0 : 
				self.actif = True #fonctionne si j'ai du temps au minuteur et que la cuisson n'est pas en cours
			else : 
				self.actif = False
		return " Bouton {} : {}".format(self.nom, self.actif) 

start_btn = OnOff("Start")
print("test str - " , start_btn)
print("test cuisson - ", start_btn.cuisson())
