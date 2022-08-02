from utils import utils
import unittest
import subprocess
import jsonschema
import glob
import os

class TestMethodologies(unittest.TestCase):
    def setUp(self):
        self.methodologyFilenames = list(
            glob.glob(f'{utils.METHODOLOGIES_DIR}/*.json')
        )

    def validate_schema(self, schema_file, data_file):
        print("validating ", data_file)
        schema = utils.get_json(schema_file)
        data = utils.get_json(data_file)
        jsonschema.Draft7Validator.check_schema(schema)
        if error := jsonschema.exceptions.best_match(
            jsonschema.Draft7Validator(schema).iter_errors(data)
        ):
            raise error

    def test_schemas(self):
        for methodologyFilename in self.methodologyFilenames:
            self.validate_schema(utils.SCHEMA_FILENAME, methodologyFilename)

if __name__ == '__main__':
    unittest.main()
