
from fetch_data import get_gene_id, get_nucleotide_id, fetch_nucleotide_sequence

"""This file tests the fetch_data module."""
# Manually verified function for input provided in upper/lower cases. 

# Data from ncbi for validation (testing gene - SOD1) 
# Gene ID : 6647
# Nucleic acid ID : 1780222508
# First 20 bases (coding sequence) : GCGTCGTAGTCTCCTGCAGC


def test_get_gene_id():
    gene_name = input("Enter the gene name to test: ")
    gene_id = get_gene_id(gene_name)
    assert gene_id is not None, f"Failed to retrieve Gene ID for {gene_name}" 
    # Ensures that a valid gene ID is returned. 
    print(f"Gene ID for {gene_name}: {gene_id}")

def test_get_nucleotide_id():
    gene_name = input("Enter the gene name to test: ")
    gene_id = get_gene_id(gene_name)
    if gene_id:
        nucleotide_id = get_nucleotide_id(gene_id)
        assert nucleotide_id is not None, f"Failed to retrieve Nucleotide ID for {gene_name}" 
        # Ensures that a valid Nucleotide ID is returned.
        print(f"Nucleotide ID for {gene_name}: {nucleotide_id}")
    else:
        print("Gene ID retrieval failed.")

def test_fetch_nucleotide_sequence():
    gene_name = input("Enter the gene name to test: ")
    gene_id = get_gene_id(gene_name)
    if gene_id:
        print(f"Gene ID: {gene_id}")
        nucleotide_id = get_nucleotide_id(gene_id)
        if nucleotide_id:
            print(f"Nucleotide ID: {nucleotide_id}")
            sequence = fetch_nucleotide_sequence(nucleotide_id)
            assert sequence is not None and len(sequence) > 0, f"Failed to fetch nucleotide sequence for {gene_name}"
            # Ensures that the sequence is not empty.
            print(f"Nucleotide sequence is: {sequence[:]}")
            return sequence
        else:
            print("Nucleotide ID retrieval failed.")
    else:
        print("Gene ID retrieval failed.")

test_fetch_nucleotide_sequence()