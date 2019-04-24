import json, random

with open('matrix.json') as matrix_json:
	 data = json.load(matrix_json)
         insult = [random.choice(data['start']), random.choice(data['middle']), random.choice(data['end'])]
	 print u' '.join(insult) 
