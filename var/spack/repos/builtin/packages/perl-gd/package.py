##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class PerlGd(PerlPackage):
    """Interface to Gd Graphics Library"""

    homepage = "http://search.cpan.org/~lds/GD-2.53/GD.pm"
    url      = "http://search.cpan.org/CPAN/authors/id/L/LD/LDS/GD-2.53.tar.gz"

    version('2.53', 'd2c9b18123bcaff8672eb50f2eb37ed3')

    depends_on('perl-module-build', type='build')
    depends_on('perl-extutils-makemaker', type=('build', 'run'))
    depends_on('perl-extutils-pkgconfig', type=('build', 'run'))
    depends_on('libgd')
