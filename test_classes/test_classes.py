import unittest
from classes import Dna
from classes import Rna

class TestDna(unittest.TestCase):

    def test_is_correct_seq(self):
        dna = Dna('AATGCC')
        self.assertEqual(dna.sequence, 'AATGCC')

    def test_is_not_empty_seq(self):
        self.assertRaises(ValueError, Dna, '')

    def test_is_not_lowercase_seq(self):
        self.assertRaises(ValueError, Dna, 'acTgC')

    def test_is_not_non_nucleotide_seq(self):
        self.assertRaises(ValueError, Dna, 'MWQPR')

    def test_is_not_rna_seq(self):
        self.assertRaises(ValueError, Dna, 'AAUGCC')

    def test_equal(self):
        self.assertEqual(Dna('AATGCC'), Dna('AATGCC'))

    def test_iterable(self):
        dna = Dna('AATGCC')
        self.assertListEqual([x for x in dna.sequence], ['A', 'A', 'T', 'G', 'C', 'C'])

    def test_gc_content(self):
        dna = Dna('AATGCC')
        self.assertEqual(dna.gc_content(), 50)

    def test_reverse_complement(self):
        dna = Dna('AATGCC')
        self.assertEqual(dna.reverse_complement(), 'GGCATT')

    def test_transcribe(self):
        dna = Dna('AATGCC')
        self.assertEqual(dna.transcribe(), Rna('AAUGCC'))


class TestRna(unittest.TestCase):

    def test_is_correct_seq(self):
        rna = Rna('AAUGCC')
        self.assertEqual(rna.sequence, 'AAUGCC')

    def test_is_not_empty_seq(self):
        self.assertRaises(ValueError, Rna, '')

    def test_is_not_lowercase_seq(self):
        self.assertRaises(ValueError, Rna, 'acUgC')

    def test_is_not_non_nucleotide_seq(self):
        self.assertRaises(ValueError, Rna, 'MWQPR')

    def test_is_not_dna_seq(self):
        self.assertRaises(ValueError, Rna, 'AATGCC')

    def test_equal(self):
        self.assertEqual(Rna('AAUGCC'), Rna('AAUGCC'))

    def test_iterable(self):
        rna = Rna('AAUGCC')
        self.assertListEqual([x for x in rna.sequence], ['A', 'A', 'U', 'G', 'C', 'C'])

    def test_gc_content(self):
        rna = Rna('AAUGCC')
        self.assertEqual(rna.gc_content(), 50)

    def test_reverse_complement(self):
        rna = Rna('AAUGCC')
        self.assertEqual(rna.reverse_complement(), 'GGCAUU')


if __name__ == '__main__':
    unittest.main()