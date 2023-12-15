"""
Division is to subtract constantly a given number of times
Multiplication is to a add constantly a given number of times

Addition is to give or have more
Subraction is to take or have less

Modulo is to display/give the user the remainder, or left over, of a division expression
Floor division
"""

given_key = " asdfghjklzxcvbnm,.?;:'qwertyuiop|`~!@#$%^&*_+-=(){}[]<>\/ASDFGHJKLZXCVBNMQWERTYUIOP0123456789" + '"'
# this is necessary to account for modulos higher than 9
base_93 = "0123456789abcedfghijklmnopqrstuvwxyABCDEFGHIJKLMNOPQRSTUVWXYZ,.?;:|`~!@#$%^&*-_=+<>\/[]{}()'" + '"'

class process:
    
    """
    This is a class to encode or decode information within a given set of characters. using the n-nary algorithmn    
    """

    def __init__(save, nary=1,given_key=given_key, for_modulo=base_93):
        save.key = given_key
        # Convert the key to a dictionary, mapping each character to its index
        save.key_dict = {given_key[i]: i for i in range(len(save.key))}
        # Convert the base_93 string into a dictionary to easily call upon it; Also, to retain the value and keep the n-nary position
        ## by using different symbols for values higher than 9
        save.base_93 = {for_modulo[i]: i for i in range(len(for_modulo))}
        save.base = nary
        
    def decode(saved, text):
        # text: G'101 1' -> text.split(): G['101','1'] -> [int(num) for num...]G[[1,0,1],[1]] -> list(): [[1,0,1],[1]];
        # in a generator-expression, split text: encoded.split: G['101','1'] 
        ## then for each index, using list-comprehension, get each character in a string of an index and convert into an integer
        ## list-comprehension makes a list out of the output of the for loop, therefore, G[[1,0,1],[1]]
        # finally convert the generator into a list and have a useable list
        encoded_data = list([saved.base_93[num] for num in char] for char in text.split(" "))
        # make the convert the encoded data into a string
        line = "".join([saved.key[nary_to_decimal(char_values, saved.base)] for char_values in encoded_data])
        return line

    def encode(saved, text):
        # Convert the message to decimal values using the saved.key
        decimal_values = [saved.key_dict[c] for c in text]
        # with the decimal values from a string parse them into their n-nary representations
        nary_string = [decimal_to_nary(i, saved.base) for i in decimal_values]
        # make the encoded data into string
        line = " ".join("".join(c for c in chars) for chars in nary_string)
        return line




def nary_to_decimal(nary_digits, base):

    """
    Convert a number in a certain base to decimal to be turned back into readable text
    """

    # as base 1 returns 0's the value is equivalent to the lenght of the nary_digits
    if base == 1:
        # AH, because nothing is represented as a string!
        if nary_digits == str():
            return 0
        return len(nary_digits) * base
    # using generator funciton, as list comprehension is this but enclosed in brackets, and the sum() function to get the generator's values
    decimal_total = sum( digit * (base ** ( len(nary_digits)-(i+1) )) for i, digit in enumerate(nary_digits) )
    return decimal_total



def decimal_to_nary(decimal_value, base):
    
    """
    Converts a decimal value to an n-ary value with the specified base.
    """        

    # return 0 if 0 is given as 0 would return an empty list as it wouldn't flag the while loop
    if decimal_value == 0:
        # an empty list is to meant to describe the first character of the key, length of nothing is 0
        return []
    # if the base is 1 then, to avoid an infinite loop, using list comprehension, append to unary. Also semi-colon use.
    if base == 1:
        unary = [];[unary.insert(i, 0) for i in range(decimal_value)];
        return unary
    # initalize a list to store the remainder of the modulo of the decimal_value
    nary_digits = []
    while decimal_value > 0:
        # return the modulo of decimal_value to a given base, this returns a good 
        mod = decimal_value % base
        # in case the modulo returns a value higher than 9 return another character to represent higher values
        nary_digits.append(base_93[mod])
        # update the decimal_value through floor divison, returning a whole number; Repeat until the decimal_value isn't greater than 0
        decimal_value //= base
    # Reverse the nary_digit list as the least significant digit is always first and the coresponding digits of significance follows left to right.
    nary_digits.reverse()
    return nary_digits




#troubleshooting or t
if __name__ == '__main__':
    x = process(1, alphabet).encode("Hello World!")
    y = process(1, alphabet).decode(x)
    print(x)
    print(y)
