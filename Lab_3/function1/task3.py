def solve(numheads, numlegs):
    for rab in range(numheads+1):
        chick=numheads-rab
        if(2*chick+4*rab)==numlegs:
            return rab,chick
    return None

print(solve(35, 94))