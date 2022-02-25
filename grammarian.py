from pathlib import Path
from typing import List, Dict

import extractor
import distancer


ALLOWED_DISTANCE: int = 1


if __name__ == '__main__':
    # If 'spells' dir does not exist, create it
    Path('spells/compendiums').mkdir(parents=True, exist_ok=True)
    
    compendium_spell_names: Dict[str, List[str]] = {}
    
    # Saving spell lists for possible later use
    for compendium in extractor.COMPENDIUMS:
        with open(f'spells/compendiums/{compendium}.txt', 'w') as out:
            spell_names = extractor.load_spell_names(
                Path(f'DnDAppFiles/Spells/{compendium}.xml')
            )
            
            compendium_spell_names[compendium] = spell_names
            
            out.writelines(map(lambda x: x + '\n', spell_names))
        
    # Making directory for alterations
    Path('spells/alterations').mkdir(parents=True, exist_ok=True)
    
    # Loading default dictionary
    dct = extractor.load_dictionary('english-words/words_alpha.txt')
    
    # Writing all alterations to corrresponding compendium files
    for compendium in extractor.COMPENDIUMS:
        with open(f'spells/alterations/{compendium}.md', 'w') as out:
            out.write(f'# {compendium}\n\n')
            
            for spell in compendium_spell_names[compendium]:
                prepared_spell = spell.lower()
                
                out.write(f'## {prepared_spell}\n\n')
                
                alterations = distancer.find_equidistances_sentence(
                    prepared_spell,
                    ALLOWED_DISTANCE,
                    dct
                )
                
                for alteration in alterations:
                    out.write(f'- {alteration}\n')
                
                out.write('\n')
