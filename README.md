# Spack Updater

This is a fork of spack that deploys an automated set of workflows to do updates,
and ensure that changes to your packages OR to spack do not break your builds.
This means that:

1. We have a main branch that is an orphan from spack develop
2. Spack develop is updated from upstream nightly
3. The packages here (in the main branch) can be worked on, are automatically updated, and builds are always tested.

Or in short terms, you can maintain your spack packages in one simple place,
and the automation will support you to update the package versions, test builds
with updates (and nightly) and assist with opening pull requests to spack.

## Setting Up

### Repository

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

### Content

You'll then want to:

1. Update the repo.yaml with some name for your packages repository (it will be added to spack and needs a different name than builtin).
2. Delete the subdirectories of packages that you don't need (and add your own from spack). 
3. Ensure issues are enabled on your fork.
4. Add a label for "spack-updater"
5. Ensure your develop branch is protected (so you cannot delete it).
6. After that, you can push the main branch and make it default so it's the first seen upon visiting your repository (akin to this one!)


To see how it works, check out the [spack updater action](https://github.com/sciworks/spack-updater) and [documentation](https://sciworks.github.io/spack-updater/).
