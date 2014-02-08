string = ""
for word in raw_input():
    if word not in "AEIOUaeiou":
        string += word
print string
