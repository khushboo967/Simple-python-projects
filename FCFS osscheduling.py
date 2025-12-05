n = int(input("Enter number of processes: "))
at = list(map(int, input("Enter arrival times: ").split()))
bt = list(map(int, input("Enter burst times: ").split()))


procs = sorted(zip(range(1, n+1), at, bt), key=lambda x: x[1])

ct = []
time = 0
for p, a, b in procs:
    time = max(time, a) + b
    ct.append(time)

tat = [ct[i] - procs[i][1] for i in range(n)]
wt  = [tat[i] - procs[i][2] for i in range(n)]

print("\nP\tAT\tBT\tCT\tWT\tTAT")
for i in range(n):
    p, a, b = procs[i]
    print(f"P{p}\t{a}\t{b}\t{ct[i]}\t{wt[i]}\t{tat[i]}")

print("\nAverage WT =", sum(wt)/n)
print("Average TAT =", sum(tat)/n)
