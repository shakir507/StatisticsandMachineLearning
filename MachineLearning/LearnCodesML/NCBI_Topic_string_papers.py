from Bio import Entrez, Medline
import pandas as pd

# Set your email address and API key
Entrez.email = "your@email.com"
api_key = "xyz123"

# Define the search query
query = "system dynamics AND patient flow optimization AND healthcare"

# Perform the search
def search_pubmed(query, max_results=100):
    handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results, api_key=api_key)
    record = Entrez.read(handle)
    handle.close()
    return record['IdList']

# Fetch paper details
def fetch_details(id_list):
    ids = ','.join(id_list)
    handle = Entrez.efetch(db="pubmed", id=ids, rettype="medline", retmode="text", api_key=api_key)
    papers = Medline.parse(handle)
    papers_list = list(papers)
    handle.close()
    return papers_list

# Save papers to Excel
def save_to_excel(papers, filename='papers.xlsx'):
    # Extract relevant details
    data = []
    for paper in papers:
        title = paper.get('TI', '')
        authors = ', '.join(paper.get('AU', []))
        journal = paper.get('JT', '')
        pub_date = paper.get('DP', '')
        abstract = paper.get('AB', '')
        doi = paper.get('LID', '')
        
        data.append({
            'Title': title,
            'Authors': authors,
            'Journal': journal,
            'Publication Date': pub_date,
            'Abstract': abstract,
            'DOI': doi
        })
    
    # Create a DataFrame
    df = pd.DataFrame(data)
    
    # Save to Excel
    df.to_excel(filename, index=False)

# Search for papers
paper_ids = search_pubmed(query)

# Fetch details of the papers
if paper_ids:
    papers = fetch_details(paper_ids)
    save_to_excel(papers, filename='pubmed_papers.xlsx')
    print("Papers saved to 'pubmed_papers.xlsx'.")
else:
    print("No papers found for the given query.")
