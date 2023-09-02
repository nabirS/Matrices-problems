def matrics_add(X):
    s=0
    k=0
    for i in range(len(X)):
        #iteration in coloumn ways.
        for j in range(k, i+1):               
            s+=X[i][j]
            j=j+1
            k=j

    return s

X = [ [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9] ]

print(matrics_add(X))