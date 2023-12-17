from AES import *
from random import randbytes

def test_AES():

    NewAES = AES()

    KB = 1024
    MB = 1024*1024
    GB = 1024*1024*1024

    testText = "This is a test for text encryption using AES"

    NewAES.FromText("Tis is a test for text encryption using AES")
    NewAES.UseTextKey("Hello there, my key")

    print(NewAES.ToText())

    NewAES.Cipher()

    print(NewAES.ToText())

    NewAES.UnCipher()

    print(NewAES.ToText())



if __name__ == "__main__" :

    if True:

        path = "test.jpg"

        # NewAES = AES()

        # NewAES.FromFile("InFiles/test.jpg")
        # NewAES.UseTextKey("This is my key for AES encryption.txt")

        # NewAES.ToFile("InFiles/test.jpg")

        # NewAES.Cipher()

        # NewAES.ToFile("OutFiles/test_cipher.jpg")


        SecAES = AES()

        SecAES.FromFile("OutFiles/test_cipher.jpg")
        SecAES.UseTextKey("This is my wrong key for AES encryption.txt")

        SecAES.UnCipher()

        SecAES.ToFile("OutFiles/test_uncipher_with_wrong_key.jpg")






         
