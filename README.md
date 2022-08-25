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

### Packages Workflows

How does it all work? 

#### Organization

The main branch has a simple structure with a packages folder where you can keep your recipes.
You don't need to go digging through many levels of paths that you might forget, or get lost in
the wildnerness of thousands of packages. They are front and center. The repository also has a spack develop branch, 
and you largely don't need to interact with it. The reason it's there is because when there are changes here 
to our packages, we create a branch (that needs to be forked from spack) here, and then can give you a link to open a pull request.

### Testing Builds

Importantly, we want to always test that our packages build against the develop build of spack.
This means we want to test a matrix of builds nightly, and this is done by way of the
[.github/workflows/test-build.yaml](.github/workflows/test-build.yaml) workflow. The only thing you
need to update here is the list of your packages under the matrix:

```yaml
jobs:
  package-builds:
    name: Test Package Builds
    runs-on: ubuntu-latest
    strategy:
      max-parallel: 4
      matrix:
        # Here are the names you'll want to edit
        package: [flux-core, flux-sched, flux-pmix]
```

Those names should correspond to package folders in [packages](packages). If you are interested,
[here is an example](https://github.com/flux-framework/spack/actions/runs/2916603405) of a nightly build running.

### Update Upstream

When we create a new branch with a package update to prepare to open a pull request to spack,
it's important that it's updated! It also doesn't look good to have a develop branch that is severely behind.
To support this, we have the [.github/workflows/upstream-update.yaml](.github/workflows/upstream-update.yaml)
workflow, which you can copy and use as is. If you are interested, [here is an example](https://github.com/flux-framework/spack/actions/runs/2916613894)
of it running. It will run nightly.

### Look for New Releases

If you maintain packages on GitHub, we use the releases API to (also nightly) check to see if there is a new release.
When we find one we:

- update the package.py file
- test the new build
- open a pull request on success

You can see an example workflow under [flux-sched](https://github.com/flux-framework/spack/runs/7988450863?check_suite_focus=true),
and the [pull request it opened](https://github.com/flux-framework/spack/pull/31). Once these changes are in, the next run of
the spack updater action, discussed next, will prepare to open a pull request to spack.

**Important** checking for new releases is currently only supported for GitHub releases. If you have another
package release type with an API that could be supported, please open an issue and it can be added.


spack updater that looks for changes here, and then opens and issue that can be clicked to open a PR to spack (e.g., https://github.com/spack/spack/pull/32320), or if there are changes to spack, opens a PR here (this is the last one I need to ensure is still working after the changes, so far one direction to spack has worked ok!)
I'd really like the opened PR to spack to link back to the issue, but so far adding variables to the get request doesn't seem to work (it gets stripped!) So I'm taking two seconds to just copy paste the issue into the new PR and that works for me, for now.
:tada:
1


