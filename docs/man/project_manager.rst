project manager user manual
***************************

installation of pjm
===================

to installing this tool open a console window and run the following command::

        pip install aedev_project_manager

after the installation the commands ``project-manager`` and its shortcut ``pjm`` will be available in your OS console.


usage of pjm
============

``pjm`` is supporting you on all devops (development operations) of your python library, application and web projects.

this covers all actions done on your local machine, on your repository host servers (like ``gitlab.com``
or ``github.com``) and on your web and application deployment servers, like:

    * creating new projects
    * maintaining and upgrading existing projects
    * checking project status and integrity
    * maintaining, syncing and pushing of your git repositories
    * creating and maintaining merge requests on your git repository servers
    * release of your project onto PyPI - the cheese shop (pypi.com and test.pypi.com)
    * deployment of your app/web project


command line options and action arguments
-----------------------------------------

the pjm command line consist of options, action keywords, action arguments and optional
action argument flags::

        pjm [options] [action-keywords] [action-arguments] [action-flags]

executing ``pjm`` with the `--help` command line option (short `-h`) displays a short summary of the available
command line options::

        pjm --help

all command line options are available in a long form, preceded with two leading hyphen characters. most of them are
also available in a short form, as a single character, preceded with a single hyphen character.

general command line options like e.g. `--more_verbose` (`-v`), `--debug_level` (`-D`), `--path` (`-p`) or
`--project` (`-P`) can be specified for any action. other options, like e.g. the filter options `--filterBranch` (`-B`)
and `--filterExpression` (`-F`), are only supported for bulk actions.


execute ``pjm`` with the :func:`~aedev.project_manager.__main__.show_actions` action to display a brief summary of all
the available/registered actions for a project::

        pjm show_actions

the ``action-keywords`` argument is composed of several words, separated by either a space character, a hyphen character
or an underscore character. some actions can even be abbreviated by a single word shortcut. therefore the following four
commands are identical/equivalent::

        pjm show_actions
        pjm show-actions
        pjm show actions
        pjm actions

add the `--more_verbose` (-v) and/or :ref:`--debug_level <pre-defined-config-options>` (-D) command line options to get
a more verbose output. e.g. to include for each listed action also their ``action-arguments`` and ``action-flags``,
their supported project types and their action shortcut, simply add these options to command line of the
:func:`~aedev.project_manager.__main__.show_actions` action::

        pjm --more_verbose --debug_level=2 show_actions

the equivalent command line using the short option form (with only one leading hyphen character), and the shortcut of
the :func:`~aedev.project_manager.__main__.show_actions` action (which is
:func:`actions <aedev.project_manager.__main__.show_actions>`) would look like::

        pjm -v -D 2 actions

some actions are expecting additional ``action-arguments``, e.g. to execute the
:meth:`~aedev.project_manager.__main__.GitlabCom.release_project` action the
:paramref:`~aedev.project_manager.__main__.GitlabCom.release_project.version_tag` action argument has to specify
the project version to release.

for some actions you can optionally specify ``action-flags``. each flag has a default value, which will be used
if the flag is not specified on the command line.

the action :meth:`~aedev.project_manager.__main__.PythonanywhereCom.check_deploy` e.g. is supporting the flag `CLEANUP`
with a default value of ``False``. specifying this flag on the command line is switching the flag value to ``True``. the
resulting flag value can also be specified on the command line by adding an equal character ('=') to the flag name,
directly followed by the flag value. so the following two commands are identical::

        pjm check_deploy ... CLEANUP
        pjm check_deploy ... CLEANUP=True


bulk actions
^^^^^^^^^^^^

most of the ``pjm`` actions operate on a single project or repository and should be executed in the root folder of the
project working tree.

some of them are also available as bulk actions, which are affecting multiple projects, e.g. the portions of
a namespace, or the projects located under the same parent directory.

bulk actions on portions of a namespace are processed by executing them in the namespace root project root folder.

bulk actions on projects underneath a parent directory are executed in the parent folder.

alternatively they can be executed from any other folder by specifying the namespace root project
or the projects parent folder via the `--project_path` (-p) option.

for example, bulk actions on namespace root project, like e.g.
`the ae namespace root project <https://gitlab.com/ae-group/ae_ae>`_ via
``--project_path path_to_namespace_root_project/ae_ae`` or the
`the aedev namespace root project <https://gitlab.com/aedev-group/aedev_aedev>`_ via ``-p=path/to/aedev_aedev``.

.. hint:: bulk actions are recognizable by the additional ``children`` keyword in their action name.


repository status check actions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

a quick overview over the current project version numbers on (1) your local machine, the (2) origin and (3) upstream
remotes, the project releases on (4) the PyPI and (5) your web server (only for Django projects) can be archived with
the :func:`~aedev.project_manager.__main__.show_versions` action (short: ``versions``):

        pjm versions

the :func:`~aedev.project_manager.__main__.check_integrity` action (short: ``check``) is proofing
the integrity of your project on your local machine. this includes linting and style checks (using
`flake0 <https://flake8.pycqa.org/>`__ and `pylint <https://www.pylint.org/>`__),
the unit and integration tests (using `pytest <https://docs.pytest.org/>`__),
test coverage (using `coverage.py <https://coverage.readthedocs.io/>`__) and
if the managed project files, created from templates, are up-to-date:

        pjm check

.. hint::
    the ``check_integrity`` action is also used on the CI tasks on the Git remote servers, excluding the
    integration tests. to simulate the checks done in the CI tasks on your local machine put the OS environment variable
    ``CI_PROJECT_ID=1`` in front of the ``pjm check`` command line.

the general status overview of your project on the local machine and on the remote Git repository server provides the
action :func:`~aedev.project_manager.__main__.show_status` (short: ``status``). run this action to display the current
branch name, a compact ``git diff`` between your working tree against the locally and remotely committed project files
and a recommendation which pjm action should be executed next:

        pjm status

.. hint::
    specifying the `--more_verbose` (-v) option on all these check actions are amending the console output.
    e.g. the ``show_status`` action displays a complete Git status and diff output.

.. note::
    most of these actions can be executed as a bulk action for namespace portions or sister projects under
    the same source project parent directory. for more details see
    :func:`~aedev.project_manager.__main__.check_children_integrity`,
    :func:`~aedev.project_manager.__main__.show_children_status`, and
    :func:`~aedev.project_manager.__main__.show_children_versions`.


Git remote investigation actions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

to search for repositories on the Git remote servers run the action
:meth:`~aedev.project_manager.__main__.GitlabCom.search_repos`. a detailed overview over a foreign remote
repository can be displayed with the :meth:`~aedev.project_manager.__main__.GitlabCom.show_remote` action.

.. note:: these actions are currently only implemented for ``GitLab`` remote servers.


project and repository maintenance actions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

useful actions to create, extend or renew a project repository respectively multiple project repositories, are e.g.
:func:`~aedev.project_manager.__main__.new_app`,
:func:`~aedev.project_manager.__main__.new_children`,
:func:`~aedev.project_manager.__main__.new_django`,
:func:`~aedev.project_manager.__main__.new_module`,
:func:`~aedev.project_manager.__main__.new_namespace_root`,
:func:`~aedev.project_manager.__main__.new_package`,
:func:`~aedev.project_manager.__main__.new_playground`,
:func:`~aedev.project_manager.__main__.new_project`,
:func:`~aedev.project_manager.__main__.refresh_managed`,
:func:`~aedev.project_manager.__main__.refresh_children_managed`.

actions for your other repository maintenance workflows are e.g.
:func:`~aedev.project_manager.__main__.clone_project`,
:func:`~aedev.project_manager.__main__.clone_children_project`,
:meth:`~aedev.project_manager.__main__.GitlabCom.fork_project`,
:meth:`~aedev.project_manager.__main__.GitlabCom.fork_children`,
:func:`~aedev.project_manager.__main__.prepare_commit`,
:func:`~aedev.project_manager.__main__.prepare_children_commit`,
:func:`~aedev.project_manager.__main__.commit_project`,
:func:`~aedev.project_manager.__main__.commit_children`,
:meth:`~aedev.project_manager.__main__.GitlabCom.push_project`,
:meth:`~aedev.project_manager.__main__.GitlabCom.push_children`,
:meth:`~aedev.project_manager.__main__.GitlabCom.request_merge`,
:meth:`~aedev.project_manager.__main__.GitlabCom.request_children_merge`,
:meth:`~aedev.project_manager.__main__.GitlabCom.release_project`,
:meth:`~aedev.project_manager.__main__.GitlabCom.release_children`,
:func:`~aedev.project_manager.__main__.install_editable`, and
:func:`~aedev.project_manager.__main__.install_children_editable`.

to manipulate single files in project repositories use the actions
:func:`~aedev.project_manager.__main__.add_file`,
:func:`~aedev.project_manager.__main__.add_children_file`,
:func:`~aedev.project_manager.__main__.delete_file`,
:func:`~aedev.project_manager.__main__.delete_children_file`,
:func:`~aedev.project_manager.__main__.rename_file`,
:func:`~aedev.project_manager.__main__.rename_children_file`.

in order to synchronize the local main branch with any changes
done to same branch on the 'origin' remote, execute ``pjm`` with the
:func:`~aedev.project_manager.__main__.update_project` and
:func:`~aedev.project_manager.__main__.update_children` actions.

the :meth:`~aedev.project_manager.__main__.GitlabCom.clean_releases` action deletes local+remote release tags and
branches of the specified project that got not published to PYPI.

the execution of bulk command lines for a group of projects can be done with the
:func:`~aedev.project_manager.__main__.run_children_command` action.


web and app deployment server actions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

the actions :meth:`~aedev.project_manager.__main__.PythonanywhereCom.check_deploy` and
:meth:`~aedev.project_manager.__main__.PythonanywhereCom.deploy_project` are working directly with the
deployment servers of your web/Django or app project.

:meth:`~aedev.project_manager.__main__.PythonanywhereCom.check_deploy` is comparing the deployed files against any
repository version tag or against the package files in your project work tree.

the :meth:`~aedev.project_manager.__main__.PythonanywhereCom.deploy_project` action is deploying any new or
changed package files to your web or app deployment server.


filtering children of projects parent or portions of a namespace
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

which children will get processed in a bulk actions get specified by a children-set-expression
action argument, which can combine one or more of the following placeholders via the
set operators of python (`|` for union, `&` for intersection, `-` for difference and `^` for symmetric difference):

    * `all`: all children projects
    * `editable`: projects installed as editable
    * `modified`: projects having uncommitted changes
    * `develop`: projects having checked-out the main branch
    * `filterBranch`: projects having checked-out the branch specified with the `--filterBranch` (short `-B`) option
    * `filterExpression`: projects matching the expression specified with the `--filterExpression` (short `-F`) option

for example to show the project versions of namespace portions with uncommitted changes, execute the following command
in the root folder of the namespace root project::

        pjm show_children_versions modified

to additionally restrict the last example to projects with uncommitted changes in the
:data:`~aedev.project_manager.__main__.MAIN_BRANCH` run::

        pjm show_children_versions "modified & develop"

.. note:: children-set-expression with set-operators have to be included into high-commas.

more flexible filtering can be done with the command line options `--filterExpression` and `--filterBranch`.
by specifying one of these options the selected/filtered children are then available as a children-set-expression
with the same name as the specified option.

for example to only show the versions of projects with uncommitted changes in the branch ``branch_name`` run::

        pjm --filterBranch=branch_name show_children_versions "modified & filterBranch"

.. hint::
    the name of the branch get specified with the `--filterBranch` option. and the name of the option can then be
    used like a `python set <https://docs.python.org/3/library/stdtypes.html#set>`__ in the children-set-expression
    action argument.

in general, any bulk action can be restricted to only process children/portions projects that have the specified
branch name checked-out. e.g. to only process all children that have checked out the branch ``branch_name`` run::

        pjm --filterBranch=branch_name <any_bulk_action> filterBranch

exactly the same selection result could be achieved via a more complex Python expression, using the
`--filterExpression` option/children-set-expression::

        pjm --filterExpression="_git_current_branch(chi_pdv)=='branch_name'" <any_bulk_action> filterExpression

.. hint::
    the filter expression can contain project environment variables and any globals of the project-manager tool.
    additionally, the variable `chi_pdv` can be used to additionally access the project
    environment variables of the other children/portion projects.

.. note:: filter expressions should be included in high-commas.

the next example is selection all children with a project package version number below or equal to ``1.2.3``::

        pjm --filterExpression "project_version<='1.2.3'" <children_bulk_action> filterExpression

the example underneath is showing the local, remote and PyPI versions of the children projects that have a branch
(checked-out or not) with the name ``branch_name`` in their repository::

        pjm -F "'branch_name' in _git_branches(chi_pdv)" show_children_versions filterExpression

to bulk-release multiple children projects in a :ref:`contribution process <contribution steps>` workflow,
the following bulk actions can be executed, e.g. from within the root folder of a namespace root project:

    * :func:`~aedev.project_manager.__main__.new_children` to increment the versions and refresh managed
      files from templates::

            pjm -b=branch_name new_children modified

    * :func:`~aedev.project_manager.__main__.prepare_children_commit` to prepare the commit message files
      (after you implemented all changes into the above created branch with the name ``branch_name``)::

            pjm prepare_children_commit "commit message for branch_name" modified

    * :func:`~aedev.project_manager.__main__.commit_children` to commit changes to the local git repositories::

            pjm commit_children modified

    * :meth:`~aedev.project_manager.__main__.GitlabCom.push_children` to push the committed changes
      to the remote repositories::

            pjm --filterBranch=branch_name push_children filterBranch

    * :meth:`~aedev.project_manager.__main__.GitlabCom.request_children_merge` to merge pushed changes to the main
      branches on the remote host (without a repository forg add the options: -f -u=group_or_user_name)::

            pjm --filterBranch=branch_name request_children_merge filterBranch

    * :meth:`~aedev.project_manager.__main__.GitlabCom.release_children` to bulk-release the project packages to PyPI::

            pjm --filterBranch=branch_name release_children filterBranch

    * :func:`~aedev.project_manager.__main__.install_children_editable`: updates/updates editable installations
      of your local projects into your virtual environment::

            pjm -F "'branch_name' in _git_branches(chi_pdv)" install_children_editable filterExpression


remote server configuration
---------------------------

``pjm`` supports two types of remote servers. remote servers that are hosting the project repository
(e.g. on ``gitlab.com`` or ``github.com``), and remote servers that are hosting deployable apps or web sites
(e.g. ``pythonanywhere.com``).

``pjm`` actions with write access to any remote host (web/repository server), like e.g.
:meth:`~aedev.project_manager.__main__.PythonanywhereCom.deploy_project` or
:meth:`~aedev.project_manager.__main__.GitlabCom.push_project`, are
requesting the user credentials for the authentication from the remote server configurations.

.. note::
    remote server configurations can be specified in multiple ways.
    configuration options specified to ``pjm`` via command line arguments have the highest priority, followed
    by OS environment variables, :ref:`pjm config variables`, and the :ref:`remote server configuration` files.

OS environment variables are mostly used to store credential secrets like authentication tokens, and can get
declared in various ways. default values for these variables can get specified in ``.env`` files (see
:func:`~ae.base.load_env_var_defaults`). these defaults getting preceded by the OS environment variable values
declared via a startup shell script (like e.g. ``.bashrc``), and these getting overwritten by variable values
set directly in an open console/shell.


command line config options
^^^^^^^^^^^^^^^^^^^^^^^^^^^

the remote server domain address can be specified via command line config-option
`--repo_domain`  for Git repository remotes
and `--web_domain` for web servers.

user names and credentials can be specified via the ``pjm`` command line :ref:`options <config-options>`:
`--repo_token` and `--repo_user` or `--repo_group`, respectively `--web_token` and `--web_user`.


pjm config variables
^^^^^^^^^^^^^^^^^^^^

user credentials not specified by the command line :ref:`config-options` are determined from the
OS environment variables and .env files via a user- and domain-specific lookup
with the help of the :meth:`~ae.shell.get_domain_user_var` function.

to resolve the value of the not specified `--repo_token` command line option, the lookup first checks if there
exists an OS environment variable and if not found then it is looking for an
:ref:`application config variable <config-variables>`.

for example the lookup of the default value of the not specified `--repo_token` command line option,
for an user with the username ``michael`` at the domain ``www.example.com``, is done in the
following order:

    * OS environment variable ``AE_OPTIONS_HOST_TOKEN_AT_WWW_EXAMPLE_COM_MICHAEL``
    * config variable ``host_token_at_www_example_com_michael`` in the config section ``aeOptions``
    * OS environment variable ``AE_OPTIONS_HOST_TOKEN_AT_WWW_EXAMPLE_COM``
    * config variable ``host_token_at_www_example_com`` in the config section ``aeOptions``


project development variables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

this type of configuration variables are compiled by an instance of the :class:`~aedev.project_vars.ProjectDevVars`
provided by the :mod:`aedev.project_vars` module. the variable values can be configured via the
OS environment variables or the ``.env`` files, situated in the root folder of a project working tree (or above).

by providing for example the user name (of your account at your repository host server), you don't need to specify
it any longer on the ``pjm`` command line via the `--repo_user` option. in the most cases you will want to provide
also the repository group name of the repository owner instead of the `--repo_group` option. therefore create a
``.env`` file in the project root with the following content::

    PDV_repo_user = "UserName"
    PDV_repo_group=UserOrGroupName

.. hint::
    the default value of the repository group name, if not specified, gets compiled from the project name followed
    by a hyphen and the word `group`.

in order to change the default domain (``gitlab.com``) of the git repository server/host for
a project to ``github.com``, add also the following two lines have into this dict literal::

    PDV_repo_domain=github.com


git credential storage
^^^^^^^^^^^^^^^^^^^^^^

the git credential storage can be used as the last fallback if your user credentials are neither specified as
:ref:`command line config options` nor via the :ref:`pjm config variables`.

the user credentials for actions on git repository hosts (``gitlab.com``/``github.com``/...) like
:meth:`~aedev.project_manager.__main__.GitlabCom.push_project` can alternatively
be set and stored via the git configuration settings
(see `<https://git-scm.com/book/en/v2/Git-Tools-Credential-Storage>`__
and `<https://stackoverflow.com/questions/46645843>`__).

.. hint::
    see `<https://stackoverflow.com/questions/65163081>`__ to disable user/password prompts for fetch and check actions
    to git repository hoster that don't need authentication (and not using the `token` option), like e.g.
    :func:`~aedev.project_manager.__main__._git_fetch`.


pjm example workflows
=====================

this section describes some typical development workflows managed with the help of the ``pjm`` tool.


create a new project
--------------------

first make sure you have installed the ``pjm`` tool, by running the following command::

    pip install aedev-project-manager

to create a new project (in this example a small console app module with the project name ``con_app``),
first change the current working directory of your used shell (e.g. bash) to your
projects source parent folder (e.g. ``~/src``)::

    cd ~/src
    pjm --project_name=con_app new_module
    cd con_app

the above pjm command will create a new root folder with the name ``con_app`` and within the project structure
based on the templates from the ``aedev`` namespace.

.. hint::
    the pjm action ``new_module`` specifies the type of the project as a single module.
    for a more complex project (including multiple modules) use instead the ``new_package`` action,
    for a namespace root project the ``new_namespace_root`` action,
    for a GUI application the ``new_app`` action,
    and for a django project the ``new_django`` action.

then create, within the new project root folder a ``.env`` file to put your username and credentials, like explained
in the above section :ref:`project development variables`.

.. hint::
    the section :ref:`remote server configuration` describes alternative ways on how you can configure
    default values of your repository server, your user account name and your credentials/tokens.

optionally create and activate a virtual environment for the new project. the following command is
using the tool `pyenv <https://github.com/pyenv/pyenv>`__ to set an existing virtual environment (``py_env``)
as the default for the new project (stored within the ``.python-version`` in the project root folder).

    pyenv local py_env

.. hint::
    using ``pyenv local`` has the advantage to ensure that the project's virtual environment gets activated
    automatically, as soon as you change the current directory of your shell/console to the project root folder.

now you can start completing the unit and integration tests code by editing the prepared file ``tests/test_con_app.py``.
then the project code can be amended in the generated file ``con_app.py``.

to complete the documentation of your new project, amend the prepared files ``README.md``,
``docs/index.rst`` and ``docs/features_and_examples.rst`` accordingly.

.. hint::
    at any time in the implementation process you can run the actions
    :func:`renew <aedev.project_manager.__main__.refresh_project>` and
    :func:`check <aedev.project_manager.__main__.check_integrity>` in order to
    keep the files created from templates up-to-date, and to test your implementation::

        pjm refresh
        pjm check

after finishing the implementation, create the commit message file ``.commit_msg.txt`` in the project root
folder with the :func:`prepare <aedev.project_manager.__main__.prepare_commit>` action::

    pjm prepare

the content of the commit message file can then be amended with additional notes.

to commit the first implementation of your new project into your local git repository, execute the
:func:`commit <aedev.project_manager.__main__.commit_project>` action::

    pjm commit

now the new project can be pushed to your repository host server (``gitlab.com`` by default)
by executing the :meth:`push <aedev.project_manager.__main__.GitlabCom.push_project>`
action::

    pjm push


change request on an existing project
-------------------------------------

a typical workflow to change or add code of an already existing project gets processed with
the following ``pjm`` actions:

    * :meth:`fork <aedev.project_manager.__main__.GitlabCom.fork_project>`
      - create your fork or update an exiting fork (for already forked projects).
    * :func:`renew <aedev.project_manager.__main__.new_project>`
      - update/refresh/renew the files created from templates,
      update/bump your project version and create a new feature branch.
    * :func:`prepare <aedev.project_manager.__main__.prepare_commit>`
      - create a commit message after all planned changes/additions are implemented.
    * :func:`commit <aedev.project_manager.__main__.commit_project>`
      - create a new commit.
    * :meth:`push <aedev.project_manager.__main__.GitlabCom.push_project>`
      - push the commit to the origin repository (your fork).
    * :meth:`request <aedev.project_manager.__main__.GitlabCom.request_merge>`
      - create a merge request (respective a push request at github.com).

as a repository maintainer and to complete the workflow, the release and deployment of a project,
you can initiate the following ``pjm`` actions:

    * :meth:`release <aedev.project_manager.__main__.GitlabCom.release_project>`
      - merge the changes from a merge request into the main branch ({MAIN_BRANCH})
      and create a new project release at PyPI.
    * :meth:`deploy <aedev.project_manager.__main__.PythonanywhereCom.deploy_project>`
      - deployment of the new/changed project (only available for web projects).


setup a new Django CMS server project
-------------------------------------

the following example describes the steps done in the bash shell/console on your computer,
in order to create a new Django project (using Django 4.2 and DjangoCms 4.1), with the project name ``oaio_server``.

.. hint::
    alternative to the previous example we first create the project folder (oaio_server) manually, and prepare the
    virtual environment, before we use the pjm tool to create the initial project files from the ``aedev`` templates.

after changing your current working directory to the projects source parent folder (e.g. <username>/src), execute the
following commands to create the project root folder ``oaio_server``,
and setup a new virtual environment with the name ``dj4``::

    pyenv install 3.12.3                    (released on 9 april 2024)
    pyenv virtualenv 3.12.3 dj4
    mkdir oaio_server
    cd oaio_server
    pyenv local dj4
    pip install --upgrade pip setuptools aedev-project-manager

now, still from within the project root folder and with the new virtual environment activated, you can
install Django and DjangoCms and prepare an initial project structure by executing the following commands.
the ``djangocms`` command will prompt you to enter the name, email address and password of the django admin/superuser::

    pip install Django==4.2.13              (released on 7 may 2024, 4.2.16 on 12 oct 2024)
    pip install django-cms==4.1.1           (released on 1 may 2024, 4.1.3 on 12 oct 2024)
    djangocms oaio_server .

.. note::
    don’t miss the final dot in the ``djangocms`` command.

to adapt your web project declare the values of the :ref:`project development variables`,
by creating a new ``.env`` file with the following content::

    PDV_AUTHOR=YourAuthorName
    PDV_AUTHOR_EMAIL='your-email-address@somewhere.com'
    PDV_repo_user=yourGitRemoteUserName
    PDV_repo_token=your-private-secret-token-on-your-git-repository-server
    PDV_repo_group='repo-host-owner-user-or-group-id'       # e.g. 'ae-group'
    PDV_web_domain='web-app-host-domain'                    # e.g. 'eu.pythonanywhere.com'
    PDV_web_user='web-server-user-name'
    PDV_web_token=your-password-or-token-on-your-web-server

.. hint::
    to prevent the release of your web project onto the PyPI cheese shop, set the value of the
    `PDV_pip_name` variable to an empty string.

now execute the following commands in order to adapt the new project to be managed by ``pjm`` and to use the
template files provided by the projects in the
`aedev namespace <https://gitlab.com/aedev-group/aedev_aedev>`_ ::

    mv requirements.in requirements.txt
    rm LICENSE
    pjm -b new-project-branch-name new_django

now your web project is ready to be implemented. after you wrote your unit tests and the django apps and views,
you prepare your first push by running the following ``pjm`` actions/commands::

    pjm prepare             # prepare the commit message
    pjm commit              # commit to git repository
    pjm push                # push the commit to your Git repository server


additional information to setup Django/CMS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* install Django development version (finally NOT used for this project/venv):
  `<https://docs.djangoproject.com/en/4.2/topics/install/#installing-the-development-version>`__
* install DjangoCms by hand (not using docker):
  `<https://docs.django-cms.org/en/latest/introduction/01-install.html#installing-django-cms-by-hand>`__
* Django/Cms software versions:
  `<https://docs.djangoproject.com/en/4.2/faq/install/#faq-python-version-support>`__ and
  `<https://docs.django-cms.org/en/latest/index.html#software-version-requirements-and-release-notes>`__


more pjm example workflows
--------------------------

``pjm`` workflow examples for ``aedev`` namespace portion projects can be found in the
`contribution documentation of a project
<https://aedev.readthedocs.io/en/latest/index.html#using-the-project-manager-pjm>`__,
and for web projects in the `programmer manual
<https://kairos.readthedocs.io/en/latest/programmer_manual.html#using-the-project-manager-pjm>`__
of the ``kairos`` web project.
