# FIFO Page Replacement

# input reference string
n = int(input("Enter number of pages: "))
pages = list(map(int, input("Enter page reference string: ").split()))

# input frame size
f = int(input("Enter number of frames: "))

frames = []   # page frames
faults = 0    # page faults
idx = 0       # index pointer

# simulate FIFO
for p in pages:
    if p not in frames:
        if len(frames) < f:
            frames.append(p)
        else:
            frames[idx] = p
            idx = (idx + 1) % f
        faults += 1
    print("Frames:", frames)

# print result
print("\nTotal Page Faults =", faults)
