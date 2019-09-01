import sys

import Main

if __name__ == '__main__':
    if len (sys.argv) >= 1:
        Path = sys.argv[1]

        if not Path.endswith ('.plist'):
            Path += '.plist'

        Instance = Main.Plistr (Path)
        Instance.Run ()
