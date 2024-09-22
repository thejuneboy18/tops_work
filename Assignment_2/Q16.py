#Write a Python program to count the occurrences of each word in a given sentence

main_string = input("Enter main string=")
main_string = main_string.split()
sub_string = input("Enter sub string=")

count_sub = main_string.count(sub_string)

print(f"The Substring {sub_string} occures {count_sub} times.")
