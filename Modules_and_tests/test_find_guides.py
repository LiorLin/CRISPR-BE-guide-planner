from guide_finder import find_guides
import re

def test_find_guides():
    """Test guide identification, mutation assessment, and filtering with debugging."""

    test_sequence = (
        "GCGTCGTAGTCTCCTGCAGCGTCTGG" # Valid 2 G's
        "TTGCTTTCCGTTCGAGTGCTTCGG" # Valid 3 G's
        "TTTTGACTGACTGACTGACTTGG"  # Should be filtered due to TTTT
        "GACTGACTGACTTACTCACTTGG"  # Should be filtered due to no G in editing window
        "GCGCGCGCGCGCGCGCGCGCTGG"  # Should be filtered due to high GC content
        "ATATATATATATATAGATATTGG"  # Should be filtered due to low GC content
    )
    # Guides expected :  
    # 1 - TCG|TAG|TCT|CCT|*G*CA|*G*CG|TC position 4-23 (or 3-22 with 0-based indexing)
    # GC Content: 12, Gs in Editing Window: 2
    # First G mutated *G*CA (A) --> ACA (T)   Type: Missense Mutation, position 15
    # Other G mutated *G*CG (A) --> ACG (T)   Type : Missense Mutation, position 18
    # Both G's mutated - Missense mutation

    # 2 - T|TGC|TTT|CCG|TTC|*G*A*G*|T*G*C|TT position 25-44 (or 24-43 with 0-based indexing)
    # GC Content: 10, Gs in Editing Window: 3
    # first/second G mutated GAG/GAA (E) --> AAG/AAA (K)  Type: Missense Mutation, position 39/41
    # Thirs G mutated TGC (C) --> TAC (Y)   Type : Missense Mutation, position 43
    # All G's mutated - Missense mutation. 

    print("Searching for guides by NGG sites...")
    guides = find_guides(test_sequence)
    
    if len(guides) == 0:
        print(" No valid guides found! Possible filtering issue.")
    
    # Loops thrpugh all identified guides and prints their details : 
    for guide_seq, left_pos, right_pos, num_g_in_window, mutation_results in guides:
        print(f"Guide: {guide_seq} at {left_pos}-{right_pos}")
        print(f"GC Content: {guide_seq.count('G') + guide_seq.count('C')}, Gs in Editing Window: {num_g_in_window}")
        
        if num_g_in_window == 0:
            print("Guide filtered out due to lack of G in editing window")
            continue
        
        # Loops through the mutation results for each guide, and prints mutation details : 
        for mutation_type, original_aa, mutated_aa, mutated_positions in mutation_results:
            print(f"Type: {mutation_type}, AA Change: {original_aa} → {mutated_aa}, Mutated Positions: {mutated_positions}")

    
    # The first part deals with all identified guides that are the output of find_guides.
    # In this second part we search for all potential guides in the test sequence (6 guides) independently
    # of the find_guides module and use the module's filters to validate that the guides were filtered
    # for the right reasons. 

    print("\nListing all potential guides and filtering reason:\n")
    
    # Like in the guide_finder.py seaches for NGG sequence and extracts guides 20 nucleotides upstream of N.  
    for match in re.finditer(r'([ACGT])GG', test_sequence):
        pam_index = match.start(1)
        guide_seq = test_sequence[pam_index - 20:pam_index] if pam_index >= 20 else None

        # Calculate GC content and counts G's in editing window. 
        if guide_seq:
            gc_content = guide_seq.count("G") + guide_seq.count("C")
            num_g_in_window = sum(1 for i in range(12, 17) if guide_seq[i] == 'G') if guide_seq else 0
            print(f"Potential Guide: {guide_seq} | Position: {pam_index - 20}-{pam_index - 1}")
            print(f"GC Content: {gc_content} | Gs in Editing Window: {num_g_in_window}")
            
            # Filters if GC content outside the 8-12 range: 
            if not (8 <= gc_content <= 12):
                print(f"Guide filtered: GC content out of range ({gc_content})")

            # Filters if 4 or more consecutive Ts are present: 
            if "TTTT" in guide_seq:
                print(f"Guide filtered: Contains TTTT")
            
            # Filters out guides with no G's in the editing window: 
            if num_g_in_window == 0:
                print(f"Guide filtered: No G in editing window")
    
    assert len(guides) > 0, "No valid guides found! Check debug output."


test_find_guides()


