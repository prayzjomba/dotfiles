# .bashrc

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

PS1='[\u@\h \W]\$ '


export EDITOR=nvim
export HISTCONTROL=ignorespace

eval "$(starship init bash)"

pfetch | lolcat -F 0.8 -S 8 -p 10


# trash
# alias rm='gio trash' # << this will save you some day
# alias lt='gio trash --list'
# alias et='gio trash --empty'
# alias rt='gio trash --restore'


# list
alias l='lsblk | lolcat -F 0.8 -S 8 -p 10'
alias ls='ls --color=auto'

# git
alias gs='git status'
alias gd='git diff'
alias gds='git diff --staged'
alias gl='git log --oneline -5'

