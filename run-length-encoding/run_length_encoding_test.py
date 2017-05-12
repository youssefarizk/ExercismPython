import unittest

from run_length_encoding import encode, decode


# test cases adapted from `x-common//canonical-data.json` @ version: 1.0.0

class WordCountTests(unittest.TestCase):
    def test_encode_empty_string(self):
        self.assertEqual(encode(''), '')

    def test_encode_single_characters_only_are_encoded_without_count(self):
        self.assertEqual(encode('XYZ'), 'XYZ')

    def test_encode_string_with_no_single_characters(self):
        self.assertEqual(encode('AABBBCCCC'), '2A3B4C')

    def test_encode_single_characters_mixed_with_repeated_characters(self):
        self.assertEqual(
            encode('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB'),
            '12WB12W3B24WB')

    def test_encode_multiple_whitespace_mixed_in_string(self):
        self.assertEqual(encode('  hsqq qww  '), '2 hs2q q2w2 ')

    def test_encode_lowercase_characters(self):
        self.assertEqual(encode('aabbbcccc'), '2a3b4c')

    def test_decode_empty_string(self):
        self.assertEqual(decode(''), '')

    def test_decode_single_characters_only(self):
        self.assertEqual(decode('XYZ'), 'XYZ')

    def test_decode_string_with_no_single_characters(self):
        self.assertEqual(decode('2A3B4C'), 'AABBBCCCC')

    def test_decode_single_characters_with_repeated_characters(self):
        self.assertEqual(
            decode('12WB12W3B24WB'),
            'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB')

    def test_decode_multiple_whitespace_mixed_in_string(self):
        self.assertEqual(decode('2 hs2q q2w2 '), '  hsqq qww  ')

    def test_decode_lower_case_string(self):
        self.assertEqual(decode('2a3b4c'), 'aabbbcccc')

    def test_combination(self):
        self.assertEqual(decode(encode('zzz ZZ  zZ')), 'zzz ZZ  zZ')


if __name__ == '__main__':
    unittest.main()
