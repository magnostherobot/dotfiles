import XMonad
import XMonad.Hooks.EwmhDesktops

main = xmonad $ ewmh $ def
    { terminal = "urxvtcd"
    , modMask = mod4Mask
    , borderWidth = 0
    }
