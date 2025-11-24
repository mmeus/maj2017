A = [7, 5, 11, 33]
n = len(A)
p = 3

maks_l = 0
maks_l2 = 0
for l in A:
    if l > maks_l and l % p != 0:
        maks_l = l
        '''break
    if l > maks_l2 and l % p != 0:
        maks_l2 = l'''
for l in A:
    if l > maks_l2 and l != maks_l and l % p != 0:
        maks_l2 = l
s = maks_l * maks_l2
print(s)
