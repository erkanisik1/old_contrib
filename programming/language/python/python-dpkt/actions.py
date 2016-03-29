#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules


def install():
    pythonmodules.install()

    pisitools.dodoc("AUTHORS", "CHANGES","LICENSE", "README*")
    pisitools.insinto("/usr/share/doc/python-dpkt/","docs/")
