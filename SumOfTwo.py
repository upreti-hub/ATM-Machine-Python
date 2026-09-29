array = [2, 4, 6, 8, 3]
target = 10
for i in range(len(array)):
  for j in range(i+1, len(array)):
    if array[i]+array[j] == target :   
      print("our two numbers whose sum is 10 are",array[i],array[j])