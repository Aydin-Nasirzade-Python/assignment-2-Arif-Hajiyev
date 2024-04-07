#import libraries here

def main():
  a=input('Enter name of the month [ex. June]: ')
  b=int(input('Enter the day [ex. 5]: '))
  if (a=='December' and 21<=b<=31) or a=='January' or (a=='February' and 1<=b<=29) or (a=='March' and 1<=b<=19):
    print(f"{a} {b} is in Winter")
  elif (a=='March' and 20<=b<=31) or a=='April' or a=='May' or (a=='June' and 1<=b<=20):
    print(f"{a} {b} is in Spring")
  elif (a=='June' and 21<=b<=30)  or a=='July' or a=='August' or (a=='September' and 1<=b<=21):
    print(f"{a} {b} is in Summer")
  elif (a=='September' and 22<=b<=30)  or a=='October' or a=='November' or (a=='December' and 1<=b<=20):
    print(f"{a} {b} is in Fall")
  else:
    print('Enter correct month and day!')

  pass

if __name__ == "__main__":
  main()
