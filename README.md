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

Interested to create your own, or see how it works?
Check out the [spack updater action](https://github.com/sciworks/spack-updater) and ⭐️ [documentation](https://sciworks.github.io/spack-updater/) ⭐️.
