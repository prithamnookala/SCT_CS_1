def caesar_cipher(text: str, shift: int, mode: str = "encrypt") -> str:
    """
    Encrypts or decrypts a message using the Caesar cipher.
    
    :param text: The message to process.
    :param shift: The number of positions to shift each character.
    :param mode: Either 'encrypt' or 'decrypt'.
    :return: The processed text.
    """
    # Decryption is simply encryption with a negative shift
    if mode == "decrypt":
        shift = -shift
        
    # Standardize shift value within 0-25 range
    shift = shift % 26
    
    result = []
    
    for char in text:
        if char.isalpha():
            # Determine ASCII base (uppercase vs. lowercase)
            start = ord('A') if char.isupper() else ord('a')
            
            # Apply shift with wraparound
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
            result.append(shifted_char)
        else:
            # Preserve spaces, punctuation, numbers, and special characters
            result.append(char)
            
    return "".join(result)


def main():
    print("--- Caesar Cipher Program ---")
    
    while True:
        # Prompt for mode
        print("\nSelect an option:")
        print("1. Encrypt message")
        print("2. Decrypt message")
        print("3. Exit")
        
        choice = input("Enter choice (1, 2, or 3): ").strip()
        
        if choice == '3':
            print("Goodbye!")
            break
            
        if choice not in ('1', '2'):
            print("Invalid selection. Please enter 1, 2, or 3.")
            continue
            
        mode = "encrypt" if choice == '1' else "decrypt"
        
        # Get input text
        text = input(f"\nEnter the message to {mode}: ")
        
        # Get and validate shift value
        while True:
            try:
                shift = int(input("Enter the shift value (e.g., 3): "))
                break
            except ValueError:
                print("Please enter a valid integer for the shift value.")
                
        # Perform cipher operation
        output = caesar_cipher(text, shift, mode)
        print(f"\nResult ({mode.capitalize()}ed): {output}")


if __name__ == "__main__":
    main()