def sample(a):
    for i in range(len(a)):
        if a[i] in 'aeiouAEIOU':
            yield a[i]
            yield i
out=sample('god father anil')
res=''
for i in out:
    res+=str(i)
print(res)
