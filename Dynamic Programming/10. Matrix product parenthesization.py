P = [3, 100, 2]

def matrix_chain_ordering(P):
    M = [[9999 for i in range(len(P))] for j in range(len(P))]
    for i in range(len(P)):
        M[i][i] = 0
    for l in range(2, len(P)):
        for i in range(1, len(P)-l+i+1):
            j = i+l-1
            for k in range(i, j-i+1):
                cost = M[i][j] + M[k+1][j] + P[i-1]*P[k]*P[j]
                if cost < M[i][j]:
                    M[i][j] = cost
    for m in M:
        print(m)


matrix_chain_ordering(P)