from bs4 import BeautifulSoup
from .open_ai_api import OpenAIConnection
from .ollama_ai import Ollama_AI

try:
    open_ai_connect = OpenAIConnection()
    ollama_ai = Ollama_AI()
    with open("../CO_production.html", "r", encoding="utf-8") as f:
        html_content = f.read()
        soup = BeautifulSoup(html_content, 'html.parser')
        tables = soup.find_all('table')
        for i, table in enumerate(tables):
            for tag in table.find_all(['style', 'option', "select", "table"]):
                tag.extract()

            for tag in table.find_all(True):
                if 'border' in tag.attrs:
                    del tag.attrs['border']
                if 'cellpadding' in tag.attrs:
                    del tag.attrs['cellpadding']
                if 'cellspacing' in tag.attrs:
                    del tag.attrs['cellspacing']
                if 'bordercolor' in tag.attrs:
                    del tag.attrs['bordercolor']
            rows = table.find_all('tr')[:5]
            new_table = soup.new_tag("table")
            for row in rows:
                new_table.append(row)

            clean_html = new_table.prettify()
            open_ai_connect.open_ai_connect(clean_html, i)
            print(clean_html)
except FileNotFoundError:
    print("File not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred: {e}")
