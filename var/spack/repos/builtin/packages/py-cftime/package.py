# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyCftime(PythonPackage):
    """Python library for decoding time units and variable values in a
    netCDF file conforming to the Climate and Forecasting (CF)
    netCDF conventions"""

    homepage = "https://unidata.github.io/cftime/"
    url = "https://github.com/Unidata/cftime/archive/refs/tags/v1.0.3.4rel.tar.gz"

    version("1.6.4", sha256="38970aa0d0ed9ed6b1d90f2cff2301b7299ae62d38e39a540400ab00edb4d2ce")
    version("1.0.3.4", sha256="f261ff8c65ceef4799784cd999b256d608c177d4c90b083553aceec3b6c23fd3")

    # https://github.com/Unidata/cftime/blob/v1.6.3rel/Changelog#L7
    depends_on("python@:3.11", when="@:1.6.2")

    depends_on("py-setuptools@18.0:", type="build", when="@1.0.3.4")
    depends_on("py-setuptools@41.2:", type="build", when="@1.6.4:")

    depends_on("py-cython@0.19:", type="build", when="@1.0.3.4")
    depends_on("py-cython@0.29.20:", type="build", when="@1.6.4:")

    # https://github.com/Unidata/cftime/blob/v1.6.4rel/Changelog#L6
    depends_on("py-numpy@:1.26.4", type=("build", "run"), when="@1.0.3.4")
    depends_on("py-numpy@1.26.0:", type=("build", "run"), when="@1.6.4:")
