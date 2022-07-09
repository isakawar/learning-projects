alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
            "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]


def display_menu():
    # displays a menu to the user
    print(" 1) Make a code \n 2) Decode a message \n 3) Quit")
    selection = int(input("\n Enter your selection: "))
    return selection


def encode_message():
    # text encoding function
    encoded_text = ""
    text_for_coding = input(" Enter your text to encode : ").lower()
    shear_level = int(input(" Enter shear level (1 - 26): "))
    count_current_letter = 0
    for letter in text_for_coding:
        index_letter = alphabet.index(letter)
        index_encoding_letter = index_letter + shear_level
        if index_encoding_letter > 26:
            encoded_text += alphabet[index_encoding_letter - 27]
        else:
            encoded_text += alphabet[index_encoding_letter]
    count_current_letter += 1
    print(encoded_text)


def decode_message():
    # text decode function
    decoded_text = ""
    count_current_letter = 0
    text_for_decoding = input(" Enter your text to decoding : ").lower()
    shear_level = int(input(" Enter shear level (1 - 26): "))
    for letter in text_for_decoding:
        index_letter = alphabet.index(letter)
        index_decoding_letter = index_letter - shear_level
        if index_decoding_letter <= 0:
            decoded_text += alphabet[index_decoding_letter]
        else:
            decoded_text += alphabet[index_decoding_letter]
    count_current_letter += 1
    print(decoded_text)


def main():
    run_status = True
    while run_status:
        num_select = display_menu()
        if num_select == 1:
            encode_message()
        elif num_select == 2:
            decode_message()
        elif num_select == 3:
            run_status = False
        else:
            print(" Incorect input")


if __name__ == "__main__":
    main()