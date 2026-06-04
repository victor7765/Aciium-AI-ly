class SymbolEngine:

    def compress(self, node):

        return self._simplify(node)

    """
    ======================================================
    AST SIMPLIFIER
    ======================================================
    """

    def _simplify(self, node):

        # NUMBER
        if isinstance(node, (int, float)):
            return node

        if not isinstance(node, dict):
            return node

        node_type = node.get("type")

        # -----------------------------
        # SIMPLIFY CHILDREN FIRST
        # -----------------------------

        for key, value in node.items():

            if isinstance(value, dict):
                node[key] = self._simplify(value)

        # -----------------------------
        # ADDITION RULES
        # -----------------------------

        if node_type == "add":

            left = node["left"]
            right = node["right"]

            # 0 + x = x
            if left == 0:
                return right

            if right == 0:
                return left

        # -----------------------------
        # MULTIPLICATION RULES
        # -----------------------------

        if node_type == "mul":

            left = node["left"]
            right = node["right"]

            # 1 * x = x
            if left == 1:
                return right

            if right == 1:
                return left

            # 0 * x = 0
            if left == 0 or right == 0:
                return 0

        return node