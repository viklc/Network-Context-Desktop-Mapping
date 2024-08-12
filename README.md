# Network-Context-Desktop-Mapping
Extends Houdinis nodegraph event handling by wrapping the handleEventCoroutine generator from  $HFS/houdini/pythonX.Ylibs/nodegraph.py. The networkContextDesktop function maps network contexts to  desktops specified in the editor_desktop_map dictionary.

The idea came from ajz3d, see: https://www.sidefx.com/forum/topic/97428/

How to install:
Download the folder network_context_desktop (package) and place it in a desired location. The folder contains a json file with the same name as the folder. Open it and set the property: "NETWORKCONTEXTDESKTOP" with the current directory where you have opened the file and save it. Now copy and paste this file under $HOUDINI_USER_PREF_DIR/packages.

Under windows for example: C:\Users\*user\Documents\houdini20.5\packages

Restart Houdini.
