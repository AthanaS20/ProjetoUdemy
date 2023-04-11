# count é um interador sem fim (itertools)

from itertools import count

c1 = count(10, 2) #Pode passar o inicio e o pulo, mas não o fim
r1 = range(10)

print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))

for i in c1:
    if i > 50:
        break
    print(i)