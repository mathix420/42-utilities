********************************************************************************
                                                                                
                                                          :::      ::::::::     
     todo.md                                            :+:      :+:    :+:     
                                                      +:+ +:+         +:+       
     By: agissing <agissing@student.42.fr>          +#+  +:+       +#+          
                                                  +#+#+#+#+#+   +#+             
     Created: 2019/02/01 15:02:06 by agissing          #+#    #+#               
     Updated: 2019/02/01 15:19:06 by agissing         ###   ########.fr         
                                                                                
********************************************************************************


# mf-gen:
## Done:
- Une option pour les librairies locales
  - Ajout en dependance ??
  - Exemple :
  	- `--lib libft.libft`
	- `--lib <nom-de-dossier>.<nom-de-la-lib>`
	- egalement un prompt supplementaire :
	  - Librairie locale (`<dirname>.<libname>`) :
	  - separer les differentes lib par un espace

- Une option pour compiler plusieurs programmes en meme temps :
  - `--and` pour ajouter un nouveau programme ou `-n <nbr>` pour le mode prompt
  - Exemple :
  	- `mf-gen push_swap srcs/push_swap inc --lib libft.libft --and checker srcs/checker inc --lib libft.libft --lib minilibx.libmlx`
	- `mf-gen -n 2` > Prompt 1; Prompt 2

## To Do:
- Un commentaire d'escape dans le Makefile pour ne pas modifier certaines lignes
  - Exemple :
  	- "### ESCAPE mf-gen START"
	- "### ESCAPE mf-gen STOP"

- Une option `--sumary` ou `-S` qui peut résumer les changements apportés au Makefile
