import random
a=range(1,81)
random.shuffle(a)
ans='.'*100
ans=list(ans)
for x in xrange(0,9):
    ans[a[x]]=chr(ord('1')+x)
print ''.join(ans)