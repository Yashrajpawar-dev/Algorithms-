# Banker's Algorithm

# input processes, resources
n = int(input("Enter number of processes: "))
m = int(input("Enter number of resources: "))

# input allocation
alloc = []
print("Enter Allocation Matrix:")
for i in range(n):
    alloc.append(list(map(int, input().split())))

# input max matrix
maxm = []
print("Enter Max Matrix:")
for i in range(n):
    maxm.append(list(map(int, input().split())))

# input available
avail = list(map(int, input("Enter Available Resources: ").split()))

# need matrix
need = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        need[i][j] = maxm[i][j] - alloc[i][j]

# initialize work
work = avail[:]
finish = [0]*n
safe_seq = []

# check safety
while len(safe_seq) < n:
    found = False
    for i in range(n):
        if not finish[i]:
            if all(need[i][j] <= work[j] for j in range(m)):
                for j in range(m):
                    work[j] += alloc[i][j]
                safe_seq.append(i)
                finish[i] = 1
                found = True
    if not found:
        break

# print result
if len(safe_seq) == n:
    print("\nSystem is in a SAFE state")
    print("Safe Sequence:", " -> ".join("P"+str(i) for i in safe_seq))
else:
    print("\nSystem is in an UNSAFE state")
