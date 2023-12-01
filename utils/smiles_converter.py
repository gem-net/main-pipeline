from py2opsin import py2opsin
import warnings
from functools import cache

@cache
def iupac_to_smiles(iupac_name):
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=RuntimeWarning, module='py2opsin')
        
        if type(iupac_name) != str:
            return None
        
        # replace all whitespace with dashes, double dashes with single dashes
        iupac_name = iupac_name.replace(' ', '-').replace('\n', '-').replace('\t', '-') 
        iupac_name = iupac_name.strip('-')
        while '--' in iupac_name:
            iupac_name = iupac_name.replace('--', '-')

        # corner case 1: remove stereochemistry
        iupac_name = iupac_name.lstrip('(R/S)-').lstrip('(S/R)-')

        smiles_string = py2opsin(
            chemical_name=iupac_name,
            output_format="SMILES"
        )

        if not smiles_string:
            return None
        return smiles_string