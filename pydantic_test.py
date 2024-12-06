
from pydantic import BaseModel, validator
from ddi4Datamodel import *
import json

with open('data/dataset.ddi40.json') as fp:
    ddiModel = json.load(fp)

physicalInstance=PhysicalInstance(**ddiModel['PhysicalInstance']['urn:ddi:int.example:uuid-1:1'])
