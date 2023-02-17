from instanceParser import Instance, Algo, np


class FullRandom(Algo):
    # Implementation of the algorithm, returns a random technician
    def doStep(self, site):
        return np.random.randint(0, self.instance.k)


class Closest(Algo):
    # Implementation of the algorithm, returns the closest technician
    def doStep(self, site):
        return np.argmin(
            [
                abs(site[0] - tech[0]) + abs(site[1] - tech[1])
                for tech in self.technicians
            ]
        )


class Periodic(Algo): # Optimal quand la periode est inferieure au nombre de techniciens
    def doStep(self, site):

        # Dans un premier temps, on verifie si le site est deja couvert
        for tech in self.technicians:
            if abs(site[0] - tech[0]) + abs(site[1] - tech[1]) == 0:
                return self.technicians.index(tech)

        # Si le site n'est pas couvert, on sort les techniciens encore à la base
        for tech in self.technicians:
            if tech[0] == 0 and tech[1] == 0:
                return self.technicians.index(tech)

        # Si tous les techniciens sont en deplacement, on retourne le plus proche du site
        return np.argmin(
            [
                abs(site[0] - tech[0]) + abs(site[1] - tech[1])
                for tech in self.technicians
            ]
        )


instance = Instance("instances/instance_N200_OPT221.inst")
print("FullRandom")
algo = FullRandom(instance)
instance.run(algo, draw=False)
print("\n\n\n")
print("Closest")
algo = Closest(instance)
instance.run(algo, draw=False)
print("\n\n\n")
print("Periodic")
algo = Periodic(instance)
instance.run(algo, draw=False)
