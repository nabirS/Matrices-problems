def matrics_add(X):
    result =[ [0, 0],
              [0, 0],
              [0, 0] ]
    
    #Iteration in row ways.
    for i in range(len(X)):
        #iteration in coloumn ways.
        for j in range(len(X[0])):                
            result[j][i] = X[i][j]

    return result

X = [ [1, 2, 3],
      [4, 5, 6] ]

print(matrics_add(X))

#------ListComprehension---------
# def matrics_add(X):
#     # #Iteration in row ways.
#     # for i in range(len(X)):
#     #     #iteration in coloumn ways.
#     #     for j in range(len(X[0])):                
#     #         result[j][i] = X[i][j]
#     result =[[result[j][i] = X[i][j] for j in range(len(X[0]))] for i in range(len(X))]
                       
#     return result

# X = [ [1, 2, 3],
#       [4, 5, 6] ]

# print(matrics_add(X))