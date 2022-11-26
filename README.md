# Acronym lister

Want to extract acronyms from a `.docx` or from a `.txt`file? This'll do it

## How to use

You'll need `python`.

If you're dealing with `.docx`, you'll also need to install `docx2python`. For example, with `pip`:
```shell
$ pip install docx2python
```

Then run the program, passing as an argument the path to the file from which acronyms need to be extracted. 

From the root of the project, you can enter: 

```shell
$ python .\USAFREEDOM.py "path\to\file"
extracting...
'acronyms.txt' has been created or updated to contain your acronyms
```

## Output

### → `.txt`

By default, the output is placed in a `.txt` file created at the root of this project.

### → terminal

If you prefer to have the acronyms printed in your terminal instead, you can type `-t` as a second argument, and you should see that kind of output:
```shell
$ python .\USAFREEDOM.py "path\to\file" -t
extracting...
['BA', 'BASIC', 'BTS', 'CAB', 'CAP', 'CEA', 'CM', 'CP', 'DUT', 'GSP', 'IBM', 'MITRA', 'NASA', 'PAF', 'SEA', 'SUDRIA', 'SUPELEC', 'URSS']
```