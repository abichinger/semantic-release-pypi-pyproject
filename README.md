# semantic-release-pypi - `pyproject.toml`

A template on how to use [`semantic-release-pypi`](https://github.com/abichinger/semantic-release-pypi) for a python package with `pyproject.toml`

important files:
- [`.releaserc.json`](.releaserc.json) - `semantic-release` [configuration](https://semantic-release.gitbook.io/semantic-release/usage/configuration)
- [`release.yml`](.github/workflows/release.yml) - Github workflow to run `semantic-release`
- [`package.json`](package.json) - defines the required dependencies

### Other templates

[`setup.py`](https://github.com/abichinger/semantic-release-pypi-setup) based 