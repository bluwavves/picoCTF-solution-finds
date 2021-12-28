**Explanation

File given is a simple Python programme, and the inital skimming shows the string 'bezos_cc_secret' should be our flag and function 'decode_secret' is the
decrypting fuction. I had solution 1 first because I didn't even end up reading through the rest of the code before I got the idea, however reading 
through the whole code once again properly, simply calling for decode_secret() function is a faster solution. 


**Solution 1: 

1. Because through the decode_secret() function, we know that the flag is encrypted by ROT47
2. Write very simple decoding script using Python, I used rot47 from secretpy (source code is solution.py) 
3. Flag: picoCTF{1|\/|_4_p34|\|ut_f3bc410e}

**Solution 2:

1. Replace 'choose_greatest()' with 'decode_secret(bezos_cc_secret)'
2. Run: the file 
3. Flag: picoCTF{1|\/|_4_p34|\|ut_f3bc410e}
