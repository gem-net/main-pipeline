import requests
from functools import cache

@cache
def get_metadata_from_doi(doi):
    """
    Parameters: 
        doi (str): A string containing the DOI of a paper.
    
    Returns: 
        dict: A dictionary containing the metadata of the paper.
            - 'Title': Title of the article
            - 'Authors': List of authors
            - 'Date': Publication date
            - 'Journal': Journal name
    """

    base_url = "https://api.crossref.org/works/"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    
    if doi.startswith("https://doi.org/"):
        doi = doi.replace("https://doi.org/", "")
    
    response = requests.get(base_url + doi, headers=headers)
    data = response.json()

    if "message" in data:
        message = data["message"]
        
        title = message.get("title", ["N/A"])[0]
        authors = [author["given"] + " " + author["family"] for author in message.get("author", [])]
        date = "-".join(map(str, message.get("created", {}).get("date-parts", [["N/A"]])[0]))
        journal = message.get("container-title", ["N/A"])[0]
        
        return {
            "Title": title,
            "Authors": authors,
            "Date": date,
            "Journal": journal
        }
    else:
        return {"Error": "Unable to fetch data for the given DOI."} 

def generate_jacs_citation(metadata):
    """
    Generate a JACS (Journal of the American Chemical Society) citation from metadata.

    Parameters:
        metadata (dict): Dictionary containing metadata of a given DOI.
        - 'Authors': List of authors
        - 'Title': Title of the article
        - 'Date': Publication date
        - 'Journal': Journal name

    Returns:
        citation (str): JACS citation
    """
    authors = metadata.get('Authors', [])
    title = metadata.get('Title', "N/A")
    date = metadata.get('Date', "N/A")
    journal = metadata.get('Journal', "N/A")

    formatted_authors = "; ".join([f"{author.split(' ')[-1]}, {''.join([i[0] for i in author.split(' ')[:-1]])}" for author in authors])

    # TODO: how do I abbreviate journal names?
    journal_abbreviation = journal

    # TODO: what is volume number in italics, page numbers, first-last.   
    citation = f"{formatted_authors}.  {journal_abbreviation} {date}."
    
    return citation

