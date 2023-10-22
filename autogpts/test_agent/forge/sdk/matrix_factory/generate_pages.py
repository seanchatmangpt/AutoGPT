import jinja2
import yaml


def generate_module_pages(yaml_data):
    template_loader = jinja2.FileSystemLoader(
        searchpath="./templates"
    )  # Change the path to your template directory
    env = jinja2.Environment(loader=template_loader)
    template = env.get_template("module_template.html")

    for class_name, class_info in yaml_data.items():
        # Render the HTML for each module
        rendered_html = template.render(class_name=class_name, class_info=class_info)

        # Write the rendered HTML to a separate file for each module
        with open(f"{class_name}.html", "w") as html_file:
            html_file.write(rendered_html)


if __name__ == "__main__":
    # Load the YAML data from "source.yaml"
    with open("source.yaml", "r") as yaml_file:
        yaml_data = yaml.load(yaml_file, Loader=yaml.FullLoader)

    # Generate module-specific HTML pages
    generate_module_pages(yaml_data)

    print("Module-specific HTML pages have been generated.")
