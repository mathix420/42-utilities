# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mf-gen.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: agissing <agissing@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/11/10 18:01:56 by agissing          #+#    #+#              #
#    Updated: 2018/11/10 18:35:52 by agissing         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import subprocess, time, sys, os

def ft_putspc(str):
    return(' ' * (40 - len(str)))

c = len(sys.argv)
if (c == 1):
    prog = input('Program name : ')
    dir = input("Sources directory : ")
    inc = input("Headers directory : ")
elif (c == 4):
    prog = sys.argv[1]
    dir = sys.argv[2]
    inc = sys.argv[3]
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

header = '''# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: {0} <{1}>{2}+#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: {3}{4} #+#    #+#              #
#    Updated: {3}{4}###   ########.fr        #
#                                                                              #
# **************************************************************************** #
'''

text = header.format(user, mail, ft_putspc(user + mail), date, ft_putspc(date)) + '''
NAME = {0}

IDIR = {1}
_INC = {0}.h
INC = $(patsubst %,$(IDIR)/%,$(_INC))

SDIR = {2}
_SRC = {3}
SRC = $(patsubst %,$(SDIR)/%,$(_SRC))

OBJ = $(_SRC:.c=.o)

FLAGS = -Wall -Wextra -Werror
OPTS = -o $(NAME) -I$(IDIR)

.PHONY: all clean fclean re

all: $(NAME)

$(NAME): $(OBJ)
\t\t@gcc $(FLAGS) $(OPTS) $(SRC)

$(OBJ): $(SRC)
\t\t@gcc -c -I$(IDIR) $(SRC)

clean:
\t\t@/bin/rm -f $(OBJ)

fclean: clean
\t\t@/bin/rm -f $(NAME)

re: clean all'''.format(prog, inc, dir, files)

makefile.write(text)

sys.exit("All done !")
