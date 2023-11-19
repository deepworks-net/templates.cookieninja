# Cookiecutter Template for a DeepWork (Deepworks Framework) Project

## Overview
This cookiecutter template serves to create the boilerplate code for a range of new projects that will conform to the deepworks framework. It's interactive experience allows it to be customized while ensuring consistency, best practices, and ease of use. It also cuts down on all the mundane setup tasks and lets you get going on what you really want to build, while giving you a customized code repository with all of the stuff that is less exciting all ready set up and ready to go.

### Requirements
- Python >= 3.11
- Pip >= 22.3
- Cookiecutter >= 2.4.0 (This dependency is 'included' with the development environment)

**NOTE:** This guide and project is aimed at Windows users running a development environment of Visual Code Studio with the powershell terminal. Any part can be adapted to your own development platform with minor alterations to the commands, but the steps should all remain the same.

## Development
Developing new updates to the Cookiecutter template is a different game than simply using it to create a new project. The following will guide you through how the project is developed, built and published.

### Setup the environment
To setup the development environment locally, perform the following:
```
py -m venv .venv
```

Then activate the environment via the activate script. For powershell, use this command:
```
./venv/Scripts/Activate.ps1
```

There are other scripts under the `./venv/Scripts` directory if you prefer an alternative to powershell.

Once your environment is activated, update pip and install dependencies:
```
py -m pip install --upgrade pip
py -m pip install -r requirements.txt
```

#### Documentation
Serve the documentation locally while you update it via:
```
py -m mkdocs serve
```

You can reach the documentation via a web browser at: `http://127.0.0.1:8000/`

The documentation itself is located in the `docs/` directory, and the mkdocs config is `mkdocs.yml`

To build the documentation locally:
```
py -m mkdocs build
```

This builds the documentation and places it in the new folder `site/`