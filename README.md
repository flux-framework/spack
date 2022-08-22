# Spack Updater

This is a fork of spack that deploys an automated set of workflows to do updates!
This means that:

1. We have a main branch that is an orphan from spack develop
2. Spack develop is updated from upstream nightly
3. The packages here (in the main branch) can be worked on, and are automatically updated.

## Setting Up

To setup, you can do the following:

1. Create a fork of spack to your organization, only grabbing the develop branch.
2. Clone and create an orphan branch `git switch --orphan main` and then add the content here (the README, and .github workflows0
3. Add your custom packages and repo.yaml under packages.

The above might look like the following:

```bash
$ git clone https://flux-framework/spack /tmp/spack-template

# This is your fork
$ git clone git@github.com:<your-org>/spack spack
$ cd spack

# Create an orphan branch
$ git switch --orphan main

# Copy over the content you need (or you can emulate / update)
cp /tmp/spack-template/README.md ./README.md
cp -R /tmp/spack-template/scripts ./scripts/
cp -R /tmp/spack-template/.github ./.github
cp -R /tmp/spack-template/repo.yaml ./repo.yaml
```

You'll then want to update the repo.yaml with some name for your packages repository (it will
be added to spack and needs a different name than builtin), delete the subdirectories of packages
that you don't need (and add your own from spack). After that, you can push the main branch
and make it default so it's the first seen upon visiting your repository (akin to this one!)

### Packages Workflows

In [.github/workflows/test-build.yaml](.github/workflows/test-build.yaml) edit the packages names
to be those you want to test, adding additional testing blocks if needed. We are planning to eventually
expand this into a matrix for easier (and faster) use when we have more than one package here.
