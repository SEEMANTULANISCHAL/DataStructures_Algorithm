# I need to find the key element in a given array

n = int(input("Enter the number: "))
arr = list(map(int, input("Enter the array: ").strip().split()))
x = int(input("Enter the key element: "))

def key_element(n,arr,x):
    for i in range(0, n):
        if arr[i] == x:
            return True
        else:
            return False
            
if key_element(n,arr,x):
        print("The key is present in the array")
else:
        print("They key is not present in the array")
