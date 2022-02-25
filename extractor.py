from typing import Set, List

from pathlib import Path
import xml.etree.ElementTree as ET


COMPENDIUMS = [
    'Acquisitions Incorporated',
    'Box Sets',
    'Explorer\'s Guide to Wildemount',
    'Guildmaster\'s Guide to Ravnica',
    'Lost Laboratory of Kwalish',
    'Player\'s Handbook',
    'Sword Coast Adventure\'s Guide',
    'Xanathar\'s Guide to Everything'
]


def load_dictionary(dictionary: str) -> Set[str]:
    with open(dictionary, 'r') as dct:
        return set(dct.read().split())


def load_spell_names(spell_set: Path) -> List[str]:
    root = ET.parse(spell_set).getroot()
    
    spell_names = [spell_name.text for spell_name in root.findall('spell/name')]
    
    return list(filter(None, spell_names))
