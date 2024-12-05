import json
import yaml



##
# VBE
##

with open('config.yaml', 'r') as file:
 config = yaml.safe_load(file)


with open(config['input_path']+"/"+config['ddi4_cogs_json']) as f:
    ddi_json = json.load(f)

ddi_property = ddi_json['properties']['studyUnit']

#print(json.dumps(ddi_property['patternProperties'], indent=4))

for k,v in ddi_property['patternProperties'].items():
   print(k+" | "+str(v))
   print(json.dumps(v['properties'], indent=4))
