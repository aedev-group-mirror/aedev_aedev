git repository manager user manual
**********************************

installation of grm
===================

to installing this tool open a console window and run the following command::

    pip install aedev_git_repo_manager

after the installation the ``grm`` command will be available in your OS console.


usage of grm
============

the git repository manager on the command line can consist of options, an action keyword and action
arguments::

    grm [options] [action-keyword] [action-arguments]

most of the ``grm`` actions operate on a single project or repository. some of them are also available as
bulk actions, which are affecting multiple projects, e.g. the portions of a namespace or the projects
located under the same parent directory.

bulk actions on portions of a namespace are processed by executing them in the namespace root project root folder.
bulk actions on projects underneath a parent directory are executed in the parent folder.
alternatively they can be executed from any other folder by specifying the namespace root project
or the projects parent folder via the `package` or `path` options.
for example, bulk actions on namespace root project, like e.g.
`the ae namespace root project <https://gitlab.com/ae-group/ae_ae>`_ via ``--package ae_ae`` or the
`the aedev namespace root project <https://gitlab.com/aedev-group/aedev_aedev>`_ via ``--path path/to/aedev_aedev``.

.. hint:: bulk actions are recognizable by the additional ``children`` keyword in their action name.


command line options and action arguments
-----------------------------------------

check the available command line arguments and options by specifying the `--help` (short `-h`) command line option::

    grm --help

additional information provided by `grm` on the available/registered actions of a local project are printed to the
console by specifying the `show-actions` action::

    grm show-actions

to get a more verbose output add the `--verbose` and/or :ref:`--debug_level <pre-defined-config-options>` command line
options::

    grm --verbose --debug_level=2 show-actions

an identical abbreviated execution using the short command line options and the shortcut of `show-actions` looks like::

    grm -v -D 2 actions

general command line options like e.g. `verbose`, `debug_level`, `path` or `package` can be specified for any action.
other options. other options like e.g. the filter options `filterBranch` and `filterExpression` are only recognized
by bulk actions.


repository status actions
^^^^^^^^^^^^^^^^^^^^^^^^^

several actions are determining the status of a project, like e.g. `show-status`, `show-children-status`,
`show-repo`, `show-children-repo`,
`check-integrity`, `check-children-integrity`, `show-versions` and `show-children-versions`.


project and repository maintenance actions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

typical actions for repository maintenance workflow are e.g.
`clone-project`, `clone-children-project`, `fork-project`, `fork-children`,
`prepare-commit`, `prepare-children-commit`, `commit-project`, `commit-children-project`,
`push-project`, `push-children`, `request-merge`, `request-children-merge`, `release-project`, `release-children`,
`install-editable`, `install-children-editable`, and `search-repos`.

several actions allow you to create, extend or renew a project repository, like e.g. `new_app`, `new_children`,
`new_django`, `new_module`, `new_package`, `new_project`, `bump-version`,
`refresh-outsourced`, `refresh-children-outsourced`.

to manipulate single files in project repositories use the actions
`add-file`, `add-children-file`, `delete-file`, `delete-children-file`, `rename-file`, `rename-children-file`.

in order to synchronize the local :data:`~aedev.git_repo_manager.MAIN_BRANCH` branch with any changes done to same
branch on the 'origin' remote, execute `grm` with the `update-project` and `update-children` actions.

the `clean-releases` action deletes local+remote release tags and branches of the specified project that
got not published to PYPI.

the execution of bulk command lines for a group of projects can be done with the `run-children-command` action.


filtering children of projects parent or portions of a namespace
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

which children will get processed in a bulk actions get specified by a children-set-expression
action argument, which can combine one or more of the following placeholders via the
set operators of python (`|` for union, `&` for intersection, `-` for difference and `^` for symmetric difference):

    * `all`: all children projects
    * `editable`: projects installed as editable
    * `modified`: projects having uncommitted changes
    * `develop`: projects having checked-out the :data:`~aedev.git_repo_manager.MAIN_BRANCH`
    * `filterBranch`: projects having checked-out the branch specified with the `filterBranch` (short `-B`) option
    * `filterExpression`: projects matching the expression specified with the `filterExpression` (short `-F`) option

for example to show the project versions via the `show-children-versions` action of only the ae namespace portions
with uncommitted changes::

    grm -p ../ae_ae show-children-versions modified

to additionally restrict the last example to projects with uncommitted changes in the
:data:`~aedev.git_repo_manager.MAIN_BRANCH` run::

    grm -p ../ae_ae show-children-versions "modified & develop"

.. note:: children-set-expression with set-operators have to be included into high-commas.

more flexible filtering can be done with the command line options `filterExpression` and `filterBranch`.
by specifying one of these options the selected/filtered children are then available as a children-set-expression
with the same name as the specified option.

for example to only show the versions of projects with uncommitted changes in the branch ``my_branch`` run::

    grm --filterBranch=my_branch show-children-versions "modified & filterBranch"

.. note::
    the name of the branch get specified with the `filterBranch` option. and the name of the option can then be
    used like a `python set <https://docs.python.org/3/library/stdtypes.html#set>`__ in the children-set-expression
    action argument.

in general, any bulk action can be restricted to only process children/portions projects that have the specified
branch name checked-out. e.g. to only process all children that have checked out the branch ``my_branch`` run::

    grm --filterBranch=my_branch <any-bulk-action> filterBranch

exactly the same selection result could be achieved via a more complex Python expression, using the
`filterExpression` option/children-set-expression::

    grm --filterExpression="_git_current_branch(chi_pdv)=='my_branch'" <any-bulk-action> filterExpression

.. hint::
    the filter expression can contain project environment variables and any globals of the git-repo-manager tool.
    additionally, the variable `chi_pdv` can be used to additionally access the project
    environment variables of the other children/portion projects.

.. note:: filter expressions should be included in high-commas.

the next example is selection all children with a package version number below or equal to ``0.2``::

    grm --filterExpression "package_version<='0.2'" <children-bulk-action> filterExpression

the example underneath is showing the local, remote and PyPI versions of the children projects that have a branch
(checked-out or not) with the name ``my_branch`` in their repository::

  grm -F "'my_branch' in _git_branches(chi_pdv)" show-children-versions filterExpression


remote server authentication
----------------------------

actions with write access to the remote repository server, like e.g. `push-project`, are requesting authentication via
the :ref:`config-options` `gitToken` and `gitUser`.

.. hint::
   see https://stackoverflow.com/questions/65163081 to disable user/password prompts for fetch and check actions
   that don't need authentication (and not using `gitToken`), like e.g. :func:`~aedev.git_repo_manager._git_fetch`.
   alternatively
   a function _get_repo_url() could be implemented to replace all usages of pdv_str(..., 'repo_url') and 'origin'.
