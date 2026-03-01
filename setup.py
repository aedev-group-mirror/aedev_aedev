# THIS FILE IS EXCLUSIVELY MAINTAINED by the project aedev.project_tpls v0.3.76
""" setup of aedev namespace-root: aedev namespace root, providing setup, development and documentation tools/templates for Python projects.. """
import sys
# noinspection PyUnresolvedReferences
import pathlib
# noinspection PyUnresolvedReferences
import setuptools


print("SetUp " + __name__ + ": " + sys.executable + str(sys.argv) + f" {sys.path=}")

setup_kwargs = {
    'author': 'AndiEcker',
    'author_email': 'aecker2@gmail.com',
    'classifiers': [
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development',
        'Typing :: Typed',
    ],
    'description': 'aedev namespace-root: aedev namespace root, providing setup, development and documentation tools/templates for Python projects.',
    'extras_require': {
        'dev': [
            'aedev_project_tpls',
            'aedev_app_tpls',
            'aedev_namespace_root_tpls',
            'aedev_base',
            'aedev_commands',
            'aedev_project_vars',
            'aedev_project_manager',
            'aedev_aedev',
            'sphinx',
            'sphinx-rtd-theme',
            'sphinx_autodoc_typehints',
            'sphinx_paramlinks',
            'aedev_project_vars',
            'anybadge',
            'flake8',
            'mypy',
            'pylint',
            'pytest',
            'pytest-cov',
            'pytest-django',
            'typing',
            'types-setuptools',
        ],
        'docs': [
            'sphinx',
            'sphinx-rtd-theme',
            'sphinx_autodoc_typehints',
            'sphinx_paramlinks',
            'aedev_project_vars',
        ],
        'tests': [
            'anybadge',
            'flake8',
            'mypy',
            'pylint',
            'pytest',
            'pytest-cov',
            'pytest-django',
            'typing',
            'types-setuptools',
        ],
    },
    'install_requires': [],
    'keywords': [
        'configuration',
        'development',
        'environment',
        'productivity',
    ],
    'license': 'GPL-3.0-or-later',
    'long_description': (pathlib.Path(__file__).parent / 'README.md').read_text(encoding='utf-8'),
    'long_description_content_type': 'text/markdown',
    'name': 'aedev_aedev',
    'package_data': {
        '': [
            'templates/de_spt_namespace-root_de_otf_de_tpl_README.md',
        ],
    },
    'packages': [
        'aedev.aedev',
        'aedev.aedev.templates',
    ],
    'project_urls': {
        'Bug Tracker': 'https://gitlab.com/aedev-group/aedev_aedev/-/issues',
        'Documentation': 'https://aedev.readthedocs.io/en/latest/_autosummary/aedev.aedev.html',
        'Repository': 'https://gitlab.com/aedev-group/aedev_aedev',
        'Source': 'https://aedev.readthedocs.io/en/latest/_modules/aedev/aedev.html',
    },
    'python_requires': '>=3.12',
    'url': 'https://gitlab.com/aedev-group/aedev_aedev',
    'version': '0.3.32',
    'zip_safe': False,
}

if __name__ == "__main__":
    setuptools.setup(**setup_kwargs)
    pass
