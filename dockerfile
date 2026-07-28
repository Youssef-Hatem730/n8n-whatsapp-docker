FROM tzahi12345/youtubedl-material:latest

USER root

RUN apt-get update && apt-get install -y curl unzip && rm -rf /var/lib/apt/lists/*
RUN curl -fsSL https://deno.land/x/install/install.sh | DENO_INSTALL=/usr/local sh

USER root
