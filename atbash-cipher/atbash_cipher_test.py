import unittest

from atbash_cipher import decode, encode


# test cases adapted from `x-common//canonical-data.json` @ version: 1.0.0

class AtbashCipherTest(unittest.TestCase):
    def test_encode_no(self):
        self.assertEqual(encode("no"), "ml")

    def test_encode_yes(self):
        self.assertEqual(encode("yes"), "bvh")

    def test_encode_OMG(self):
        self.assertEqual(encode("OMG"), "lnt")

    def test_encode_O_M_G(self):
        self.assertEqual(encode("O M G"), "lnt")

    def test_encode_long_word(self):
        self.assertEqual(encode("mindblowingly"), "nrmwy oldrm tob")

    def test_encode_numbers(self):
        self.assertEqual(
            encode("Testing, 1 2 3, testing."), "gvhgr mt123 gvhgr mt")

    def test_encode_sentence(self):
        self.assertEqual(
            encode("Truth is fiction."), "gifgs rhurx grlm")

    def test_encode_all_things(self):
        plaintext = "The quick brown fox jumps over the lazy dog."
        ciphertext = "gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt"
        self.assertEqual(encode(plaintext), ciphertext)

    def test_decode_word(self):
        self.assertEqual(decode("vcvix rhn"), "exercism")

    def test_decode_sentence(self):
        self.assertEqual(
            decode("zmlyh gzxov rhlug vmzhg vkkrm thglm v"),
            "anobstacleisoftenasteppingstone")

    def test_decode_numbers(self):
        self.assertEqual(
            decode("gvhgr mt123 gvhgr mt"), "testing123testing")

    def test_decode_all_the_letters(self):
        ciphertext = "gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt"
        plaintext = "thequickbrownfoxjumpsoverthelazydog"
        self.assertEqual(decode(ciphertext), plaintext)

    # additional track specific test
    def test_encode_decode(self):
        self.assertEqual(
            decode(encode("Testing, 1 2 3, testing.")), "testing123testing")


if __name__ == '__main__':
    unittest.main()
