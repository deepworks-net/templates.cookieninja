import os
import shutil

target_directory = '../{{ cookiecutter._template }}{% raw %}{{cookiecutter.project_slug}}/{% endraw %}'

def merge_directories(source_dir, target_dir = target_directory):
    # Create target directory if it does not exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Iterate over all the files in the source directory
    for filename in os.listdir(source_dir):
        source_file = os.path.join(source_dir, filename)
        target_file = os.path.join(target_dir, filename)
        # Check if it's a file and not a directory
        if os.path.isfile(source_file):
            # Copy the file to the target directory
            shutil.copy2(source_file, target_file)
            print(f"Copied {source_file} to {target_file}")
        else:
            merge_directories(source_file, target_file)
            print(f"Copied Directory {source_file} to {target_file}")

print(f"Starting pre-generation script")

skel_directory = '../{{ cookiecutter._template }}skel/'
core_directory = '{skel_directory}core_files/'
docker_directory = '{skel_directory}docker/'

shutil.rmtree(target_directory, ignore_errors=True)

merge_directories(core_directory)

if '{{ cookiecutter.has_docker }}' == 'True':
    merge_directories(docker_directory)
