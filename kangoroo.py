def kangaroo(x1, v1, x2, v2):
    result = 0

    for i in range(10000):

        # initial location + jump distance = kangoroo location
        x = x1 + (v1 * i)
        y = x2 + (v2 * i)
        if x == y:
            result = 1
            break
            
    return result

#main      
x1, v1, x2, v2 = map(int,input().split())
result = kangaroo(x1, v1, x2, v2)
if result:
  print ('YES', sep='\n')
else :  print ('NO', sep='\n')