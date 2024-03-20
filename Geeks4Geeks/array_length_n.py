n = int(input("Enter an odd or even number: "))
arr = list(map(int, input("Enter the array: ").strip().split()))

def odd_even_array(arr,n):
    if n%2 == 0:
        return 0
    sum = 0
    for i in range(n): 
        sum += arr[i]
    return sum
print(n, "is even so sum is: ", odd_even_array(arr,n))
