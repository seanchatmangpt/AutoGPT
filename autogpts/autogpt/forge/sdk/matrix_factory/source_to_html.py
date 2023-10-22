import jinja2
import yaml

# Load the YAML data from "source.yaml"
with open("source.yaml", "r") as yaml_file:
    yaml_data = yaml.load(yaml_file, Loader=yaml.FullLoader)

# Create a Jinja2 environment and load the template
template_loader = jinja2.FileSystemLoader(
    searchpath="./templates"
)  # Change the path to your template directory
env = jinja2.Environment(loader=template_loader)
template = env.get_template("template.html")

# Render the YAML data into HTML using the template
rendered_html = template.render(yaml_data=yaml_data)

# Write the rendered HTML to "source.html"
with open("index.html", "w") as html_file:
    html_file.write(rendered_html)

print("HTML file 'index.html' has been generated.")
