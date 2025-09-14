#1
a = list(map(int,input().split()))
n = a[0]
a.pop(0)
for i in range(1, n+1):
    if i not in a:
        print(i)
        break

#2
a, b = input().split()
n = int(a)
z = str()
for i in range(0, len(b), n):
    m = b[i:(i+n)]
    k = len(b)
    z += m[-1:0:-1] + m[0]
print(z)

#3
s = input()
n = 0
for i in range(len(s)):
    if s[i] in 'AHIMOYUVWXY18EJSZ3L25':
        n+=1
if len(s) != n:
    if s == s[::-1]:
        print('"', s, ' is a regular palindrome.', '"', sep= '')
    else:
        print('"', s, ' is not a palindrome.', '"', sep= '')
else:
    q = str()
    for i in range(len(s)):
        if s[i] == 'E':
            q = '3' + q
        elif s[i] == '3':
            q = 'E' + q
        elif s[i] == 'J':
            q = 'L' + q
        elif s[i] == 'L':
            q = 'J' + q
        elif s[i] == 'S':
            q = '2' + q
        elif s[i] == '2':
            q = 'S' + q
        elif s[i] == 'Z':
            q = '5' + q
        elif s[i] == '5':
            q = 'Z' + q
        else:
            q = s[i] + q
    if q == s and q == q[::-1]:
        print('"', s, ' is a mirrored palindrome.', '"', sep= '')
    elif q == s:
        print('"', s, ' is a mirrored string.', '"', sep= '')
    else:
        print('"', s, ' is not a palindrome.', '"', sep= '')

#4
a = list(map(int,input().split()))
for i in range(0, len(a)-(len(a)%2), 2):
    a[i], a[i+1] = a[i+1], a[i]
print(*a)

#5
a = list(map(int, input().split()))
q = [a[-1]] + a[:-1]
print(*q)

#6
a = list(map(int,input().split()))
for i in range(len(a)):
    if a.count(a[i])==1:
        print(a[i], end=' ')

#7
a = list(map(int,input().split()))
q = 0
for i in range(len(a)):
    if a.count(a[i])>q:
        q = a.count(a[i])
        z = a[i]
print(z)

#8
n = int(input())
a = list(map(int,input().split()))
for i in range(n):
    m = 0
    for e in range(n):
        if a[i]>a[e]:
            q = 1
        elif a[i]<a[e]:
            q = -1
        else:
            q = 0
        m+=q
    if m==0:
        print(a[i])
        break

#9
f = open('input.txt')
q = f.readline()
alf = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
zn = '.!?'
n = 0
for i in range(len(q)-1):
    if q[i] in alf and q[i+1] in zn:
        n+=1
print(n)
f.close()

#10
s = input()
glas = 'аеёиоуыэюя'
sogl = 'бвгджзйклмнпрстфхцчшщъь'
q = s[0]
for i in range(1, len(s)):
    q += s[i]
    if s[i] in glas and s[i-1] in sogl:
        q = q + 'с' + s[i]
print(q)