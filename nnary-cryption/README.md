# for Downloading the package through pip
```
 pip install -i https://test.pypi.org/simple/ nnary-Hotodog808==0.0.1
```
# n-nary cryption details
A python script able to encode and decode a given string given a certain base; and, if wanted, an optional Given_Key and For_Modulo (base-93)
## For_Modulo: Reference-For-Higher-Values
When working with number systems that are higher than the base-10 (decimal) number systems, such as hexadecimal (base-16) or duodecimal (base-12), numbers with a value of 10 or greater are represented by more than one digit. If you convert these numbers to decimal (base-10) before encoding or decoding a message, it can cause errors in the position of characters in the encoded message. To avoid this issue, it is important to encode and decode the message using the same non-decimal number system, which would be converting the values with double digits into another symbol. That is done with another key referenced as For_Modulo.
## Why the excess comments? 
I like to describe each part of the code for my own understand, I am a noob at python and wish to write down what each part does to understand. This is essentially my first, and best, project I made and I wish to share it.
