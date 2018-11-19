# 42-utilities
Simple tools to help your daily coding routine!
### Installation
```bash
git clone https://github.com/mathix420/42-utilities.git ~/42-utilities && sh ~/42-utilities/install.sh
```

## mf-gen
Generates Makefiles for you.
### Alias
An alias is added to your `shell rc` to use **mf-gen** anywhere:
```bash
alias mf-gen="python3 ~/42-utilities/mf-gen.py"
```
### Usage
Run `mf-gen` in your project folder.
Or if you prefer the arguments version:
```bash
mf-gen <executable_and_header_name> <sources_folder> <header_folder>
```

## proto-list
Lists all function prototypes (with how many tabs you want) so you can easily add them to your header file.
### Alias
An alias is added to your `shell rc` to use **proto-list** anywhere:
```bash
alias proto-list="python3 ~/42-utilities/proto-list.py"
```
### Usage
Run `proto-list` in your sources folder.

## Contributors
**agissing** [GitHub](https://github.com/mathix420)
**flklein** [GitHub](https://github.com/floklein)
