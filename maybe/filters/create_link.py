# maybe - see what a program does before deciding whether you really want it to happen
#
# Copyright (c) 2016 Philipp Emanuel Weidmann <pew@worldwidemann.com>
#
# Nemo vir est qui mundum non reddat meliorem.
#
# Released under the terms of the GNU General Public License, version 3
# (https://gnu.org/licenses/gpl.html)


from os.path import abspath

from maybe import SyscallFilter, SYSCALL_FILTERS, T


def format_create_link(path_source, path_target, symbolic):
    label = "create symbolic link" if symbolic else "create hard link"
    return "%s from %s to %s" % (T.cyan(label), T.underline(abspath(path_source)), T.underline(abspath(path_target)))


SYSCALL_FILTERS["create_link"] = [
    SyscallFilter(
        name="link",
        format=lambda args: format_create_link(args[1], args[0], False),
    ),
    SyscallFilter(
        name="linkat",
        format=lambda args: format_create_link(args[3], args[1], False),
    ),
    SyscallFilter(
        name="symlink",
        format=lambda args: format_create_link(args[1], args[0], True),
    ),
    SyscallFilter(
        name="symlinkat",
        format=lambda args: format_create_link(args[2], args[0], True),
    ),
]
