import json
import yaml

with open('./input/jsonSchema.json', 'r') as file:
    ddi_l = json.load(file)

for property_name, property_attr in ddi_l["properties"].items():
    code_class_str = f"""
class {property_name}:
    
    def __init__(self):
        self = self
    """
    class_file = open(f"classes/{property_name}.py", "w+")
    class_file.write(code_class_str)
    class_file.close()

