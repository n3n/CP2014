encryp = [ord(i) for i in raw_input()]
cnt = 1
decryp = ''
for word in encryp:
    if 97 <= word <= 122:
        decryp += chr(97 + (word - 97 + cnt) % 26)
        cnt += 1
    elif 65 <= word <= 90:
        decryp += chr(65 + (word - 65 + cnt) % 26)
        cnt += 1
    else:
        decryp += chr(word)
print decryp
