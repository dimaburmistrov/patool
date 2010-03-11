# -*- coding: utf-8 -*-
# Copyright (C) 2010 Bastian Kleineidam
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""Archive commands for the rpm2cpio program."""
import os
from patoolib import util

def extract_rpm (archive, encoding, cmd, **kwargs):
    """Extract a DEB archive."""
    # also check cpio
    cpio = util.find_program("cpio")
    if not cpio:
        raise util.PatoolError("cpio(1) is required for rpm2cpio extraction; please install it")
    cmdlist = [cmd, os.path.abspath(archive), "|", cpio, '--extract',
        '--make-directories', '--preserve-modification-time',
        '--no-absolute-filenames', '--force-local', '--nonmatching',
        '"*\.\.*"']
    if kwargs['verbose']:
        cmdlist.append('-v')
    cmd = " ".join([util.shell_quote(x) for x in cmdlist])
    return (cmd, {'cwd': kwargs['outdir'], 'shell': True})
