from os import listdir
from os.path import isfile, join
from instanceParser import Instance
from scipy.stats import norm, stats

sampleSize = 100    # Number of samples for the random algorithm
confidence = 0.95   # standard deviation confidence

# Benchmark the algorithm on all available instances
def benchmark(algo, isRandom=False):
    allInstancesPath = [join("./instances", f) for f in listdir("./instances") if isfile(join("./instances", f))]
    instances = [Instance(path) for path in allInstancesPath] # Load all instances
    results = []    # List of tuples (distance, optimal), one for each instance (mean if random)
    
    if isRandom:
        for instance in instances:
            sample = []
            for i in range(sampleSize):
                algo.reset(instance)
                instance.run(algo)
                sample.append(algo.distance)
            sampleMoy = sum(sample) / sampleSize
            sem = stats.sem(sample)
            if sem == 0:
                results.append((sampleMoy, sampleMoy, sampleMoy, instance.optimal))
            else:
                (lower_bound, upper_bound) = norm.interval(confidence, loc=sampleMoy, scale= stats.sem(sample))
                results.append((sampleMoy, lower_bound, upper_bound, instance.optimal))
    else:
        for instance in instances:
            algo.reset(instance)
            instance.run(algo)
            results.append((algo.distance, algo.distance, algo.distance, instance.optimal))
            print("\n")
    
    print(results)
    print("\n")

    ratios = [dist / optimal for (dist, lower, upper, optimal) in results]
    print(ratios)
    print("\n")

    moy = sum(ratios) / len(ratios)
    print("Moyenne du benchmark: " + str(moy))

    lowers = [lower / optimal for (dist, lower, upper, optimal) in results]
    uppers = [upper / optimal for (dist, lower, upper, optimal) in results]

    lowerMoy = sum(lowers) / len(lowers)
    upperMoy = sum(uppers) / len(uppers)

    print("Intervalle de confiance: [" + str(lowerMoy) + ", " + str(upperMoy) + "]")
