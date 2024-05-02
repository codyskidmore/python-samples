import json


def get_template(template_name):
    with open(template_name, "r") as template:
        return template.read()

def get_json_data(json_file):
    with open(json_file, "r") as file:
        return json.load(file)

def save_template_output(template_output, file_name):
    with open(file_name, "w") as output_file:
        output_file.write(template_output)
