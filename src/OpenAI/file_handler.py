class FileHandler:
    def file_reader(self):
        with open("src.html", 'r') as f:
            file_data = f.read()
            return file_data

    def file_writer(self, table_no, response):
        with open(f"../output/{table_no}.json", 'w') as writer:
            writer.write(response)
