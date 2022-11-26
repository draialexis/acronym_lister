from sys import argv

from docx2python import docx2python
from docx2python.iterators import enum_cells, enum_at_depth


def extract_acronyms(in_acronyms_list, in_text):
    acronym = ""
    for character in in_text:
        if character.isupper():
            acronym += character
        else:
            if len(acronym) >= 2 and acronym not in in_acronyms_list:
                in_acronyms_list.append(acronym)
            else:
                acronym = ""


def remove_empty_paragraphs(tables):
    for (i, j, k), cell in enum_cells(tables):
        tables[i][j][k] = [x for x in cell if x]


def get_text_from_body(tables):
    res = ""
    for paragraph in enum_at_depth(tables, 4):
        res += paragraph.value[0]
    return res


filepath = argv[1]

if ".docx" in filepath:
    everything = docx2python(filepath)

    body = everything.body_runs
    remove_empty_paragraphs(body)

    footnotes = everything.footnotes_runs
    remove_empty_paragraphs(footnotes)

    out_acronyms_list = []

    print('extracting from body and footnotes...')
    extract_acronyms(out_acronyms_list, get_text_from_body(body))
    extract_acronyms(out_acronyms_list, get_text_from_body(footnotes))
    print(out_acronyms_list)

    print('sorting...')
    out_acronyms_list.sort()
    print(out_acronyms_list)

    # TODO: produce a txt file with the acronyms, one by line

else:
    print("ERROR: wrong format -- a 'docx' document was expected')")
