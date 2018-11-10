# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    proto-list.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: agissing <agissing@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/11/10 13:41:54 by agissing          #+#    #+#              #
#    Updated: 2018/11/10 13:41:57 by agissing         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import subprocess

nb_tab = input("Veuillez renseigner le nombre de tab(s) : ")
tabs = int(nb_tab) * '\t'
commande = "cat *.c | grep \"^\\w.*\$\" | grep -v \"^static\" | sed -E 's/[" + '\t' + r"]+/" + tabs + r"/' | sed 's/$/;/' | sort"
output = subprocess.check_output(['bash','-c', commande])
print (output.decode(), end = '')
