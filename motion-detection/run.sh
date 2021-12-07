dbus-monitor --session "type='signal',interface='org.gnome.ScreenSaver'" |
  while read x; do
    echo $x
    case "$x" in
      *"boolean true"*) echo SCREEN_LOCKED;;
      *"boolean false"*) echo SCREEN_UNLOCKED;;
    esac
  done
