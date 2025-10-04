# Round Robin Scheduling

# input processes
n = int(input("Enter number of processes: "))
bt = []  # burst time
for i in range(n):
    bt.append(int(input(f"Enter burst time for P{i+1}: ")))

# time quantum
q = int(input("Enter time quantum: "))

rem_bt = bt[:]     # remaining burst
wt = [0]*n         # waiting time
tat = [0]*n        # turnaround time
t = 0              # current time

# round robin loop
while True:
    done = True
    for i in range(n):
        if rem_bt[i] > 0:
            done = False
            if rem_bt[i] > q:
                t += q
                rem_bt[i] -= q
            else:
                t += rem_bt[i]
                wt[i] = t - bt[i]
                rem_bt[i] = 0
    if done:
        break

# calculate turnaround
for i in range(n):
    tat[i] = wt[i] + bt[i]

# calculate averages
avg_wt = sum(wt)/n
avg_tat = sum(tat)/n

# print result
print("\nProcess\tBT\tWT\tTAT")
for i in range(n):
    print(f"P{i+1}\t{bt[i]}\t{wt[i]}\t{tat[i]}")

print(f"\nAverage Waiting Time = {avg_wt:.2f}")
print(f"Average Turnaround Time = {avg_tat:.2f}")
