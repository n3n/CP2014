def count(message, char):
    count = 0
    for letter in message:
        if letter == char:
            count += 1
    return count


print count('banana','n')
