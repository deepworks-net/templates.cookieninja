import os
import shutil
import sys

# Define target directory relative to cookiecutter project
target_directory = '../{{ cookiecutter._template }}{% raw %}{{cookiecutter.project_slug}}/{% endraw %}'

def merge_directories(source_dir, target_dir=None):
    """
    Recursively merge directories, copying all files and subdirectories.
    """
    if target_dir is None:
        target_dir = target_directory

    try:
        # Create target directory if it does not exist
        os.makedirs(target_dir, exist_ok=True)

        # Check if source directory exists
        if not os.path.exists(source_dir):
            print(f"Error: Source directory '{source_dir}' does not exist")
            sys.exit(1)

        # Iterate over all the files in the source directory
        for filename in os.listdir(source_dir):
            source_file = os.path.join(source_dir, filename)
            target_file = os.path.join(target_dir, filename)
            
            try:
                if os.path.isfile(source_file):
                    # Copy the file to the target directory
                    shutil.copy2(source_file, target_file)
                    print(f"Copied file: {filename}")
                else:
                    # Recursively copy directory
                    merge_directories(source_file, target_file)
                    print(f"Copied directory: {filename}")
            except Exception as e:
                print(f"Error copying {filename}: {str(e)}")
                sys.exit(1)

    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

def main():
    print("Starting pre-generation script...")

    # Define directories relative to cookiecutter template
    skel_directory = os.path.abspath('../{{ cookiecutter._template }}skel')
    core_directory = os.path.join(skel_directory, 'core_files')
    docker_directory = os.path.join(skel_directory, 'docker')

    # Clean target directory if it exists
    if os.path.exists(target_directory):
        try:
            shutil.rmtree(target_directory)
        except Exception as e:
            print(f"Error cleaning target directory: {str(e)}")
            sys.exit(1)

    # Copy core files
    merge_directories(core_directory)

    # Copy docker files if enabled
    if '{{ cookiecutter.has_docker }}' == 'True':
        merge_directories(docker_directory)

    print("Pre-generation script completed successfully")

if __name__ == "__main__":
    main()