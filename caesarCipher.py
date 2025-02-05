def caesar_cipher(text, shift, direction):
    result = ""
    
    for char in text:
        if char.isalpha():  # Check if character is an alphabet
            shift_amount = shift if direction == "encode" else -shift
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift_amount) % 26 + ascii_offset)
        else:
            result += char  # Non-alphabet characters are added directly
    
    return result

# Encode a message
message = "Hello, World!"
shift = 3
encoded_message = caesar_cipher(message, shift, "encode")
print(f"Encoded Message: {encoded_message}")

# Decode the message
decoded_message = caesar_cipher(encoded_message, shift, "decode")
print(f"Decoded Message: {decoded_message}")
