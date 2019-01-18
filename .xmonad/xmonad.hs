import XMonad

main = xmonad defaultConfig
  { modMask = mod4Mask
  , terminal = "urxvtcd"
  , borderWidth = 0
  }
