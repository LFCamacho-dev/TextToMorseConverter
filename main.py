import morse


def encrypt(word):
    code = []
    for letter in word:
        if letter in morse.MORSE_CODE_DICT:
            char = morse.MORSE_CODE_DICT.get(letter)
            code.append(char)
        else:
            code.append(' ')
    print(*code, sep=' ')


def main():
    word = input("Enter the word to encrypt: ").upper()
    encrypt(word)
    main()


if __name__ == "__main__":
    main()
