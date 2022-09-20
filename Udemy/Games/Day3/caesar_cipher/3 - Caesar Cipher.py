# import:
from Games.Day3.caesar_cipher import caesar_cipher_art

print(caesar_cipher_art.logo)

# letters:
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# by repeating the alphabet over twice it stops a: 'Index Error: list out of range' as if the word has say a 'z' it
# won't reach the end of the list it will just keep going as there's more after it.

# loop:
start_again = True

while start_again:
    # asking the user:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # main code:
    def caesar(start_text, shift_change, cipher_direction):
        # empty string:
        end_text = ""
        # decode the end_text
        if cipher_direction == "decode":
            shift_change *= -1
        # works out encode:
        for char in start_text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + shift_change
                end_text += alphabet[new_position]
            else:
                end_text += char

        print(f"The {direction}ed text is: {end_text}")


    shift = shift % 26
    caesar(start_text=text, shift_change=shift, cipher_direction=direction)

    again = input("\nType 'yes' if you'd like to go again. Type 'no' if you'd like to quit:\n").lower()
    if again == "yes" or again == "y":
        start_again = True
        print("\nRestarting...\n")
    else:
        print("\nGoodbye!")
        quit()
