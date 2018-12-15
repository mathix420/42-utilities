#!/bin/bash

[ "$(cat ~/.zshrc 2> /dev/null)" ] && ([ "$(grep 'alias mf-gen=' ~/.zshrc)" ] && echo "\nAliases already exist.\nPlease verify if they are correct!" || ( echo 'alias mf-gen="python3 ~/42-utilities/mf-gen.py"' >> ~/.zshrc && echo 'alias proto-list="sh ~/42-utilities/proto-list.sh"' >> ~/.zshrc && echo "\nAliases added!" ));
[ "$(cat ~/.shrc 2> /dev/null)" ] && ([ "$(grep 'alias mf-gen=' ~/.shrc)" ] && echo "\nAliases already exist.\nPlease verify if they are correct!" || ( echo 'alias mf-gen="python3 ~/42-utilities/mf-gen.py"' >> ~/.shrc && echo 'alias proto-list="sh ~/42-utilities/proto-list.sh"' >> ~/.shrc && echo "\nAliases added!" ));
[ "$(cat ~/.cshrc 2> /dev/null)" ] && ([ "$(grep 'alias mf-gen=' ~/.cshrc)" ] && echo "\nAliases already exist.\nPlease verify if they are correct!" || ( echo 'alias mf-gen="python3 ~/42-utilities/mf-gen.py"' >> ~/.cshrc && echo 'alias proto-list="sh ~/42-utilities/proto-list.sh"' >> ~/.cshrc && echo "\nAliases added!" ));
