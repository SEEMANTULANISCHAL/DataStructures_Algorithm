# I need to print the possible pair in an array usig two nested loops
n = int(input("Enter number: "))
a = list(map(int,input("Enter the array:").strip().split()))

def pair(a,n):
    for i in range(n):   #[1,2,3]
        for j in range(n): #[1,2,3]
            if i != j:
                print(a[i], a[j])

pair(a, n)
