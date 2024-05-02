from TemplateData import TemplateData
import json

def get_json_data(json_file):
    with open(json_file, "r") as file:
        return json.load(file)

if __name__ == '__main__':
    json_data = get_json_data("template-data.json")
    template_data = TemplateData(**json_data)
    print(template_data)
