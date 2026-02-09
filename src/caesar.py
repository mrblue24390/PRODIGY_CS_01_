def display_banner():
    """Display the program banner"""
    print("\n" + "="*60)
    print("        CAESAR CIPHER ENCRYPTION & DECRYPTION TOOL")
    print("="*60)

def display_menu():
    """Display the main menu options"""
    print("\n" + "-"*40)
    print("MAIN MENU")
    print("-"*40)
    print("1. Encrypt a Message")
    print("2. Decrypt a Message")
    print("3. View Instructions")
    print("4. Try Auto Demo")
    print("5. Exit")
    print("-"*40)

def show_instructions():
    """Display program instructions"""
    print("\n" + "📘 " + "INSTRUCTIONS".center(40, "-") + " 📘")
    print("\n1. Caesar Cipher is a substitution cipher where each letter")
    print("   in the plaintext is shifted by a fixed number of positions.")
    print("\n2. For ENCRYPTION: Choose option 1, enter your message,")
    print("   then enter a shift value (0-25).")
    print("\n3. For DECRYPTION: Choose option 2, enter the encrypted")
    print("   message, then enter the same shift value used for encryption.")
    print("\n4. Example: With shift 3, 'A' becomes 'D', 'B' becomes 'E', etc.")
    print("\n5. Non-alphabetic characters (spaces, punctuation, numbers)")
    print("   remain unchanged.")
    print("\n" + "-"*40)

def get_valid_shift():
    """
    Get and validate shift value from user
    Returns a valid integer between 0 and 25
    """
    while True:
        try:
            shift_input = input("Enter shift value (0-25): ")
            shift = int(shift_input)

            if shift < 0 or shift > 25:
                print("⚠️  Error: Shift must be between 0 and 25. Try again.")
                continue

            return shift
        except ValueError:
            print("⚠️  Error: Please enter a valid number (0-25).")

def caesar_cipher(text, shift, operation):
    """
    Perform Caesar Cipher encryption or decryption

    Parameters:
    text (str): Input text
    shift (int): Shift value (0-25)
    operation (str): 'encrypt' or 'decrypt'

    Returns:
    str: Encrypted or decrypted text
    """
    result = ""

    # For decryption, shift in opposite direction
    if operation == "decrypt":
        shift = -shift

    for char in text:
        if char.isupper():
            # Shift uppercase letters
            shifted = chr((ord(char) - 65 + shift) % 26 + 65)
            result += shifted
        elif char.islower():
            # Shift lowercase letters
            shifted = chr((ord(char) - 97 + shift) % 26 + 97)
            result += shifted
        else:
            # Keep non-alphabetic characters unchanged
            result += char

    return result

def encrypt_message():
    """Handle message encryption"""
    print("\n" + "🔐 " + "ENCRYPTION".center(40, "-") + " 🔐")

    # Get user input
    message = input("\nEnter message to encrypt: ")
    if not message:
        print("⚠️  No message entered. Returning to menu.")
        return

    print("\nShift Value Guide:")
    print("• 3: Julius Caesar's original shift")
    print("• 13: ROT13 (popular for simple obfuscation)")
    print("• Any number 0-25")

    shift = get_valid_shift()

    # Perform encryption
    encrypted = caesar_cipher(message, shift, "encrypt")

    # Display results
    print("\n" + "✓ " + "RESULT".center(40, "-") + " ✓")
    print(f"\nOriginal Message:   {message}")
    print(f"Shift Value:        {shift}")
    print(f"Encrypted Message:  {encrypted}")
    print(f"\n💡 Remember: To decrypt, use shift value {shift}")

def decrypt_message():
    """Handle message decryption"""
    print("\n" + "🔓 " + "DECRYPTION".center(40, "-") + " 🔓")

    # Get user input
    message = input("\nEnter message to decrypt: ")
    if not message:
        print("⚠️  No message entered. Returning to menu.")
        return

    print("\nEnter the shift value used for encryption.")
    print("If unknown, try common values like 3 or 13,")
    print("or use the brute force option in demo mode.")

    shift = get_valid_shift()

    # Perform decryption
    decrypted = caesar_cipher(message, shift, "decrypt")

    # Display results
    print("\n" + "✓ " + "RESULT".center(40, "-") + " ✓")
    print(f"\nEncrypted Message:  {message}")
    print(f"Shift Value:        {shift}")
    print(f"Decrypted Message:  {decrypted}")

def auto_demo():
    """Run an automatic demonstration"""
    print("\n" + "🎬 " + "AUTO DEMONSTRATION".center(40, "-") + " 🎬")

    # Example messages
    examples = [
        ("HELLO WORLD", 3),
        ("Python Programming", 7),
        ("Caesar Cipher is fun!", 13),
        ("Attack at dawn!", 5)
    ]

    for i, (message, shift) in enumerate(examples, 1):
        print(f"\n{' Example ' + str(i) + ' ':=^40}")
        print(f"Message:    {message}")
        print(f"Shift:      {shift}")

        # Encrypt
        encrypted = caesar_cipher(message, shift, "encrypt")
        print(f"Encrypted:  {encrypted}")

        # Decrypt
        decrypted = caesar_cipher(encrypted, shift, "decrypt")
        print(f"Decrypted:  {decrypted}")

        # Verify
        if message == decrypted:
            print("✓ Verification: SUCCESS")
        else:
            print("✗ Verification: FAILED")

    # Brute force example
    print(f"\n{' BRUTE FORCE EXAMPLE ':=^40}")
    secret_message = "Xlmw mw e qiwweki sj xli typpi"
    print(f"Secret Message: {secret_message}")
    print("\nTrying all possible shifts (0-25):")
    print("-"*40)

    for s in range(26):
        decrypted = caesar_cipher(secret_message, s, "decrypt")
        if s == 4:  # Correct shift is 4
            print(f"Shift {s:2d}: {decrypted}  ← CORRECT!")
        else:
            print(f"Shift {s:2d}: {decrypted}")

def main():
    """Main program function with menu system"""
    display_banner()

    while True:
        display_menu()

        try:
            choice = input("\nEnter your choice (1-5): ").strip()

            if choice == "1":
                encrypt_message()

            elif choice == "2":
                decrypt_message()

            elif choice == "3":
                show_instructions()

            elif choice == "4":
                auto_demo()

            elif choice == "5":
                print("\n" + "="*40)
                print("Thank you for using Caesar Cipher Tool!")
                print("Goodbye! 👋")
                print("="*40)
                break

            else:
                print("⚠️  Invalid choice! Please enter 1, 2, 3, 4, or 5.")

            # Ask to continue after each operation (except exit)
            if choice != "5":
                input("\nPress Enter to continue...")

        except KeyboardInterrupt:
            print("\n\n⚠️  Program interrupted. Exiting...")
            break
        except Exception as e:
            print(f"\n⚠️  An error occurred: {e}")
            input("\nPress Enter to continue...")

# Run the program
if __name__ == "__main__":
    main()
