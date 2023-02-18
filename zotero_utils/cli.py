"""Console script for zotero_utils."""

import click

from zotero_utils.bibliography import fix_journal_abbreviations
from zotero_utils.zotero_utils import ZoteroConn


@click.command()
def main():
    """Main entrypoint."""
    click.echo("zotero-utils")
    click.echo("=" * len("zotero-utils"))
    click.echo("Utils for Zotero")


@main.command()
def fix_abbreviations():
    """Fix journal abbreviations in Zotero library"""
    zot_conn = ZoteroConn.create_zotero_connection()
    click.echo("Fixing journal abbreviations")
    fix_journal_abbreviations(zot_conn=zot_conn)


if __name__ == "__main__":
    main()  # pragma: no cover
