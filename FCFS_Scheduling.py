# FCFS Scheduling

# input processes
n = int(input("Enter number of processes: "))
bt = []  # burst time

# take burst times
for i in range(n):
    bt.append(int(input(f"Enter burst time for P{i+1}: ")))

wt = [0]*n  # waiting time
tat = [0]*n # turnaround time

# calculate waiting
for i in range(1, n):
    wt[i] = wt[i-1] + bt[i-1]

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
