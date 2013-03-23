pfacs = []
def pfac(n):
    d=2
    while (n > 1):
        while (n%d==0):
            pfac.append(d)
            n = n/d
        d+=1
        
    return pfac
    
pfs = pfac(10)
lfp=pfac[-1]
print lfp
