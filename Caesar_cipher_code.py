#!/usr/bin/env python
# coding: utf-8

# In[8]:


#import colorama
import sys
from colorama import Fore


# In[ ]:


def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text :
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a') 
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_text += shifted_char
        else: 
            encrypted_text += char 
    return encrypted_text
    
plaintext = input("Enter your message:")
shift = int(input("Enter the shift value (0-25): "))
encrypted_message = caesar_cipher(plaintext, shift)
print(f"Encrypted message:{Fore.GREEN}{encrypted_message}{Fore.RESET}")


# In[ ]:




