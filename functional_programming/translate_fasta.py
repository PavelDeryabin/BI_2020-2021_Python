from Bio.SeqIO import parse
from Bio.Seq import transcribe
from Bio.Seq import translate

path_to_fasta = input('Indicate pathway to the fasta file: ')
codons_table = input('Indicate preferable codon translation table (default is \"Standard\",\ndo nothing and press Enter if \"Standard\" is required): ')
if codons_table == '':
    codons_table = 'Standard'

def translator(path_to_fasta, codons_table):
    fasta_file = open(path_to_fasta, 'r')
    seq_records = parse(fasta_file, 'fasta')

    for seq_record in seq_records:
        dna_seq = seq_record.seq
        rna_seq = transcribe(dna_seq)
        protein_seq = translate(rna_seq, codons_table)
        yield protein_seq

    fasta_file.close()

generator_of_translated_seqs = translator(path_to_fasta, codons_table)

# print(type(generator_of_translated_seqs)) # <class 'generator'>

print(next(generator_of_translated_seqs)) # RNKVSVGEPAEGSLMRPWNKRSS...
print(next(generator_of_translated_seqs)) # FNKVSVGEPAEGSLLRQQNI*SS...
print(next(generator_of_translated_seqs)) # NNKVSVGEPAEGSLLRQQNIRSS...
print(next(generator_of_translated_seqs)) # GNKVSVGEPAEGSLLKQHNKRLS...
print(next(generator_of_translated_seqs)) # StopIteration
