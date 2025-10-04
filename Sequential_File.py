# Sequential File Allocation

# input disk size
n = int(input("Enter total number of disk blocks: "))

# initialize disk
disk = [0]*n

# input number of files
f = int(input("Enter number of files: "))

# file details
files = {}

# allocate sequentially
for i in range(f):
    name = input(f"\nEnter file name {i+1}: ")
    start = int(input("Enter starting block: "))
    length = int(input("Enter length of file: "))

    # check space
    if start+length > n:
        print("Not enough space!")
        continue
    
    allocated = True
    for j in range(start, start+length):
        if disk[j] == 1:
            allocated = False
            break
    
    if allocated:
        for j in range(start, start+length):
            disk[j] = 1
        files[name] = (start, length)
        print(f"File {name} allocated from block {start} to {start+length-1}")
    else:
        print(f"File {name} cannot be allocated (space occupied)")

# print allocation
print("\nFile\tStart\tLength")
for name, (start, length) in files.items():
    print(f"{name}\t{start}\t{length}")
