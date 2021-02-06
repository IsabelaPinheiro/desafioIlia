s = []
for i in range (0,3):
  a, b, c = map(int,input().split())
  s.append(a)
  s.append(b)
  s.append(c)
# print(s)

# only magic squares possible for a square 3x3 fom 1 to 9, total = 8
magic_squares = [
      [8, 3, 4, 1, 5, 9, 6, 7, 2],
      [8, 1, 6, 3, 5, 7, 4, 9, 2],
      [6, 7, 2, 1, 5, 9, 8, 3, 4],
      [6, 1, 8, 7, 5, 3, 2, 9, 4],
      [4, 9, 2, 3, 5, 7, 8, 1, 6],
      [4, 3, 8, 9, 5, 1, 2, 7, 6],
      [2, 9, 4, 7, 5, 3, 6, 1, 8],
      [2, 7, 6, 9, 5, 1, 4, 3, 8]
  ]
# print(magic_squares)  
costs = []

# compares every item s with the magic_squares
for item in magic_squares:

  # makes the cost betwen the magic-squares and the s into a list of costs 
  costs.append(sum([abs(item[i] - s[i]) for i in range(0,9)]))

#print(costs)  
print(min(costs), sep='\n')
