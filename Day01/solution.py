file = open("input.txt", "r") 
sum = 0
for line in file: 
  sum += int(int(line)/3) - 2      

print(sum)
