# Write a Python program to count the number of characters (character frequency) in a string

name = input('Enter your name=')
name=name.lower()
chr_count={}
for ch in name:
    if ch in chr_count:
        chr_count[ch]+=1
    else:
        chr_count[ch]=1
print(chr_count)                