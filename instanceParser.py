class Instance:
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

    def __str__(self):
        return "Instance(Optimal: " + str(self.optimal) + ", k: " + str(self.k) + ", sites: " + str(self.sites) + ", demands: " + str(self.demands) + ")"          

#print(Instance ("instances/instance_N200_OPT221.inst"))