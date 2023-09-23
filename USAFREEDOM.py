import re
import os.path
from sys import argv

from docx2python import docx2python
from docx2python.iterators import enum_cells, enum_at_depth

def extract_acronyms(in_acronyms_list, in_text):
    in_acronym = ""
    for character in in_text:
        if re.match("[A-Z]", character):
            in_acronym += character
        else:
            if len(in_acronym) >= 2 and in_acronym not in in_acronyms_list:
                in_acronyms_list.append(in_acronym)
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

if len(argv) > 1 and (filepath.endswith(".docx") or filepath.endswith(".txt")):

    body = ""
    footnotes = ""

    if filepath.endswith(".docx"):

        # get all relevant text from docx file
        everything = docx2python(filepath)

        body = everything.body_runs
        remove_empty_paragraphs(body)

        footnotes = everything.footnotes_runs
        remove_empty_paragraphs(footnotes)

    elif filepath.endswith(".txt"):

        # get all relevant text from txt file
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = [line.rstrip() for line in f]
            for line in lines:
                body += line

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

    print("extracting...")
    if len(argv) > 2 and argv[2] == "-t":
        print(out_acronyms_list)
    else:
        # rewrite the txt document with the new list
        with open('acronyms.txt', 'w+', encoding='utf-8') as f:
            for acronym in out_acronyms_list:
                f.write(acronym + '\n')
        print("'acronyms.txt' has been created or updated to contain your acronyms")

else:
    print("ERROR: wrong format... a path to a 'docx' or '.txt' document was expected as argument 1")
