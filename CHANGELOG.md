# DeepWork Cookiecutter Project Template Changelog
### Latest Release: v0.2.1 (11/26/2024)

### v0.2.1 (11/26/2024)
- Fixed file path handling in `pre_gen_project.py` script
- Added robust error handling and logging to file copy operations
- Improved directory creation and validation in pre-generation hooks
- Updated path construction to use `os.path.join()` for better cross-platform compatibility
- Added status messages for debugging template generation process
- Fixed issues with template directory structure recognition
- Updated requirements.txt with new package versions:
  - mkdocs 1.6.0
  - mkdocs-material 9.5.19
  - mkdocs-material-extensions 1.3.1
  - cookiecutter 2.6.0
  - cookieninja 1.0.0
- Streamlined setup.ps1 script to use requirements.txt
- Updated minimum requirements in README:
  - Python >= 3.11.4
  - Pip >= 24.3.1
- Improved documentation clarity regarding cookieninja usage

### v0.2.0 (11/19/2023)
- Bumped mkdocs-material from 9.4.8 to 9.4.9
- Added git submodule dependency checks for dependabot
- Added `pre_gen_project.py` script that (can) copy files from the skel directory and perform other tasks
- Added deepworks fork of cookieninja as a submodule to utilize the dependent questions functionality
- Moved stictly files related to docker in the skel directory
- Updated project files to add content based on the `has_docker` flag
- Updated default mkdocs config to omit the rabbit icon
- Updated user documentation
- Changed project structure and name
- Fixed bugs and issues with project generation

### v0.1.0 (11/13/2023)
- Initial Build and Release