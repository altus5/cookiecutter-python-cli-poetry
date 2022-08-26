#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath: str) -> None:
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_dir(filepath: str) -> None:
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_dir_if_empty(filepath: str) -> None:
    if len(os.listdir(filepath)) == 0:
        remove_dir(filepath)


if __name__ == "__main__":

    if "{{ cookiecutter.use_mysql }}" != "y":
        remove_dir("docker/mysql")
        remove_file(".envs/.mysql")

    if "{{ cookiecutter.use_jupyterlab }}" != "y":
        remove_dir("notebooks")

    if "no cli" in "{{ cookiecutter.command_line_interface|lower }}":
        cli_file = os.path.join("src", "{{ cookiecutter.module_name }}", "cli.py")
        remove_file(cli_file)

    remove_dir_if_empty(".envs")
