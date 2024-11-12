import random


def main():
    random.seed()
    guess = input("Enter your guess for the flag: ")

    if check(guess):
        print("I think that's right!")
    else:
        print("I'm not too sure about that one...")


def check(guess):
    return random.getrandbits(1)


if __name__ == "__main__":
    main()
