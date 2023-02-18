"""Main module."""
import getpass
import os

import pyzotero as zotero


class ZoteroConn:

    def __init__(self, library_id: str, api_key: str) -> None:
        self._zot = zotero.Zotero(library_id=library_id,
                                  library_type='user',
                                  api_key=api_key)

    @property
    def connection(self):
        """Return the connection to the Zotero library"""
        return self._zot

    @classmethod
    def create_zotero_connection(cls,
                                 library_id: str = "",
                                 api_key: str = "") -> 'ZoteroCon':
        """Create a connection to the Zotero library"""
        if library_id and api_key:
            return cls(library_id=library_id, api_key=api_key)
        try:
            library_id = os.environ['ZOTERO_LIBRARY_ID']
            api_key = os.environ['ZOTERO_API_KEY']
        except KeyError:
            library_id = input('Zotero library id: ')
            api_key = getpass.getpass('Zotero api key: ')

        return cls(library_id=library_id, api_key=api_key)
