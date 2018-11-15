#!/bin/bash

[ "$(grep 'alias mf-gen=' ~/.zshrc)" ] && echo "Aliases already exists.\nPlease verify if they are exacts !" || echo 'alias mf-gen="python3 ~/42-utilities/mf-gen.py"' >> ~/.zshrc; echo 'alias proto-list="python3 ~/42-utilities/proto-list.py"' >> ~/.zshrc;

