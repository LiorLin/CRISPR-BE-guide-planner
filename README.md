## CRISPR Base-Editor Guide Planner
<img src="CRISPR BE.jpg" align="right" width="200" style="border-radius: 50%; margin-right: 10px;"> CRISPR-Cas9 systems, originally discovered as part of the adaptive immune system of bacteria, have revolutionized genome editing by enabling precise and efficient DNA modifications using RNA-guided endonucleases. 

In particular, CRISPR base-editor is an advanced tool that generates single-nucleotide changes without introducing double-strand breaks. This holds great promise for studying genetic variants and therapeutic applications. Designing guide RNAs (gRNAs) for base editing is challenging and requires detailed computation to ensure specificity and efficacy. 

## Aim
<img src="sgRNA.jpg" align="right"  width="250" style="border-radius: 50%; margin-right: 10px;">
<p>This project aims to develop a Python-based tool to assist us - students and researchers - in designing gRNAs tailored for CRISPR base-editing. The tool will identify candidate gRNAs and predict their potential edits. It will further assess the biological impact of the induced mutation (mis-sense, non-sense, frameshifts etc.) and search for those associated with disease.</p>

<p>As part of my research on the devastating neurodegenerative disease Amyotrophic lateral sclerosis (ALS) I aim to model familial SOD1-ALS in cell culture.This tool will help me design guides for creating ALS-related mutations in HT29 cells that have the CRISPR base-editor integrated into their genomes.</p>

## Workflow

- **Data Retrieval:** Fetch gene sequences from the UCSC Genome Browser.
- **Guide Identification:** Identify 20-base sequences upstream of PAM sites (NGG) with Cytidines (C) in target positions.
- **Off-target assesment:** Identify Cytidines within the guide sequence outside the raget position that might convert to <br> T with as well but with low efficiency. 
- **Mutation Simulation:** Simulate C → T edits in the sequence.
- **Protein Alignment:** Align modified coding sequences with amino acid sequences to assess mutation effects on the protein.
- **Disease Association:** Compare simulated mutations with known disease variants to prioritize guides.
- **Output:** Export the results including guide sequences, position, simulated mutation, predicted effect,<br> and disease-association to CSV or Excel format.

## Requirments
- Python 3.8+
- Libraries: BioPython, Pandas, Requests
- Access to UCSC Genome Browser or equivalent genome database

During the project's development, the requirements may be added or changed.  

## Note 
This project is a final assignment for the [Basic programming in Pyhton course](https://github.com/szabgab/wis-python-course-2024-11) at the Weizmann Institute of Science taught by [Gabor Szabo](https://github.com/szabgab). 

