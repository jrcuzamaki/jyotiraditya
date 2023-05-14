def generate_substrings(string):
    stack = []
    for c in string:
        if c == '\b':
            if stack:
                stack.pop()
        else:
            stack.append(c)
            yield ''.join(stack)

# Ask the user to enter a string
string = input("Enter a string: ")

# Generate all substrings where a backspace is encountered
substrings = list(generate_substrings(string))

# Print out the substrings
print("Substrings where backspaces are encountered:")
print(substrings)
