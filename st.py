
string = input("Enter a string: ")
sub_string = input("Enter a substring to count and replace: ")
new_sub_string = input("Enter the new substring to replace with: ")
count = string.count(sub_string)
new_string = string.replace(sub_string, new_sub_string)
print("Original string:", string)
print(f"The substring '{sub_string}' appears {count} times.")
print("New string:", new_string)
