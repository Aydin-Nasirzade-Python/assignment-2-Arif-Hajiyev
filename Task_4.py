#import libraries here

def main():
  a=int(input('Enter the year [ex. 2021]: '))
  if a<=0:
    print('Invalid year!')
  elif (a-8)%12==0:
    print(f"{a} is the year of the Dragon")
  elif (a-9)%12==0:
    print(f"{a} is the year of the Snake")
  elif (a-10)%12==0:
    print(f"{a} is the year of the Horse")
  elif (a-11)%12==0:
    print(f"{a} is the year of the Sheep")
  elif a%12==0:
    print(f"{a} is the year of the Monkey")
  elif (a-1)%12==0:
    print(f"{a} is the year of the Rooster")
  elif (a-2)%12==0:
    print(f"{a} is the year of the Dog")
  elif (a-3)%12==0:
    print(f"{a} is the year of the Pig")
  elif (a-4)%12==0:
    print(f"{a} is the year of the Rat")
  elif (a-5)%12==0:
    print(f"{a} is the year of the Ox")
  elif (a-6)%12==0:
    print(f"{a} is the year of the Tiger")
  elif (a-7)%12==0:
    print(f"{a} is the year of the Hare")
  pass

if __name__ == "__main__":
  main()
