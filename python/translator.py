from sys import argv
def braille_to_english(string: str) -> str:
    pass
def english_to_braille(string: str) -> str:
    pass
def is_braille(string: str) -> bool:
    pass
def translator() -> None:
    input_string = " ".join(argv[1:])

    if is_braille(input_string):
        print(braille_to_english(input_string))
        return

    print(english_to_braille(input_string))

if __name__ == "__main__":
    translator()
