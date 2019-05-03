"""Dans ce programme je vais créer le programme d'un micro-onde et lui faire une interface graphique. Ce module sera écrit en python en utilisant la POO"""

"""
### Projet terminé :)
"""

import time

temps = 0 #détermine le temps de cuisson

class Bouton:
	"""Ce sont les différents boutons sur lequel je devrai clicker poyur effectuer des actions"""
	def __init__(self, nom):
		self.nom = nom

	def __str__(self) :
		return "je clique sur le bouton " + self.nom

class Start(Bouton):
	"""Lance la cuisson en fonction du temps donné"""
	def __init__(self, nom) :
		Bouton.__init__(self, nom)
		self.actif = False


	def cuisson(self):
		"""Quand je clique sur ce bouton j'active ou désactive la cuisson"""
		if self.actif :
			self.actif = False
			return "Pause ! "
		else :
			if temps > 0 :
				self.actif = True #fonctionne si j'ai du temps au minuteur et que la cuisson n'est pas en cours
				for i in range(temps, 0, -1):
					print("Cuisson en cours ... ({})".format(i))
					time.sleep(1)
					if i == 1 :
						print("Cuisson terminée =)")
			else :
				self.actif = False
				return "Renseignez un temps de cuisson."

class Minuteur(Bouton):

	def __init__(self, nom) :
		Bouton.__init__(self, nom)

	def reglerTemps(self):
		#2 conditions : self.temps doit être un int supérieur à 0
		global temps
		temps = input("Donnez le temps de cuisson : ")
		while True :
			try :
				temps = int(temps)
				print("Je règle le temps sur {} seconde(s) de cuisson".format(temps))
				break
			except ValueError :
				print("Besoin d'un nombre supérieur à 0")
				temps = input("Donnez le temps de cuisson : ")
				continue




print("- "*10)
minuteur_btn = Minuteur("Minuteur")
print("test str - " , minuteur_btn)
minuteur_btn.reglerTemps()

print("- "*10)
start_btn = Start("Start")
print("test str - " , start_btn)
start_btn.cuisson()
