"tests.py"
import unittest
from regex import RegexFSM

class Tests(unittest.TestCase):
    """Tests for the RegexFSM class"""

    def test_letters(self):
        regex_pattern = "abcdhhhf"
        regex_compiled = RegexFSM(regex_pattern)

        self.assertTrue(regex_compiled.check_string("abcdhhhf"),"abcdhhhf")
        self.assertFalse(regex_compiled.check_string("acdhhhf"), "acdhhhf")
        self.assertFalse(regex_compiled.check_string("bcdhhhf"), "bcdhhhf")
        self.assertFalse(regex_compiled.check_string("abcdhhh"), "abcdhhh")

    def test_dots(self):
        regex_pattern = "dge.rrw.ad.t."
        regex_compiled = RegexFSM(regex_pattern)

        self.assertTrue(regex_compiled.check_string("dgearrweadvtz"))
        self.assertTrue(regex_compiled.check_string("dge~rrw0adet/"))
        self.assertTrue(regex_compiled.check_string("dge.rrw.adlt."))
        self.assertFalse(regex_compiled.check_string("dgerrweadvtz"))
        self.assertFalse(regex_compiled.check_string("dge2rrw6ad5t"))
        self.assertFalse(regex_compiled.check_string("de.rrw.ad.t."))

    def test_stars(self):
        regex_pattern = "b*nhj*el*hihi*"
        regex_compiled = RegexFSM(regex_pattern)

        self.assertTrue(regex_compiled.check_string("bbbbnhjjjjjelllllhihiiiii"))
        self.assertTrue(regex_compiled.check_string("nhehih"))
        self.assertTrue(regex_compiled.check_string("bbnhjelhihiii"))
        self.assertFalse(regex_compiled.check_string("bbbnhjjjel00001hihii"))
        self.assertFalse(regex_compiled.check_string("bWnhjelhihi"))
        self.assertFalse(regex_compiled.check_string("bbbbnhjjjjelWWWWWhihiiiiiiik"))

    def test_plus(self):
        regex_pattern = "r+ngd+4+ndjd"
        regex_compiled = RegexFSM(regex_pattern)

        self.assertTrue(regex_compiled.check_string("rrrrngddddd4444ndjd"))
        self.assertTrue(regex_compiled.check_string("rngd4ndjd"))
        self.assertTrue(regex_compiled.check_string("rrngd44444444ndjd"))
        self.assertFalse(regex_compiled.check_string("ngdddd44ndjd"))
        self.assertFalse(regex_compiled.check_string("rngdddd5444ndjd"))
        self.assertFalse(regex_compiled.check_string("rng44ndjd"))

    def test_mixed_1(self):
        regex_pattern = "ab*cd+ee."
        regex_compiled = RegexFSM(regex_pattern)

        self.assertTrue(regex_compiled.check_string("abbbbcddddee0"))
        self.assertTrue(regex_compiled.check_string("acdeeg"))
        self.assertTrue(regex_compiled.check_string("abbbbbcdee9"))
        self.assertFalse(regex_compiled.check_string("abbbcee2"))
        self.assertFalse(regex_compiled.check_string("abcddee"))
        self.assertFalse(regex_compiled.check_string("abbbcddeke"))


if __name__ == "__main__":
    unittest.main()
