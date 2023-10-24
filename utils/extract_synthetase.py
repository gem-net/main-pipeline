import re

def extract_synthetase(text, page=-1):
    pattern = r'(\w*RS\w*)\s?(\([\w\/]+\))?'
    matches = re.findall(pattern, text)
    
    extracted_data = []
    for match in matches:
        synthetase_type = match[0]
        mutation = match[1]
        extracted_data.append({
            'Combined': match[0] + match[1] if match[1] else match[0],
            'Synthetase': synthetase_type,
            'Mutation': mutation,
            'Page': page + 1
        })
    
    return extracted_data
