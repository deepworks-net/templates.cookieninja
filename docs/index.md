# DeepWork Project Template

## Overview
The DeepWork Project Template is a sophisticated cookiecutter template designed to streamline the creation of projects that conform to the deepworks framework. This template automates the setup of boilerplate code while providing a customizable, interactive experience that ensures consistency and adherence to best practices.

By handling routine setup tasks automatically, developers can focus on core development work while benefiting from a pre-configured repository that includes all essential infrastructure components.

## Key Features
- Interactive project customization
- Automated boilerplate code generation
- Built-in best practices enforcement
- Framework compliance validation
- Docker support (optional)
- Comprehensive documentation setup

## Technical Requirements
### Prerequisites
- Python >= 3.11.4
- Pip >= 24.3.1
- Git (for submodule management)

### Dependencies
All project dependencies are managed through `requirements.txt` and include:
- mkdocs 1.6.0
- mkdocs-material 9.5.19
- mkdocs-material-extensions 1.3.1
- cookiecutter 2.6.0
- cookieninja 1.0.0

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/templates.cookieninja.git
cd templates.cookieninja
```

### 2. Initialize Submodules
```bash
git submodule update --init --recursive
```

### 3. Setup Environment
Using the automated script:
```powershell
./setup.ps1
```

Or manually:
```powershell
py -m venv .venv
& ".venv/Scripts/Activate.ps1"
py -m pip install --upgrade pip
py -m pip install -r requirements.txt
```

## Usage

### Creating a New Project
1. Navigate to your desired parent directory
2. Run cookieninja:
```powershell
py -m cookieninja template/
```
3. Follow the interactive prompts to customize your project
4. Your new project will be generated in the current directory

### Template Options
During project creation, you'll be prompted to configure various aspects of your project:
- Project name and slug
- Docker support
- Documentation preferences
- Additional features (based on project type)

## Special Note on Cookieninja
This template utilizes a custom fork of cookieninja (included as a submodule) instead of standard cookiecutter. This fork provides:
- Enhanced feature set
- Additional customization options
- Various bug fixes and improvements

For detailed information about template options and features, please refer to the [cookieninja documentation](https://cookieninja.readthedocs.io/).

## Development and Contributing

### Local Development
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests
5. Submit a pull request

### Contributing Guidelines
Please review our [Contributing Guide](CONTRIBUTING.md) for detailed information about:
- Code style and standards
- Pull request process
- Testing requirements
- Documentation guidelines

### Code of Conduct
All contributors are expected to adhere to our [Code of Conduct](CODE_OF_CONDUCT.md).

## Documentation
For complete documentation, including advanced usage and customization options, please visit the [DeepWork Cookiecutter Project Template Documentation](https://deepworks-net.github.io/templates.cookieninja/).

## Support
- Issue Tracker: GitHub Issues
- Documentation: Project Documentation Site
- Wiki: GitHub Wiki

## Acknowledgments
- Cookiecutter project team
- All contributors to this template
- The DeepWork framework team