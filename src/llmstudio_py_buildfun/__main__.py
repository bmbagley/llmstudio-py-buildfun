"""Command-line interface."""

import click


@click.command()
@click.version_option()
def main() -> None:
    """Llmstudio Py Buildfun."""


if __name__ == "__main__":
    main(prog_name="llmstudio-py-buildfun")  # pragma: no cover
