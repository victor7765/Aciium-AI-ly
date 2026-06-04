import random
import time
import math
import json
import os

class SelfTestEngine:

    def __init__(self, ai):

        self.ai = ai

        self.discovered_patterns = []

        self.running = False

        import os

        self.base_dir = os.path.dirname(os.path.abspath(__file__))

        self.file_path = os.path.join(self.base_dir, "patterns.json")

        self.load_patterns()

    """
    ======================================================
    LOAD PATTERNS
    ======================================================
    """

    def load_patterns(self):

        try:
            with open(self.file_path, "r") as file:
                self.discovered_patterns = json.load(file)

            print("[AI] Loaded learned patterns.")

        except:
            self.discovered_patterns = []
            print("[AI] No existing patterns found.")

    """
    ======================================================
    SAVE PATTERNS
    ======================================================
    """

    def save_patterns(self):

        import os

        try:
            print("Saving to:", self.file_path)

            with open(self.file_path, "w") as file:
                json.dump(self.discovered_patterns, file, indent=4)

            print("[AI] Patterns successfully written.")

        except Exception as e:
            print("[AI ERROR] Failed to save patterns:", e)
            
    """
    ======================================================
    GENERATE ADVANCED PROBLEMS
    ======================================================
    """

    def generate_problem(self):

        problem_types = [

            "basic",
            "nested",
            "sqrt",
            "log",
            "aciium_power",
            "recursive",
            "compression",
            "mixed",
            "factorial",
            "summation"
        ]

        selected = random.choice(
            problem_types
        )

        # BASIC

        if selected == "basic":

            a = random.randint(1, 500)
            b = random.randint(1, 500)

            operator = random.choice(
                ["+", "-", "*", "/"]
            )

            if operator == "/":

                b = random.randint(1, 25)

            return f"{a}{operator}{b}"

        # NESTED

        if selected == "nested":

            a = random.randint(1, 50)
            b = random.randint(1, 50)
            c = random.randint(1, 50)

            return f"({a}+{b})*{c}"

        # SQRT

        if selected == "sqrt":

            value = random.choice(
                [
                    16,
                    25,
                    36,
                    49,
                    64,
                    81,
                    100,
                    144,
                    256
                ]
            )

            return f"√{value}"

        # LOG

        if selected == "log":

            powers = [

                (2, 1024),
                (2, 2048),
                (10, 1000),
                (3, 729)
            ]

            base, value = random.choice(
                powers
            )

            return f"log({value},{base})"

        # ACIIUM POWER

        if selected == "aciium_power":

            value = random.randint(2, 6)

            repetitions = random.randint(
                2,
                6
            )

            return f"{value}^^{repetitions}"

        # RECURSIVE POWER

        if selected == "recursive":

            value = random.randint(2, 4)

            depth = random.randint(2, 4)

            return f"{value}^^^{depth}"

        # COMPRESSION

        if selected == "compression":

            base = random.choice(
                [2, 3, 4]
            )

            exponent = random.randint(
                3,
                10
            )

            value = base ** exponent

            return f"{value}↧{base}"

        # MIXED

        if selected == "mixed":

            a = random.randint(2, 10)

            b = random.randint(2, 5)

            return f"({a}^{b})+√64"

        # FACTORIAL

        if selected == "factorial":

            value = random.randint(3, 8)

            return f"Π{value}"

        # SUMMATION

        if selected == "summation":

            value = random.randint(5, 30)

            return f"Σ{value}"

    """
    ======================================================
    RUN TEST
    ======================================================
    """

    def run_test(self):

        expression = self.generate_problem()

        print("\n[SELF TEST]")
        print("Generated Problem:", expression)

        start = time.time()

        result = self.ai.solve_expression(
            expression
        )

        end = time.time()

        runtime = end - start

        print("Solved Result:", result)

        print(
            "Execution Time:",
            runtime
        )

        self.analyze_pattern(
            expression,
            result,
            runtime
        )

    """
    ======================================================
    ANALYZE PATTERNS
    ======================================================
    """

    def analyze_pattern(
        self,
        expression,
        result,
        runtime
    ):

        pattern = {

            "expression": expression,
            "result": str(result),
            "runtime": runtime
        }

        self.discovered_patterns.append(
            pattern
        )

        self.save_patterns()

        print(
            "[AI] Pattern stored permanently."
        )

        # SYMBOL DETECTION

        if "^^^" in expression:

            print(
                "[AI] Recursive power discovered."
            )

        if "^^" in expression:

            print(
                "[AI] Exponential compression detected."
            )

        if "^" in expression:

            print(
                "[AI] Repeated addition pattern detected."
            )

        if "√" in expression:

            print(
                "[AI] Root optimization possible."
            )

        if "Π" in expression:

            print(
                "[AI] Factorial growth structure identified."
            )

        if "Σ" in expression:

            print(
                "[AI] Sequence accumulation pattern found."
            )

        # PERFORMANCE ANALYSIS

        if runtime < 0.0001:

            print(
                "[AI] Ultra-fast symbolic execution."
            )

        elif runtime < 0.001:

            print(
                "[AI] Efficient optimization."
            )

        else:

            print(
                "[AI] Slow execution detected."
            )

    """
    ======================================================
    AUTONOMOUS LEARNING
    ======================================================
    """

    def autonomous_learning(self):

        print("\n================================")
        print("AUTONOMOUS ACIIUM LEARNING")
        print("================================")

        print(
            "\nType CTRL + C to stop learning.\n"
        )

        self.running = True

        cycle = 1

        try:

            while self.running:

                print(f"\nCycle {cycle}")

                self.run_test()

                cycle += 1

                time.sleep(0.5)

        except KeyboardInterrupt:

            print(
                "\n[AI] Learning manually stopped."
            )

            self.running = False

        print("\n================================")
        print("LEARNING SESSION COMPLETE")
        print("================================")

        print(
            "\nTotal Patterns Learned:",
            len(self.discovered_patterns)
        )

    """
    ======================================================
    SHOW LEARNED PATTERNS
    ======================================================
    """

    def show_patterns(self):

        print("\n================================")
        print("LEARNED PATTERNS")
        print("================================")

        for pattern in self.discovered_patterns[-20:]:

            print("\nExpression:",
                  pattern["expression"])

            print("Result:",
                  pattern["result"])

            print("Runtime:",
                  pattern["runtime"])