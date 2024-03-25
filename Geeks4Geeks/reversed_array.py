def reversed_array(arr):
  reverse = arr[::-1]
  print("Reversed array: ", end="")
  for i in reverse:
    print(i, end=" ")  
    
original_array = [10,20,30,40,50]
reversed_array(original_array)
