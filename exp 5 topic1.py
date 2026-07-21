a=[[1,2],[1,2]]
b=[[1,2],[1,2]]
c=[[0,0],[0,0]]
for i in range(2):
    for j in range(2):
        for k in range(2):
            c[i][j] = c[i][j] + a[i][k] * b[k][j]
            
print(c)


