import re

def extract_tRNA(text, page=-1):
    pattern = r'(\w+[-–])?(tRNA\n\w+\n\w+)'
    matches = re.findall(pattern, text)
    
    extracted_data = []
    for match in matches:
        prefix, tRNA_data = match
        prefix = prefix.strip('tRNA') # clean up prefix
        tRNA_parts = tRNA_data.split('\n')
        
        if len(tRNA_parts) == 3:
            tRNA_type, part1, part2 = tRNA_parts
            part2 = part2.strip('pair') # clean up part2
        else:
            continue 
        
        extracted_data.append({
            'Full Name': prefix + tRNA_data if prefix else tRNA_data,
            'Prefix': prefix if prefix else None,
            'tRNA Type': tRNA_type,
            'Part 1': part1,
            'Part 2': part2,
            'Page': page + 1
        })
    
    return extracted_data
