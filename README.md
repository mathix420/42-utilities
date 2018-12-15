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
Copies all function prototypes (with how many tabs you want) to your clipboard, so you can easily add them to your header file.
### Alias
An alias is added to your `shell rc` to use **proto-list** anywhere:
```bash
alias proto-list="sh ~/42-utilities/proto-list.sh"
```
### Usage
Use the `display` option to show the prototypes copied to your clipboard.
```bash
proto-list <sources_folder> <number_of_tabs> [display]
```

## Contributors
* agissing: [GitHub](https://github.com/mathix420)
* flklein: [GitHub](https://github.com/floklein)
