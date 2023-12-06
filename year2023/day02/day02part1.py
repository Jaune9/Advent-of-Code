from typing import Dict

"""
regex for game id
    \w* (\d*):

regex for each sac
    (((\d* \w*)(, |)){1,3})
"""

def get_total_id(max_colors: Dict[str, int]):
    max_red = max_colors['red']
    max_green = max_colors['green']
    max_blue = max_colors['blue']

    
