def minimum(arr):
    arr.sort()
    return arr[0]
def maximum(arr):    
    arr.sort()
    return arr[len(arr)-1]
if __name__=="__main__":
    arr=[4,6,2,1,9,63,-134,566]
    print("Minimum {}".format(minimum(arr)))
    print(f"Maximum {maximum(arr)}")
