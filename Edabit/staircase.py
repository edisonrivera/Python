def staircase(levels:int) -> None:
    und = "_"
    ha = "#"
    if levels > 0:
        for level in range (levels):
            n_ha = level + 1
            n_und = levels - n_ha
            print(und*n_und + ha*n_ha)
    else:
        levels = abs(levels)
        for level in range (levels,0,-1):
            n_und = levels - level
            print(und*n_und + ha*level)

    
if __name__ == "__main__": 
    staircase(-8)