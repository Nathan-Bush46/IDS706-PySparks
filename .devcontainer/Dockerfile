# Start with the Python 3.12 Dev Container image
FROM mcr.microsoft.com/vscode/devcontainers/python:3.12

# Install dependencies for downloading Java
RUN apt-get update && \
    apt-get install -y wget tar && \
    rm -rf /var/lib/apt/lists/*

# Download and install OpenJDK 11
RUN wget https://github.com/adoptium/temurin11-binaries/releases/download/jdk-11.0.20+8/OpenJDK11U-jdk_x64_linux_hotspot_11.0.20_8.tar.gz -O /tmp/openjdk11.tar.gz && \
    mkdir -p /usr/local/openjdk-11 && \
    tar -xzf /tmp/openjdk11.tar.gz -C /usr/local/openjdk-11 --strip-components=1 && \
    rm /tmp/openjdk11.tar.gz

# Set JAVA_HOME environment variable
ENV JAVA_HOME=/usr/local/openjdk-11
ENV PATH="$JAVA_HOME/bin:$PATH"