from instanceParser import Instance, Algo, np
from Benchmarker import benchmark

# score: 15.67
# complexity per step: O(log N) (assumed for randint) where N is the number of technicians
class FullRandom(Algo):
    # Implementation of the algorithm, returns a random technician
    def doStep(self, site):
        return np.random.randint(0, self.instance.k)

# score: 35.21
# complexity per step: O(N) where N is the number of technicians
class Closest(Algo):
    # Implementation of the algorithm, returns the closest technician
    def doStep(self, site):
        return np.argmin(
            [
                abs(site[0] - tech[0]) + abs(site[1] - tech[1])
                for tech in self.technicians
            ]
        )

# score: 92.48
# complexity per step (worst case): O(N) where N is the number of technicians
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

# score: 67.33
# complexity per step (worst case): O(N) where N is the number of technicians
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

        # Si tous les techniciens sont en deplacement, on retourne un technicien aleatoire
        return np.random.randint(0, self.instance.k)

# score: 64.70
# complexity per step (worst case): O(N) where N is the number of technicians
class WeightedRandom(Algo):
    # Implementation of the algorithm, returns a random technician weighted by the distance to the site (the closer the more likely)
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

# score: 60.31
# complexity per step (worst case): O(N) where N is the number of technicians
class RandomClosest(Algo):
    def doStep(self, site):
        # Dans un premier temps, on verifie si le site est deja couvert
        for tech in self.technicians:
            if abs(site[0] - tech[0]) + abs(site[1] - tech[1]) == 0:
                return self.technicians.index(tech)

        # Si le site n'est pas couvert, on sort un technicien aleatoire
        return np.random.randint(0, self.instance.k)

# score: 15.80
# complexity per step: O(N^3) where N is the max between the number of technicians and the number of sites
class MaxCoverage(Algo):
    # Try to maximize the coverage of the sites (spread the technicians as much as possible)
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
