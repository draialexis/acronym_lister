import os.path
from sys import argv

from docx2python import docx2python
from docx2python.iterators import enum_cells, enum_at_depth


def extract_acronyms(in_acronyms_list, in_text):
    in_acronym = ""
    for character in in_text:
        if character.isupper():
            in_acronym += character
        else:
            if len(in_acronym) >= 2 and in_acronym not in in_acronyms_list:
                in_acronyms_list.append(in_acronym)
            else:
                in_acronym = ""


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

    # get all relevant text from docx file
    everything = docx2python(filepath)

    body = everything.body_runs
    remove_empty_paragraphs(body)

    footnotes = everything.footnotes_runs
    remove_empty_paragraphs(footnotes)

    out_acronyms_list = []

    # get all older acronyms if any
    if os.path.exists('acronyms.txt'):
        with open('acronyms.txt', 'r', encoding='utf-8') as f:
            lines = [line.rstrip() for line in f]
            for acronym in lines:
                out_acronyms_list.append(acronym)

    # mix in acronyms from this body and footnotes
    extract_acronyms(out_acronyms_list, get_text_from_body(body))
    extract_acronyms(out_acronyms_list, get_text_from_body(footnotes))

    out_acronyms_list.sort()

    # rewrite the txt document with the new list
    with open('acronyms.txt', 'w', encoding='utf-8') as f:
        for acronym in out_acronyms_list:
            f.write(acronym + '\n')

else:
    print("ERROR: wrong format... a 'docx' document was expected")
