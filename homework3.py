#1
def fibb(n):
    if n == 1 or n == 2:
        return 1
    return fibb(n-1) + fibb(n-2)
n = int(input())
print(fibb(n))

#2
def pros(n, k=2):
    if n==1:
        return []
    if n%k==0:
        return [k]+pros(n//k, k)
    else:
        return pros(n, k+1)
n = int(input())
q = pros(n)
print(*q)

#3
def nod(a,b):
    if b==0:
        return a
    else:
        return nod(b, a%b)
a, b = map(int,input().split())
d = nod(a,b)
X = []
Y = []
if (d/b)%1==0.0:
    print(0, d//b, d)
elif (d/a)%1==0.0:
    print(d//a, 0, d)
else:
    x = 1
    for i in range(5):
        if ((d-a*x)/b)%1 == 0.0 and ((d+a*x)/b)%1 == 0.0:
            if x + abs((d-a*x)/b) < abs((d+a*x)/b) - x:
                X.append(x)
                Y.append((d-a*x)//b)
            else:
                X.append(-x)
                Y.append((d+a*x)//b)
        elif ((d-a*x)/b)%1 == 0.0:
            X.append(x)
            Y.append((d-a*x)//b)
        elif ((d+a*x)/b)%1 == 0.0:
            X.append(-x)
            Y.append((d+a*x)//b)

        x+=1
    q = abs(X[0])+abs(Y[0])
    w = abs(X[0])
    x0 = X[0]
    y0 = Y[0]
    for i in range(1, len(X)):
        if abs(X[i])+abs(Y[i])<q:
            q = abs(X[i])+abs(Y[i])
            w = abs(X[0])
            x0=X[i]
            y0 = Y[i]
        elif abs(X[i])+abs(Y[i])==q:
            if abs(X[i])<w:
                q = abs(X[i])+abs(Y[i])
                w = abs(X[0])
                x0=X[i]
                y0 = Y[i]
    print(x0, y0, nod(a,b))

#4
q, a = map(str, input().split())
n = int(q)
if n%2!=0:
    w = n//2+1
    m = w-1
else:
    w = n//2
    m = w
for i in range(1, w+1):
    print(a*i)
for i in range(m, 0, -1):
    print(a*i)

#5
import numpy as np
n, m = map(int, input().split())
st = np.array([0]*m)
matrix = np.array([st]*n)
left = 0
right = m-1
top = 0
bottom = n-1
q = 1
while left<=right and top<=bottom:
    for i in range(left, right+1):
        matrix[top][i] = q
        q+=1
    top+=1
    for i in range(top, bottom+1):
        matrix[i][right] = q
        q+=1
    right-=1
    if top <= bottom:
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = q
            q += 1
        bottom -= 1

    if left <= right:
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = q
            q += 1
        left += 1

print(matrix)

#6
import numpy as np
x = list(map(float, input().split()))
y = list(map(float, input().split()))
def coeff(x, y):
    x = np.array(x)
    y = np.array(y)
    n = len(x)
    sumx = 0
    sumx2 = 0
    sumy = 0
    sumxy = 0
    for i in range(n):
        sumx += x[i]
        sumx2 += (x[i])**2
        sumy += y[i]
        sumxy += x[i]*y[i]
    a = (n*sumxy-sumx*sumy)/(n*sumx2-sumx**2)
    return a
print(coeff(x, y))

#7
n, m = map(int, input().split())
import numpy as np
matrix = np.zeros((n, m))
for i in range(n):
    q = list(map(float,input().split()))
    for e in range(m):
        matrix[i][e] = q[e]

def resh(matrix):

    A = matrix[:, :-1]
    B = matrix[:, -1]

    try:
        solution = np.linalg.solve(A, B)
        return solution
    except np.linalg.LinAlgError as e:
        return e
print(resh(matrix))

#8
import random
import numpy as np
n = int(input())
a = float(input())
b = float(input())
std = float(input())
def generate(n, a, b, std):
    q = []
    for _ in range(n):
        x = random.uniform(-10, 10)
        noise = random.gauss(0, std)
        y = a * x + b + noise
        q.append((x, y))
    return q
print(generate(n, a, b, std))
