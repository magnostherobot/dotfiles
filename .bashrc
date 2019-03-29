sourceif () { [ -f "$1" ] && \. "$1"; }

sourceif "/etc/bashrc"

usable () { command -v $1 > /dev/null; }
atpide () { [ -d "$1" ] && export PATH="$1:$PATH"; }

export PS1='[\[\e[34m\]\u@\h \W\[\e[39m\]]\$ '

if [[ -n "$VIM" ]] ; then
    export PS1='[\[\e[31m\]\u@\h \W\[\e[39m\]]\$ '
fi

export LSCOLORS="exgxdxdxcxbxbxcxcxexex"
export LS_COLORS="di=34:ln=36:so=33:pi=33:ex=32:bd=31:cd=31:su=32:sg=32:tw=34:ow=34"
export WWW_HOME='google.co.uk'
export MC_SKIN="$HOME/.mc/solarized.ini"

usable make && export MAKEFLAGS="-j$(nproc)"
usable java && export JAVACMD="java"
usable drip && export JAVACMD="drip"
usable vim  && export EDITOR="vim -e"
usable vim  && export VISUAL="vim"
usable go   && export GOROOT="$HOME/usr/local/go"
usable lynx && export LYNX_LSS="$HOME/.lynx.lss"

atpide "$HOME/.local/bin"
atpide "$HOME/usr/bin"

export PATH="$HOME/usr/bin:$PATH"
export PATH="$HOME/usr/local/bin:$PATH"
usable cabal && export PATH="$HOME/.cabal/bin:$PATH"
usable go    && export PATH="$GOROOT/bin:$PATH"
atpide "$HOME/.nimble/bin"

usable ruby && for d in $HOME/.gem/ruby/*/bin;
  do export PATH="$d:$PATH"; done

set +o ignoreeof

alias ls='ls --color=auto'
alias ll='ls -l'
alias lA='ls -A'
usable cowsay     && alias cowsay=':'
usable vim        && alias vim='vim -O'
usable vim && ! usable view && alias view='vim -R'
usable hub        && alias git='hub'
usable lab        && alias git='lab'
usable acpi       && alias battery='acpi -bi'
usable apacman    && alias pacman='sudo apacman'
usable neomutt    && alias mutt='neomutt'
usable stacscheck && alias sc='stacscheck'
usable tokei      && alias tokei='tokei -c 80'
usable gdb        && alias gdb='gdb -q'
alias java="$JAVACMD"
alias dotfiles="git --git-dir=$HOME/.dotfiles --work-tree=$PWD"

# makes a sym-link to folder "current" in home directory:
set-current () { ln -svfT $(pwd)/$1 $HOME/current; }

# prints something to stderr:
echoerr () { echo "$@" 1>&2; }

# run scripts installed in local npm_modules:
if usable npm; then
  npm-do () { (PATH=$(npm bin):$PATH; eval $@;) }
fi

# loads nvm on first use of node or npm:
NVM_DIR="$HOME/.nvm"
if [ -d "$NVM_DIR" ]; then
  export NVM_DIR
  alias load-nvm='echoerr "Initialising nvm..." && \
    unalias node npm nvm load-nvm npm-do && \. "$NVM_DIR/nvm.sh" \
    [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"'
  alias node='load-nvm && node'
  alias npm='load-nvm && npm'
  alias nvm='load-nvm && nvm'
  alias npm-do='load-nvm && npm-do'
fi

[ -f ~/.fzf.bash ] && source ~/.fzf.bash
if usable fzf && usable ag ; then
  export FZF_DEFAULT_COMMAND='ag --nocolor -g ""'
  export FZF_CTRL_T_COMMAND="$FZF_DEFAULT_COMMAND"
  export FZF_ALT_C_COMMAND="$FZF_DEFAULT_COMMAND"
  export FZF_DEFAULT_OPTS=''
fi
