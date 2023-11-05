# Source: https://github.com/Standard-IO/devcontainers-templates/blob/main/src/python3-poetry-pyenv/.devcontainer/Dockerfile
# FROM mcr.microsoft.com/devcontainers/base:${templateOption:imageVariant}
# FROM mcr.microsoft.com/devcontainers/base:jammy
FROM mcr.microsoft.com/devcontainers/universal:2-linux

ARG DEBIAN_FRONTEND=noninteractive

RUN DEBIAN_FRONTEND=noninteractive \
    && apt-get update \
    && apt-get install -y build-essential screen

RUN echo "codespace:dev" | sudo chpasswd

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt-get install -y ./google-chrome-stable_current_amd64.deb \
    && rm ./google-chrome-stable_current_amd64.deb
