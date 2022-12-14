abc = "abcdefghijklmonpqrstuvwxyz"

def normalize(rot : int, base : int):
    while rot > base:
        rot -= base
    return rot

def lshift(text : str, times : int):
    for i in range(times):
        text = text[1:] + text[0]
    return text


def encrypt(text : str, key : str):
    if not text.isalpha() or not key.isalpha():
        raise TypeError("key or text should only be letters")
    text = text.lower()
    key = key.lower()
    rotmax = len(key)
    rot = -1
    abc2 = ""
    out = ""
    keys = []
    counter = -1
    counter2 = -1
    # get alphabet keys
    for letter in key:
        for letter2 in abc:
            rot += 1
            if letter == letter2:
                abc2 = lshift(abc, rot)
                break
        keys += [abc2]
        rot = -1
    #print(keys)

    # get cyphertext
    for letter in text:
        counter += 1
        for letter2 in abc:
            counter2 += 1
            if letter == letter2:
                out += keys[normalize(counter, rotmax) - 1][counter2]
                counter2 = -1
                break
    return out

def decrypt(text : str, key : str):
    if not text.isalpha() or not key.isalpha():
        raise TypeError("key or text should only be letters")
    text = text.lower()
    key = key.lower()
    rotmax = len(key)
    rot = -1
    abc2 = ""
    out = ""
    keys = []
    counter = -1
    counter2 = -1
    #get alphabet keys
    for letter in key:
        for letter2 in abc:
            rot += 1
            if letter == letter2:
                abc2 = lshift(abc, rot)
                break
        keys += [abc2]
        rot = -1
    
    #print(keys)

    #get plaintext
    for letter in text:
        counter += 1
        for letter2 in keys[normalize(counter, rotmax) - 1]:
            counter2 += 1
            if letter == letter2:
                out += abc[counter2]
                counter2 = -1
                break
    return out