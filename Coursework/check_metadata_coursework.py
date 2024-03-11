"""
Usage:
1. Download a clean version of the coursework from Moodle
2. run: 
`python check_metdata.py <path to clean coursework>.ipynb <path to your submission>.ipynb`
3. If it runs through with no errors your coursework should be fine, if not, copy your answers over to the clean version of the notebook and try again (don't copy the cells but copy the code/answers into the existing cells)
"""

import sys
import json


nb1 = json.load(open(sys.argv[1], 'rb'))
nb2 = json.load(open(sys.argv[2], 'rb'))

altered = False
for idx, cells_1, cells_2 in zip(range(len(nb1['cells'])), nb1['cells'], nb2['cells']):
    
    if 'nbgrader' in cells_1["metadata"] or 'nbgrader' in cells_2["metadata"]:
        try:
            # metadata doesn't match
            if cells_1['metadata']['nbgrader']['grade_id'] != cells_2['metadata']['nbgrader']['grade_id']:
                altered = True
                print(f'Cell metadata of cell {idx +1} is not the same')
        except:
            # cell doesn't have nbgrader data
            altered = True
            print(f'Cell metadata of cell {idx +1} is not the same')

if altered:
    print("The metadata of the notebooks is not the same, see messages above.")
else:
    print("The metadata of the notebooks is the same.")