import string
b = string.ascii_letters
x = input('Type 2 letters through a hyphen:')
a = x[0]
a = b.find(a)
c = x[2]
c = b.find(c) + 1
print(b[a:c])