import sys
import random
ans=list(sys.argv[1])
cnt=random.randint(30,60)
a=range(1,81)
random.shuffle(a)
for x in xrange(0,cnt):
    ans[a[x]]='.'
print ''.join(ans)
