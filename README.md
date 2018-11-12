# 42-utilities
Simple tools to help your daily coding routine!

## mf-gen
Generates Makefiles.
### Installation

Get the file `mf-gen.py` and put it into a folder (eg. `~/42-utilities/mf-gen.py`).

Then add an alias to `.zshrc` or `.shrc` to use *mf-gen* anywhere.
```bash
alias mf-gen="python3 ~/Utilities/mf-gen.py"
```
### Usage

If you added the alias, run `mf-gen` in your project folder.

Or run this single line command: 
```bash
mf-gen <executable_and_header_name> <srcs_folder> <header_folder>
```
## proto-list
Lists all function prototypes (with how many tabs you want) to easily add them to your header file.

### Usage

Run in your sources folder: `python3 proto-list.py`.
