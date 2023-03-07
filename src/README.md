# oneHotCipher

An encryption library in python that can convert and revert strings into/from one_hot, ciphers and enigmas

------------------------------------------------------

Requirements:
- IDE (your choice)
- Python
- pip
    - unidecode
    - numpy
    - .
        - installs the internal library   

File to run in the IDE:
- demo.py
    - need to open the folder on the explorer (left) to access the functions

------------------------------------------------------

Implementations:
- Cipher
    - Firstly, transforms the text into a lengh-of-text by 27 array, where all the letters and spaces are indicated by a 1 in the corresponding spot (0 for spaces, 1-27 for letters)
    - Does the same thing with the cipher, making it a 27x27 matrix
    - Multiplies the matrixes togheter, forming a new matrix that is the lengh-of-text by 27
        - By multiplying the matrixes, you essentially shift the positions of the column by the amount specified in the 27x27 matrix, thus producing the same effect as a caesar cipher
    - Reverses the array transformation by re-assigning the letters and spaces to the spots that have a 1 in them
    
- Enigma
    - Starts off similar to cipher, where the text is transformed into an array
    - Same thing with both the ciphers, making them both a 27x27 matrix
    - The first letter gets multiplied by the main cipher
    - For every subsequent letter of the string, the main cipher is multiplied by the auxiliary cipher before being applied
    - Reverses the array transformation, placing letters and spaces in their respective spots
