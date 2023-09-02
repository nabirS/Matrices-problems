def matrics_add(X):
    for row in range(len(X)):
        #iteration in coloumn ways.
        for col in range(len(X[0])): 
            # Check 1 in diagonally and 0 for others. 
            if((row != col) and (X[row][col]!=0)):
                return False
            elif((row == col) and (X[row][col]!=1)):
                return False
            
    return True

X = [ [1, 0, 0],
      [0, 1, 0],
      [0, 0, 1] ]

print(matrics_add(X))