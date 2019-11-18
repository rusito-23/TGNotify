#!/bin/zsh
source $HOME/.shell_config/src/dirs.zsh
source $ASSETS_DIR/colours.zsh

install()
{
    echo "${BGreen}Installing $1 ${Color_Off}"

    echo "alias $1='python3.7 ${CUSTOM_SCRIPTS_DIR}/src/$1.py'" >> $CUSTOM_SCRIPTS_DIR/aliases.zsh
}

installCustomBins() {
    pip3 install -r ~/.shell_config/scripts/custom/requirements.txt --user

    # create new alias file
    rm $CUSTOM_SCRIPTS_DIR/aliases.zsh
    touch $CUSTOM_SCRIPTS_DIR/aliases.zsh

    install twinotify
    install gnotify
    install netnotify
    install tgnotify
    install tgnetnotify
    install whanotify
    install netwhanotify

    echo "source $CUSTOM_SCRIPTS_DIR/aliases.zsh" >> $HOME/.zshrc
}

installCustomBins
