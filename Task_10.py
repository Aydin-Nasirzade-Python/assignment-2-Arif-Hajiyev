#import libraries here

def main():
  x=float(input('Enter x: '))
  y=float(input('Enter y: '))
  if y>x**2 and (x>0 and y>4-x**2 or y<2-x and x<0 and y<4-x**2) or y<x**2 and (x<0 and y>2-x or x>0 and y<2-x):
    print('The point is in the shaded area')
  else:
    print('The point is not in the shaded area')
  pass

if __name__ == "__main__":
  main()
