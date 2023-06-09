n, k = map(int, input().strip().split())
a = list(map(int, input().strip().split()))

li = [x for x in a if x>0 and x>=a[k-1]]
print(li)
print(*(0<v>=a[k-1]for v in a))
print(sum([]))


inp = lambda: map(int, input().strip().split())
n, k = inp()
a = list(inp())




i=lambda:[*map(int,input().split())]
a,k=i()
l=i()
print(sum(0<v>=l[k-1]for v in l))