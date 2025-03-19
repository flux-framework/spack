# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyCwlUtils(PythonPackage):
    """Python Utilities and Autogenerated Classes
    for loading and parsing CWL v1.0, CWL v1.1, and CWL v1.2 documents.
    """

    homepage = "https://github.com/common-workflow-language/cwl-utils"
    pypi = "cwl-utils/cwl-utils-0.21.tar.gz"

    license("Apache-2.0")

    version("0.37", sha256="7b69c948f8593fdf44b44852bd8ef94c666736ce0ac12cf6e66e2a72ad16a773")
    version("0.21", sha256="583f05010f7572f3a69310325472ccb6efc2db7f43dc6428d03552e0ffcbaaf9")

    depends_on("python@3.6:", type=("build", "run"))
    depends_on("python@3.8:", when="@0.29:", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    depends_on("py-cwl-upgrader@1.2.3:", type=("build", "run"))
    depends_on("py-packaging", type=("build", "run"))
    depends_on("py-rdflib", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-cachecontrol", type=("build", "run"))
    depends_on("py-schema-salad@8.3.20220825114525:8", when="@:0.31", type=("build", "run"))
    # intermediate versions 0.32:0.36 may not require 8.8, but should work with this stricter
    # requirement
    depends_on("py-schema-salad@8.8.20250205075315:8", when="@0.32:", type=("build", "run"))
    depends_on("py-ruamel-yaml@0.17.6:0.18", when="@0.30:", type=("build", "run"))
    depends_on("py-typing-extensions", when="@0.37 ^python@:3.9", type=("build", "run"))

    def url_for_version(self, version):
        url = "https://files.pythonhosted.org/packages/source/c/cwl-utils/cwl{}utils-{}.tar.gz"
        if version >= Version("0.34"):
            sep = "_"
        else:
            sep = "-"
        return url.format(sep, version)
