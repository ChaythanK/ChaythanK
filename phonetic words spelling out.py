nato_alphabet = {
    'A': 'Alpha',
    'B': 'Bravo',
    'C': 'Charlie',
    'D': 'Delta',
    'E': 'Echo',
    'F': 'Foxtrot',
    'G': 'Golf',
    'H': 'Hotel',
    'I': 'India',
    'J': 'Juliett',
    'K': 'Kilo',
    'L': 'Lima',
    'M': 'Mike',
    'N': 'November',
    'O': 'Oscar',
    'P': 'Papa',
    'Q': 'Quebec',
    'R': 'Romeo',
    'S': 'Sierra',
    'T': 'Tango',
    'U': 'Uniform',
    'V': 'Victor',
    'W': 'Whiskey',
    'X': 'X-ray',
    'Y': 'Yankee',
    'Z': 'Zulu'
}
print("hello guys, whats the word you wanna spell out?...")
wor = (str(input(":>"))).upper()
word = [i for i in wor]
print(word)
# word_spelled_out = [nato_word if nato_word == for i in range(len(word))]
word_spelled_out = []
for letter in word:
    for nato_letter in nato_alphabet:
        if letter == nato_letter:
            word_spelled_out.append(nato_alphabet[nato_letter])
print(word_spelled_out)
words_spelled_out = []
