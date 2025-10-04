# LRU Page Replacement

# input reference string
n = int(input("Enter number of pages: "))
pages = list(map(int, input("Enter page reference string: ").split()))

# input frame size
f = int(input("Enter number of frames: "))

frames = []   # page frames
faults = 0    # page faults

# simulate LRU
for i in range(n):
    p = pages[i]
    if p not in frames:
        if len(frames) < f:
            frames.append(p)
        else:
            # find LRU
            lru_index = min(range(len(frames)), key=lambda x: 
                            max((j for j in range(i-1, -1, -1) if pages[j] == frames[x]), default=-1))
            frames[lru_index] = p
        faults += 1
    print("Frames:", frames)

# print result
print("\nTotal Page Faults =", faults)
