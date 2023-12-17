import warnings
from Block import Block
from Key import Key

class AES :

    def __init__(self, sequence : bytearray, cipherKey : bytearray) :
        """
        Create a new AES object
        'sequence' - Sequence of bytes to be ciphered / unciphered
        'cipherKey' -  Sequence of 16 / 24 / 32 bytes used as a key
        """
            
        # Verify the key length
        if len(cipherKey) not in [16, 24, 32]:

            warnings.warn("Wrong number of bytes in the key")

            return -1
        
        # Divide the byte sequence in multiple blocks of 15 bytes
        nBlocks = len(sequence) // 16 if len(sequence)%16 == 0 else len(sequence) // 16 + 1

        blocks = []

        # Create new blocks from slices of 16 bytes
        for blockIndex in range(nBlocks):

            blocks.append(Block(sequence[blockIndex * 16 : (blockIndex + 1) * 16 ]))
        
        self.blocks = blocks
        self.key = Key(cipherKey)

    def CipherBlock(self, block : Block):
        """
        Encrypt a block of 16 bytes using the AES using the key
        'block' - Block to by encrypted
        """

        # Get the key schedule from the key
        keySchedule = self.key.KeyExpansion()

        # Encrypt the block
        block.AddRoundKey(0, keySchedule)

        # Repetition depending on the key size (128 - 10 rep, 192 - 12 rep, 256 - 14 rep)
        for round in range(1, self.key.Nb):

            block.SubBytes()
            block.ShiftRows()
            block.MixColumns()
            block.AddRoundKey(round, keySchedule)

        block.SubBytes()
        block.ShiftRows()
        block.AddRoundKey(self.key.Nb, keySchedule)

    def UnCipherBlock(self, block : Block):
        """
        Decrypt a block of 16 bytes using the AES using the key
        'block' - Block to be decrypted
        """

        # Get the key schedule from the key
        keySchedule = self.key.KeyExpansion()

        block.AddRoundKey(self.key.Nb, keySchedule)        

        # Reverse the encryption 
        for round in range(self.key.Nb - 1, 0, -1):

            block.InvShiftRows()
            block.InvSubBytes()
            block.AddRoundKey(round, keySchedule)
            block.InvMixColumns()
 
        block.InvShiftRows()
        block.InvSubBytes()
        block.AddRoundKey(0, keySchedule)


    def Cipher(self):

        print(0)


    def Uncipher(self):

        print(0)




