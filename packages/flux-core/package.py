# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class FluxCore(AutotoolsPackage):
    """A next-generation resource manager (pre-alpha)"""

    homepage = "https://github.com/flux-framework/flux-core"
    url = "https://github.com/flux-framework/flux-core/releases/download/v0.8.0/flux-core-0.8.0.tar.gz"
    git = "https://github.com/flux-framework/flux-core.git"
    tags = ["radiuss", "e4s"]

    maintainers("grondo")

    license("LGPL-3.0-only")

    version("master", branch="master")
    version("0.73.0", sha256="d029c3da68bd0a0bea40d964de772e90a55eec72303b610396882f9e94d8c0c6")
    version("0.72.0", sha256="1642d9f93cca6e0e934b534609787a31753462215ab376d190cdced16c386524")
    version("0.71.0", sha256="023fd3e2153e20ba28cdf60fefa14d60053df61de3b9e273bf6f9a9ebdef0b52")
    version("0.70.0", sha256="f68fbc2038d7c0d54c71260b4a8253a73cf6abc09a663ab060a00a4181a9fa94")
    version("0.69.0", sha256="c44fe9c41e54c2a7dcde24c660c07c8b422072540add0447cbba867719e167b5")
    version("0.68.0", sha256="fd3d0b0b13136f3914733c7f9e775372a8808d3c7c724ba076fda277a5abeae3")
    version("0.67.0", sha256="9406e776cbeff971881143fd1b94c42ec912e5b226401d2d3d91d766dd81de8c")
    version("0.66.0", sha256="0a25cfb1ebc033c249614eb2350c6fb57b00cdf3c584d0759c787f595c360daa")
    version("0.65.0", sha256="a60bc7ed13b8e6d09e99176123a474aad2d9792fff6eb6fd4da2a00e1d2865ab")
    version("0.64.0", sha256="0334d6191915f1b89b70cdbf14f24200f8899da31090df5f502020533b304bb3")
    version("0.63.0", sha256="f0fd339f0e24cb26331ad55062d3c1e1c7c81df41c0d7f8727aa0700c7baa1ae")
    version("0.62.0", sha256="54a227741901ca758236c024296b8cd53718eea0050fc6363d2b2979aa0bf1e9")
    version("0.61.2", sha256="06f38143723e3f8331f55893ad8f74d43eb0588078f91abb603690c3e5f5112c")
    version("0.61.1", sha256="59cc730b34b732a1d00355bb5589bf2d26bf522b4a31ebfabff70ddb3afb51d6")
    version("0.61.0", sha256="02cedc6abb12816cbb01f2195c1acf7b6552c1d8b9029f899148df48a7cd05e2")
    version("0.60.0", sha256="f96025204a20f94c2821db47fe010b2c19e076ef93281ac7d308e82853e135ff")
    version("0.59.0", sha256="465d24294b92962d156ad49768ea804ff848d5c0b3470d80e07ebf24cd255f2d")
    version("0.58.0", sha256="3125ace7d4d3c99b362290344f97db74c06c37b5510cfcb746e1bf48e1dc1389")
    version("0.57.0", sha256="a412b8370b5236605a5261c892f48d65c1357a83c88446cd1723236f58a807ce")
    version("0.56.0", sha256="dfce5aa21bcb1f990397343cdff8a60542b2d18cbd929e46bdb444d21a961efb")
    version("0.55.0", sha256="2925b8a084e9d1069a96de7689b515ad6f2051ecfb9fbbe4d2643507de7ccd30")
    version("0.54.0", sha256="721fc3fff64b3b167ae55d0e29379ff3211729248ef97e3b9855816219063b42")
    version("0.53.0", sha256="2f14d032a2d54f34e066c8a15c79917089e9f7f8558baa03dbfe63dbf56918b7")
    version("0.52.0", sha256="dca434238405e4cae4686c8143f2cc79919bfd9e26b09c980e1e5f69ffd0c448")
    version("0.51.0", sha256="e57b71b708482f20d2a2195a000c0c3b9176faa6aaadfad4d2117f8671ca67ce")
    version("0.50.0", sha256="77414299a7ca081199aa0f57bcaea3e05860e2095df73c0f6b7672b88fadf683")
    version("0.49.0", sha256="9b8d7af1d8aaa7ee110bcb9815b6b8647af686de949097c9bb2a0269d5551051")
    version("0.48.0", sha256="32c1bfdde44123e90606422807d381406874bb6dbec170ddb493f905208cc275")
    version("0.47.0", sha256="c13c8df3dd3db565ff7a3db727f087b7c1a3946b98c4b945ac43fe44a4c534c3")
    version("0.46.1", sha256="a7873fd49889c11f12e62d59eb992d4a089ddfde8566789f79eca1dfae1a5ffa")
    version("0.45.0", sha256="6550fe682c1686745e1d9c201daf18f9c57691468124565c9252d27823d2fe46")
    version("0.44.0", sha256="6786b258657675ed573907a2a6012f68f2dd5053d7d09eb76b4e7f9943d6d466")
    version("0.43.0", sha256="4b9816d04e8b5b248a8d5e3dac3f9822f8f89831e340f36745e01512d768597b")
    version("0.42.0", sha256="ac64055976cd7cda26e2991174b9a58048bd4fb75c5c2012023050d76c718445")
    version("0.41.0", sha256="3f3a6a8a1e7d2f326b0e684dcf70e4489076b3f52dd14480e2f33cfdaeba690a")
    version("0.40.0", sha256="b15996b6165f037e5a6c42ea277e2c1c56a4f4b6bf47334105e324dcfefbf6fa")
    version("0.39.0", sha256="ad55529fc3f056ac167b53b5bd489167c2ef218c3c49e721ad507a8ea9c409db")
    version("0.38.0", sha256="69d150c3d48b5985bca606e1a4de12282eb76233b6b730de1a9fff4136faf65f")
    version("0.37.0", sha256="4779f739da573c02df32a834179cc0c157688f6e82bb4cd2049eb0aa59fffffc")
    version("0.36.0", sha256="04def00d8679a30f51c030791b69a536176725b19dc13e7bfc0df58d0041e975")
    version("0.35.0", sha256="28094c77d0a0d34f8fd71c9b397ae25dd7a4b138aad83f02e75c5a182c76b32b")
    version("0.34.0", sha256="e045b0a4f38d1a08280c2acc7f6e03a06e3715282ff84d9a0d1037b86e0aae33")
    version("0.33.0", sha256="b6f07fb6c0fc36bf300852d71df527778c46517bf61e26c7f54c6978898df2f1")
    version("0.32.0", sha256="fabe4450ce805db547de2675afebc077e4f833d86e00a8c0dd4cd0727b374e30")
    version("0.31.0", sha256="a18251de2ca3522484cacfa986df934ba8f98c54586e18940ce5d2c6147a8a7f")
    version("0.30.0", sha256="e51fde4464140367ae4bc1b44f960675ea0a6f58eede3a561cacd8a11ca3e776")
    version("0.29.0", sha256="c13b40e82d66356e75208a689a495ca01f0a013e2e45ac8ea202ed8224987323")
    version("0.28.0", sha256="9a784def7186b0036091bd8d6d8fe5bc3425ab2927e1465e1c9ad266631c285d")

    # Avoid the infinite symlink issue
    # This workaround is documented in PR #3543
    build_directory = "spack-build"

    variant("docs", default=False, description="Build flux manpages and docs")
    variant("cuda", default=False, description="Build dependencies with support for CUDA")
    variant("security", default=False, description="Build with flux-security")

    # Restrict flux to Linux based platforms where builds are possible.
    conflicts("platform=darwin", msg="flux-core does not support MacOS based platforms.")
    conflicts("platform=windows", msg="flux-core does not support Windows based platforms.")

    depends_on("c", type="build")  # generated

    depends_on("libarchive+iconv", when="@0.38.0:")
    depends_on("ncurses@6.2:", when="@0.32.0:")
    depends_on("libzmq@4.0.4:")
    depends_on("czmq@3.0.1:", when="@:0.54.0")
    depends_on("hwloc@1.11.1:")
    depends_on("hwloc +cuda", when="+cuda")
    # Provide version hints for lua so that the concretizer succeeds when no
    # explicit flux-core version is given. See issue #10000 for details
    depends_on("lua", type=("build", "run", "link"))
    depends_on("lua@5.1:5.3")
    depends_on("lua-luaposix")
    # `link` dependency on python due to Flux's `pymod` module
    depends_on("python@3.6:", type=("build", "link", "run"))
    # Use of distutils in configure script dropped in v0.55
    # Detection of cffi version fixed in v0.68
    depends_on("python@:3.11", when="@:0.67", type=("build", "link", "run"))
    depends_on("py-cffi@1.1:", type=("build", "link", "run"))
    depends_on("py-pyyaml@3.10:", type=("build", "run"))
    depends_on("py-jsonschema@2.3:", type=("build", "run"), when="@:0.58.0")
    depends_on("py-ply", type=("build", "run"), when="@0.46.1:")
    depends_on("py-setuptools", type="build", when="@0.67.0:")
    # distutils was dropped in Python 3.12, this fallback was added 9/19/2023
    # for version 0.54.0 but we don't need it until setuptools is dropped
    depends_on("py-packaging", type=("build", "run"))
    depends_on("jansson@2.10:")
    depends_on("pkgconfig")
    depends_on("lz4")
    depends_on("sqlite")
    # Before this version, czmq brings it in
    depends_on("uuid", when="@0.55.0:")
    depends_on("asciidoc", type="build", when="+docs")
    depends_on("py-docutils", type="build", when="@0.32.0: +docs")

    # Flux security variant
    # Note that if you install with this variant, it is
    # recommended to create a view and then a broker.toml that
    # has the path to flux-imp generated by flux-security
    depends_on("flux-security", when="+security")

    # Need autotools when building on master:
    depends_on("autoconf", type="build", when="@master")
    depends_on("automake", type="build", when="@master")
    depends_on("libtool", type="build", when="@master")

    # Testing Dependencies
    depends_on("mpich pmi=pmi", type="test")
    depends_on("valgrind", type="test")
    depends_on("jq", type="test")

    # Patch 0.27-0.30 for build errors when czmq built with "draft APIs":
    patch("0001-build-fix-build-errors-with-side-installed-0MQ.patch", when="@0.27.0:0.30.0")

    def url_for_version(self, version):
        """
        Flux uses a fork of ZeroMQ's Collective Code Construction Contract
        (https://flux-framework.readthedocs.io/projects/flux-rfc/en/latest/spec_1.html).
        This model requires a repository fork for every stable release that has
        patch releases.  For example, 0.8.0 and 0.9.0 are both tags within the
        main repository, but 0.8.1 and 0.9.5 would be releases on the v0.8 and
        v0.9 forks, respectively.

        Rather than provide an explicit URL for each patch release, make Spack
        aware of this repo structure.
        """
        if version[-1] == 0:
            url = "https://github.com/flux-framework/flux-core/releases/download/v{0}/flux-core-{0}.tar.gz"
        else:
            url = "https://github.com/flux-framework/flux-core-v{1}/releases/download/v{0}/flux-core-{0}.tar.gz"
        return url.format(version.up_to(3), version.up_to(2))

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
        if not os.path.exists("configure"):
            # Bootstrap with autotools
            bash = which("bash")
            bash("./autogen.sh")

    @property
    def lua_version(self):
        return self.spec["lua"].version.up_to(2)

    @property
    def lua_share_dir(self):
        return os.path.join("share", "lua", str(self.lua_version))

    @property
    def lua_lib_dir(self):
        return os.path.join("lib", "lua", str(self.lua_version))

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        #  Ensure ./fluxometer.lua can be found during flux's make check
        env.append_path("LUA_PATH", "./?.lua", separator=";")

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        # If this package is external, we expect the external provider to set things
        # like LUA paths. So, we early return. If the package is not external,
        # properly set these environment variables to make sure the user environment
        # is configured correctly
        if self.spec.external:
            return
        env.prepend_path(
            "LUA_PATH", os.path.join(self.spec.prefix, self.lua_share_dir, "?.lua"), separator=";"
        )
        env.prepend_path(
            "LUA_CPATH", os.path.join(self.spec.prefix, self.lua_lib_dir, "?.so"), separator=";"
        )
        env.prepend_path(
            "PYTHONPATH",
            os.path.join(
                self.spec.prefix.lib,
                "python{0}".format(self.spec["python"].version.up_to(2)),
                "site-packages",
            ),
        )
        env.prepend_path("FLUX_MODULE_PATH", self.prefix.lib.flux.modules)
        env.prepend_path("FLUX_EXEC_PATH", self.prefix.libexec.flux.cmd)
        env.prepend_path("FLUX_CONNECTOR_PATH", self.prefix.lib.flux.connectors)

    def configure_args(self):
        args = ["--enable-pylint=no"]
        if "+docs" not in self.spec:
            args.append("--disable-docs")
        if self.spec.satisfies("+security"):
            args.append("--with-flux-security")
        return args

    def flag_handler(self, name, flags):
        if name == "cflags":
            # https://github.com/flux-framework/flux-core/issues/3482
            if self.spec.satisfies("%gcc@10:") and self.spec.satisfies("@0.23.0:0.23"):
                if flags is None:
                    flags = []
                flags.append("-Wno-error=stringop-truncation")

            if self.spec.satisfies("%gcc@8:") and self.spec.satisfies("@0.23.0"):
                if flags is None:
                    flags = []
                flags.append("-Wno-error=maybe-uninitialized")

        return flags, None, None
