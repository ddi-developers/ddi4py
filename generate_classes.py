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
  
### write files
for property_name, property_attr in ddi_json["properties"].items():
    
    ddi_property = ddi_json['properties'][property_name]
    code_class_comment = '"""'+"\n"+json.dumps(property_attr, indent=4)+"\n"+'"""'
  



    code_class_str = f"""

class {property_name}:
    
    def __init__(self):
        self = self
    """
    class_file = open(f"classes/{property_name}.py", "w+")
    class_file.write(code_class_comment)
    class_file.write(code_class_str)
    
    class_file.close()
