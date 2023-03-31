##Challenge: Specialer

##Category: General Skills

##Description: Reception of Special has been cool to say the least. That's why we made an exclusive version of Special, called Secure Comprehensive Interface for Affecting Linux Empirically Rad, or just 'Specialer'. With Specialer, we really tried to remove the distractions from using a shell. Yes, we took out spell checker because of everybody's complaining. But we think you will be excited about our new, reduced feature set for keeping you focused on what needs it the most.

###Hints:

####1. What programs do you have access to?

Looking at the hints and the server, I found the following commands in the server by pressing tab on an empty command prompt:

>!          bind       compopt    elif       fc         if         printf     shift      true       while
>./         break      continue   else       fg         in         pushd      shopt      type       {
>:          builtin    coproc     enable     fi         jobs       pwd        source     typeset    }
>[          caller     declare    esac       for        kill       read       suspend    ulimit
>[[         case       dirs       eval       function   let        readarray  test       umask
>]]         cd         disown     exec       getopts    local      readonly   then       unalias
>alias      command    do         exit       hash       logout     return     time       unset
>bash       compgen    done       export     help       mapfile    select     times      until
>bg         complete   echo       false      history    popd       set        trap       wait

I found cd to be my biggest ally, as whenever I pressed tab after typing the command, it listed out the directories that there were in my home directory, and from my findings there were 2 text files per folder, makign there 6 text files in total (3 directories are there). I then found a way to display each file's contents by using the echo command:

>echo "$(<filename)"

With that, I found the flag to be in the directory ala/kazam.txt:

>echo "$(<ala/kazam.txt)"

P.S. I appreciate the reference in the file of abra/cadaniel.txt and its contents: "Yes, I did it! I really did it! I'm a true wizard!" LT, you are a real one for that. o7

###Flag: picoCTF{y0u_d0n7_4ppr3c1473_wh47_w3r3_d01ng_h3r3_811ae7e9}

Solved by giggsterpuku
