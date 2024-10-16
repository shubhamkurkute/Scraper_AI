import openai
import os
from .file_handler import FileHandler
from pydantic import BaseModel
from .scraper_definition import TableData


class OpenAIConnection:

    def open_ai_connect(self, html_table_src, table_no):
        file_handle = FileHandler()
        openai.api_key = os.environ["OPEN_API_KEY"]
        prompt = html_table_src
        # response_json = '''
        # {
        # "table_no": "Int",
        # "row_index": "Int"
        # "css_selector": "String",
        # "attrs": {
        #     "class": "String",
        #     "id": "String",
        #     "name": "String"
        #     }
        # }'''
        response_schema = file_handle.json_schema_reader()
        completion = openai.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
                {"role": "system", "content": "You are an expert HTML extractor. From the provided source, identify the head row. Create a CSS selector for the head row. Steps for CSS selector: Create a CSS selector on the basis of design or inline styling of the head row as the table can be nested. Also, provide all the fields asked by the user."},
                {"role": "user", "content": f"From the source:{html_table_src}, identify the head row, head row number inside the table starting index as 0, and CSS selector for the head row from the table. Also give all the text or names of head row along with the attributes such as class, id, and name. Inject table number into response and table number is {table_no}"}
            ],
            temperature=0,
            response_format={
                "type": "json_schema",
                "json_schema": {
                    "name": "math_reponse",
                    "schema": response_schema
                }
            }
                
        )
        print(completion.choices[0].message.parsed)
        file_handle.file_writer(table_no, completion.choices[0].message.content)
