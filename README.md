# Cookiecutter Template for a DeepWork (Deepworks Framework) Project

## Overview
This cookiecutter template serves to create the boilerplate code for a range of new projects that will conform to the deepworks framework. It's interactive experience allows it to be customized while ensuring consistency, best practices, and ease of use. It also cuts down on all the mundane setup tasks and lets you get going on what you really want to build, while giving you a customized code repository with all of the stuff that is less exciting all ready set up and ready to go.

**NOTE:** While this is a cookiecutter template, it utilizes a fork of cookieninja (included in the project as a submodule) for generation as it has enhanced features and fixes. Please refer to the [cookieninja docs](https://cookieninja.readthedocs.io/) as the cookiecutter documentation will not cover all the options the cookieninja fork uses.

### Requirements
- Python >= 3.11
- Pip >= 22.3

## Quick Start
Make sure to pull down this repository and initialize the submodule, then install the submodule via pip from within the project directory:
```
cd dw-project-template
py -m pip install cnsrc/
```

Then customize and create a project with cookieninja!
```
cookieninja template/
```

You will then be walked through the setup of your project. Once completed, the customized project will be created in your current working directory.


## Template Development

Please see the full documentation here: [DeepWork Cookiecutter Project Template Documentation](https://deepworks-net.github.io/dw-project-template/)