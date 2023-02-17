import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

class Instance:
    # Constructor, reads the instance file, parse and stores the data in an object (optimal, k, sites, demands)
    def __init__(self, path):
        f = open(path, "r")
        lines = f.readlines()
        self.optimal = int(lines[1])
        self.k = int(lines[4])
        self.sites = []

        i = 7
        while lines[i] != "\n":
            coords = lines[i].split(" ")
            self.sites.append((int(coords[0]), int(coords[1])))
            i += 1

        i += 2
        self.demands = [int(x) for x in lines[i].split(" ") if x != "\n"]
        f.close()

    # Returns a string representation of the instance (util function)
    def __str__(self):
        return "Instance(Optimal: " + str(self.optimal) + ", k: " + str(self.k) + ", sites: " + str(self.sites) + ", demands: " + str(self.demands) + ")"          

    # Prints the result of the algorithm (util function)
    def printResult(self, algo):
        print("Run result:")
        print("Optimal: " + str(self.optimal))
        print("Algo result: " + str(algo.distance))
        print("Ratio: " + str((self.optimal / algo.distance) * 100) + "%")
        print("Rapport: " + str(algo.distance / self.optimal))

    # Runs the given algorithm on the instance and returns its result
    def run(self, algo, draw=False):
        if draw:
            fig = plt.figure()
            ax = fig.add_subplot(1, 1, 1)

            # Major ticks every 20, minor ticks every 5
            major_ticks = np.arange(0, 101, 20)
            minor_ticks = np.arange(0, 101, 5)

            ax.set_xticks(major_ticks)
            ax.set_xticks(minor_ticks, minor=True)
            ax.set_yticks(major_ticks)
            ax.set_yticks(minor_ticks, minor=True)

            ax.set_xlim(0, 100)
            ax.set_ylim(0, 100)

            # And a corresponding grid
            ax.grid(which='minor', alpha=0.2)
            ax.grid(which='major', alpha=0.5)

            plt.scatter([x[0] for x in self.sites], [x[1] for x in self.sites], s=30)
            scatter = plt.scatter([x[0] for x in algo.technicians], [x[1] for x in algo.technicians], s=5)

            def update(frame_number):
                algo.nextStep()
                scatter.set_offsets(algo.getOffsets())

                if frame_number == len(self.demands) - 2:
                    self.printResult(algo)

                return scatter,

            animation = FuncAnimation(fig, update, interval=100, frames=(len(self.demands) - 1), repeat=False)
            plt.show()
            
            if algo.step < len(self.demands) - 1:
                for i in range(len(self.demands) - algo.step):
                    algo.nextStep()
                
                self.printResult(algo)
        else:
            for i in range(len(self.demands)):
                algo.nextStep()

            self.printResult(algo)
        return algo.distance

class Algo:

    # Constructor, stores the data associated with an algorithm in an object
    def __init__(self, instance):
        if instance is not None:
            self.instance = instance
            self.technicians = [(0, 0) for i in range(instance.k)]
        else:
            self.technicians = []
            self.instance = None
            
        self.step = 0
        self.distance = 0

    # Simulates the next step of the algorithm
    def nextStep(self):
        demand = self.instance.demands[self.step]
        demandSite = self.instance.sites[demand]
        techMoving = self.doStep(demandSite)
        movingDist = abs(demandSite[0] - self.technicians[techMoving][0]) + abs(demandSite[1] - self.technicians[techMoving][1])
        self.technicians[techMoving] = demandSite
        self.distance += movingDist
        self.step += 1

    # Implementation of the algorithm, returns the index of the technician that will move to the given site (to be overridden)
    def doStep(self, site):
        return 0

    # Returns the current positions of the technicians
    def getOffsets(self):
        return self.technicians
    
    def reset(self, instance):
        self.instance = instance
        self.step = 0
        self.technicians = [(0, 0) for i in range(instance.k)]
        self.distance = 0