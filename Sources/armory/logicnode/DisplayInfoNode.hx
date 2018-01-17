package armory.logicnode;

class DisplayInfoNode extends LogicNode {

	static inline var displayIndex = 0;

	public function new(tree:LogicTree) {
		super(tree);
	}

	override function get(from:Int):Dynamic {
		if (from == 0) return kha.Display.width(displayIndex);
		else return kha.Display.height(displayIndex);
	}
}
