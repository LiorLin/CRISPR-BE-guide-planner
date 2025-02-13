
from mutation_assessment import assess_mutation
import re

def find_guides(sequence):
    """Identify 20-base sequences to the left of NGG filters them and simulate mutations."""

    guides = [] # Will store all valid gudies. 

    for match in re.finditer(r'([ACGT])GG', sequence): # Using regular expressions to locate PAM sequence (NGG)
        pam_index = match.start(1) # Finds the position of N in the sequence. 
        if pam_index < 20: # Skips guide if its too close to the start. 
            continue
        guide_seq = sequence[pam_index - 20:pam_index] # Extract a 20-nucleotide sequence upstream of N. 
        leftmost_position = pam_index - 20 # 20 upstream (to the left) of N. 
        rightmost_position = pam_index - 1 # One upstream (to the left) of N. 
        
        # Calculate GC content
        gc_content = guide_seq.count("G") + guide_seq.count("C")
        
        # Apply filters :
        if not (8 <= gc_content <= 12):
            continue  # Skip if GC content is outside the 8-12 range
        if "TTTT" in guide_seq:
            continue  # Skip if 4 or more consecutive Ts are present
        
        # Identify G's in the 4-8 (inclusive) editing window when counting from 3'-to-5' (right-to-left),  
        # stores their relative position and sums them up :   

        g_positions = [i for i in range(12, 17) if guide_seq[i] == 'G'] # In 0-based indexing left-to-right position 12-16. 
        # in range(12, 17) - start index inclusive, end index  exclusive. 

        num_g_in_window = len(g_positions) 
        if num_g_in_window == 0: # Filters out guides that don't have G's in their editing window. 
            continue
        

        mutation_results = [] # Will store all valid non-silent mutations. 
        for g_pos in g_positions: # Looping through each G in the editing window

            # Creating a temporary mutated guide sequence : 
            temp_mutated_guide = list(guide_seq) # Converts the guide sequence to a list so it could be modified. 
            temp_mutated_guide[g_pos] = 'A' # Changing G to A in a specific positon. 
            temp_mutated_guide = ''.join(temp_mutated_guide) # Converts the guide sequence back to a string. 
            
            # Creating a temporary mutated full length sequence :
            temp_mutated_sequence = sequence[:leftmost_position] + temp_mutated_guide + sequence[rightmost_position+1:]
            
            # Using assess_mutation which translates the original and mutated codon to amino acids
            # and classifies the mutation type. 
            mutation_type, original_aa, mutated_aa = assess_mutation(sequence, temp_mutated_sequence, leftmost_position + g_pos)

            if mutation_type != "Silent Mutation": # Keeps only non-silent mutations (Missense, Nonsense).
                mutated_positions = [leftmost_position + g_pos]  # Single G mutation position
                # Storing the details of a single mutation in a list : 
                mutation_results.append((mutation_type, original_aa, mutated_aa, mutated_positions))
        
        if mutation_results:  # Keep only guides with at least one non-silent mutation
            # Addung the details of a single guide, to the guides liat. 
            guides.append((guide_seq, leftmost_position, rightmost_position, num_g_in_window, mutation_results))
    
    # Sorts guides by #G's in window (prioritizing guides with fewer G's): 
    guides.sort(key=lambda x: (x[3]))
    return guides