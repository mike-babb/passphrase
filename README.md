# passphrase
Use python to create a passphrase from a list of words

NOTE: THIS IS A SIMPLE PASSPHRASE GENERATOR.

V1.0: Current
Generates passphrases from the Electronic Frontier Foundations' list of long words:
https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt

Randomly selects 5 words, randomly capitalizes five letters, inserts numbers and special characters. 

Basically, the generator produces [correcthorsebatterystaple](https://xkcd.com/936/) instead of r]j.?%H7Qg(ST>W"

Included in this repository: 
- jupyter notebook with the passphrase generating function
- a python script with the same function
- a windows batch file showing how the generator can be called from the windows' "Run" dialog which generates the password and places it into the current clipboard.
- a simple ctrl-v will paste the passphrase into any new form that requires a password.

V1.1: TBD
Planned features:
- Specify the number of words in the passphrase
- options to include or exclude capital letters, numbers, and special characters




