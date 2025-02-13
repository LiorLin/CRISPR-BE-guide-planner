import requests
import time
import urllib.parse

""" This module gets a gene name from the user (default organism - Homo apiens) and retrieves 
    its Gene ID, fetches the corresponding RefSeq nucleotide ID and returns the nucleotide sequence
    of the coding region (mRNA) for further analysis"""

def get_gene_id(gene_name, organism="Homo sapiens"):
    # Fetch NCBI Gene ID for a given gene name.

    encoded_gene_name = urllib.parse.quote(gene_name.strip())  # Converts into URL-friendly format. 
    search_url = (f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?"
                  f"db=gene&term={encoded_gene_name}[Gene Name]+AND+{organism}[Organism]&retmode=json")
    # from gene data base (db)

    response = requests.get(search_url)
    time.sleep(0.5)  # Avoid rate limits by adding 0.5 second delay. 

    if response.status_code != 200: # if request fails 
        print(f"Error: HTTP {response.status_code}")
        return None

    data = response.json()
    gene_ids = data.get("esearchresult", {}).get("idlist", []) # extract the gene ID list. 

    if not gene_ids:  # If the list is empty, return None and print a message
        print(f"Error: No valid Gene ID found for '{gene_name}'. Check the spelling or try another gene.")
        return None

    return gene_ids[0]  # Return the first valid Gene ID

def get_nucleotide_id(gene_id):
    # Fetch NCBI Nucleotide Sequence ID (RefSeq) using Gene ID.
    search_url = (f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?"
                  f"db=nuccore&term={gene_id}[Gene ID]&retmode=json")
    # from nucleodite data base (nuccore)
    
    response = requests.get(search_url)
    time.sleep(0.5)

    if response.status_code != 200:
        print(f"Error: HTTP {response.status_code}")
        return None

    data = response.json()
    nucleotide_ids = data.get("esearchresult", {}).get("idlist", []) # extract the nucleotide ID list.

    if not nucleotide_ids:
        print(f"Error: No nucleotide sequence found for Gene ID: {gene_id}.")
        return None

    return nucleotide_ids[0] # Return the first valid nucleotide ID

def fetch_nucleotide_sequence(nucleotide_id):
    # Fetch Nucleotide Sequence from NCBI given a valid nucleotide ID
    fetch_url = (f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?"
                 f"db=nuccore&id={nucleotide_id}&rettype=fasta&retmode=text")
    # Fetch the FASTA sequence (text)

    response = requests.get(fetch_url)
    time.sleep(0.5)

    if response.status_code != 200:
        print(f"Error: HTTP {response.status_code}") 
        return None

    sequence_data = response.text.split("\n")[1:]  # Remove FASTA header
    return "".join(sequence_data) # Joins the remaining lines into a single string. 
