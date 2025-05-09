# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class FluxSecurity(AutotoolsPackage):
    """Independent project for Flux security code and APIs."""

    homepage = "https://github.com/flux-framework/flux-security"
    url = "https://github.com/flux-framework/flux-security/releases/download/v0.8.0/flux-security-0.8.0.tar.gz"
    git = "https://github.com/flux-framework/flux-security.git"
    tags = ["radiuss", "e4s"]

    maintainers("grondo")

    license("LGPL-3.0-or-later")

    version("master", branch="master")
    version("0.14.0", sha256="fae93bdaf94110a614d2806dfddf8b70bb43f73d89a7cb6856f26ab9055afc70")
    version("0.13.0", sha256="d61b8d0e6d6c8d7497e9542eadc110c496cbd57ba6a33bfd26271d805bda9869")
    version("0.12.0", sha256="2876d1f10c4f898f2ff10d60ddb446af9c8a913dda69f0136d820ad1fdf28a93")
    version("0.11.0", sha256="d1ef78a871155a252f07e4f0a636eb272d6c2048d5e0e943860dd687c6cf808a")
    version("0.10.0", sha256="b0f39c5e32322f901454469ffd6154019b6dffafc064b55b3e593f70db6a6f68")
    version("0.9.0", sha256="2258120c6f32ca0b5b13b166bae56d9bd82a44c6eeaa6bc6187e4a4419bdbcc0")
    version("0.8.0", sha256="9963628063b4abdff6bece03208444c8f23fbfda33c20544c48b21e9f4819ce2")

    depends_on("c", type="build")  # generated

    # Need autotools when building on master:
    depends_on("autoconf", type="build", when="@master")
    depends_on("automake", type="build", when="@master")
    depends_on("libtool", type="build", when="@master")

    depends_on("pkgconfig")
    depends_on("libsodium@1.0.14:")
    depends_on("jansson")
    depends_on("uuid")
    depends_on("munge")
    depends_on("libpam")

    def setup(self):
        pass

    @when("@master")
    def setup(self):
        with working_dir(self.stage.source_path):
            # Allow git-describe to get last tag so flux-version works:
            git = which("git")
            # When using spack develop, this will already be unshallow
            try:
                git("fetch", "--unshallow")
                git("config", "remote.origin.fetch", "+refs/heads/*:refs/remotes/origin/*")
                git("fetch", "origin")
            except ProcessError:
                git("fetch")

    def autoreconf(self, spec, prefix):
        self.setup()
        if os.path.exists(self.configure_abs_path):
            return
        # make sure configure doesn't get confused by the staging symlink
        with working_dir(self.configure_directory):
            # Bootstrap with autotools
            bash = which("bash")
            bash("./autogen.sh")
