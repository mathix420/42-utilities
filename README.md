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
> alias mf-gen="python3 ~/42-utilities/mf-gen.py"


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
> alias proto-list="sh ~/42-utilities/proto-list.sh"

### Usage
Use the `display` option to show the prototypes copied to your clipboard.
```bash
proto-list <sources_folder> <number_of_tabs> [display]
```

## Auto-updater
Updates **42-utilities** when necessary. Checks for updates only once a day. Takes about one second to do so.
### Alias
This command is prepended to all aliases:
> /bin/sh ~/42-utilities/update.sh

### How does it work?
- Checks if the date stored in `/tmp/.42_utilities_date` is different from the current date.
- If so, checks if `https://raw.githubusercontent.com/mathix420/42-utilities/master/sum` is different from `~/42-utilities/sum`.
- Again, if so, performs a `git pull` in the **42-utilities** directory.

## Contributors
* agissing: [GitHub](https://github.com/mathix420)
* flklein: [GitHub](https://github.com/floklein)
