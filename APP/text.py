from copy import copy, deepcopy
from pickle import dumps, loads
a=[1,2,3]
b=[a]*3
c=copy(b)
d=deepcopy(b)
e=loads(dumps(b,4))
# b[1].append(999)  #[[1,2,3],[1,2,3,999],[1,2,3]]
# c[1].append(999)
d[1].append(999)
e[1].append(999)
print(e)