bin_to_ascii_dict = {
    "00001010": "\n",
    "00100000": " ",
    "00100001": "!",
    "00100010": "\"",
    "00100011": "#",
    "00100100": "$",
    "00100101": "%",
    "00100110": "&",
    "00100111": "\'",
    "00101000": "(",
    "00101001": ")",
    "00101010": "*",
    "00101011": "+",
    "00101100": ",",
    "00101101": "-",
    "00101110": ".",
    "00101111": "/",
    "00110000": "0",
    "00110001": "1",
    "00110010": "2",
    "00110011": "3",
    "00110100": "4",
    "00110101": "5",
    "00110110": "6",
    "00110111": "7",
    "00111000": "8",
    "00111001": "9",
    "00111010": ":",
    "00111011": ";",
    "00111100": "<",
    "00111101": "=",
    "00111110": ">",
    "00111111": "?",
    "01000000": "@",
    "01000001": "A",
    "01000010": "B",
    "01000011": "C",
    "01000100": "D",
    "01000101": "E",
    "01000110": "F",
    "01000111": "G",
    "01001000": "H",
    "01001001": "I",
    "01001010": "J",
    "01001011": "K",
    "01001100": "L",
    "01001101": "M",
    "01001110": "N",
    "01001111": "O",
    "01010000": "P",
    "01010001": "Q",
    "01010010": "R",
    "01010011": "S",
    "01010100": "T",
    "01010101": "U",
    "01010110": "V",
    "01010111": "W",
    "01011000": "X",
    "01011001": "Y",
    "01011010": "Z",
    "01011011": "[",
    "01011100": "\\",
    "01011101": "]",
    "01011110": "^",
    "01011111": "_",
    "01100000": "`",
    "01100001": "a",
    "01100010": "b",
    "01100011": "c",
    "01100100": "d",
    "01100101": "e",
    "01100110": "f",
    "01100111": "g",
    "01101000": "h",
    "01101001": "i",
    "01101010": "j",
    "01101011": "k",
    "01101100": "l",
    "01101101": "m",
    "01101110": "n",
    "01101111": "o",
    "01110000": "p",
    "01110001": "q",
    "01110010": "r",
    "01110011": "s",
    "01110100": "t",
    "01110101": "u",
    "01110110": "v",
    "01110111": "w",
    "01111000": "x",
    "01111001": "y",
    "01111010": "z",
    "01111011": "{",
    "01111100": "|",
    "01111101": "}",
    "01111110": "~"
}

import sys
import subprocess

try:
    input_File = sys.argv[1]
except IndexError:
    print("Please specify a file to compile!")
    sys.exit()

with open(input_File, "r") as file:
    inputfile_list = file.read().strip()

if len(inputfile_list) == 0:
    print("Really?")
    sys.exit()

# Clean up spaces between binary sequences and ensure each sequence is exactly 8 bits
inputfile_list = inputfile_list.replace(" ", "")  # remove spaces between the binary data

# Split the binary string into chunks of 8 bits
inputfile_list = [inputfile_list[i:i+8] for i in range(0, len(inputfile_list), 8)]

# Filter out invalid chunks that aren't exactly 8 bits
inputfile_list = [chunk for chunk in inputfile_list if len(chunk) == 8]

# Decode the binary sequences into ASCII text
output_string = ''.join(bin_to_ascii_dict.get(line, "Error") for line in inputfile_list)

# Save the output to a file and print it
with open("temp.c", "w") as file:
    file.write(output_string)

import os
subprocess.run("clang temp.c -o output")

os.remove("temp.c")