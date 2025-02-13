from fetch_data import get_gene_id, get_nucleotide_id, fetch_nucleotide_sequence
from guide_finder import find_guides
from utils import save_to_csv

def main():
    """This script executes the full workflow for retrieving gene data (coding sequence),
    identifying guides for CRISPER Cytidine Base-Editor, simulating expected mutations at the codon level, 
    and assesing their effect on the amino acid sequence, and saving the results to a table in CVS format."""

    gene_name = input("Enter the gene of interest: ")

    # Gets the gene-of-interest as an input from the user,
    # and retrieves its coding sequence from NCBI : 
    gene_id = get_gene_id(gene_name)
    if not gene_id:
        print("Could not find Gene ID.")
        return
    nucleotide_id = get_nucleotide_id(gene_id)
    if not nucleotide_id:
        print("Could not find Nucleotide ID.")
        return
    sequence = fetch_nucleotide_sequence(nucleotide_id)
    
    # The extracted coding sequencence is provided to the guide finder
    # to find valid gudies and their potential resulting mutation : 
    guides = find_guides(sequence)
    results = []

    # Loops through all identified guides and for each one extract its related mutations.
    for guide_seq, left_pos, right_pos, g_in_window, mutation_results in guides:
        for mutation_type, original_aa, mutated_aa, mutated_positions in mutation_results:
            results.append([guide_seq, f"({left_pos}-{right_pos})", g_in_window, mutation_type, original_aa, mutated_aa, mutated_positions])
    
    # Stores guide details (results list) to a CSV file,
    # Using a save_to_csv file coded in utils.py file. 
    save_to_csv("gRNA_results.csv", results)
    print("Results saved to gRNA_results2.csv")

if __name__ == "__main__":
    main()
