r,c=map(int,input().split())
s=0
mat=[list(map(int,input().split())) for i in range(r)]
for i in range(r):
    for j in range(c):
        s=s+mat[i][j]
print(s)