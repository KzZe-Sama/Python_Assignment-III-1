# This algorithm is based on recursion
def movement(fro,to):
    print(f"Moved  from {fro} to {to}")
def puzzle(n,origin,target,auxillary):
    # if block is equal to one it moves the block to target
    if n==1:
        movement(origin,target)
    else:
        # here n-1 is the main solver whereas remaining 1 is the base which is kept at target
        # after keeping base block at target we again solve the
        puzzle(n-1,origin,auxillary,target)
        puzzle(1,origin,target,auxillary)
        puzzle(n-1,auxillary,target,origin)

puzzle(3,"Origin","Destination","Temp")