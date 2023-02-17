from instanceParser import Instance, Algo, np
from Benchmarker import benchmark

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

class PeriodicRandom(Algo):
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
        return np.random.randint(0, self.instance.k)

class WeightedRandom(Algo):
    def doStep(self, site):
        dist = [
                abs(site[0] - tech[0]) + abs(site[1] - tech[1])
                for tech in self.technicians
            ]
        for i in range(len(dist)):
            if dist[i] == 0:
                return i

        p = [sum(dist) / (d * d) for d in dist]
        sumP = sum(p)
        p = [i / sumP for i in p]
        return np.random.choice(range(len(self.technicians)), p=p)

class RandomClosest(Algo):
    def doStep(self, site):
        # Dans un premier temps, on verifie si le site est deja couvert
        for tech in self.technicians:
            if abs(site[0] - tech[0]) + abs(site[1] - tech[1]) == 0:
                return self.technicians.index(tech)

        # Si le site n'est pas couvert, on sort un technicien aleatoire
        return np.random.randint(0, self.instance.k)

class MaxCoverage(Algo):
    def doStep(self, site):
        dist = []
        for tech in range(len(self.technicians)):
            d = 0
            for tech2 in range(len(self.technicians)):
                if tech == tech2:
                    for site2 in self.instance.sites:
                        d += abs(site2[0] - site[0]) + abs(site2[0] - site[0])
                else:
                    for site2 in self.instance.sites:
                        d += abs(site2[0] - self.technicians[tech2][0]) + abs(site2[1] - self.technicians[tech2][1])
            dist.append(d)

        return np.argmax(dist)

#instance = Instance("instances/instance_N200_OPT221.inst")
#print("FullRandom")
#algo = FullRandom(instance)
#instance.run(algo, draw=False)
#print("\n\n\n")
#print("Closest")
#algo = Closest(instance)
#instance.run(algo, draw=False)
#print("\n\n\n")
#print("Periodic")
#algo = Periodic(instance)
#instance.run(algo, draw=False)

#print("\n\n\n")
#print("RandomClosest")
#algo = RandomClosest(instance)
#instance.run(algo, draw=False)

#instance = Instance("instances/instance_N200_OPT221.inst")
#algo = MaxCoverage(instance)
#instance.run(algo, draw=True)

algo = Periodic(None)
benchmark(algo, isRandom=False)