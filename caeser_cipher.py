import caeser_cipher_art

def caesar(direction, original_text, shift_amount):
    new_word = ""

    if direction == "encode":
        for letter in original_text:

            if letter not in alphabet:
                new_word += letter

            else:
                index = alphabet.index(letter)
                if index+shift_amount > 25:
                    new_word += alphabet[index+shift_amount-26]

                else: 
                    new_word += alphabet[alphabet.index(letter)+shift_amount]

        print(f"Here is the encoded result: {new_word}")

    elif direction == "decode":
        for letter in original_text:

            if letter not in alphabet:
                new_word += letter

            else:
                index = alphabet.index(letter)
                if index+shift_amount < 0:

                    new_word += alphabet[25-shift_amount]

                else: 
                    new_word += alphabet[alphabet.index(letter)-shift_amount]

        print(f"Here is the decoded result: {new_word}")

    else:
        print("Choose one of the options!")

alphabet = [
    "a","b","c","d","e","f","g","h","i","j","k","l","m",
    "n","o","p","q","r","s","t","u","v","w","x","y","z"
]
print(caeser_cipher_art.art)
situation = True

while situation:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    text = input("\nType your message: ").lower()
    shift = int(input("\nType the shift number: "))

    caesar(direction=direction, original_text=text, shift_amount=shift)

    decision = input("Do you want to restart? Type yes or no: ")

    if decision == "no":
        print("Finishing...")
        situation = False