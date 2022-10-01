def machine():
    keys = 'abcdefghijklmnopqrstuvwxyz !'
    value = keys[-1] + keys[0:-1]
    enctypy = dict(zip(keys,value))
    decrypt = dict(zip(value,keys))
    message = input("please enter ur secret message: ")        
    mode = input("please enter ur choice Encode(E) Or decode(D): ")
    if(mode.upper() == 'E'):
        newmessage = ''.join(enctypy[letter] for letter in message.lower())
    elif mode.upper() == 'D':
        newmessage = ''.join(decrypt[letter] for letter in message.lower())
    else:
        print("please enter a current choice")
    return newmessage

print(machine())