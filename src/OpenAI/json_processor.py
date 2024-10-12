import re
import json

class JSONProcessor:

   
    def process_json(self):
        input_string = """
            The head row of the table seems to be the second table row "<tr>", where the title "Production Data" is stated. Note that this table does not have the traditional "<th>" elements to mark the head row.

                    The CSS selector for that row will be tbody > tr:nth-child(2)

                    The JSON for your request would be following :

                    ```json
                    {
                        "table_no": 0,
                        "css_selector": "tbody > tr:nth-child(2)",
                        "attrs": {
                            "class": "labelLargeBold",
                            "id": "lblHeading",
                            "name": null
                        }
                    }"""
        json_match = re.search(r'json\n(.*?)', input_string, re.DOTALL)
        print(json_match)


json_process = JSONProcessor()
json_process.process_json()
