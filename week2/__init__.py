q = lambda f:[[f(i,j) for j in range(9)] for i in range(9)]
print q(lambda a,b: "%s, %s"%(a,b))