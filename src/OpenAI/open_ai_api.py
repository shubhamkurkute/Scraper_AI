import openai
import os
from .file_handler import FileHandler


class OpenAIConnection:

    def open_ai_connect(self, html_table_src, table_no):
        file_handle = FileHandler()
        openai.api_key = os.environ["OPEN_API_KEY"]
        prompt = html_table_src
        response_json = '''
        {
        "table_no": "Int",
        "css_selector": "String",
        "attrs": {
            "class": "String",
            "id": "String",
            "name": "String"
            }
        }'''


# Initialize the completion
        completion = openai.chat.completions.create(
            model="gpt-4-0613",
            messages=[
                {"role": "system", "content": "You are an expert HTML parser. Your task is to parse the given HTML source. Analyze and extract all the tags from the HTML source. Provide accurate information asked by the user and return the result in a well-structured JSON strictly specified by the user. Do not include any additional explainations, just return the JSON. Steps for CSS creation should be on the basis of styling and design."},
                {"role": "user", "content": f"From the source:{html_table_src} identify head row, row number of the head row and CSS selector for the head row from the table, also give all the text of head row along with the attributes such as class, id and name. The response format should be in specified JSON: {response_json}. Table number is {table_no}"}
            ],
        )

        # Print the result
        print(completion.choices[0].message.content)
        file_handle.file_writer(table_no, completion.choices[0].message.content)      
