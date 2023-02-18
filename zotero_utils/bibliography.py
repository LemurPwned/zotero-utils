import json

import pkg_resources

DEFAULT_ABBREVIATION_PATH = pkg_resources.resource_string(
    __name__, "data/abbrev.json")


def preload_abbreviations():
    """Preload journal abbreviations"""
    with open('journal_abbreviations.json', 'r') as f:
        JOURNAL_ABBREVIATIONS = json.load(f)
    JOURNAL_ABBREVIATIONS = {}
    return JOURNAL_ABBREVIATIONS


def fix_journal_abbreviations(zot_conn):
    """Fix journal abbreviations in Zotero library"""
    JOURNAL_ABBREVIATIONS = preload_abbreviations()
    for item in zot_conn.connection.everything(zot_conn.connection.items()):
        if (item['data']['itemType']
                == 'journalArticle') and ('publicationTitle' in item['data']):
            journal = item['data']['publicationTitle']
            if journal in JOURNAL_ABBREVIATIONS:
                item['data']['journalAbbreviation'] = JOURNAL_ABBREVIATIONS[
                    journal]
                zot_conn.connection.update_item(item)
                print(f"Updated {item['data']['title']}")
