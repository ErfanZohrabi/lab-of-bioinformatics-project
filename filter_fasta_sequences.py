"""
This script filters out sequences from a positive set that are already present
in a list of Uniprot entries. It takes three input files:
1. uniprot_ids.fasta: Uniprot entries in FASTA format.
2. positive_set.fasta: The positive set of proteins.
3. cleaned_positive_set.fasta: The cleaned positive set without proteins used for the model.

Functions:
- read_sequences(file): Reads sequences from a given FASTA file and returns them as a set.
- filter_sequences(file, exclude_sequences): Filters out sequences in the given file that are present in the exclude_sequences set.
- write_sequences(sequences, output_file): Writes a list of sequences to a specified FASTA output file.
- filter_common_sequences(file1, file2, output_file): Orchestrates the filtering process by using the above functions.
"""


from Bio import SeqIO

def read_sequences(file):
    """Read sequences from a FASTA file and return as a set of sequences."""
    sequences = set()
    with open(file, "r") as handle:
        for record in SeqIO.parse(handle, "fasta"):
            sequences.add(str(record.seq))
    return sequences

def filter_sequences(file, exclude_sequences):
    """Filter out sequences from the file that are in the exclude_sequences set."""
    filtered_sequences = []
    with open(file, "r") as handle:
        for record in SeqIO.parse(handle, "fasta"):
            sequence = str(record.seq)
            if sequence not in exclude_sequences:
                filtered_sequences.append(record)
    return filtered_sequences

def write_sequences(sequences, output_file):
    """Write sequences to a FASTA file."""
    with open(output_file, "w") as handle:
        SeqIO.write(sequences, handle, "fasta")

def filter_common_sequences(file1, file2, output_file):
    """
    Filters out sequences from file2 that are present in file1 and writes the remaining sequences to output_file.
    
    Parameters:
    file1 (str): Path to the first FASTA file containing Uniprot entries.
    file2 (str): Path to the second FASTA file containing the positive set.
    output_file (str): Path to the output FASTA file for filtered sequences.
    """
    # Read sequences from the first file
    sequences1 = read_sequences(file1)
    
    # Filter sequences from the second file
    filtered_sequences = filter_sequences(file2, sequences1)
    
    # Write filtered sequences to the output file
    write_sequences(filtered_sequences, output_file)

# Define file paths
file1 = "uniprot_ids.fasta" 
file2 = "positive_set.fasta"  
output_file = "cleaned_positive_set.fasta"  

# Run the filtering process
filter_common_sequences(file1, file2, output_file)
