from pydantic import BaseModel, PositiveInt, ValidationError
from ddi4Datamodel import *
import json
import pprint


# Generating DDI4 from scratch using the Pydantic classes
try:
    sofware_object = SoftwareType(
        softwareName = [NameType(
           # String = "Hello",
            context = "Test")

        ]
    )

    study_unit_object = StudyUnit(
        URN = "0.0.1",
        Agency = "INSERM",
        ID = 'xzze09121245555',
        Version = '0.1',
        Software = [sofware_object]
    )
# In case of validation problem, raise a ValidationError
except ValidationError as e:
    pprint.pp(e.errors())


# Serialize the DDI object in JSON and print it
print(study_unit_object.model_dump_json(exclude_none=True))