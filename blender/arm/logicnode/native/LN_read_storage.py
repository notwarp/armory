from arm.logicnode.arm_nodes import *

class ReadStorageNode(ArmLogicTreeNode):
    """Reads a stored content.

    @seeNode Write Storage"""
    bl_idname = 'LNReadStorageNode'
    bl_label = 'Read Storage'
    arm_section = 'file'
    arm_version = 1

    def init(self, context):
        super(ReadStorageNode, self).init(context)
        self.add_input('NodeSocketString', 'Key')
        self.add_input('NodeSocketString', 'Default')

        self.add_output('NodeSocketShader', 'Value')
