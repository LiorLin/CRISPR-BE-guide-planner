from mutation_assessment import translate_codon, assess_mutation

def test_translate_codon():
    # Test the translation of codons into amino acids.
    test_codons = {
        "ATG": "M",  # Methionine (Start codon)
        "TAA": "*", "TGA": "*", "TAG": "*",  # Stop codons
        "GGC": "G",  # Glycine
        "AAA": "K",  # Lysine
        "TTC": "F",  # Phenylalanine
    }
    
    for codon, expected_aa in test_codons.items():
        translated_aa = translate_codon(codon)
        print(f"Codon: {codon} -> Translated: {translated_aa}, Expected: {expected_aa}")
        assert translated_aa == expected_aa, f"Codon {codon} translated to {translated_aa}, expected {expected_aa}"
        # If translated_aa does not match expected_aa, the test fails.
    print("translate_codon test passed.")

def test_assess_mutation():
    # Test the assessment of mutations in the codon level on the amino acid sequence. 
    # Exampled for each of the three possible mutation types. 

    # Test G → A missense mutation

    original_seq = "ATGCGTTAA"  # Normal sequence
    mutated_seq = "ATGCATTAA"   # G → A mutation at position 4 
    # CG*T (R) --> CAT (H)
    mutation_position = 4  # Position in sequence (0-based)
    mutation_result = assess_mutation(original_seq, mutated_seq, mutation_position)
    print(f"Mutation: G → A at position {mutation_position}, Result: {mutation_result}")
    assert mutation_result == ("Missense Mutation", "R", "H"), f"Unexpected result: {mutation_result}"
    
    # Test G → A Nonsense Mutation (creates stop codon) : 

    original_seq_nonsense = "ATGTGGCAA"  # Normal sequence
    mutated_seq = "ATGTGACAA"  # G → A mutation at position 5
    # TGG* (W) --> TGA (*)
    mutation_position = 5  # Position in sequence (0-based)
    mutation_result = assess_mutation(original_seq_nonsense, mutated_seq, mutation_position)
    print(f"Nonsense Mutation: G → A at position {mutation_position}, Result: {mutation_result}")
    assert mutation_result == ("Nonsense Mutation", "W", "*"), f"Unexpected result: {mutation_result}"

    # Test G → A Silent Mutation (no amino acid change):

    original_seq_silent = "ATGGGGTAA"  # Normal sequence
    mutated_seq = "ATGGGATAA"  # G → A mutation at position 5
    # GGG (G) --> GGA (G)
    mutation_position = 5  # Position in sequence (0-based)
    mutation_result = assess_mutation(original_seq_silent, mutated_seq, mutation_position)
    print(f"Silent Mutation: G → A at position {mutation_position}, Result: {mutation_result}")
    assert mutation_result == ("Silent Mutation", "G", "G"), f"Unexpected result: {mutation_result}"
    

test_translate_codon()
test_assess_mutation()
   
