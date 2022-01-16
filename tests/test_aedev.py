# THIS FILE IS EXCLUSIVELY MAINTAINED by the project tpl_project V0.3.4 
""" default integration and unit tests for new app/namespace-root/aedev-template/... projects.

remove the outsourced marker in the first line of this test module if you want to add more specialized tests. you then
want also to replace importlib.import_module (only there to prevent syntax errors in this template) with an import
statement.
"""
import importlib
import os

from ae.base import TESTS_FOLDER
from ae.inspector import module_attr

main_module = importlib.import_module("aedev.aedev")


def test_version():
    # noinspection PyUnresolvedReferences
    pkg_version = main_module.__version__
    assert pkg_version
    assert isinstance(pkg_version, str)
    assert pkg_version.count(".") == 2
    assert pkg_version == module_attr("aedev.aedev", '__version__')


def test_docstring():
    pkg_docstring = main_module.__doc__
    assert pkg_docstring
    assert isinstance(pkg_docstring, str)
    assert pkg_docstring == module_attr("aedev.aedev", '__doc__')


def test_tests_folder_exists():
    assert os.path.isdir(TESTS_FOLDER)
