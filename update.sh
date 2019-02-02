# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    update.sh                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: agissing <agissing@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/02/02 09:50:31 by agissing          #+#    #+#              #
#    Updated: 2019/02/02 18:07:37 by agissing         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

DATE=$(cat /tmp/.42_utilities_date 2> /dev/null)
path="~/42-utilities"
var="n"

if [ "$DATE" != $(date +%Y-%m-%d) ]; then
	date +%Y-%m-%d > /tmp/.42_utilities_date
	HOST=$(curl -s https://raw.githubusercontent.com/mathix420/42-utilities/master/sum)
	SUM=$(cat ~/42-utilities/sum)
	if [ "$HOST" != "$SUM" ]; then
		read -p "Would you update 42-utilities [Y/n] : " var
		if [ "$var" = "y" ] || [ "$var" = "Y" ] || [ "$var" = "" ]; then
			eval git -C "$path" pull > /dev/null && echo "\n42-utilities has been updated !" || echo "\nError !"
		fi
	fi
fi
