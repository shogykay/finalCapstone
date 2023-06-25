

def encrypt_text(yourtext,n):
    result = ""
    # iterate over the given text
    for i in range(len(yourtext)):
        ch = yourtext[i]
        
        # check if space is there then simply add space
        if ch==" ":
            result+=" "
        # check if a character is uppercase then encrypt it accordingly 
        elif (ch.isupper()):
            result += chr((ord(ch) + n-65) % 26 + 65)

        # check if a character is lowercase then encrypt it accordingly
        
        else:
            result += chr((ord(ch) + n-97) % 26 + 97)
    
    return result

yourtext = input("Enter text to encrypt:\n>")
n = 15
print("Cipher Text is : " + encrypt_text(yourtext,n))


