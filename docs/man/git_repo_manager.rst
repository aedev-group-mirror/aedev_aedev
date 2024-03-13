git repository manager user manual
**********************************

installation of grm
===================

to installing this tool open a console window and run the following command::

    pip install aedev_git_repo_manager

after the installation the ``grm`` command will be available in your OS console.


usage of grm
============

``grm`` is supporting you on all devops (development operations) of your python library, application and web projects.

this covers all actions done on your local machine, on your repository host servers (like gitlab.com or github.com)
and on your web and applikcation deployment servers, like:

    * creating new projects
    * maintaining and upgrading existing projects
    * running integrity checks and unit tests
    * maintaining, syncing and pushing of your git repositories
    * creating and maintaining merge requests on your git repository servers
    * release of your project onto the cheese shop (PyPI.com)
    * deployment of your app/web project


command line options and action arguments
-----------------------------------------

the git repository manager command line consist of options, action keywords and action arguments::

    grm [options] [action-keywords] [action-arguments]

all command line options are available in a long form, preceded with two leading hyphen characters, and in a short form,
preceded with a single hyphen character.

executing ``grm`` with the `--help` command line option (short `-h`) displays a short summary of the available
command line options::

    grm --help

general command line options like e.g. `--verbose` (`-v`), `--debug_level` (`-D`), `--path` (`-p`) or `--project` (`-P`)
can be specified for any action. other options, like e.g. the filter options `--filterBranch` (`-B`) and
`--filterExpression` (`-F`), are only supported for bulk actions.


execute ``grm`` with the `show_actions` action to display a brief summary of all the available/registered actions
for a project::

    grm show_actions

for a more verbose output, including the expected action-arguments, the supported project types and the action shortcut,
add the `--verbose` and/or :ref:`--debug_level <pre-defined-config-options>` command line options::

    grm --verbose --debug_level=2 show_actions

the equivalent command line using the short option form and the shortcut of `show_actions` looks like::

    grm -v -D 2 actions

the action keywords argument is composed of several words, seperated by either a space character, a hyphen character
or an underscore character. some actions can even be abbreviated by a single word shortcut. e.g. the following four
commandos are equivalent::

    grm check integrity
    grm check-integrity
    grm check_integrity
    grm check

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

several actions are determining the project(s) status, like e.g. `show_status`, `show_children_status`,
`show_repo`, `show_children_repo`,
`check_integrity`, `check_children_integrity`, `show_versions`, `show_children_versions`, and `search_repos`.


project and repository maintenance actions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

useful actions to create, extend or renew a project repository respectively multiple project repositories, are e.g.
`new_app`, `new_children`, `new_django`, `new_module`, `new_package`, `new_project`, `bump_version`,
`refresh_outsourced`, `refresh_children_outsourced`.

actions for your other repository maintenance workflows are e.g.
`clone_project`, `clone_children_project`, `fork_project`, `fork_children`,
`prepare_commit`, `prepare_children_commit`, `commit_project`, `commit_children`,
`push_project`, `push_children`, `request_merge`, `request_children_merge`, `release_project`, `release_children`,
`install_editable`, and `install_children_editable`.

to manipulate single files in project repositories use the actions
`add_file`, `add_children_file`, `delete_file`, `delete_children_file`, `rename_file`, `rename_children_file`.

in order to synchronize the local :data:`~aedev.git_repo_manager.__main__.MAIN_BRANCH` branch with any changes
done to same branch on the 'origin' remote, execute ``grm`` with the `update_project` and `update_children` actions.

the `clean_releases` action deletes local+remote release tags and branches of the specified project that
got not published to PYPI.

the execution of bulk command lines for a group of projects can be done with the `run_children_command` action.


web and app deployment server actions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

the actions `check_deploy` and `deploy_project` are working directly with the deployment servers of your web or app
project.

`check_deploy` is comparing the deployed files against any repository version tag or against the package files in your
project work tree.

the `deploy_project` action is deploying any new or changed package files to your deployment web or app server.


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

    grm show_children_versions modified

to additionally restrict the last example to projects with uncommitted changes in the
:data:`~aedev.git_repo_manager.__main__.MAIN_BRANCH` run::

    grm show_children_versions "modified & develop"

.. note:: children-set-expression with set-operators have to be included into high-commas.

more flexible filtering can be done with the command line options `--filterExpression` and `--filterBranch`.
by specifying one of these options the selected/filtered children are then available as a children-set-expression
with the same name as the specified option.

for example to only show the versions of projects with uncommitted changes in the branch ``branch_name`` run::

    grm --filterBranch=branch_name show_children_versions "modified & filterBranch"

.. note::
    the name of the branch get specified with the `--filterBranch` option. and the name of the option can then be
    used like a `python set <https://docs.python.org/3/library/stdtypes.html#set>`__ in the children-set-expression
    action argument.

in general, any bulk action can be restricted to only process children/portions projects that have the specified
branch name checked-out. e.g. to only process all children that have checked out the branch ``branch_name`` run::

    grm --filterBranch=branch_name <any_bulk_action> filterBranch

exactly the same selection result could be achieved via a more complex Python expression, using the
`--filterExpression` option/children-set-expression::

    grm --filterExpression="_git_current_branch(chi_pdv)=='branch_name'" <any_bulk_action> filterExpression

.. hint::
    the filter expression can contain project environment variables and any globals of the git-repo-manager tool.
    additionally, the variable `chi_pdv` can be used to additionally access the project
    environment variables of the other children/portion projects.

.. note:: filter expressions should be included in high-commas.

the next example is selection all children with a project package version number below or equal to ``0.2``::

    grm --filterExpression "project_version<='0.2'" <children_bulk_action> filterExpression

the example underneath is showing the local, remote and PyPI versions of the children projects that have a branch
(checked-out or not) with the name ``branch_name`` in their repository::

    grm -F "'branch_name' in _git_branches(chi_pdv)" show_children_versions filterExpression

to bulk-release multiple children projects in a :ref:`contribution process <contribution steps>` workflow,
the following bulk actions are executed, e.g. from within the root folder of a namespace root project:

    * `new_children` to increment the versions and refresh outsourced files from templates::

        grm -b=branch_name new_children modified

    * `prepare_children_commit` to prepare the commit message files (after you implemented
      all changes into the above created branch with the name ``branch_name``)::

        grm prepare_children_commit "commit message for branch_name" modified

    * `commit_children` to commit changes to the local git repositories::

        grm commit_children modified

    * `push_children` to push the committed changes to the remote repositories::

        grm --filterBranch=branch_name push_children filterBranch

    * `request_children_merge` to merge pushed changes to the main branches on the remote host
      (without a repository forg add the options: -f -u=group_or_user_name)::

        grm --filterBranch=branch_name request_children_merge filterBranch

    * `release_children` to bulk-release the project packages to PyPI::

        grm --filterBranch=branch_name release_children filterBranch

    * `install_children_editable`: updates/updates editable installations of your local projects into
      your virtual environment::

        grm -F "'branch_name' in _git_branches(chi_pdv)" install_children_editable filterExpression


remote server authentication
----------------------------

actions with write access to any remote host (web/repository server), like e.g. `deploy_project` or `push_project`, are
requesting the user credentials for the authentication.


config options
^^^^^^^^^^^^^^

user credentials can be specified via the ``grm`` command line :ref:`config-options`: `token` and `user` or `group`.


config variables
^^^^^^^^^^^^^^^^

user credentials not specified by the command line :ref:`config-options` are determined from the
:ref:`application config variable <config-variables>` via a user- and domain-specific lookup
with the help of the :meth:`~ConsoleApp.get_variable` method.

for example to resolve the value of the not specified `token` command line option, the lookup first checks if there
exists an OS environment variable (also via the `python-dotenv <https://pypi.org/project/python-dotenv/>`__ package),
and if not found then it is looking for an :ref:`application config variable <config-variables>`.

in detail the lookup of a variable holding the `token` value of an user with the name ``michael``
at the domain ``www.example.com`` is done in the following order:

    * OS environment variable `AE_OPTIONS_HOST_TOKEN_AT_WWW_EXAMPLE_COM_MICHAEL`
    * config variable `host_token_at_www_example_com_michael` in the config section `aeOptions`
    * OS environment variable `AE_OPTIONS_HOST_TOKEN_AT_WWW_EXAMPLE_COM`
    * config variable `host_token_at_www_example_com` in the config section `aeOptions`


git credential storage
^^^^^^^^^^^^^^^^^^^^^^

the user credentials for actions on git repository hosts (gitlab/github/...) like `push_project` can alternatively
be set and stored via the git configuration settings
(see `https://git-scm.com/book/en/v2/Git-Tools-Credential-Storage`__
and `https://stackoverflow.com/questions/46645843`__).

.. hint::
    see `https://stackoverflow.com/questions/65163081`__ to disable user/password prompts for fetch and check actions
    to git repository hoster that don't need authentication (and not using `token`), like e.g.
    :func:`~aedev.git_repo_manager.__main__._git_fetch`.


typical development workflow
----------------------------

a typical workflow to create or change a project gets processed with the following ``grm`` actions:

    * `fork` - create or update your fork (only for already existing porjects).
    * `renew` - create a new project or prepare existing project to be changed.
    * `prepare` - create a commit message.
    * `commit` - create a new commit.
    * `push` - push the commit to the origin repository (your fork).
    * `request` - create a merge request.

to complete the workflow, the release and deployment of a project has to be done by an repository maintainer with
the following ``grm`` actions:
    * `deploy` - deployment of the new/changed project (only available for web and app projects).
    * `release` - merge the changes into the main branch ({MAIN_BRANCH}) and create a new project release at PyPI.


more detailed workflow examples can be found in the `contribution documentation of a project
<https://aedev.readthedocs.io/en/latest/index.html#using-the-git-repository-manager-grm>`__, and for web projects
in the `programmer manual
<https://kairos.readthedocs.io/en/latest/programmer_manual.html#update-from-version-vx-x-xx-to-vx-x-yy-on-pythonanywhere
>`__ of the kairos web project.
