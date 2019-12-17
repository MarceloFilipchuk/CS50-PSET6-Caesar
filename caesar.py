import sys


def main():

    # Ensures proper usage
    if len(sys.argv) != 2:
        print("Usage: python caesar.py k")
        return main()

    # Defines the key to be used on the plaintext
    key = int(sys.argv[1])
    if key < 0:
        return main()

    # Promts the user for a plaintext to encipher
    plaintext = input("Plaintext: ")
    print("ciphertext: ", end="")
    # Iterates over the plaintext
    for character in plaintext:
        if character.isalpha():
            if character.isupper():
                character = ord(character) + key
                if int(character) > 90:
                    while int(character) > 90:
                        character = 65 + (character % 91)
                print(chr(character), end="")
            elif character.islower():
                character = ord(character) + key
                if int(character) > 122:
                    while int(character) > 122:
                        character = 97 + (character % 123)
                print(chr(character), end="")
        else:
            print(character, end="")
    print()
    return


# Calls the main function
if __name__ == "__main__":
    main()

