class PatternEngine:

    def __init__(self):

        self.pattern_memory = {}

    """
    ======================================================
    DETECT PATTERNS FROM AST
    ======================================================
    """

    def detect(self, node):

        patterns = []

        self._walk(node, patterns)

        print("\n[PATTERN ENGINE]")
        print("Detected Patterns:", patterns)

        return patterns

    """
    ======================================================
    TREE WALKER
    ======================================================
    """

    def _walk(self, node, patterns):

        # NUMBER
        if isinstance(node, (int, float)):
            return

        if not isinstance(node, dict):
            return

        node_type = node.get("type")

        # STORE PATTERN
        patterns.append(node_type)

        # RECURSION DETECTION
        if node_type == "recursive_power":
            patterns.append("deep_recursion")

        # EXPONENTIAL STRUCTURE
        if node_type in [
            "repeat_add",
            "repeat_multiply",
            "recursive_power"
        ]:
            patterns.append("growth_pattern")

        # ROOT STRUCTURE
        if node_type in [
            "sqrt",
            "cbrt",
            "root_collapse"
        ]:
            patterns.append("root_pattern")

        # LOG STRUCTURE
        if node_type in [
            "log",
            "ln"
        ]:
            patterns.append("logarithmic_pattern")

        # FACTORIAL / SIGMA
        if node_type in [
            "pi",
            "sigma"
        ]:
            patterns.append("sequence_pattern")

        # -----------------------------
        # WALK CHILDREN
        # -----------------------------

        for key, value in node.items():

            if isinstance(value, dict):
                self._walk(value, patterns)

            elif isinstance(value, list):

                for item in value:
                    self._walk(item, patterns)