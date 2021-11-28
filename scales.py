print(' _  '*5)
print('/ \\' + '_/ \\'*4)
print('\_/ '*5)
print('  ' + '\_/ '*4)
print('  '*2 + '\_/ '*3)
print('  '*3 + '\_/ '*2)
print('  '*4 + '\_/ '*1)

# original attempt (106 chars)
def scales(n):print(' _  '*n,('/ \\_'*n)[:-1],'\_/ '*n,*('  '*i+'\_/ '*(n-i)for i in range(1,n)),sep='\n')

# after discussing with Clarence (96 chars)
def scales(n):print(' _  '*n,('/ \\_'*n)[:-1],*('  '*i+'\\_/ '*(n-i)for i in range(n)),sep='\n')

# further reduction (94 chars)
def scales(n):print(' _  '*n,('/ \_'*n)[:-1],*('  '*i+'\_/ '*(n-i)for i in range(n)),sep='\n')

for i in range(0,10):
    print(f'\nscales({i})')
    scales(i)

