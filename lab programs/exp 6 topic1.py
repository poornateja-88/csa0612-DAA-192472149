def merge(a):
    if len(a)>1:
        m=len(a)//2
        l=a[:m]
        r=a[m:]

        merge(l)
        merge(r)

        i=j=k=0

        while i<len(l) and j<len(r):
            if l[i]<r[j]:
                a[k]=l[i]
                i+=1
            else:
                a[k]=r[j]
                j+=1
            k+=1

        while i<len(l):
            a[k]=l[i]
            i+=1
            k+=1

        while j<len(r):
            a[k]=r[j]
            j+=1
            k+=1

a=[38,27,43,3,9,82,10]
merge(a)
print(a)