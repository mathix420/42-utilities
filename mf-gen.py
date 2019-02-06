# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mf-gen.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: agissing <agissing@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/11/10 18:01:56 by agissing          #+#    #+#              #
#    Updated: 2019/02/05 17:18:02 by agissing         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import subprocess, sys, re
from time import strftime
from os import path, environ

app_path = path.dirname(path.realpath(__file__))
PARAMS = ['-n', '--lib', '--and', '--type']
OPTIONS = ['-v', '--verbose', '-f']
LIBS = []
ESCAPE = []
OPT = [0 for i in OPTIONS]

objects = []

class obj():
    def __init__(self):
        self.name = ''
        self.dir = ''
        self.inc = ''
        self.lib = []

def usage():
    usage = """Usage: mf-gen [OPTIONS] [[NAME] [SRCS] [INCLUDES] [OPTIONS]]...

Makefile Options:
{0}--lib        {1}Add local library (template: <directory>.<library_name>)
{0}--and        {1}Append new program to makefile (only in command line mode)

General Options:
{0}-v, --verbose{1}Verbose the Makefile output
{0}-h, --help   {1}Show help output
{0}-n <int>     {1}Make multiple programs in GUI mode
{0}-f           {1}Force writing (may cause unwanted overwriting)

Command line Examples:
{0}$ mf-gen program "srcs" "includes mine" --lib mine.lib
{0}$ mf-gen -S prog1 src1 inc1 --and prog2 src2 inc2 --lib some.library

GUI mode Examples:
{0}$ mf-gen
{0}$ mf-gen -fn 2

Made with <3 by agissing and flklein
GitHub page: https://github.com/mathix420/42-utilities""".format(' ' * 3, ' ' * 5)
    sys.exit(usage)
    
        
def ft_putspc(str):
    return(' ' * (40 - len(str)))

def get_userinfos():
    try:
        _mail = environ['MAIL']
    except:
        _mail = 'marvin@42.fr'
    try:
        _user = environ['USER']
    except:
        _user = 'marvin'
    return (_user, _mail)
    
def check_args(argv, OPTS):
# Return 0 for gui > 3 for command line and < 0 if errors occurs
    c = 0
    n = 1
    for arg in argv[1:]:
        if arg == '-':
            usage()
        if arg in PARAMS:
            ESCAPE.append(arg)
            if arg == '-n':
                n = -1
            c -= 2
        elif arg[0] == '-':
            ESCAPE.append(arg)
            if arg[1] == '-' and arg in OPTIONS:
                OPTS[OPTIONS.index(arg)] = 1
            elif arg[1] == '-':
                usage()
            if arg[-1] == 'n':
                n = -1
                c -= 1
                arg = arg[:-1]
            for char in arg[1:]:
                if '-' + char in OPTIONS:
                    OPTS[OPTIONS.index('-' + char)] = 1
                else:
                    usage()
            c -= 1
        elif n == -1:
            ESCAPE.append(arg)
            n = int(arg)
        c += 1
    return (c, n, OPTS)

c, n, OPT = check_args(sys.argv, OPT)
if (c == 0): #GUI mode
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
                if l.rstrip('.').count('.') == 1:
                    objects[-1].lib.append(l.split('.'))
                else:
                    sys.exit("\nmf-gen: %s: Bad librairy format" % l)
    print ("\nNext time you can use this command :\n\n\t$ mf-gen",
           ' --and '.join([('%s "%s" "%s"' % (o.name, o.dir, o.inc))
                           + ''.join([' --lib %s.%s' % (l[0], l[1])
                                       for l in o.lib])
                           for o in objects]))
elif (c >= 3): #Command line mode
    d = 0
    for i in range(1, len(sys.argv)):
        if d == 0 and not sys.argv[i] in ESCAPE:
            objects.append(obj())
            objects[-1].name = sys.argv[i]
            d += 1
        elif d == 1 and not sys.argv[i] in ESCAPE:
            objects[-1].dir = sys.argv[i]
            d += 1
        elif d == 2 and not sys.argv[i] in ESCAPE:
            objects[-1].inc = sys.argv[i]
            d += 1
        elif sys.argv[i] == "--and":
            d = 0;
        elif i > 0 and sys.argv[i - 1] == "--lib":
            if sys.argv[i].rstrip('.').count('.') == 1:
                objects[-1].lib.append(sys.argv[i].split('.'))
            else:
                sys.exit("\nmf-gen: %s: Bad librairy format" % sys.argv[i])
        for i in range(4, len(sys.argv)):
            if (i + 1 < len(sys.argv) and sys.argv[i] == "--type"):
                model_name = sys.argv[i + 1]
else:
    usage()

def header_42():
    user, mail = get_userinfos()
    date = strftime('%Y/%m/%d %X') + ' by ' + user
    header_template = open(path.join(app_path, 'header_42'), 'r')
    return (header_template.read().format(user, mail, ft_putspc(user + mail),
                                          date, ft_putspc(date)))

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

for prog in objects:
    for lib in prog.lib:
        if not lib in LIBS:
            LIBS.append(lib)
            output += beautify(lib[1]) + ' = ' + path.join(lib[0], lib[1]) + '.a\n'

output += '''
################################################################################
#####                           COMPILER OPTIONS                           #####
################################################################################

CC = gcc
FLAGS = -Wall -Wextra -Werror

################################################################################
#####                            MAKEFILE RULES                            #####
################################################################################

.PHONY : all clean fclean re

all :'''

for o in objects:
    output += ' $(%s)' % beautify(o.name)

output += '\n\n'

#Librairies rules
for lib in LIBS:
    output += '$(%s) :\n' % beautify(lib[1])
    output += '\t%smake -C %s\n\n' % ('' if (OPT[0] or OPT[1]) else '@', lib[0])

for prog in objects:
    #Objects rules
    output += '$({0}_OBJ) : %.o : %.c\n'.format(beautify(prog.name))
    output += '\t%s$(CC) $(FLAGS) -c $< -o $@ ' % ('' if (OPT[0] or OPT[1]) else '@')
    output += ' '.join(['-I%s' % n for n in prog.inc.split(' ')]) + '\n\n'
    #Program rule
    output += '$({0}) : $({0}_OBJ) {1}\n'.format(beautify(prog.name), ' '.join('$(%s)' % beautify(v[0]) for v in prog.lib))
    output += '\t{1}$(CC) $(FLAGS) $({0}_OBJ) -o $@ '.format(beautify(prog.name), '' if (OPT[0] or OPT[1]) else '@')
    output += ' '.join(['-I%s' % n for n in prog.inc.split(' ')]) + ' '
    if len(prog.lib) > 0:
        output += ' '.join(['-L%s -l%s' % (v[0], v[1].lstrip('lib')) for v in prog.lib])
    output += '\n\n'
#clean
output += 'clean :\n\t%s/bin/rm -f ' % ('' if (OPT[0] or OPT[1]) else '@')
output += ' '.join(['$(%s_OBJ)' % beautify(o.name) for o in objects]) + '\n\n'
#fclean
output += 'fclean : clean\n\t%s/bin/rm -f ' % ('' if (OPT[0] or OPT[1]) else '@')
output += ' '.join(['$(%s)' % beautify(o.name) for o in objects]) + '\n\n'
#re
output += 're : fclean all\n'

#Writing
if (not OPT[2]) and path.isfile('Makefile'):
    makefile = open('Makefile', 'r')
    content = makefile.read()
    get = 'q'
    if content[924:939] == 'MF-GEN MAKEFILE':
        while not get.lower() in ['y', '', 'n']:
            get = input("mf-gen Makefile already exist, would-you overwrite it [Y/n]: ")
        if get.lower() == 'n':
            exit("Abort.")
    else:
        while not get.lower() in ['y', '', 'n']:
            get = input("Makefile already exist, would-you overwrite it [Y/n]: ")
        if get.lower() == "n":
            exit("Abort.")
    makefile.close()

makefile = open('Makefile', 'w+')

makefile.write(output)

makefile.close()
