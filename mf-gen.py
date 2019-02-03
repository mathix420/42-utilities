# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mf-gen.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: agissing <agissing@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/11/10 18:01:56 by agissing          #+#    #+#              #
#    Updated: 2019/02/03 10:58:56 by agissing         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import subprocess, time, sys, os, re
from os import path

app_path = path.dirname(path.realpath(__file__))
PARAMS = ['-n', '--lib', '--and', '--type']
OPTIONS = ['-S', '--sumary']

objects = []

class obj():
    def __init__(self):
        self.name = ''
        self.dir = ''
        self.inc = ''
        self.lib = []

def ft_putspc(str):
    return(' ' * (40 - len(str)))

def get_userinfos():
    try:
        _mail = os.environ['MAIL']
    except:
        _mail = 'marvin@42.fr'
    try:
        _user = os.environ['USER']
    except:
        _user = 'marvin'
    return (_user, _mail)
    
def check_args(argv):
# Return 0 for gui > 3 for command line and < 0 if errors occurs
    c = 0
    n = 1
    for arg in argv[1:]:
        if arg in PARAMS:
            if arg == '-n':
                n = -1
            c -= 2
        elif arg in OPTIONS:
            c -= 1
        elif n == -1:
            n = int(arg)
        c += 1
    return (c, n)

c, n = check_args(sys.argv)
model_name = "MakeSimple"
if (c == 0):
    for i in range(n):
        objects.append(obj())
        objects[-1].name = input('Program name : ')
        if objects[-1].name == "" or ' ' in objects[-1].name:
            sys.exit("\nmf-gen: '%s': Bad program name" % objects[-1].name)
        objects[-1].dir = input("Sources directory [.]: ")
        if objects[-1].dir == "":
            objects[-1].dir = '.'
        objects[-1].inc = input("Headers directory [.]: ")
        if objects[-1].inc == "":
            objects[-1].inc = '.'
        for l in input("Local librairies (<dirname>.<libname>) : ").split(' '):
            if l != '':
                if l.count('.') == 1:
                    objects[-1].lib.append(l.split('.'))
                else:
                    sys.exit("\nmf-gen: %s: Bad librairy format" % l)
    print ("\nNext time you can use this command :\n\n\t$ mf-gen",
           ' --and '.join([('%s "%s" "%s"' % (o.name, o.dir, o.inc))
                           + ' '.join(['--lib %s.%s' % (l[0], l[1])
                                       for l in o.lib])
                           for o in objects]))
elif (c >= 3):
    d = 0
    for i in range(1, len(sys.argv)):
        if d == 0:
            objects.append(obj())
            objects[-1].name = sys.argv[i]
            d += 1
        elif d == 1:
            objects[-1].dir = sys.argv[i]
            d += 1
        elif d == 2:
            objects[-1].inc = sys.argv[i]
            d += 1
        elif sys.argv[i] == "--and":
            d = 0;
        elif i > 0 and sys.argv[i - 1] == "--lib":
            objects[-1].lib.append(sys.argv[i].split('.'))
        for i in range(4, len(sys.argv)):
            if (i + 1 < len(sys.argv) and sys.argv[i] == "--type"):
                model_name = sys.argv[i + 1]
else:
    sys.exit("Bad arguments !")

def header_42():
    user, mail = get_userinfos()
    date = time.strftime('%Y/%m/%d %X') + ' by ' + user
    header_template = open(path.join(app_path, 'header_42'), 'r')
    return (header_template.read().format(user, mail, ft_putspc(user + mail),
                                          date, ft_putspc(date)))

makefile = open('Makefile', 'w+')

output = header_42() + '''
################################################################################
#####                              FILES VARS                              #####
################################################################################

'''

def beautify(str):
    return (re.compile('[\W_]+').sub('', str).upper())

for prog in objects:
    output += beautify(prog.name) + ' = ' + prog.name + '\n'
for prog in objects:
    end = beautify(prog.name) + '_SRC ='
    i = objects.index(prog)
    for d in prog.dir.split(' '):
        try:
            commande = "cd %s 2> /dev/null && ls *.c 2> /dev/null | sort | sed 's/$/ \\\/'" % d
            files = subprocess.check_output(['bash','-c', commande]).decode()[:-2]
        except:
            sys.exit("\nmf-gen: %s: No such file or directory" % d)
        output += "\nDIR_" + beautify(d) + str(i) + ' = ' + d + '\n'
        output += "_" + beautify(d) + str(i) + ' = ' + files + '\n'
        end += ' $(patsubst %,$(' + "DIR_" + beautify(d) + str(i)
        end += ')/%,$(' + "_" + beautify(d) + str(i) + '))'
    output += end + '\n'
    output += '\n{0}_OBJ = $({0}_SRC:.c=.o)\n'.format(beautify(prog.name))

output += '''
################################################################################
#####                           COMPILER OPTIONS                           #####
################################################################################

CC = gcc
FLAGS = -Wall -Wextra -Werror

################################################################################
#####                            MAKEFILE RULES                            #####
################################################################################

.PHONY: all clean fclean re

all :'''

for o in objects:
    output += ' $(%s)' % beautify(o.name)

output += '\n\n'

for prog in objects:
    output += '$({0}_OBJ) : %.o : %.c\n'.format(beautify(prog.name))
    output += '\t@$(CC) $(FLAGS) -c $< -o $@ '
    output += ' '.join(['-I %s' % n for n in prog.inc.split(' ')]) + '\n\n'
    output += '$({0}) : $({0}_OBJ)\n\t@$(CC) $(FLAGS) $({0}_OBJ) -o $@ '.format(beautify(prog.name))
    output += ' '.join(['-I %s' % n for n in prog.inc.split(' ')]) + ' '
    if len(prog.lib) > 0:
        output += ' '.join(['-L%s -l%s' % (v[0], v[1].lstrip('lib')) for v in prog.lib])
    output += '\n\n'
output += 'clean :\n\t@/bin/rm -f '
output += ' '.join(['$(%s_OBJ)' % beautify(o.name) for o in objects]) + '\n\n'
output += 'fclean : clean\n\t@/bin/rm -f '
output += ' '.join(['$(%s)' % beautify(o.name) for o in objects]) + '\n\n'
output += 're : fclean all\n'

makefile.write(output)

if (c == 1):
    print ("All done !")
