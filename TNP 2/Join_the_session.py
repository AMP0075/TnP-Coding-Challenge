try:
    a=[int(items) for items in input().split()]
    d=a[0]
    g=a[1]
    l=a[2]
    t_tnp=d*60
    t_left=l-t_tnp
    print(int(t_left/g))
except(ValueError):
    pass
