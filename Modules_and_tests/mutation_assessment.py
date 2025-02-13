from Bio.Data import CodonTable

""" This module translates DNA sequences to their corresponding amino acid sequencs
and assess the impact of a mutation (provided original and mutated sequence) on the amino acid 
sequence, and classifies it : 
- silent mutation: no change in amino acid. 
- missense: change in amino acid 
- nonsense : created stop codon * """

def translate_codon(codon):
    # Translate a 3-letter codon into an amino acid using the standard genetic code
    
    genetic_code = CodonTable.unambiguous_dna_by_id[1] # A dictionary that maps codons to amino acids.
    return '*' if codon in genetic_code.stop_codons else genetic_code.forward_table.get(codon, '?')
    # Return * for stop codon, otherwise aa, or ? if codon is invalid. 

def assess_mutation(original_seq, mutated_seq, mutation_position):
    # Assess mutation impact on the amino acid sequence, and classifies it. 

    codon_index = mutation_position // 3
    original_codon = original_seq[codon_index * 3 : (codon_index * 3) + 3]
    mutated_codon = mutated_seq[codon_index * 3 : (codon_index * 3) + 3]
    original_aa = translate_codon(original_codon)
    mutated_aa = translate_codon(mutated_codon)
    if original_aa == '*' and mutated_aa == '*':
        return "Silent Mutation", original_aa, mutated_aa
        # Unchanged stop codon is defined as silent mutation. 
    elif mutated_aa == '*':
        return "Nonsense Mutation", original_aa, mutated_aa
        # Amino acid changed to stop codon is defined as nonesense mutation.
    elif original_aa == mutated_aa:
        return "Silent Mutation", original_aa, mutated_aa
        # Unchanged amino acid is a silent mutation. 
    return "Missense Mutation", original_aa, mutated_aa
    # In all other cases, there is amino acid change leading to missene mutation. 
