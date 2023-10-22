def cereal_box_decoder(string):
    s = string.split(',')
    msg = ''
    for i in range(len(s)):
        msg += chr(int(s[i]))
    return msg

def cereal_box_encoder(string):
    msg = str(ord(string[0]))
    for i in range(1, len(string)):
        msg += ',' + str(ord(string[i]))
    return msg

def main():
    encoded = cereal_box_encoder('This is a message')
    msg = cereal_box_decoder(encoded)
    print(msg)

main()