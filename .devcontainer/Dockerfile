FROM mcr.microsoft.com/devcontainers/cpp:1-debian-11

# Install additional OS packages
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
    python3 \
    python3-pip \
    build-essential \
    sudo \
    curl \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

# Install Node.js and npm
RUN curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - \
    && apt-get update \
    && apt-get install -y nodejs \
    && npm install -g npm@latest \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

# Create the node user and group with flexible ID assignment
RUN if ! getent group node > /dev/null 2>&1; then \
        groupadd -g 1001 node; \
    fi \
    && if ! getent passwd node > /dev/null 2>&1; then \
        useradd -u 1001 -g node -s /bin/bash -m node; \
    fi

# Add node user to sudo group and configure passwordless sudo
RUN adduser node sudo \
    && echo "node ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/node \
    && chmod 0440 /etc/sudoers.d/node

# Create and set up directories for node user
RUN mkdir -p /home/node/.npm-global \
    && chown -R node:node /home/node \
    && chmod -R 755 /home/node/.npm-global

# Set up environment variables for the node user
ENV HOME=/home/node
ENV NPM_CONFIG_PREFIX=/home/node/.npm-global
ENV PATH=/home/node/.npm-global/bin:$PATH

# Switch to node user
USER node

# Configure npm and install global packages
RUN npm config set prefix /home/node/.npm-global \
    && npm install -g node-gyp

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-here> 