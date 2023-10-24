import re
from collections import Counter

def extract_compounds(text, page=-1):
    pattern = r'(([\w()-]+)\s*-\s*([\w-]+)-\d-\([\w\[\](),\s-]+\)([\w\s]+)\((\d+)\))'
    matches = re.findall(pattern, text)
    
    extracted_data = []
    for match in matches:
        compound = {
            'Full Name': match[0].strip(),
            'Prefix': match[1],
            'Core': match[2],
            'Suffix': match[3],
            'Compound Number': match[4],
            'Page': page + 1
        }
        extracted_data.append(compound)
    
    return extracted_data

