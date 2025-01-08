#!/bin/sh
datamodel-codegen  --output-model-type pydantic_v2.BaseModel   \
  --input ./data/jsonSchema.json \
  --input-file-type jsonschema \
  --output ddi4Datamodel.py \
  --use-field-description \
  --field-include-all-keys \
  --use-annotated