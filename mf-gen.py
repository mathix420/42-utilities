# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mf-gen.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: agissing <agissing@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/11/10 18:01:56 by agissing          #+#    #+#              #
#    Updated: 2018/11/15 15:13:36 by agissing         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import subprocess, time, sys, os

def ft_putspc(str):
    return(' ' * (40 - len(str)))

c = len(sys.argv)
model_name = "MakeSimple"
if (c == 1):
    prog = input('Program name : ')
    dir = input("Sources directory : ")
    inc = input("Headers directory : ")
elif (c >= 4):
    prog = sys.argv[1]
    dir = sys.argv[2]
    inc = sys.argv[3]
    for i in range(4, len(sys.argv)):
        if (i + 1 < len(sys.argv) and sys.argv[i] == "--type"):
            model_name = sys.argv[i + 1]
else:
    sys.exit("Bad arguments !")
    
makefile = open('Makefile', 'w+')

try:
    mail = os.environ['MAIL']
except:
    mail = 'marvin@42.fr'
user = os.environ['USER']
date = time.strftime('%Y/%m/%d %X') + ' by ' + user

commande = "cd %s && ls *.c | sort | sed 's/$/ \\\/'" % dir
files = subprocess.check_output(['bash','-c', commande]).decode()[:-2]

model = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), model_name), 'r')

makefile.write(model.read().format(user, mail, ft_putspc(user + mail),
                     date, ft_putspc(date), prog, inc, dir, files))

if (c == 1):
    print ("All done !")
