from parser_engine import ParserEngine
from symbol_engine import SymbolEngine
from pattern_engine import PatternEngine
from benchmark_engine import BenchmarkEngine
from knowledge_base import KnowledgeBase
from aciium_engine import Aciium
from self_test_engine import SelfTestEngine
from evaluator_engine import EvaluatorEngine



class AciiumAI:

    def __init__(self):

        self.parser = ParserEngine()
        self.symbols = SymbolEngine()
        self.patterns = PatternEngine()
        self.benchmark = BenchmarkEngine()
        self.kb = KnowledgeBase()

        self.ac = Aciium()

        # SELF TEST ENGINE
        self.self_test = SelfTestEngine(self)
        self.evaluator = EvaluatorEngine(self.ac)

    def divider(self):

        print("\n====================================")

    """
    ======================================================
    SOLVER
    ======================================================
    """

    def solve_expression(self, expression):

        expression = expression.strip()
        expression = expression.replace("(", "").replace(")", "")

        # -------------------------------------------------
        # REPEATED ADDITION
        # Example:
        # 5^4
        # -------------------------------------------------

        if "^" in expression and "^^" not in expression:

            parts = expression.split("^", 1)

            try:
                value = float(parts[0])
                repetitions = int(float(parts[1]))
            except:
                return "Invalid ^ expression"

            return self.ac.repeat_add(value, repetitions)

        # -------------------------------------------------
        # REPEATED MULTIPLICATION
        # Example:
        # 2^^4
        # -------------------------------------------------

        if "^^" in expression and "^^^" not in expression:

            parts = expression.split("^^", 1)

            try:
                value = float(parts[0].strip())
                repetitions = int(float(parts[1].strip()))
            except:
                return "Invalid ^^ expression"

            return self.ac.repeat_multiply(
                value,
                repetitions
            )

        # -------------------------------------------------
        # RECURSIVE POWER
        # Example:
        # 2^^^3
        # -------------------------------------------------

        if "^^^" in expression:

            parts = expression.split("^^^", 1)

            try:
                value = float(parts[0].strip())
                depth = int(float(parts[1].strip()))
            except:
                return "Invalid ^^^ expression"

            return self.ac.recursive_power(value, depth)

        # -------------------------------------------------
        # ROOT COLLAPSE
        # Example:
        # 256⌋2
        # -------------------------------------------------

        if "⌋" in expression:

            parts = expression.split("⌋", 1)

            try:
                value = float(parts[0].strip())
                root = float(parts[1].strip())
            except:
                return "Invalid root expression"

            return self.ac.root_collapse(value, root)

        # -------------------------------------------------
        # COMPRESSION DEPTH
        # Example:
        # 1024↧2
        # -------------------------------------------------

        if "↧" in expression:

            parts = expression.split("↧", 1)

            try:
                value = float(parts[0].strip())
                base = float(parts[1].strip())
            except:
                return "Invalid compression expression"

            return self.ac.compression_depth(value, base)

        # -------------------------------------------------
        # SIGMA
        # Example:
        # Σ5
        # -------------------------------------------------

        if expression.startswith("Σ"):

            value = int(
                expression.replace("Σ", "")
            )

            return self.ac.sigma(value)

        # -------------------------------------------------
        # PI OPERATOR
        # Example:
        # Π5
        # -------------------------------------------------

        if expression.startswith("Π"):

            value = int(
                expression.replace("Π", "")
            )

            return self.ac.pi_operator(value)

        # -------------------------------------------------
        # SQRT
        # Example:
        # √256
        # -------------------------------------------------

        if expression.startswith("√"):

            value = float(
                expression.replace("√", "")
            )

            return self.ac.sqrt(value)

        # -------------------------------------------------
        # CBRT
        # Example:
        # ∛27
        # -------------------------------------------------

        if expression.startswith("∛"):

            value = float(
                expression.replace("∛", "")
            )

            return self.ac.cbrt(value)

        # -------------------------------------------------
        # LOG
        # Example:
        # log(1024,2)
        # -------------------------------------------------

        if expression.startswith("log"):

            try:
                inner = expression.replace("log", "").replace("(", "").replace(")", "")

                if "," not in inner:
                    return "Invalid log format"

                value, base = inner.split(",")

                return self.ac.logarithm(float(value), float(base))

            except:
                return "Invalid log expression"

        # -------------------------------------------------
        # LN
        # Example:
        # ln(100)
        # -------------------------------------------------

        if expression.startswith("ln"):

            inner = expression.replace(
                "ln(",
                ""
            ).replace(
                ")",
                ""
            )

            value = float(inner)

            return self.ac.natural_log(value)

        # -------------------------------------------------
        # NORMAL PYTHON MATH
        # -------------------------------------------------

        try:

            return eval(expression)

        except:

            return "Unknown Expression"

    """
    ======================================================
    MAIN LOOP
    ======================================================
    """

    def run(self):

        self.divider()
        print("ACIIUM AI ENGINE v3.0")
        self.divider()

        print("\nSupported Operators:")
        print("+     Addition")
        print("-     Subtraction")
        print("*     Multiplication")
        print("/     Division")
        print("^     Repeated Addition")
        print("^^    Repeated Multiplication")
        print("^^^   Recursive Power")
        print("√     Square Root")
        print("∛     Cube Root")
        print("⌋     Root Collapse")
        print("↧     Compression Depth")
        print("Σ     Summation")
        print("Π     Factorial")
        print("log   Logarithm")
        print("ln    Natural Log")

        print("\nCommands:")
        print("selftest     -> AI tests itself")
        print("exit         -> Close engine")

        while True:

            user_input = input("\nAciium > ")

            # ---------------------------------------------
            # EXIT
            # ---------------------------------------------

            if user_input.lower() == "exit":

                print("\nClosing Aciium Engine...")
                break

            # ---------------------------------------------
            # SELF TEST MODE
            # ---------------------------------------------

            if user_input.lower() == "selftest":

                self.self_test.autonomous_learning()

                continue

            # ---------------------------------------------
            # STEP 1 — Parse
            # ---------------------------------------------

            tree = self.parser.parse(user_input)

            # ---------------------------------------------
            # STEP 2 — Compression
            # ---------------------------------------------

            compressed = self.symbols.compress(tree)

            # ---------------------------------------------
            # STEP 3 — Pattern Detection
            # ---------------------------------------------

            patterns = self.patterns.detect(tree)

            # ---------------------------------------------
            # STEP 4 — Benchmark
            # ---------------------------------------------

            self.benchmark.compare(
                user_input,
                compressed
            )

            # ---------------------------------------------
            # STEP 5 — Store Knowledge
            # ---------------------------------------------

            self.kb.store(
                user_input,
                compressed
            )

            # ---------------------------------------------
            # STEP 6 — Solve
            # ---------------------------------------------

            tree = self.parser.parse(user_input)
            result = self.evaluator.evaluate(tree)

            print("\nACIIUM OUTPUT >", result)


"""
==========================================================
START ENGINE
==========================================================
"""

if __name__ == "__main__":

    ai = AciiumAI()

    ai.run()
