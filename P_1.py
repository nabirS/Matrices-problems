def matrics_add(X,Y):
    result =[ [0, 0],
              [0, 0] ]
    
    #Iteration in row ways.
    for row in range(len(X)):
        #iteration in coloumn ways.
        for col in range(len(X[0])):
            result[row][col] = X[row][col] + Y[row][col]

    return result

X = [ [1, 2],
      [3, 4] ]

Y = [ [5, 6],
      [7, 8] ]
print(matrics_add(X,Y))

#----Using listComprehension----------

# def matrics_add(X,Y):
#     result = [[X[row][col] + Y[row][col] for col in range(len(X[0]))] for row in range(len(X)) ]
 
#     return result

# X = [ [1, 2],
#       [3, 4] ]

# Y = [ [5, 6],
#       [7, 8] ]
# print(matrics_add(X,Y))

