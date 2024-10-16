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
        "row_index": "Int"
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
                {"role": "system", "content": "You are a expert HTML extractor. From the provided source identify the head row. Create a CSS selector for the head row. Steps for CSS selector: Create a CSS selector on the basis of design or inline styling of head row as the table can be nested table. Also provide all the fields mentioned by the user in strictly specified JSON format user. Do not include any additional explainations, just return the JSON."},
                {"role": "user", "content": f"From the source:{html_table_src} identify head row, head row number inside the table starting index as 0 and CSS selector for the head row from the table, also give all the text of head row along with the attributes such as class, id and name. The response format should be in strictly specified JSON: {response_json}. Table number is {table_no}"}
            ],
            temperature=0,
        )

        # Print the result
        print(completion.choices[0].message.content)
        file_handle.file_writer(table_no, completion.choices[0].message.content)
