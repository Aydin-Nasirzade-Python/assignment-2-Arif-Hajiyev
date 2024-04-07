#import libraries here

def main():
  a=input('Enter a letter of the alphabet: ')
  b='aeiou'
  if a in b:
    print('Entered alphabet is a vowel!')
  elif a=='y':
    print('Sometimes it is a vowel, and sometimes it is a consonant!')
  else:
    print('Entered alphabet is a consonant!')
  pass

if __name__ == "__main__":
  main()
