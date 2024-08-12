
""" ------------------------------------------------------------------------------------------------
Extends Houdini's nodegraph event handling by wrapping the handleEventCoroutine generator from 
$HFS/houdini/pythonX.Ylibs/nodegraph.py. The networkContextDesktop function maps network contexts to 
desktops specified in the editor_desktop_map dictionary.
------------------------------------------------------------------------------------------------ """
import hou, nodegraph
from canvaseventtypes import *

# network context mapping to desktops
editor_desktop_map: dict = {'Object' : 'Build', 
                            'Sop'    : 'Modeling', 
                            'Vop'    : 'Labs', 
                            'Dop'    : 'Technical', 
                            'CopNet' : 'Image'}

def networkContextDesktop(editor, editor_desktop_map):
    current_editor_type = editor.pwd().childTypeCategory().name()
    desktop = hou.ui.curDesktop()
    if current_editor_type in editor_desktop_map.keys() and desktop.name() != editor_desktop_map[current_editor_type]:
        for editor_type, desktop_name in editor_desktop_map.items():
            if current_editor_type == editor_type:
                desktops_dict = dict((d.name(), d) for d in hou.ui.desktops())
                desktops_dict[desktop_name].setAsCurrent()
                break

handleEventCoroutine = nodegraph.handleEventCoroutine
def _handleEventCoroutine(): # wrapper for coroutine
    coroutine = handleEventCoroutine()
    next(coroutine)

    uievent = yield
    editor = uievent.editor
    keep_state = True

    while keep_state:
        uievent = (yield)
        if isinstance(uievent, ContextEvent):
            networkContextDesktop(editor, editor_desktop_map)
        # elif isinstance(uievent, MouseEvent):
        #     ...

        try: coroutine.send(uievent)
        except StopIteration: break

nodegraph.handleEventCoroutine = _handleEventCoroutine
