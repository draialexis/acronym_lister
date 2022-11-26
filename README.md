# Acronym lister (`.docx` → `.txt`)

Want to extract acronyms from a `.docx` file? This'll do it

## How to use

You'll need `pip` and `python`

First install `docx2python`:
```shell
$ pip install docx2python
```

Then run it, passing as an argument the path to the file from which acronyms need to be extracted. 

From the root of the project, you can enter: 

```shell
$ python .\USAFREEDOM.py "path\to\file.docx"
```

## Output

### → `.txt`

By default, the output is put in a `.txt` file created at the root of this project.

### → terminal

If you prefer to have the acronyms printed in your terminal instead, you can type `-t` as a second argument:
```shell
$ python .\USAFREEDOM.py "path\to\file.docx" -t
```
```shell
['BA', 'BASIC', 'BTS', 'CAB', 'CAP', 'CEA', 'CM', 'CP', 'DUT', 'GSP', 'IBM', 'MITRA', 'NASA', 'PAF', 'SEA', 'SUDRIA', 'SUPELEC', 'URSS']
```