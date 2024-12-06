# EDDI24  Hackathon Project

Goal : build Python classes for DDI4 with `cogs` input.

## Usage
### Get the COGS model in json
- Go to https://github.com/ddialliance/ddimodel/tags
- Get the latest release
- pick ddi-lifecycle_alloutputs_...zip
- extract `/json/jsonScheme.json` from the zip

-  Create a `data` folder on repo root
-  Copy `jsonScheme.json` to `data/jsonScheme.json` 
### Create config file
- Copy the `config.yaml.template` to `config.yaml`
- Change the path and name of the jsonScheme.json file if needed.
### Generate the python classes (optional)

From the repo root folder, execute 
```
sh generate_model.sh
```
Output : **ddi4Datamodel.py**

### Create a DDI
`ddi4-fromscratch.py` is a small studyUnit example.

## Known issues

- `utc-millisec` from Duration in jsonScheme is not recognized and converted to a float
- Basic inherited types (like strings) are not generated properly in jsonScheme. An issue has been submitted : https://github.com/ddialliance/ddimodel/issues/56
-  There is a problem in generated python classes in `ddi4Datamodel.py`. A `Type` property must be added manually. You can find the `ddi4DatamodelFixed.py` in the repo. TODO : generate classes and add the Type property afterwards

## Contributors
- Thibaud Ritzenthaler
- Vincent Benoit
- Oliver Lyttleton
