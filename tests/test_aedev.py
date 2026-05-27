""" aedev_aedev unit tests. """
import importlib


main_module = importlib.import_module('aedev.aedev')


def test_version():
    """ test existence of project package version. """
    pkg_version = main_module.__version__
    assert pkg_version
    assert isinstance(pkg_version, str)
    assert pkg_version.count('.') == 2


def test_docstring():
    """ test existence of project package docstring. """
    pkg_docstring = main_module.__doc__
    assert pkg_docstring
    assert isinstance(pkg_docstring, str)
