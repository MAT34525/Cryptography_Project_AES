import unittest
from Block import Block
from AES import AES
from Key import Key
from random import randbytes

class TestAESMethods(unittest.TestCase):

    def test_shift_rows(self):

        sequence = randbytes(16)
        block = Block(sequence)

        blockInit = block.block

        block.ShiftRows()

        blockShift = block.block

        block.InvShiftRows()

        blockFinal = block.block

        print("\n TEST SHIFT")
        print("\n[+] - 1 -", blockInit)
        print("\n[+] - 2 -", blockShift)
        print("\n[+] - 3 -", blockFinal)
        print("\n")

        self.assertNotEqual(blockInit, blockShift)

        self.assertEqual(blockInit, blockFinal)

    def test_sub(self):

        sequence = randbytes(16)
        block = Block(sequence)

        blockInit = block.block

        block.SubBytes()

        blockSub = block.block

        block.InvSubBytes()

        blockFinal = block.block

        print("\n TEST SUB")
        print("\n[+] - 1 -", blockInit)
        print("\n[+] - 2 -", blockSub)
        print("\n[+] - 3 -", blockFinal)
        print("\n")

        self.assertNotEqual(blockInit, blockSub)

        self.assertEqual(blockInit, blockFinal)

    def test_mix(self):

        sequence = randbytes(16)
        block = Block(sequence)

        blockInit = block.block

        block.MixColumns()

        blockSub = block.block

        block.InvMixColumns()

        blockFinal = block.block

        print("\n TEST MIX")
        print("\n[+] - 1 -", blockInit)
        print("\n[+] - 2 -", blockSub)
        print("\n[+] - 3 -", blockFinal)
        print("\n")

        self.assertNotEqual(blockInit, blockSub)

        self.assertEqual(blockInit, blockFinal)

    def test_add_round_key(self):

        keyseq = randbytes(16)
        sequence = randbytes(16)
        block = Block(sequence)
        key = Key(keyseq)
        keyExp = key.KeyExpansion()

        blockInit = block.block

        block.AddRoundKey(3, keyExp)

        blockSub = block.block

        block.AddRoundKey(3, keyExp)

        blockFinal = block.block

        print("\n TEST ADD ROUND KEY")
        print("\n[+] - 1 -", blockInit)
        print("\n[+] - 2 -", blockSub)
        print("\n[+] - 3 -", blockFinal)
        print("\n")

        self.assertNotEqual(blockInit, blockSub)

        self.assertEqual(blockInit, blockFinal)

    def test_cipher_block(self):

        keyseq = randbytes(16)
        sequence = randbytes(16)
        
        cipher = AES(sequence, keyseq)

        blockInit = cipher.blocks[0].block

        cipher.CipherBlock(cipher.blocks[0])

        blockSub = cipher.blocks[0].block

        cipher.UnCipherBlock(cipher.blocks[0])

        blockFinal = cipher.blocks[0].block

        print("\n TEST CIPHER")
        print("\n[+] - 1 -", blockInit)
        print("\n[+] - 2 -", blockSub)
        print("\n[+] - 3 -", blockFinal)
        print("\n")

        self.assertNotEqual(blockInit, blockSub)

        self.assertEqual(blockInit, blockFinal)