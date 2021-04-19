
import sys

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def rot13(string):
    global alphabet
    new_string = []
    capital = False
    
    for letter in string:
        if letter == " ":
            new_string.append(" ")
        else:
            index = alphabet.index(letter)
            if index > 25:
                capital = True
            else:
                capital = False
            index += 13
            if index > 51 or (index > 25 and not capital):
                index -= 26
            new_string.append(alphabet[index])
    print("".join(new_string))

if __name__ == '__main__':
    rot13(sys.argv[1])

