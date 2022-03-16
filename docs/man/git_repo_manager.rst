git repository manager user manual
**********************************

installation of grm
===================

to installing this tool open a console window and run the following command::

    pip install aedev_git_repo_manager

after the installation the ``grm`` command will be available in your OS console.


usage of grm
============

remote server authentication
----------------------------

actions with write access to the remote repository server, like e.g. `push-project`, are requesting authentication via
the :ref:`config-options` `gitToken` and `gitUser`.

.. hint::
   see https://stackoverflow.com/questions/65163081 to disable user/password prompts for fetch and check actions
   that don't need authentication (and not using `gitToken`), like e.g. :func:`~aedev.git_repo_manager._git_fetch`.
   alternatively
   a function _get_repo_url() could be implemented to replace all usages of pdv_str(..., 'repo_url') and 'origin'.


command line options and action arguments
-----------------------------------------

check the available command line arguments and options by specifying the `--help` command line option::

    grm --help

additional information provided by `grm` on the available/registered actions of a local project are printed to the
console by specifying the `show-actions` action::

    grm show-actions

to get a more verbose output add the `--verbose` and/or :ref:`--debug_level <pre-defined-config-options>` command line
options::

    grm --verbose --debug_level=2 show-actions

an identical abbreviated execution using the short command line options and the shortcut of `show-actions` looks like::

    grm -v -D 2 actions


repository status
^^^^^^^^^^^^^^^^^

several actions are determining the status of a project, like e.g. `show-status`, `show-repo`, `check-integrity` and
`show-versions`.

in order to synchronize the local :data:`~aedev.git_repo_manager.MAIN_BRANCH` branch with any changes done to same
branch on the 'origin' remote, execute `grm` with the `update-project` action.


file patching helper functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

this portion is also providing some helper functions to patch code and documentation files.

the function :func:`~aedev.git_repo_manager.bump_file_version` increments any part of a version number of a module,
portion, app or package.

templates are patched with the functions :func:`~aedev.git_repo_manager.patch_string` and
:func:`~aedev.git_repo_manager.refresh_templates`.

in conjunction with the template projects of the `aedev` namespace (like e.g. :mod:`aedev.tpl_project`) any common
portions file (even the ``setup.py`` file) can be created/maintained as a template in a single place, and then requested
and updated individually for each portion project.

.. hint::
    children bulk actions on portions of a namespace can be processed by `grm` via their namespace root project, e.g.
    `the ae namespace root project <https://gitlab.com/ae-group/ae_ae>`_ or the
    `the aedev namespace root project <https://gitlab.com/aedev-group/aedev_aedev>`_.


available command line options
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

general command line options like e.g. `path` and `package` can be specified for any action.

other options like e.g. the filter options `filterBranch` and `filterExpression` are only recognized by children bulk
actions.


filtering children of projects parent or namespace root
"""""""""""""""""""""""""""""""""""""""""""""""""""""""

bulk actions, like e.g. `show-children-versions`, are processing by default all its children, which are either all
projects under a projects parent folder or all the portions of a namespace. the command line options
`filterExpression` and `filterBranch` allow to filter or select specific children. the selected/filtered children are
then available as a children-set-expression with the same name as the specified option.

specify the name of a branch with the `filterBranch` option to only process children projects that have the specified
branch name checked-out. e.g. to only process all children that have checked out the branch ``my_branch`` run::

    grm --filterBranch=my_branch <children-bulk-action> filterBranch

exactly the same selection result could be achieved via a more complex Python expression, using the `filterExpression`
option/children-set-expression::

    grm --filterExpression="_git_current_branch(chi_pdv)=='my_branch'" <children-bulk-action> filterExpression

.. hint::
    the filter expression should be included in high-commas and can contain any globals of the git-repo-manager project.
    also all project environment variables of the children project can be used in such expression. additionally the
    variable `chi_pdv` can be used to directly access the project environment variable.

the next example is selection all children with the same version number, by using the project environment variable
`package_version`::

    grm --filterExpression "package_version=='1.2.3'" <children-bulk-action> filterExpression

the example underneath is showing the local, remote and PyPI versions of the children projects that have a branch
(checked-out or not) with the name ``my_branch`` in their repository::

  grm -F "'my_branch' in _git_branches(chi_pdv)" show-children-versions filterExpression

