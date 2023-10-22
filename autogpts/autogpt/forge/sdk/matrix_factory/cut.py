import click
import subprocess
from pathlib import Path


@click.command()
@click.option("--project_name", prompt="Project name", help="The name of the project.")
@click.option(
    "--target_directory",
    prompt="Target directory",
    help="The directory where the project will be created.",
)
@click.option(
    "--repo_url",
    prompt="Repository URL",
    help="The cookiecutter template repository URL.",
)
def run_matrix_factory(project_name, target_directory, repo_url):
    cmd = [
        "cookiecutter",
        repo_url,
        "--no-input",
        f"project_name={project_name}",
        f"-o {target_directory}",
    ]
    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    run_matrix_factory()
