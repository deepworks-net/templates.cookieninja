import os
import shutil

def merge_directories(source_dir, target_dir):
    # Create target directory if it does not exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Iterate over all the files in the source directory
    for filename in os.listdir(source_dir):
        source_file = os.path.join(source_dir, filename)

        # Check if it's a file and not a directory
        if os.path.isfile(source_file):
            target_file = os.path.join(target_dir, filename)

            # Copy the file to the target directory
            shutil.copy2(source_file, target_file)
            print(f"Copied {source_file} to {target_file}")


print(f"Starting pre-generation-script")

target_directory = '.'
skel_directory = '../{{ cookiecutter._template }}skel/'
docker_directory = skel_directory+'docker/'

if '{{ cookiecutter.has_docker }}' == 'True':
    merge_directories(docker_directory, target_directory)
