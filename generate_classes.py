import json
import yaml
import os
import pydantic


##
# VBE
##

with open('config.yaml', 'r') as file:
 config = yaml.safe_load(file)


with open(config['input_path']+"/"+config['ddi4_cogs_json']) as f:
    ddi_json = json.load(f)




##
# Warlock
##

property_name = 'studyUnit'

ddi_property = ddi_json['properties'][property_name]

#print(json.dumps(ddi_property))

studyUnit = warlock.model_factory(ddi_property)

print(studyUnit)

test = studyUnit()
test.URN="0.0..1"

### simpleTypes
for property_name, property_attr in ddi_json["simpleType"].items():
    
    #ddi_property = ddi_json['properties'][property_name]
    code_class_comment = '"""'+"\n"+json.dumps(property_attr, indent=4)+"\n"+'"""'
  

    property_filename=f"./{config['simple_type_path']}/{property_name}.py"
    print(property_filename)

    code_class_str = f"""

class {property_name}:
    
    def __init__(self):
    """



    class_file = open(property_filename, "w+")
    class_file.write(code_class_comment)
    class_file.write(code_class_str)
    
    class_file.close()


### Properties
for property_name, property_attr in ddi_json["properties"].items():
    
    ddi_property = ddi_json['properties'][property_name]
    code_class_comment = '"""'+"\n"+json.dumps(property_attr, indent=4)+"\n"+'"""'
  

    property_filename=f"./{config['properties_path']}/{property_name}.py"
    print(property_filename)

    code_class_str = f"""

class {property_name}:
    
    def __init__(self):
        self = self
    """
    class_file = open(property_filename, "w+")
    class_file.write(code_class_comment)
    class_file.write(code_class_str)
    
    class_file.close()

