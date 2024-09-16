# Write python program to test wheater passed letter is wovel or not.

inp = input("Enter word=")
vowels = ('a', 'e', 'i', 'o', 'u')
inp=inp.lower()
for ch in inp:
    if ch in vowels:
        print(f"{ch} is wovel")
    else:
         print(f"{ch} is not vowel.")