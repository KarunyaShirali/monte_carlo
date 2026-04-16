# monte_carlo

![PyPI version](https://img.shields.io/pypi/v/monte_carlo.svg)

A package to perform Monte Carlo simulations.

* [GitHub](https://github.com/KarunyaShirali/monte_carlo/) | [PyPI](https://pypi.org/project/monte_carlo/) | [Documentation](https://KarunyaShirali.github.io/monte_carlo/)
* Created by [Karunya Shirali](https://audrey.feldroy.com/) | GitHub [@KarunyaShirali](https://github.com/KarunyaShirali) | PyPI [@KarunyaShirali](https://pypi.org/user/KarunyaShirali/)
* MIT License

## Features

* TODO

## Documentation

Documentation is built with [Zensical](https://zensical.org/) and deployed to GitHub Pages.

* **Live site:** https://KarunyaShirali.github.io/monte_carlo/
* **Preview locally:** `just docs-serve` (serves at http://localhost:8000)
* **Build:** `just docs-build`

API documentation is auto-generated from docstrings using [mkdocstrings](https://mkdocstrings.github.io/).

Docs deploy automatically on push to `main` via GitHub Actions. To enable this, go to your repo's Settings > Pages and set the source to **GitHub Actions**.

## Development

To set up for local development:

```bash
# Clone your fork
git clone git@github.com:your_username/monte_carlo.git
cd monte_carlo

# Install in editable mode with live updates
uv tool install --editable .
```

This installs the CLI globally but with live updates - any changes you make to the source code are immediately available when you run `monte_carlo`.

Run tests:

```bash
uv run pytest
```

Run quality checks (format, lint, type check, test):

```bash
just qa
```

## Author

monte_carlo was created in 2026 by Karunya Shirali.

Built with [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and the [audreyfeldroy/cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage) project template.
