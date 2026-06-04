import math


class EvaluatorEngine:

    def __init__(self, aciium_core):
        """
        aciium_core = your Aciium() math backend
        """
        self.ac = aciium_core

    """
    ======================================================
    ERROR CHECKER
    ======================================================
    """

    def is_error(self, value):

        return isinstance(value, str)

    """
    ======================================================
    MAIN ENTRY
    ======================================================
    """

    def evaluate(self, node):
        # -----------------------------
        # NUMBERS
        # -----------------------------
        if isinstance(node, (int, float)):
            return node

        if isinstance(node, str):
            try:
                return float(node)
            except:
                return 0

        node_type = node.get("type")

        # -----------------------------
        # ADDITION
        # -----------------------------

        if node_type == "add":

            left = self.evaluate(node["left"])
            right = self.evaluate(node["right"])

            if self.is_error(left):
                return left

            if self.is_error(right):
                return right

            return left + right

        # -----------------------------
        # SUBTRACTION
        # -----------------------------

        if node_type == "sub":

            left = self.evaluate(node["left"])
            right = self.evaluate(node["right"])

            if self.is_error(left):
                return left

            if self.is_error(right):
                return right

            return left - right

        # -----------------------------
        # MULTIPLICATION
        # -----------------------------

        if node_type == "mul":

            left = self.evaluate(node["left"])
            right = self.evaluate(node["right"])

            if self.is_error(left):
                return left

            if self.is_error(right):
                return right

            return left * right

        # -----------------------------
        # DIVISION
        # -----------------------------

        if node_type == "div":

            left = self.evaluate(node["left"])
            right = self.evaluate(node["right"])

            # PROPAGATE ERRORS
            if isinstance(left, str):
                return left

            if isinstance(right, str):
                return right

            # DIVISION BY ZERO
            if right == 0:
                return "Division by zero"

            return left / right

        # -----------------------------
        # REPEATED ADDITION (^)
        # -----------------------------
        
        if node_type == "repeat_add":

            value = self.evaluate(node["value"])
            times = self.evaluate(node["times"])

            if self.is_error(value):
                return value

            if self.is_error(times):
                return times

            return self.ac.repeat_add(
                value,
                int(times)
            )

        # -----------------------------
        # REPEATED MULTIPLICATION (^^)
        # -----------------------------

        if node_type == "repeat_multiply":

            value = self.evaluate(node["value"])
            times = self.evaluate(node["times"])

            if self.is_error(value):
                return value

            if self.is_error(times):
                return times

            return self.ac.repeat_multiply(
                value,
                int(times)
            )

        # -----------------------------
        # RECURSIVE POWER (^^^)
        # -----------------------------
       
        if node_type == "recursive_power":

            base = self.evaluate(node["base"])
            depth = self.evaluate(node["depth"])

            if self.is_error(base):
                return base

            if self.is_error(depth):
                return depth

            return self.ac.recursive_power(
                base,
                int(depth)
            )

        # -----------------------------
        # SQRT
        # -----------------------------
        
        if node_type == "sqrt":

            value = self.evaluate(node["value"])

            if self.is_error(value):
                return value

            return self.ac.sqrt(value)

        # -----------------------------
        # CUBE ROOT
        # -----------------------------
        if node_type == "cbrt":

            value = self.evaluate(node["value"])

            if self.is_error(value):
                return value

            return self.ac.cbrt(value)
        
        # -----------------------------
        # ROOT COLLAPSE
        # -----------------------------
        if node_type == "root_collapse":

            value = self.evaluate(node["value"])
            root = self.evaluate(node["root"])

            if self.is_error(value):
                return value

            if self.is_error(root):
                return root

            return self.ac.root_collapse(
                value,
                root
            )

        # -----------------------------
        # COMPRESSION
        # -----------------------------
        if node_type == "compression":

            value = self.evaluate(node["value"])
            base = self.evaluate(node["base"])

            if self.is_error(value):
                return value

            if self.is_error(base):
                return base

            return self.ac.compression_depth(
                value,
                base
            )

        # -----------------------------
        # SIGMA
        # -----------------------------
        if node_type == "sigma":

            value = self.evaluate(node["value"])

            if self.is_error(value):
                return value

            return self.ac.sigma(
                int(value)
            )

        # -----------------------------
        # PI (FACTORIAL)
        # -----------------------------
        if node_type == "pi":

            value = self.evaluate(node["value"])

            if self.is_error(value):
                return value

            return self.ac.pi_operator(
                int(value)
            )
        
        # -----------------------------
        # LOG
        # -----------------------------
        
        if node_type == "log":

            value = self.evaluate(node["value"])
            base = self.evaluate(node["base"])

            if self.is_error(value):
                return value

            if self.is_error(base):
                return base

            return self.ac.logarithm(
                value,
                base
            )

        # -----------------------------
        # LN
        # -----------------------------
        
        if node_type == "ln":

            value = self.evaluate(node["value"])

            if self.is_error(value):
                return value

            return self.ac.natural_log(value)

        # -----------------------------
        # UNKNOWN
        # -----------------------------
        return f"Unknown node: {node}"

        