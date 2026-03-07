"""
===========================================
        CAESAR CIPHER PROJECT
===========================================
This program performs:
1. Encryption using Caesar Cipher
2. Decryption using Caesar Cipher
3. Brute Force Attack (Optional Feature)

Author: Your Name
Language: Python 3
===========================================
"""

# Function to encrypt text
def encrypt_text(message, shift):
    encrypted_message = ""

    for char in message:
        if char.isalpha():  # Check if character is a letter
            ascii_offset = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_message += encrypted_char
        else:
            encrypted_message += char  # Keep special characters unchanged

    return encrypted_message


# Function to decrypt text
def decrypt_text(message, shift):
    decrypted_message = ""

    for char in message:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decrypted_message += decrypted_char
        else:
            decrypted_message += char

    return decrypted_message


# Optional: Brute force attack (tries all possible shifts)
def brute_force_attack(message):
    print("\nTrying all possible shifts:\n")
    for shift in range(1, 26):
        decrypted = decrypt_text(message, shift)
        print(f"Shift {shift}: {decrypted}")


# Function to display menu
def display_menu():
    print("\n" + "=" * 45)
    print("        CAESAR CIPHER PROGRAM")
    print("=" * 45)
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Brute Force Attack")
    print("4. Exit")
    print("=" * 45)


# Main function
def main():
    while True:
        display_menu()

        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            message = input("\nEnter the message to encrypt: ")
            try:
                shift = int(input("Enter shift value (integer): "))
            except ValueError:
                print("Shift must be an integer!")
                continue

            encrypted = encrypt_text(message, shift)
            print("\nEncrypted Message:", encrypted)

        elif choice == 2:
            message = input("\nEnter the message to decrypt: ")
            try:
                shift = int(input("Enter shift value (integer): "))
            except ValueError:
                print("Shift must be an integer!")
                continue

            decrypted = decrypt_text(message, shift)
            print("\nDecrypted Message:", decrypted)

        elif choice == 3:
            message = input("\nEnter the encrypted message: ")
            brute_force_attack(message)

        elif choice == 4:
            print("\nThank you for using Caesar Cipher Program!")
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please select between 1 and 4.")


# Run the program
if __name__ == "__main__":
    main()