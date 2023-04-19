import sys

def main(argv):
  if len(argv) < 2:
    print("\nPlease provide two words to compare (separated by a space, for example: silent listen)\n")
    return
  
  print(is_anagram(argv[0], argv[1]))

def is_anagram(s1: str, s2: str) -> bool:
  return sorted(s1) == sorted(s2)

if __name__ == "__main__":
  main(sys.argv[1:3])