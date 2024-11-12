# TODO: Remember to remove this line before committing!
encrypted = [0x25, 0x26, 0x22, 0xf, 0x28, 0x5e, 0x2e, 0x33, 0x27, 0x5a, 0x25, 0x25, 0x59, 0x1e, 0x15]


def main():
    guess = input("Enter your guess for the flag: ")

    if check(guess):
        print("That is correct! Well done!")
    else:
        print("Sorry, keep trying!")


def check(guess):
    if len(guess) != len(encrypted):
        return False

    for i, c in enumerate(guess):
        if (ord(c) ^ 123) + len(guess) != encrypted[i]:
            return False

    return True


if __name__ == "__main__":
    main()
