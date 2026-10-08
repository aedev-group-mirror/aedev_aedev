""" aedev_aedev unit tests. """
from aedev.aedev import __doc__, __version__


def test_version():
    """ test existence of project package version. """
    assert __version__
    assert isinstance(__version__, str)
    assert __version__.count('.') == 2


def test_docstring():
    """ test existence of project package docstring. """
    assert __doc__
    assert isinstance(__doc__, str)
