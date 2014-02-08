def hex_to_bin(num_hex):
    return bin(int('0x'+num_hex, 16))

def validate_hex(num_hex):
    for ch in num_hex:
        if not ch in '0123456789ABCDEF':
            return False
    return True

num_hex = raw_input()
if not validate_hex(num_hex):
    print "Error"
else:
    print ['S', 'D'][hex_to_bin(num_hex).find('10010110') != -1]
