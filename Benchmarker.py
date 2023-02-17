from os import listdir
from os.path import isfile, join
from instanceParser import Instance

sampleSize = 100

def benchmark(algo, isRandom=False):
    allInstancesPath = [join("./instances", f) for f in listdir("./instances") if isfile(join("./instances", f))]
    instances = [Instance(path) for path in allInstancesPath]
    results = []
    
    if isRandom:
        for instance in instances:
            sample = []
            for i in range(sampleSize):
                algo.reset(instance)
                instance.run(algo)
                sample.append(algo.distance)
            sampleMoy = sum(sample) / sampleSize
            results.append((sampleMoy, instance.optimal))
    else:
        for instance in instances:
            algo.reset(instance)
            instance.run(algo)
            results.append((algo.distance, instance.optimal))
            print("\n")
    
    print(results)
    print("\n")

    ratios = [(optimal / dist) * 100 for (dist, optimal) in results]
    print(ratios)
    print("\n")

    moy = sum(ratios) / len(ratios)
    print("Moyenne du benchmark: " + str(moy))