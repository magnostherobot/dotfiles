[[ -f ~/.Xresources ]] && xrdb -merge -I$HOME ~/.Xresources

xloadimage -onroot -fullscreen ~/.bg/xmonad-bindings.png
exec xmonad
