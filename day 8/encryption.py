alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
            'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to Encrypt, type 'decode' to Decrypt: \n")
text = input("Type your message : \n").lower()
shift = int(input("Type the Shift Number : \n"))

def ceasar(text, shift, direction):
    end_text = ""
    if direction == "decode":
        shift *= -1
        
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift
        end_text += alphabet[new_position]
    print (f"The {text}d text is : {end_text}")

    
ceasar(text, shift, direction)
