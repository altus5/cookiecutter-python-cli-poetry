ARG PYTHON_VERSION=3.9-slim-buster

FROM python:${PYTHON_VERSION}

ARG BUILD_ENVIRONMENT=production
ARG APP_HOME=/app
ARG USERNAME=appuser
ARG USER_UID=1000
ARG USER_GID=$USER_UID

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV BUILD_ENV ${BUILD_ENVIRONMENT}

WORKDIR ${APP_HOME}

# Install required system dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
  # dependencies for building Python packages
  build-essential \
  # Verify git, process tools, lsb-release (common in install instructions for CLIs) installed
  git \
  iproute2 \
  procps \
  lsb-release \
  zip \
  unzip \
  jq \
  curl \
  less \
  vim \
  ssh \
  cookiecutter \
{%- if cookiecutter.use_mysql == "y" %}
  # mysqlclient
  default-libmysqlclient-dev \
{%- endif %}
  # Create a non-root user to use if preferred - see https://aka.ms/vscode-remote/containers/non-root-user.
  && groupadd --gid $USER_GID $USERNAME \
  && useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME \
  # [Optional] Add sudo support for the non-root user
  && apt-get install -y sudo \
  && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME\
  && chmod 0440 /etc/sudoers.d/$USERNAME \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

{%- if cookiecutter.use_jupyterlab == "y" %}
# jupyterlab は本番環境には不要なので、production 以外のときにインストールする
RUN \
  if [ "${BUILD_ENVIRONMENT}" != "production" ]; then \
    pip install pandas matplotlib ipython-sql \
    ;; \
  fi
{%- endif %}

# # Requirements are installed here to ensure they will be cached.
# COPY ./poetry.* ${APP_HOME}/
# COPY ./pyproject.toml ${APP_HOME}/

# make develop owner of the WORKDIR directory as well.
RUN chown -R $USERNAME:$USERNAME ${APP_HOME}

USER $USERNAME

# Install poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
ENV PATH /home/$USERNAME/.poetry/bin:${APP_HOME}/.venv/bin:$PATH:/home/$USERNAME/.local/bin

# RUN poetry install
