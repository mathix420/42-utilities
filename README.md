# 42-utilities
Some 42 utilities

## mf-gen
Simple utility to generate Makefiles
### Installation

Simply get the file `mf-gen.py` and put it into a folder for example `~/Utilities/mf-gen.py`.

Then add an alias to `.zshrc` or `.shrc` to use mf-gen anywhere.
```bash
alias mf-gen="python3 ~/Utilities/mf-gen.py"
```
### Usage

Just execute this command in your project folder and follow instructions `mf-gen`.

Or execute this single line command : 
```bash
mf-gen <executable_and_header_name> <srcs_folder> <header_folder>
```
## proto-list
List all prototypes with the given number of tabs

### Usage

Just execute this command in your srcs folder and follow instructions `python3 proto-list.py`.
