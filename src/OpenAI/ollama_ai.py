import ollama
from .file_handler import FileHandler


class Ollama_AI:
    def ollama_ai(self, html_table_src, table_no):
        file_handle = FileHandler()
        prompt = html_table_src
        response_json = '''
                {
                "table_no": "Int",
                "css_selector": "String",
                "head_row_number":"Int",
                "head_row_names":[],
                "attrs": {
                    "class": "String",
                    "id": "String",
                    "name": "String"
                    }
                }'''

        response = ollama.chat(model="llama3.1", messages=[
            {"role": "system", "content": "You are an expert HTML parser. Your task is to parse the given HTML source. Analyze and extract all the tags from the HTML source. Provide accurate information asked by the user and return the result in a well-structured JSON strictly specified by the user. Do not include any additional explainations, just return the JSON."},
            {"role": "user", "content": f"You have to identify the head row and create CSS selector for the head row. Also give me head row number inside the table along with the attributes of the head row and names of the head row in this json format{response_json} from this HTML source:{html_table_src} and the table number is{table_no}"}
        ])
        print(response['message']['content'])
        file_handle.file_writer(table_no, response["message"]["content"])
