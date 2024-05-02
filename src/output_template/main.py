from template_utils import get_template, get_json_data, save_template_output

from jinja2 import Template

if __name__ == '__main__':
    template_file = get_template("template.html")
    json_data = get_json_data("template-data.json")
    template = Template(template_file)
    rendered_template = template.render(json_data)
    save_template_output(rendered_template, "template_output.html")
