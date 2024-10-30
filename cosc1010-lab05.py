# Your Name Here : Aris Yeimo
# UWYO COSC 1010
# Submission Date : 10/29/2024
# Homework 3
# Sources, people worked with, help given to: 
# your
# comments
# here

mors_abjad_dictionary = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..'
}

def plaintext_to_mors(plaintext):
    plaintext = plaintext.upper()
    mors_code = " "

    for abjad in plaintext:
        if abjad.islapha():
            mors_code += mors_abjad_dictionary[abjad]
        elif abjad:
            mors_code += "  "
    return mors_code.strip()

Enter = input("Please, Write a sentence:")
output_mors = plaintext_to_mors(Enter)
print("Abjad Result:", output_mors)