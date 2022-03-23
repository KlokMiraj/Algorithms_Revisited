def insertion(a):
    comp=4
    for comp in range(len(a)):
        key=a[comp]

        i=comp-1

        while i>0 and a[i]>key:
            a[i+1]=a[i]
            i=i-1
            a[i+1]=key
            print(a) 
    

insertion([2,3,7,8,5,1])