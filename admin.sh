#!/usr/bin/bash

############################################################
# Help                                                     #
############################################################
help()
{
   echo
   echo "-h     Call help function"
   echo "-n     Change user.name to GeeKboyboss"
   echo "-g     Clean git history"
   echo
}

############################################################
############################################################
# Main program                                             #
############################################################
############################################################


############################################################
# Process the input options. Add options as needed.        #
############################################################
# Get the options
while getopts ":h|g|n" option; do
   case $option in
      h)
         help
         ;;
      g)
         git checkout --orphan TEMP_BRANCH ; git add -A ; git commit -am "Initial commit" ; git branch -D main ; git branch -m main ; git push -f origin main
         echo
         echo "## == Successfully Cleaned Git Commit History == ##"
         echo
         ;;
      n)
         git config user.name GeeKboyboss
         echo
         echo "## == Successfully changed the name of user.name == ##"
         echo
         ;;
   esac
done

help
exit 0