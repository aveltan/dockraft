#!/bin/bash 

# #######################################################################
# ######################### server.properties ###########################
# #######################################################################

difficulty() {
	if [ -n ${1+1} ]; then
		if [ $1 == "peaceful" ]; then
			sed -i 's/difficulty.*/difficulty=0/g' server.properties
		elif [ $1 == "easy" ]; then
			sed -i 's/difficulty.*/difficulty=1/g' server.properties
		elif [ $1 == "normal" ]; then
			sed -i 's/difficulty.*/difficulty=2/g' server.properties
		elif [ $1 == "hard" ]; then
			sed -i 's/difficulty.*/difficulty=3/g' server.properties
		else
			echo "difficulty value invalid"
		fi
	else
		echo "difficulty not set"
	fi	
}

gamemode() {
        if [ -n ${1+1} ]; then
                if [ $1 == "survival" ]; then
                        sed -i 's/gamemode.*/gamemode=0/g' server.properties
                elif [ $1 == "creative" ]; then
                        sed -i 's/gamemode.*/gamemode=1/g' server.properties
                elif [ $1 == "adventure" ]; then
                        sed -i 's/gamemode.*/gamemode=2/g' server.properties
                elif [ $1 == "spectator" ]; then
                        sed -i 's/gamemode.*/gamemode=3/g' server.properties
                else
                        echo "gamemode value invalid"
                fi
        else
                echo "gamemode not set"
        fi        
}

pvp() {
        if [ -n ${1+1} ]; then
                if [ $1 == "true" ]; then
                        sed -i 's/pvp.*/pvp=true/g' server.properties
                elif [ $1 == "false" ]; then
                        sed -i 's/pvp.*/pvp=false/g' server.properties
                else
                        echo "pvp value invalid"
                fi
        else
                echo "pvp not set"
        fi        
}

whitelistfile() {
        if [ -n ${1+1} ]; then
                if [ $1 == "true" ]; then
                        sed -i 's/white-list.*/white-list=true/g' server.properties
                elif [ $1 == "false" ]; then
                        sed -i 's/white-list.*/white-list=false/g' server.properties
                else
                        echo "white-list value invalid"
                fi
        else
                echo "white-list not set"
        fi       
}

serverport(){
        if [ -n ${1+1} ]; then
              sed -i 's/server-port.*/server-port='$1'/g' server.properties
        else
              echo "SERVER-PORT value invalid"
        fi        
}

onlinemode() {
        if [ -n ${1+1} ]; then
              if [ $1 == "true" ]; then
                      sed -i 's/online-mode.*/online-mode=true/g' server.properties
              elif [ $1 == "false" ]; then
                      sed -i 's/online-mode.*/online-mode=false/g' server.properties
              else
                      echo "ONLINE-MODE value invalid"
              fi
        else
              echo "ONLINE-MODE not set"
        fi
}



# #######################################################################
# ############################### eula.txt ##############################
# #######################################################################

eula(){
    if [ -n ${1+1} ]; then
        if [ $1 == "true" ]; then
            sed -i 's/eula.*/eula=true/g' eula.txt
        elif [ $1 == "false" ]; then
            sed -i 's/eula.*/eula=false/g' eula.txt
        else
            echo "EULA value invalid"
        fi
    else
        echo "EULA not set"
    fi    
}


# #######################################################################
# ############################### ops.json ##############################
# #######################################################################
addops(){
    if [ -n ${1+1} ]; then
        uuid=$(echo $1 | cut -f1 -d:)
        name=$(echo $1 | cut -f2 -d:)
        level=$(echo $1 | cut -f3 -d:)
        entry='  {\n    "uuid": "'$uuid'",\n    "name": "'$name'",\n    "level":"'$level'"\n  }\n'

        if grep -Fq "uuid" ops.json
        then
            ## at least one player registered as op
            sed -i 's|]|,\n'"$entry"']|' ops.json
        else
            ## no player registered as op
            sed -i 's|]|\n'"$entry"']|' ops.json
        fi
        
    else
        echo "WHITELIST not set"
    fi   
}


# #######################################################################
# ########################### whitelist.json ############################
# #######################################################################

addwhitelist(){  
    if [ -n ${1+1} ]; then
        uuid=$(echo $1 | cut -f1 -d:)
        name=$(echo $1 | cut -f2 -d:)
        entry=$(echo "  {\n    \"uuid\": \"$uuid\",\n    \"name\": \"$name\"\n  }\n")

        if grep -Fq "uuid" whitelist.json
        then
            ## at least one player on the whitelist
            sed -i 's/]/,\n'"$entry"']/g' whitelist.json
        else
            ## no player on the whitelist
            sed -i 's/]/\n'"$entry"']/g' whitelist.json
        fi
        
    else
        echo "WHITELIST not set"
    fi
}



## catch the parameters of the script
while test $# -gt 0; do
        case "$1" in
                -h|--help)
                        echo "$Usage : $ sh start.sh [OPTIONS]..."
                        echo " "
                        echo "options:"
                        echo "--------------- server properties ---------------"
                        echo "-h, --help                            show brief help"
                        echo "-d, --difficulty                      set the difficulty of the server"
                        echo "-g, --gamemode                        set the gamemode of the server"
                        echo "--pvp                                 activate/deactivate the pvp between players"
                        echo "--whitelist                           if true, the whitelist file is used"
                        echo "-p, --port                            set the listening port of the server"
                        echo "--onlinemode                          define if the server is in online mode"
                        echo ""
                        echo "----------------------- eula --------------------"
                        echo "--eula                                if set to true, you personnaly agree to the Mojang EULA"
                        echo ""
                        echo "----------------------- ops ---------------------"
                        echo "-o                                    add a player to the ops file"
                        echo ""
                        echo "--------------- whitelist ---------------"
                        echo "-w                                    add a player to the whitelist"
                        exit 0
                        ;;
                -a)
                        shift
                        if test $# -gt 0; then
                                export PROCESS=$1
                        else
                                echo "no process specified"
                                exit 1
                        fi
                        shift
                        ;;
                --action*)
                        export PROCESS=`echo $1 | sed -e 's/^[^=]*=//g'`
                        shift
                        ;;
                -d)
                        shift
                        if test $# -gt 0; then
                                difficulty $1
                        else
                                echo "no argument for the flag -d specified"
                                exit 1
                        fi
                        shift
                        ;;
                --difficulty*)
                        ## TODO check valid argument (not empty)
                        difficulty `echo $1 | sed -e 's/^[^=]*=//g'`
                        shift
                        ;;  
                -g)
                        shift
                        if test $# -gt 0; then
                                gamemode $1
                        else
                                echo "no argument for the flag -g specified"
                                exit 1
                        fi
                        shift
                        ;;
                --gamemode*)
                        ## TODO check valid argument (not empty)
                        gamemode `echo $1 | sed -e 's/^[^=]*=//g'`
                        shift
                        ;;
                --pvp*)
                        ## TODO check valid argument (not empty)
                        pvp `echo $1 | sed -e 's/^[^=]*=//g'`
                        shift
                        ;;                                               
                --whitelist*)
                        ## TODO check valid argument (not empty)
                        whitelistfile `echo $1 | sed -e 's/^[^=]*=//g'`
                        shift
                        ;; 
                -p)
                        shift
                        if test $# -gt 0; then
                                serverport $1
                        else
                                echo "no argument for the flag -g specified"
                                exit 1
                        fi
                        shift
                        ;;
                --onlinemode*)
                        ## TODO check valid argument (not empty)
                        onlinemode `echo $1 | sed -e 's/^[^=]*=//g'`
                        shift
                        ;; 
                --eula*)
                        ## TODO check valid argument (not empty)
                        ## TODO check it is true
                        eula `echo $1 | sed -e 's/^[^=]*=//g'`
                        shift
                        ;; 
                -w)
                        ## TODO check the format *:*
                        shift
                        if test $# -gt 0; then
                                addwhitelist $1
                        else
                                echo "no argument for the flag -g specified"
                                exit 1
                        fi
                        shift
                        ;; 
                -o)
                        ## TODO check the format *:*:*
                        shift
                        if test $# -gt 0; then
                                addops $1
                        else
                                echo "no argument for the flag -g specified"
                                exit 1
                        fi
                        shift
                        ;;                                                                                                                                            
                *)
                        break
                        ;;
        esac
done

java -Xmx512M -Xms512M -jar  /opt/minecraft-server/minecraft-server.jar nogui