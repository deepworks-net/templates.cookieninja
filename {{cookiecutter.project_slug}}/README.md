# {{cookiecutter.project_name}} Image 
[![Stage](https://img.shields.io/badge/stage-alpha-orange)](#) [![Docker Image Version (latest semver)](https://img.shields.io/docker/v/{{ cookiecutter.image_name }}/latest)](https://hub.docker.com/r/{{ cookiecutter.image_name }}) ![Maintained](https://img.shields.io/badge/maintained-yes-brightgreen.svg)

## Overview
TODO: Please enter your overview of the image here.

## Base Image
TODO: Please enter information about the base image here.

## Information 
[![Tags](https://img.shields.io/badge/{{ cookiecutter.image_name }}-%20latest%20|%20{{ cookiecutter.image_version }}%20-blue.svg)](https://hub.docker.com/r/{{ cookiecutter.image_name }}/latest) ![Docker Image Size (tag)](https://img.shields.io/docker/image-size/{{ cookiecutter.image_name }}/latest) [![Built](https://img.shields.io/badge/Built-03/15/2022-blue.svg)](#)

## Security 
![Last Snyk Scan](https://img.shields.io/badge/Last%20Snyk%20Scan-03/15/2022-blue) ![Vulnerabilities](https://img.shields.io/badge/Vulnerabilities-0-brightgreen)

## Dependencies 
TODO: Add any other dependencies here.
[![Docker Utility Scripts](https://img.shields.io/badge/docker%20utils-0.2.2--beta-blue)](https://github.com/deepworks-net/docker-utils)

## Quick Start
Here's how you can quickly start using the {{ cookiecutter.project_name }} Image:

1. Pull the latest image using the following command in your terminal:
```SHELL
docker pull {{ cookiecutter.image_name }}:latest
```

2. Run the image with Docker:
```SHELL
docker run -d {{ cookiecutter.image_name }}:latest {{ cookiecutter.Image_init_command }}
```

3. Or, run it with Docker Compose:
```SHELL
docker compose up -d latest
```
