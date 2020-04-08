r = int(input("Enter a number: "))
p = 0
q = 1
for i in range(r):
  print(p)
  temp = p
  p = q
  q = temp+p
  
