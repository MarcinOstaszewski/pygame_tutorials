wywolania = 0

def F(x):
  global wywolania
  wywolania += 1
  if x == 0:
    return 0
  else:
    return 2 + F(x // 2)

# x = 35
# print(F(x), f"X: {x}, wywolania: {wywolania}")
  
# wywolania, x = 0, 4
# x= 7
# print(F(x), f"X: {x}, wywolania: {wywolania}")
# wywolania, x = 0, 16
# print(F(x), f"X: {x}, wywolania: {wywolania}")
# wywolania, x = 0, 35
# print(F(x), f"X: {x}, wywolania: {wywolania}")
# wywolania, x = 0, 3
# print(F(x), f"X: {x}, wywolania: {wywolania}")

for x in range(100, 120):
  wywolania = 0
  print(f"X: {x}, F(x): {F(x)}, wywolania: {wywolania}")