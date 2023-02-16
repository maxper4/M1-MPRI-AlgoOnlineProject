from instanceParser import Instance, Algo, np

class FullRandom(Algo):
    # Implementation of the algorithm, returns a random technician
    def doStep(self, site):
        return np.random.randint(0, self.instance.k)

instance = Instance("instances/instance_N200_OPT221.inst")
algo = FullRandom(instance)
instance.run(algo, draw=False)