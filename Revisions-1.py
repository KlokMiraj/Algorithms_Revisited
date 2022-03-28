def insertion(a):
   
    for i in range(len(a)):
        key=a[i]
        j=i-1
        while a[j]>key and j>=0:
           a[j+1]=a[j]         
           j=j-1
           a[i-j]=key
           print(a)
        
insertion([1,4,5,8,3])
