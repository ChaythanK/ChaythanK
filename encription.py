# text = str(input("enter text: "))
# shift = str(input("enter shift: "))
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','~','`','1','2','3','4','5',
#             '6','7','8','9','0','!','@','#','$','%','^','&','*','(',')','-','_','+','=','{','[','}',']','|',':',';',"'",'"','<',',',".",'>','?','/',' ','a', 'b', 'c', 'd'
#             ,'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','~','`','1','2','3','4','5','6','7','8','9','0','!','@'
#             ,'#','$','%','^','&','*','(',')','-','_','+','=','{','[','}',']','|',':',';',"'",'"','<',',',".",'>','?','/']
# text_in_list = [letter for letter in text]
# print(text_in_list)
# text_in_list = ["a" if letter == "e" else alphabet[alphabet.index(letter) + int(shift)] for letter in text_in_list if letter in alphabet]
# print(text_in_list)
#
# text_in_list = [letter for letter in text]
# print(text_in_list)
# text_in_list = ["a" if letter == "e" else alphabet[alphabet.index(letter) + int(shift)] for letter in text_in_list if letter in alphabet]
# print(text_in_list)
#
# with open('example.txt', 'r') as file:
#     content = file.read()
#     print(content)

def caesar_cipher_file(input_file, output_file, general_shift, specific_shifts, mode='encrypt'):
    """
    Reads a file, encrypts or decrypts its content using the Caesar cipher with a general shift and specific shifts,
    and writes the result to another file.

    Args:
        input_file (str): Path to the input file.
        output_file (str): Path to the output file.
        general_shift (int): The number of positions to shift generally.
        specific_shifts (dict): Specific shifts for individual letters.
        mode (str): 'encrypt' to encrypt, 'decrypt' to decrypt.

    Returns:
        None
    """
    try:
        # Read input file
        with open(input_file, 'r') as infile:
            text = infile.read()

        # Apply Caesar cipher
        result = ""
        general_shift = general_shift % 26  # Handle shifts larger than 26

        if mode == 'decode':
            general_shift = -general_shift  # Reverse shift for decryption
            # Reverse specific shifts for decryption
            specific_shifts = {k: -v for k, v in specific_shifts.items()}

        for char in text:
            if char.isalpha():
                start = ord('A') if char.isupper() else ord('a')
                shift = specific_shifts.get(char, general_shift)  # Use specific shift if defined, else general shift
                result += chr((ord(char) - start + shift) % 26 + start)
            else:
                result += char

        # Write result to output file
        with open(output_file, 'w') as outfile:
            outfile.write(result)

        print(f"{mode.capitalize()}ion complete! Output written to '{output_file}'")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Input parameters
general_shift_inputed = int(input("General shift: "))
specific_shifts_input = input("Specific shifts (format - a:1,b:2): ")
specific_shifts_inputed = {k: int(v) for k, v in (item.split(':') for item in specific_shifts_input.split(','))}
input_filename = input("Input file name: ")
output_filename = input("Output file name: ")
choice = input("Choice (encode/decode): ")

# Perform encryption or decryption
caesar_cipher_file(input_filename, output_filename, general_shift_inputed, specific_shifts_inputed, mode=choice)


