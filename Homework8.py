#task1
A = {'Andrii', 'Petro', 'Ivan', 'Myhailo', 'Myron'}  #Septemper
B = {'Stephan', 'Petro', 'Illlia', 'Myhailo', 'Sonnya'}  #October
union_set = A.union(B)
print(union_set)
deptor_October = B.difference(A)
print(deptor_October)

#task2
permissions = {}
n = int(input('Put the number of files: '))
for _ in range(n):
    s = input().split()
    permissions[s[0]] = set(s[1:])
for _ in range(int(input('Put the number of files for checking: '))):
    perm, file = input().split()
    if perm == 'read':
        perm = 'R'
    if perm == 'write':
        perm = 'W'
    if perm == 'execute':
        perm = 'X'
    if perm in permissions[file]:
        print('OK')
    else:
        print('Access denied')







