# My answer
a, b = map(int, input().strip().split(' '))
c = a // b
d = a % b
print(c, d)

# pythonic
a, b = map(int, input().strip().split(' '))
print( *divmod(a, b) )
