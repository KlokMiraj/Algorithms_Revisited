class Search():
    
    def recBinarySearch(self,arr, left,right,x):
        if(right>=1):
            mid=left+(right-1)/2

            if(arr[mid] == x):
                return mid
            if(arr[mid]>x):
                return self.recBinarySearchrecBinarySearch(arr,left,mid-1,x)

            return self.recBinarySearch(arr,mid+1,right,x)
        return -1

    
    def BinarySearch(self,arr,left,right,x):
        while(left <=right):
             mid=left+(right-1)/2

             if(arr[mid] == x):
                 return mid
             if(arr[mid]<x):
                 left=mid+1
             else:
                 r=mid-1
        return -1

def main():
    arr=[1,2,3,5]
    size=len(arr)
    find=3
    exc=Search()
    print(exc.recBinarySearch(arr,0,size-1,find))
    print(exc.BinarySearch(arr,0,size-1,find))

if __name__=="__main()__":
    main()
