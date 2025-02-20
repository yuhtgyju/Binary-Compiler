# Binary-Compiler
Compile Binary to an executeable.

Currently only supports C code, as you need clang to compile.


This is more of an esoteric project.

# USAGE
First, if you dont already have some binaryfied ascii ready, use atb.py first on a text file that you have any text in.

ex: python3 atb.py ascii.txt

if you have followed the first step, you would now have temp.bin in the same directory that you used atb.py in. this has all the binary info about what you converted. DO NOT EDIT THIS. even one bit flip could lead to a different output or, more likely, just crashes.

Finally, use bta.py to compile the binary into an executable. 

ex: python3 bta.py temp.bin

this will output as output.exe, this is your compiled file! use ./output.exe to run it! if it works, you successfuly compiled from binary to an executable! good job!

this will require Clang (See requirements) for now, as this currently only supports C. other languages will be added in support later.


# REQUIREMENTS
Python 3.5+ (Tested with Python 3.12.0)

Clang (Installed and accessible from the command line)

# IMPORTANT
atb.py: Converts ASCII code to binary. If you don't know the ASCII binary tables, use this script to convert your code.

bta.py: Converts binary back to ASCII, then compiles the resulting code into an executable. It acts as the compiler for your binary code.
