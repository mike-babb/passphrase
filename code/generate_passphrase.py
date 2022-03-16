#!/usr/bin/env python
# coding: utf-8

# mike babb
# generate a passphrase



# standard
import os
import string

# external
import pandas as pd
import numpy as np


def generate_pass():
    
    # load list of words
    df = pd.read_csv(filepath_or_buffer='H:/git/passphrase/eff_large_wordlist.txt', sep = '\t', header = None,
                    names = ['id', 'word'])
    
    # randomly select
    words = np.random.choice(df['word'], size = 5, replace = False).tolist()
    # make random upper case stuff
    total_chars = sum([len(x) for x in words])

    # numbers
    num_chars = '1234567890'
    num_chars = [x for x in num_chars]

    # special characters
    special_chars = '`~!@#$%^&*()-_=+,<.>/?;:[{]}|]'
    special_chars = [x for x in special_chars]

    # randomly select letters to make upper case
    to_upper_case = np.random.choice(a = range(1, total_chars),
                     size = 5, replace = False)
    
    # seperate each letter
    passphrase = []
    for ii in words:
        passphrase.extend([jj for jj in ii])

    # make upper case
    for ii in to_upper_case:
        passphrase[ii] = passphrase[ii].upper()

    passphrase = ''.join(passphrase)
    # now add some numbers and some special characters

    rando_nc = np.random.choice(a = num_chars, size = 1)[0]

    rando_sc = np.random.choice(a = special_chars, size = 1)[0]

    passphrase += rando_nc + rando_sc 

    return passphrase


if __name__ == '__main__':
    print(generate_pass())
    

