print("welcome to ceaser cypher")
direction=str(input("type 'encode' to encrypt and 'decode' to decrypt"))
pext=(str(input("type the file directory you want to encode or decode"))).lower()
text=pext.strip(' ')
shift=int(input("enter the shift number"))
cipher_text = ''
li=[]


def ceaser(text1,shift1):
    global cipher_text
    alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for letter in text1:
        if letter in alphabet:
            alphabet_index=alphabet.index(letter)
            if direction == "encode":
                new_alphabet=(alphabet_index+shift1)%26
            elif direction == "decode":
                new_alphabet = (alphabet_index-shift1)%26
            a=alphabet[new_alphabet]
            cipher_text+=a
        else:
            cipher_text+=letter
    return cipher_text
with open(text, 'r') as file:
    for line in file:
        ceaser(line, shift)
with open(text,'w') as file:
    file.write(cipher_text)