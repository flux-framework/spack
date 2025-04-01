# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Pdsh(AutotoolsPackage):
    """
    PDSH: a high performance, parallel remote shell utility
    """

    homepage = "https://github.com/grondo/pdsh"
    url = "https://github.com/grondo/pdsh/archive/pdsh-2.31.tar.gz"

    license("GPL-2.0")

    version("2.31", sha256="0ee066ce395703285cf4f6cf00b54b7097d12457a4b1c146bc6f33d8ba73caa7")

    variant("ssh", default=True, description="Build with ssh module")

    variant("static_modules", default=True, description="Build with static modules")

    depends_on("c", type="build")  # generated

    def configure_args(self):
        args = []
        if "+ssh" in self.spec:
            args.append("--with-ssh")
        if "+static_modules" in self.spec:
            args.append("--enable-static-modules")
        return args
