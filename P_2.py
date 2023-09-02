def matrics_add(X,Y):
    result =[ [0, 0],
              [0, 0] ]
    
    #Iteration in row ways.
    for row in range(len(X)):
        #iteration in coloumn ways.
        for col in range(len(X[0])):
            s=0
            for k in range(len(X[0])):
                s+= X[row][k] * Y[k][col]
                result[row][col] = s
                
    return result

X = [ [1, 2],
      [3, 4] ]

Y = [ [5, 6],
      [7, 8] ]
print(matrics_add(X,Y))