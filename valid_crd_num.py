# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

card_n = re.compile(r"^"  # begin with
                    r"(?!.*(\d)(-?\1){3})" # if the first group numbers are repeated 3times
                    r"[456]\d{3}" # first digit is 4 or 5 or 6 followed by 3 digits 
                    #r"(?:-?\d{4}){3}" # rest three groups don't have 3 repeated digits
                    r"(\d{12}|(-\d{4}){3})" # no repeated digit in first 12 digits or any -4 digits
                    r"$") # end of exp

for _ in range(int(input().strip())): # strip the input by "\n" default value
    print("Valid" if card_n.search(input().strip()) else "Invalid")