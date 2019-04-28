"""Dans ce programme je vais créer le programme d'un micro-onde et lui faire une interface graphique. Ce module sera écrit en python en utilisant la POO"""

class Bouton: 
	"""Ce sont les différents boutons sur lequel je devrai clicker poyur effectuer des actions"""
	def __init__(self, nom): 
		self.nom = nom

	def __str__(self) : 
		return "je clique sur le bouton " + self.nom

class OnOff(Bouton):	

	def __init__(self, nom) : 
		Bouton.__init__(self, nom)
		self.actif = False
	

	def click(self):
		"""Quand je clique sur ce bouton j'active ou désactive l'appareil"""
		if self.actif : 
			self.actif = False
		else : 
			self.actif = True
		return " Bouton {} : {}".format(self.nom, self.actif) 

bouton_demarrer = OnOff("démarrer")
print("test str - " , bouton_demarrer)
print("test click - ", bouton_demarrer.click())
