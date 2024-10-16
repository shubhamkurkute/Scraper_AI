import json
class FileHandler:
    def file_reader(self):
        with open("src.html", 'r') as f:
            file_data = f.read()
            return file_data

    def file_writer(self, table_no, response):
        with open(f"../output/{table_no}.json", 'w') as writer:
            writer.write(response)

    def json_schema_reader(self):
        with open("D:\\Shubham_Workspace\\Pythons\\Practice\\Open_AI\\scraper_definition.json", 'r') as f:
            json_schema = json.load(f)
            return json_schema
