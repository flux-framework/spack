# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import pytest

import spack.concretize
import spack.config
import spack.solver.asp

version_error_messages = [
    "Cannot satisfy",
    "        required because quantum-espresso depends on fftw@:1.0",
    "          required because quantum-espresso ^fftw@1.1: requested explicitly",
    "        required because quantum-espresso ^fftw@1.1: requested explicitly",
]

external_error_messages = [
    (
        "Attempted to build package quantum-espresso which is not buildable and does not have"
        " a satisfying external"
    ),
    (
        "        'quantum-espresso~veritas' is an external constraint for quantum-espresso"
        " which was not satisfied"
    ),
    "        'quantum-espresso+veritas' required",
    "        required because quantum-espresso+veritas requested explicitly",
]

variant_error_messages = [
    "'fftw' requires conflicting variant values '~mpi' and '+mpi'",
    "        required because quantum-espresso depends on fftw+mpi when +invino",
    "          required because quantum-espresso+invino ^fftw~mpi requested explicitly",
    "        required because quantum-espresso+invino ^fftw~mpi requested explicitly",
]

external_config = {
    "packages:quantum-espresso": {
        "buildable": False,
        "externals": [{"spec": "quantum-espresso@1.0~veritas", "prefix": "/path/to/qe"}],
    }
}


@pytest.mark.parametrize(
    "error_messages,config_set,spec",
    [
        (version_error_messages, {}, "quantum-espresso^fftw@1.1:"),
        (external_error_messages, external_config, "quantum-espresso+veritas"),
        (variant_error_messages, {}, "quantum-espresso+invino^fftw~mpi"),
    ],
)
def test_error_messages(error_messages, config_set, spec, mock_packages, mutable_config):
    for path, conf in config_set.items():
        spack.config.set(path, conf)

    with pytest.raises(spack.solver.asp.UnsatisfiableSpecError) as e:
        _ = spack.concretize.concretize_one(spec)

    for em in error_messages:
        assert em in str(e.value)
