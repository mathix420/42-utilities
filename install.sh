#!/bin/bash

[ "$(cat ~/.zshrc 2> /dev/null)" ] && ([ "$(grep 'alias mf-gen=' ~/.zshrc)" ] && echo "\nAliases already exists.\nPlease verify if they are exacts !" || ( echo 'alias mf-gen="python3 ~/42-utilities/mf-gen.py"' >> ~/.zshrc && echo 'alias proto-list="python3 ~/42-utilities/proto-list.py"' >> ~/.zshrc && echo "\nAliases perfectly added !" ));
[ "$(cat ~/.shrc 2> /dev/null)" ] && ([ "$(grep 'alias mf-gen=' ~/.shrc)" ] && echo "\nAliases already exists.\nPlease verify if they are exacts !" || ( echo 'alias mf-gen="python3 ~/42-utilities/mf-gen.py"' >> ~/.shrc && echo 'alias proto-list="python3 ~/42-utilities/proto-list.py"' >> ~/.shrc && echo "\nAliases perfectly added !" ));
[ "$(cat ~/.cshrc 2> /dev/null)" ] && ([ "$(grep 'alias mf-gen=' ~/.cshrc)" ] && echo "\nAliases already exists.\nPlease verify if they are exacts !" || ( echo 'alias mf-gen="python3 ~/42-utilities/mf-gen.py"' >> ~/.cshrc && echo 'alias proto-list="python3 ~/42-utilities/proto-list.py"' >> ~/.cshrc && echo "\nAliases perfectly added !" ));