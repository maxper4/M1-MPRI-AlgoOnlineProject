# Algo Online Project
1 week project of Probabilistic algorithms and Games theory. 

The goal is to solve the problem of k-servers which can be described as follows:
- k mobile technicians (servers), {s1, s2, . . . , sk}, provide maintenance service to n customers,
- the technicians treat requests emanating from the customers’ sites; these requests arrive in series of length
N , (r1, r2, . . . , rN ),
- a request must be processed immediately (it is impossible to put it on hold)

----

Launch scripts (in Algos.py): 
- start specific instance
> instance = Instance("instances/instance_N200_OPT221.inst")

> algo = Periodic(instance)

> instance.run(algo, draw=False)

- benchmark all instances
> algo = FullRandom(None)

>benchmark(algo, isRandom=True)
