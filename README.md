## CRISPR Base-editor guide planner
CRISPR-Cas9 systems, originally discovered as part of the adaptive immune system of bacteria, have revolutionized genome editing by enabling precise and efficient DNA modifications using RNA-guided endonucleases. 
<img src="CRISPR BE.jpg" align="left" width="200" style="border-radius: 50%; margin-right: 10px;">
In particular, the CRISPR base-editor is an advanced tool that generates single-nucleotide changes without introducing double-strand breaks. This holds great promise for studying genetic variants and therapeutic applications. Designing guide RNAs (gRNAs) for base editing is challenging and requires detailed computation to ensure specificity and efficacy. 

As part of my research on the devastating neurodegenerative disease Amyotrophic lateral sclerosis (ALS) I aim to model familial SOD1-ALS in a cell-culture. I have already developed cells with the CRISPR base-editor system integrated into their genome, and this tool will help me design guides to create disease-related mutations in these cells.

## Aims 
This project aims to develop a Python-based tool to assist us - students and researchers - in designing gRNAs tailored for CRISPR base-editing. The tool will identify candidate gRNAs and predict their potential edits. It will further assess the biological impact of the induced mutations (causing mis-sense or non-sense mutations, frameshifts etc.) and search for those associated with disease. 

## Programs logic 

- **Data Retrieval:** Fetch gene sequences from the UCSC Genome Browser.
- **Guide Identification:** Identify 20-base sequences upstream of PAM sites (NGG) with Cytidines (C) in target positions.
- **Off-target assesment:** Identify Cytidines within the guide sequence outside the raget position that might convert to T with as well but with low efficiency. 
- **Mutation Simulation:** Simulate C → T edits in the sequence.
- **Protein Alignment:** Align modified coding sequences with amino acid sequences to assess mutation effects on the protein.
- **Disease Association:** Compare simulated mutations with known disease variants to prioritize guides.
- **Output:** Export the results including guide sequences, position, simulated mutation, predicted effect, and disease-association to CSV or Excel format.

## Predicted requirments
- Python 3.8+
- Libraries: BioPython, Pandas, Requests
- Access to UCSC Genome Browser or equivalent genome database

During the project's development, additional requirements may be added.  
