def generateKey(seed):
    key = 0
    for c in seed:
        key += ord(c) * ord(c)
    return key

def encrypt(input_text, key, reverse=False):
    if reverse: 
        return decrypt(input_text, key) 
    else:
        num_c = []
        for c in input_text:
            num_c.append(ord(c) + int(key))
        output_text = ''
        for c in num_c:
            output_text += chr(c)
        return output_text

def decrypt(input_text, key):
    vect = []
    for c in input_text:
        vect.append(ord(c))
    output_text = ''
    for c in vect:
        output_text += chr(c - int(key))
    return output_text;