class Dna():

    def __init__(self, seq):
        if len(seq) == 0:
            raise ValueError('Please, enter not empty sequence and try again')
        allowed_nucleotides = ['A', 'T', 'C', 'G']
        for nucleotide in seq:
            if nucleotide not in allowed_nucleotides:
                raise ValueError('Please, enter valid nucleotide characters: A, T, G or C')
        self.sequence = seq
        self.nucleotide_index = 0

    def __next__(self):
        if self.nucleotide_index < len(self.sequence):
            nucleotide = self.sequence[self.nucleotide_index]
            self.nucleotide_index += 1
            return nucleotide
        else:
            raise StopIteration

    def __hash__(self):
        return hash(self.sequence)

    def __eq__(self, other):
        return self.sequence == other.sequence

    def gc_content(self):
        gc_nucleotides = 0
        for nucleotide in self.sequence:
            if nucleotide in ["G", "C"]:
                gc_nucleotides += 1
        return round((gc_nucleotides / len(self.sequence)) * 100)

    def reverse_complement(self):
        complementary_Ns = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
        result = ''
        for nucleotide in self.sequence[::-1]:
            result += complementary_Ns[nucleotide]
        return result

    def transcribe(self):
        return Rna(self.sequence.replace('T', 'U'))


class Rna():

    def __init__(self, seq):
        if len(seq) == 0:
            raise ValueError('Please, enter not empty sequence and try again')
        allowed_nucleotides = ['A', 'U', 'C', 'G']
        for nucleotide in seq:
            if nucleotide not in allowed_nucleotides:
                raise ValueError('Please, enter valid nucleotide characters: A, U, G or C')
        self.sequence = seq
        self.nucleotide_index = 0

    def __next__(self):
        if self.nucleotide_index < len(self.sequence):
            nucleotide = self.sequence[self.nucleotide_index]
            self.nucleotide_index += 1
            return nucleotide
        else:
            raise StopIteration

    def __hash__(self):
        return hash(self.sequence)

    def __eq__(self, other):
        return self.sequence == other.sequence

    def gc_content(self):
        gc_nucleotides = 0
        for nucleotide in self.sequence:
            if nucleotide in ["G", "C"]:
                gc_nucleotides += 1
        return round((gc_nucleotides / len(self.sequence)) * 100)

    def reverse_complement(self):
        complementary_Ns = {'A': 'U', 'U': 'A', 'G': 'C', 'C': 'G'}
        result = ''
        for nucleotide in self.sequence[::-1]:
            result += complementary_Ns[nucleotide]
        return result