git repository manager user manual
**********************************

installation of grm
===================

to installing this tool open a console window and run the following command::

    .. code-block:: shell

        pip install aedev_git_repo_manager

after the installation the ``grm`` command will be available in your OS console.


usage of grm
============

``grm`` is supporting you on all devops (development operations) of your python library, application and web projects.

this covers all actions done on your local machine, on your repository host servers (like ``gitlab.com``
or ``github.com``) and on your web and application deployment servers, like:

    * creating new projects
    * maintaining and upgrading existing projects
    * running integrity checks and unit tests
    * maintaining, syncing and pushing of your git repositories
    * creating and maintaining merge requests on your git repository servers
    * release of your project onto the cheese shop (PyPI.com)
    * deployment of your app/web project


command line options and action arguments
-----------------------------------------

the git repository manager command line consist of options, action keywords, action arguments and optional
action argument flags::

    .. code-block:: shell

        grm [options] [action-keywords] [action-arguments] [action-flags]

all command line options are available in a long form, preceded with two leading hyphen characters, and as a single
character in a short form, preceded with a single hyphen character.

executing ``grm`` with the `--help` command line option (short `-h`) displays a short summary of the available
command line options::

    .. code-block:: shell

        grm --help

general command line options like e.g. `--verbose` (`-v`), `--debug_level` (`-D`), `--path` (`-p`) or `--project` (`-P`)
can be specified for any action. other options, like e.g. the filter options `--filterBranch` (`-B`) and
`--filterExpression` (`-F`), are only supported for bulk actions.


execute ``grm`` with the :func:`~aedev.git_repo_manager.__main__.show_actions` action to display a brief summary of all
the available/registered actions for a project::

    .. code-block:: shell

        grm show_actions

the ``action-keywords`` argument is composed of several words, separated by either a space character, a hyphen character
or an underscore character. some actions can even be abbreviated by a single word shortcut. therefore the following four
commands are identical/equivalent::

    .. code-block:: shell

        grm show_actions
        grm show-actions
        grm show actions
        grm actions

you can add the `--verbose` and/or :ref:`--debug_level <pre-defined-config-options>` command line options to get
a more verbose output. e.g. to include for each listed action also their ``action-arguments`` and ``action-flags``,
their supported project types and their action shortcut, simply add these options to command line of the
:func:`~aedev.git_repo_manager.__main__.show_actions` action::

    .. code-block:: shell

        grm --verbose --debug_level=2 show_actions

the equivalent command line using the short option form (with only one leading hyphen character), and the shortcut of
the :func:`~aedev.git_repo_manager.__main__.show_actions` action (which is
:func:`actions <aedev.git_repo_manager.__main__.show_actions>`) would look like::

    .. code-block:: shell

        grm -v -D 2 actions

some actions are expecting additional ``action-arguments``.

e.g. to execute the
:meth:`~aedev.git_repo_manager.__main__.GitlabCom.release_project` action the
:paramref:`~aedev.git_repo_manager.__main__.GitlabCom.release_project.version_tag` action argument has to specify
the project version to release.

for some actions you can optionally specify ``action-flags``. each flag has a default value, which will be used
if the flag is not specified on the command line.

the action :meth:`~aedev.git_repo_manager.__main__.PythonanywhereCom.check_deploy` e.g. is supporting the flag `CLEANUP`
with a default value of ``False``. specifying this flag on the command line is switching the flag value to ``True``. the
resulting flag value can also be specified on the command line by adding an equal character ('=') to the flag name,
directly followed by the flag value. so the following two commands are identical::

    .. code-block:: shell

        grm check_deploy ... CLEANUP
        grm check_deploy ... CLEANUP=True


bulk actions
^^^^^^^^^^^^

most of the ``grm`` actions operate on a single project or repository and should be executed in the root folder of the
project working tree.

some of them are also available as bulk actions, which are affecting multiple projects, e.g. the portions of
a namespace, or the projects located under the same parent directory.

bulk actions on portions of a namespace are processed by executing them in the namespace root project root folder.

bulk actions on projects underneath a parent directory are executed in the parent folder.

alternatively they can be executed from any other folder by specifying the namespace root project
or the projects parent folder via the `--project` or `--path` options.

for example, bulk actions on namespace root project, like e.g.
`the ae namespace root project <https://gitlab.com/ae-group/ae_ae>`_ via ``--project ae_ae`` or the
`the aedev namespace root project <https://gitlab.com/aedev-group/aedev_aedev>`_ via ``--path path/to/aedev_aedev``.

.. hint:: bulk actions are recognizable by the additional ``children`` keyword in their action name.


repository status actions
^^^^^^^^^^^^^^^^^^^^^^^^^

several actions are determining the project(s) status, like e.g.
:func:`~aedev.git_repo_manager.__main__.show_status`,
:func:`~aedev.git_repo_manager.__main__.show_children_status`,
:meth:`~aedev.git_repo_manager.__main__.GitlabCom.show_repo`,
:meth:`~aedev.git_repo_manager.__main__.GitlabCom.show_children_repos`,
:func:`~aedev.git_repo_manager.__main__.check_integrity`,
:func:`~aedev.git_repo_manager.__main__.check_children_integrity`,
:func:`~aedev.git_repo_manager.__main__.show_versions`,
:func:`~aedev.git_repo_manager.__main__.show_children_versions`, and
:meth:`~aedev.git_repo_manager.__main__.GitlabCom.search_repos`.


project and repository maintenance actions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

useful actions to create, extend or renew a project repository respectively multiple project repositories, are e.g.
:func:`~aedev.git_repo_manager.__main__.new_app`,
:func:`~aedev.git_repo_manager.__main__.new_children`,
:func:`~aedev.git_repo_manager.__main__.new_django`,
:func:`~aedev.git_repo_manager.__main__.new_module`,
:func:`~aedev.git_repo_manager.__main__.new_namespace_root`,
:func:`~aedev.git_repo_manager.__main__.new_package`,
:func:`~aedev.git_repo_manager.__main__.new_project`,
:func:`~aedev.git_repo_manager.__main__.bump_version`,
:func:`~aedev.git_repo_manager.__main__.refresh_outsourced`,
:func:`~aedev.git_repo_manager.__main__.refresh_children_outsourced`.

actions for your other repository maintenance workflows are e.g.
:func:`~aedev.git_repo_manager.__main__.clone_project`,
:func:`~aedev.git_repo_manager.__main__.clone_children_project`,
:meth:`~aedev.git_repo_manager.__main__.GitlabCom.fork_project`,
:meth:`~aedev.git_repo_manager.__main__.GitlabCom.fork_children`,
:func:`~aedev.git_repo_manager.__main__.prepare_commit`,
:func:`~aedev.git_repo_manager.__main__.prepare_children_commit`,
:func:`~aedev.git_repo_manager.__main__.commit_project`,
:func:`~aedev.git_repo_manager.__main__.commit_children`,
:meth:`~aedev.git_repo_manager.__main__.GitlabCom.push_project`,
:meth:`~aedev.git_repo_manager.__main__.GitlabCom.push_children`,
:meth:`~aedev.git_repo_manager.__main__.GitlabCom.request_merge`,
:meth:`~aedev.git_repo_manager.__main__.GitlabCom.request_children_merge`,
:meth:`~aedev.git_repo_manager.__main__.GitlabCom.release_project`,
:meth:`~aedev.git_repo_manager.__main__.GitlabCom.release_children`,
:func:`~aedev.git_repo_manager.__main__.install_editable`, and
:func:`~aedev.git_repo_manager.__main__.install_children_editable`.

to manipulate single files in project repositories use the actions
:func:`~aedev.git_repo_manager.__main__.add_file`,
:func:`~aedev.git_repo_manager.__main__.add_children_file`,
:func:`~aedev.git_repo_manager.__main__.delete_file`,
:func:`~aedev.git_repo_manager.__main__.delete_children_file`,
:func:`~aedev.git_repo_manager.__main__.rename_file`,
:func:`~aedev.git_repo_manager.__main__.rename_children_file`.

in order to synchronize the local :data:`~aedev.git_repo_manager.__main__.MAIN_BRANCH` branch with any changes
done to same branch on the 'origin' remote, execute ``grm`` with the
:func:`~aedev.git_repo_manager.__main__.update_project` and
:func:`~aedev.git_repo_manager.__main__.update_children` actions.

the :meth:`~aedev.git_repo_manager.__main__.GitlabCom.clean_releases` action deletes local+remote release tags and
branches of the specified project that got not published to PYPI.

the execution of bulk command lines for a group of projects can be done with the
:func:`~aedev.git_repo_manager.__main__.run_children_command` action.


web and app deployment server actions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

the actions :meth:`~aedev.git_repo_manager.__main__.PythonanywhereCom.check_deploy` and
:meth:`~aedev.git_repo_manager.__main__.PythonanywhereCom.deploy_project` are working directly with the
deployment servers of your web/Django or app project.

:meth:`~aedev.git_repo_manager.__main__.PythonanywhereCom.check_deploy` is comparing the deployed files against any
repository version tag or against the package files in your project work tree.

the :meth:`~aedev.git_repo_manager.__main__.PythonanywhereCom.deploy_project` action is deploying any new or
changed package files to your web or app deployment server.


filtering children of projects parent or portions of a namespace
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

which children will get processed in a bulk actions get specified by a children-set-expression
action argument, which can combine one or more of the following placeholders via the
set operators of python (`|` for union, `&` for intersection, `-` for difference and `^` for symmetric difference):

    * `all`: all children projects
    * `editable`: projects installed as editable
    * `modified`: projects having uncommitted changes
    * `develop`: projects having checked-out the :data:`~aedev.git_repo_manager.__main__.MAIN_BRANCH`
    * `filterBranch`: projects having checked-out the branch specified with the `--filterBranch` (short `-B`) option
    * `filterExpression`: projects matching the expression specified with the `--filterExpression` (short `-F`) option

for example to show the project versions of namespace portions with uncommitted changes, execute the following command
in the root folder of the namespace root project::

    .. code-block:: shell

        grm show_children_versions modified

to additionally restrict the last example to projects with uncommitted changes in the
:data:`~aedev.git_repo_manager.__main__.MAIN_BRANCH` run::

    .. code-block:: shell

        grm show_children_versions "modified & develop"

.. note:: children-set-expression with set-operators have to be included into high-commas.

more flexible filtering can be done with the command line options `--filterExpression` and `--filterBranch`.
by specifying one of these options the selected/filtered children are then available as a children-set-expression
with the same name as the specified option.

for example to only show the versions of projects with uncommitted changes in the branch ``branch_name`` run::

    .. code-block:: shell

        grm --filterBranch=branch_name show_children_versions "modified & filterBranch"

.. note::
    the name of the branch get specified with the `--filterBranch` option. and the name of the option can then be
    used like a `python set <https://docs.python.org/3/library/stdtypes.html#set>`__ in the children-set-expression
    action argument.

in general, any bulk action can be restricted to only process children/portions projects that have the specified
branch name checked-out. e.g. to only process all children that have checked out the branch ``branch_name`` run::

    .. code-block:: shell

        grm --filterBranch=branch_name <any_bulk_action> filterBranch

exactly the same selection result could be achieved via a more complex Python expression, using the
`--filterExpression` option/children-set-expression::

    .. code-block:: shell

        grm --filterExpression="_git_current_branch(chi_pdv)=='branch_name'" <any_bulk_action> filterExpression

.. hint::
    the filter expression can contain project environment variables and any globals of the git-repo-manager tool.
    additionally, the variable `chi_pdv` can be used to additionally access the project
    environment variables of the other children/portion projects.

.. note:: filter expressions should be included in high-commas.

the next example is selection all children with a project package version number below or equal to ``0.2``::

    .. code-block:: shell

        grm --filterExpression "project_version<='0.2'" <children_bulk_action> filterExpression

the example underneath is showing the local, remote and PyPI versions of the children projects that have a branch
(checked-out or not) with the name ``branch_name`` in their repository::

    .. code-block:: shell

        grm -F "'branch_name' in _git_branches(chi_pdv)" show_children_versions filterExpression

to bulk-release multiple children projects in a :ref:`contribution process <contribution steps>` workflow,
the following bulk actions can be executed, e.g. from within the root folder of a namespace root project:

    * :func:`~aedev.git_repo_manager.__main__.new_children` to increment the versions and refresh outsourced
      files from templates::

        .. code-block:: shell

            grm -b=branch_name new_children modified

    * :func:`~aedev.git_repo_manager.__main__.prepare_children_commit` to prepare the commit message files
      (after you implemented all changes into the above created branch with the name ``branch_name``)::

        .. code-block:: shell

            grm prepare_children_commit "commit message for branch_name" modified

    * :func:`~aedev.git_repo_manager.__main__.commit_children` to commit changes to the local git repositories::

        .. code-block:: shell

            grm commit_children modified

    * :meth:`~aedev.git_repo_manager.__main__.GitlabCom.push_children` to push the committed changes
      to the remote repositories::

        .. code-block:: shell

            grm --filterBranch=branch_name push_children filterBranch

    * :meth:`~aedev.git_repo_manager.__main__.GitlabCom.request_children_merge` to merge pushed changes to the main
      branches on the remote host (without a repository forg add the options: -f -u=group_or_user_name)::

        .. code-block:: shell

            grm --filterBranch=branch_name request_children_merge filterBranch

    * :meth:`~aedev.git_repo_manager.__main__.GitlabCom.release_children` to bulk-release the project packages to PyPI::

        .. code-block:: shell

            grm --filterBranch=branch_name release_children filterBranch

    * :func:`~aedev.git_repo_manager.__main__.install_children_editable`: updates/updates editable installations
      of your local projects into your virtual environment::

        .. code-block:: shell

            grm -F "'branch_name' in _git_branches(chi_pdv)" install_children_editable filterExpression


remote server configuration
---------------------------

``grm`` supports two types of remote servers. remote servers that are hosting the project repository
(e.g. on ``gitlab.com`` or ``github.com``), and remote servers that are hosting deployable apps or web sites
(e.g. ``pythonanywhere.com``).

``grm`` actions with write access to any remote host (web/repository server), like e.g.
:meth:`~aedev.git_repo_manager.__main__.PythonanywhereCom.deploy_project` or
:meth:`~aedev.git_repo_manager.__main__.GitlabCom.push_project`, are
requesting the user credentials for the authentication from the remote server configurations.

.. note::
    remote server configurations can be specified in multiple ways.
    configuration options specified to ``grm`` via command line arguments have the highest priority, followed
    by OS environment variables, :ref:`grm config variables`, and the :ref:`remote server configuration` files.

OS environment variables are mostly used to store credential secrets like authentication tokens, and can get
declared in various ways. default values for these variables can get specified in ``.env`` files (see
:func:`~ae.base.load_env_var_defaults`). these defaults getting overwritten by the OS environment variable values
declared via a startup shell script (like e.g. ``.bashrc``), and these getting overwritten by variable values
set directly in an open console/shell.


command line config options
^^^^^^^^^^^^^^^^^^^^^^^^^^^

the remote server domain address can be specified via command line config-option `domain`.

user credentials can be specified via the ``grm`` command line :ref:`config-options`: `token` and `user` or `group`.


grm config variables
^^^^^^^^^^^^^^^^^^^^

user credentials not specified by the command line :ref:`config-options` are determined from the
:ref:`application config variable <config-variables>` via a user- and domain-specific lookup
with the help of the :meth:`~ae.console.ConsoleApp.get_variable` method.

to resolve the value of the not specified `token` command line option, the lookup first checks if there
exists an OS environment variable and if not found then it is looking for an
:ref:`application config variable <config-variables>`.

for example the lookup of the default value of the not specified `token` command line option,
for an user with the name ``michael`` at the domain ``www.example.com``, is done in the
following order:

    * OS environment variable ``AE_OPTIONS_HOST_TOKEN_AT_WWW_EXAMPLE_COM_MICHAEL``
    * config variable ``host_token_at_www_example_com_michael`` in the config section ``aeOptions``
    * OS environment variable ``AE_OPTIONS_HOST_TOKEN_AT_WWW_EXAMPLE_COM``
    * config variable ``host_token_at_www_example_com`` in the config section ``aeOptions``


project development variables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

this type of configuration variables are extending the ``project environment variables`` provided by the
:mod:`aedev.setup_project` module. the variable values can be configured via the files
`pev.defaults` and/or `pev.updates`, situated in the root folder of a project working tree.

.. note:: the content of these two files consists of a single Python dictionary literal.

by providing for example the user name (of your account at your repository host server) in
the key `STK_AUTHOR`, you don't need to specify it any longer on the ``grm`` command line via
the --user option. in the most cases you will want to provide also the (user/group) name of the
repository owner in the key `REPO_GROUP`, which results in the file contents::

    {
        'STK_AUTHOR': 'UserName',
        'REPO_GROUP': 'UserOrGroupName',
    }

.. hint::
    the default value of `REPO_GROUP` gets compiled from the project name followed by a hyphen and the word `group`.

in order to change the default domain (``gitlab.com``) of the git repository server/host for
a project to ``github.com``, add also the following two lines have into this dict literal::

    'REPO_CODE_DOMAIN': 'github.com',
    'REPO_PAGES_DOMAIN': 'github.io',


git credential storage
^^^^^^^^^^^^^^^^^^^^^^

the git credential storage can be used as the last fallback if your user credentials are neither specified as
:ref:`command line config options` nor via the :ref:`grm config variables`.

the user credentials for actions on git repository hosts (``gitlab.com``/``github.com``/...) like
:meth:`~aedev.git_repo_manager.__main__.GitlabCom.push_project` can alternatively
be set and stored via the git configuration settings
(see `<https://git-scm.com/book/en/v2/Git-Tools-Credential-Storage>`__
and `<https://stackoverflow.com/questions/46645843>`__).

.. hint::
    see `<https://stackoverflow.com/questions/65163081>`__ to disable user/password prompts for fetch and check actions
    to git repository hoster that don't need authentication (and not using the `token` option), like e.g.
    :func:`~aedev.git_repo_manager.__main__._git_fetch`.


grm example workflows
=====================

this section describes some typical development workflows managed with the help of the ``grm`` tool.


create a new project
--------------------

to create a new project (in this example a small console app module with the project name ``senv``),
first create a folder with the name of the new project directly underneath of your
projects source parent folder (e.g. ``~/src``).

then, within the new project root folder create the file ``pev.defaults`` (or ``pev.updated``), like explained
in the section :ref:`project development variables`, in order to specify
your user name (in `STK_AUTHOR`), and the repository owner at your repository host server (in `REPO_GROUP`).

.. hint::
    the section :ref:`remote server configuration` describes alternative ways on how you can configure
    default values of your repository server, your user account name and your credentials/tokens,
    if you not want to specify them in every run of ``grm`` via the command line options.

optionally create and activate a virtual environment for the new project. the following command is
using the tool `pyenv <https://github.com/pyenv/pyenv>`__ to set an existing virtual environment (``py_env``)
as the default for the new project (stored within the ``.python-version`` in the project root folder).

    pyenv local py_env

.. hint::
    using ``pyenv local`` has the advantage to ensure that the project's virtual environment gets activated
    automatically, as soon as you change the current directory of your console to the project root folder.

make sure you have installed the ``grm`` tool, by running the following command within your new project root folder::

    pip install aedev-git-repo-manager

now you can run the ``grm`` tool for the first time in order to create the initial git repository,
and some basic files for the specified project type (e.g. a module project)::

    grm new module

the grm action ``new module`` specifies the type of the project as a single module.
for a more complex project (including multiple modules) use instead the ``new package`` action,
for a namespace root project the ``new namespace root`` action,
for a GUI application the ``new app`` action,
and for a django project the ``new django`` action.

.. hint:: for a console app, in contrary to a GUI app, use either the ``new module`` or ``new package`` actions.

now you can start completing the unit and integration tests code by editing the prepared file ``tests/test_senv.py``.
then the project code can be amended in the generated file ``senv.py``.

.. note::
    the project code of a project of the ``package`` type resides instead in the file ``senv/__init__.py``,
    respective in ``<namespace_name>/senv/__init__.py`` for a namespace portion package.

to complete the documentation of your new project, amend the prepared files ``README.md``,
``docs/index.rst`` and ``docs/features_and_examples.rst`` accordingly.

.. hint::
    at any time in the implementation process you can run the two actions
    :func:`renew <aedev.git_repo_manager.__main__.new_project>` and
    :func:`check <aedev.git_repo_manager.__main__.check_integrity>` in order to
    keep the files created from templates up-to-date, and to test your implementation::

        grm refresh
        grm check

after finishing the implementation you can create the commit message file ``.commit_msg.txt`` in the project root
folder with the :func:`prepare <aedev.git_repo_manager.__main__.prepare_commit>` action::

    grm prepare

the content of the commit message file can then be amended with additional notes.

to commit the first implementation of your new project into your local git repository, execute the
:func:`commit <aedev.git_repo_manager.__main__.commit_project>` action::

    grm commit

now the new project can be pushed to your repository host server (``gitlab.com`` by default)
by executing the :meth:`push <aedev.git_repo_manager.__main__.GitlabCom.push_project>`
action::

    grm push


change request on an existing project
-------------------------------------

a typical workflow to change or add code of an already existing project gets processed with
the following ``grm`` actions:

    * :meth:`fork <aedev.git_repo_manager.__main__.GitlabCom.fork_project>`
      - create or update your fork (only for already existing projects).
    * :func:`renew <aedev.git_repo_manager.__main__.new_project>`
      - update/refresh/renew the files created from templates.
    * :func:`prepare <aedev.git_repo_manager.__main__.prepare_commit>`
      - create a commit message after all planned changes/additions are implemented.
    * :func:`commit <aedev.git_repo_manager.__main__.commit_project>`
      - create a new commit.
    * :meth:`push <aedev.git_repo_manager.__main__.GitlabCom.push_project>`
      - push the commit to the origin repository (your fork).
    * :meth:`request <aedev.git_repo_manager.__main__.GitlabCom.request_merge>`
      - create a merge request.

to complete the workflow, the release and deployment of a project has to be done by an repository maintainer with
the following ``grm`` actions:

    * :meth:`release <aedev.git_repo_manager.__main__.GitlabCom.release_project>`
      - merge the changes into the main branch ({MAIN_BRANCH}) and create a new project release at PyPI.
    * :meth:`deploy <aedev.git_repo_manager.__main__.PythonanywhereCom.deploy_project>`
      - deployment of the new/changed project (only available for web and app projects).


setup a new Django CMS server project
-------------------------------------

the following example describes all the steps that need to be done in the bash console on your computer,
in order to create a new Django project (using Django 4.2 and DjangoCms 4.1), with the project name ``oaio_server``.

after changing your current working directory to the projects source parent folder (e.g. <username>/src), execute the
following commands to create the project root folder ``oaio_server``,
and setup a new virtual environment with the name ``dj4``::

    pyenv install 3.12.3                    (released on 9 april 2024)
    pyenv virtualenv 3.12.3 dj4
    mkdir oaio_server
    cd oaio_server
    pyenv local dj4
    pip install --upgrade pip setuptools aedev-git-repo-manager

now, still from within the project root folder and with the new virtual environment activated, you can
install Django and DjangoCms and prepare an initial project structure by executing the following commands.
the ``djangocms`` command will prompt you to enter the name, email address and password of the django admin/superuser::

    pip install Django==4.2.13              (released on 7 may 2024, 4.2.16 on 12 oct 2024)
    pip install django-cms==4.1.1           (released on 1 may 2024, 4.1.3 on 12 oct 2024)
    djangocms oaio_server .

.. note::
    don’t miss the final dot in the ``djangocms`` command.

now execute the following commands in order to adapt the new project to be managed by ``grm`` and using the
template files provided by the projects in the
`aedev namespace <https://gitlab.com/aedev-group/aedev_aedev>`_ ::

    mv requirements.in requirements.txt
    rm LICENSE
    cp ../kairos/CONTRIBUTING.rst .
    cp ../kairos/LICENSE.md .
    cp ../kairos/README.md .
    cp ../kairos/SECURITY.md .
    cp ../kairos/.gitignore .
    cp ../kairos/pev.defaults .

.. hint::
    alternatively to copying the template based files from another django project (``kairos`` in this case),
    you could create them as new text files, containing the string content of the ``grm``
    :data:`~aedev.git_repo_manager.__main__.OUTSOURCED_MARKER` in its first line.

now edit the empty project file ``oaio_server/__init__.py``, created by the ``djangocms`` command
and add in there the following content::

    """ oaio_server project title
    """
    __version__ = '0.3.0'

the next to adapt to your web project are the values of the :ref:`project development variables`,
which are stored in the project root folder in the file ``pev.defaults``.
a typical file content could look like::

    {
        'STK_AUTHOR':       'repo-group-account-name',
        'STK_AUTHOR_EMAIL': 'project-group-email-address',
        'REPO_GROUP':       'repo-host-owner-user-or-group-id',  # e.g. 'aedev-group'
        'pip_name':         'pip-project-package-name-on-PyPI',  # e.g. 'aedev-git-repo-manager'
        'web_domain':       'web-app-host-domain',               # e.g. 'eu.pythonanywhere.com'
        'web_user':         'web-app-host-user-name',
    }

.. hint::
    to prevent the release of your web project onto the PyPI cheese shop, set the value of the
    `pip_name` variable to an empty string.

by creating in the project root folder another file with the name ``pev.updates`` with the
following content, you don't need to specify your user name and email address, request by
some of the ``grm`` commands/actions::

    {
        'STK_AUTHOR': 'repo-group-account-name',
        'STK_AUTHOR_EMAIL': 'project-default-email-address',
    }

.. note::
    secret user credentials, like passwords and tokens should never be stored as
    project development variables. use instead the :ref:`remote server configuration`.

finally, in order to:

    #. complete the project files from the templates,
    #. prepare the commit message,
    #. commit to git repository,
    #. push the commit to Gitlab,
    #. create a merge request and
    #. release to PyPI and reset the local project (repository) to the main branch::

run the following ``grm`` actions/commands::

    grm -f -i 0 -b init_project renew
    grm prepare
    grm commit
    grm push
    grm request
    grm release LATEST

.. hint::
    the force/-f command line option has to be specified in this example for the ``renew`` actions,
    in order to use the version 0.3.0 (copied from ``kairos``, instead of an initial version 0.0.1).


additional information to setup Django/CMS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* install Django development version (finally NOT used for this project/venv):
  `<https://docs.djangoproject.com/en/4.2/topics/install/#installing-the-development-version>`__
* install DjangoCms by hand (not using docker):
  `<https://docs.django-cms.org/en/latest/introduction/01-install.html#installing-django-cms-by-hand>`__
* Django/Cms software versions:
  `<https://docs.djangoproject.com/en/4.2/faq/install/#faq-python-version-support>`__ and
  `<https://docs.django-cms.org/en/latest/index.html#software-version-requirements-and-release-notes>`__


more grm example workflows
--------------------------

``grm`` workflow examples for ``aedev`` namespace portion projects can be found in the
`contribution documentation of a project
<https://aedev.readthedocs.io/en/latest/index.html#using-the-git-repository-manager-grm>`__,
and for web projects in the `programmer manual
<https://kairos.readthedocs.io/en/latest/programmer_manual.html#using-the-git-repository-manager-grm>`__
of the ``kairos`` web project.
