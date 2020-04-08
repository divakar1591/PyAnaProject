def myfun(*args):
  print(f"All values: {args}")
  print(f"Pos-0 value: {args[0]}")

def myfun2(x, y):
  print(f"All values: {x*2}")

# myfun(1,2,3)

num = [1,2,3]
myfun(*num)

num2 = {"x":5, "y":2}
myfun2(**num2)

