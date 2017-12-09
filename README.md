LZW-Compression-Technique
A Compression algorithm or technique used to compress the texts. <br> <br>

<u> Description: </u> <br>
an LZW consist of only from the pointer to the dictionary. The method starts by initializing the dictionary to the symbol in the alphabet is user 8-bits equal to 256 that the first entry for the first symbol that is none exists in the dictionary and each time this number plus one if the symbol doesn't exist in the dictionary (ASCII code  Table). <br> <br>

<u> Steps of the algorithm: </u> <br>

1. Input the symbols from left to right one after one, first the letter itself and then take it with the next letter and so on. The first symbol is input directly to the dictionary because it is always found in the dictionary (ASCII code table). <br>

2. After that we will check if the symbol is found in the dictionary, then print Y in the In Dictionary field, else print N in the In Dictionary field and put in the New Entry field concatenate the letters with an entry is equal to 256 and in the Output field we will put the letter or letters that has entry in the dictionary between two parentheses and also the equivalent entry number in the ASCII code table.
 



