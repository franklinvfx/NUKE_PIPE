#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Viewer Input
#
#----------------------------------------------------------------------------------------------------------

from menu import path

ypos = float('-inf')
xpos = float('inf')

existingBackdrop = None
existingNode = None

classes = ['VIEWER_INPUT', 'Scanline_Ctrl1', 'Volet', 'Disable_Ctrl1', 'Controller']

for node in nuke.allNodes():
    if node.Class() == 'BackdropNode' and 'isAController' in node.knobs():
        existingBackdrop = node

    if node.ypos() > ypos and node.name() not in classes:
        ypos = node.ypos()
        xpos = node.xpos()

    for knob in node.allKnobs():
        if 'cgevviewerinput' in knob.name():
            existingNode = node

if existingBackdrop is None:
    existingBackdrop = nuke.nodes.BackdropNode(name='Controller', label='<center>Controller</center>')
    existingBackdrop.setXYpos(xpos+500, ypos+300)
    existingBackdrop.knob('label').setValue('<center>Controller</center>')
    existingBackdrop.knob('tile_color').setValue(2350981119L)
    existingBackdrop.knob('note_font_size').setValue(30)

    knob = nuke.Boolean_Knob('isAController', 'isAController', True)
    knob.setVisible(False)
    existingBackdrop.addKnob(knob)
    existingBackdrop.knob('bdwidth').setValue(445)
    existingBackdrop.knob('bdheight').setValue(150)

if existingNode is None:
    existingNode = nuke.nodePaste(path + '/Gizmos/Franklin/VIEWER_INPUT.gizmo')
    knob = nuke.Boolean_Knob('cgevviewerinput', 'cgevviewerinput', True)
    knob.setVisible(False)

    existingNode.addKnob(knob)

existingNode.setXYpos(existingBackdrop.xpos()+50, existingBackdrop.ypos()+85)
existingNode.selectOnly()
existingNode.showControlPanel()
nuke.activeViewer().node().knob('input_process_node').setValue(existingNode.name())