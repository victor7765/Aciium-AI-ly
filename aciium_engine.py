"""
==========================================================
ACIIUM SYMBOLIC ENGINE v2.0
==========================================================

FULL SYMBOL DEFINITIONS
FULL OPERATOR ENGINE
PATTERN COMPRESSION
SYMBOLIC MATHEMATICS
RECURSIVE OPERATIONS

Author:
Victor + ChatGPT

==========================================================
"""

import math


class Aciium:

    """
    ======================================================
    CORE SYMBOLIC OPERATORS
    ======================================================
    """

    # ----------------------------------------------------
    # +
    # Direct Addition
    # ----------------------------------------------------

    def add(self, a, b):

        return a + b

    # ----------------------------------------------------
    # ^
    # Repeated Addition
    #
    # 5^4
    # = 5+5+5+5
    # ----------------------------------------------------

    def repeat_add(self, value, repetitions):

        return value * repetitions

    # ----------------------------------------------------
    # ⊖
    # Recursive Subtraction
    # ----------------------------------------------------

    def recursive_subtract(
        self,
        start,
        value,
        repetitions
    ):

        return start - (value * repetitions)

    # ----------------------------------------------------
    # *
    # Direct Multiplication
    # ----------------------------------------------------

    def multiply(self, a, b):

        return a * b

    # ----------------------------------------------------
    # ^^
    # Repeated Multiplication
    #
    # 2^^4
    # = 2*2*2*2
    # ----------------------------------------------------

    def repeat_multiply(
        self,
        value,
        repetitions
    ):

        return value ** repetitions

    # ----------------------------------------------------
    # ^^^
    # Recursive Power Compression
    # ----------------------------------------------------

    def recursive_power(self, value, depth):

        result = value

        for _ in range(depth - 1):

            # prevent float overflow BEFORE it happens
            if result > 1e6:
                return 1e12

            result = value ** result

        return result
    # ----------------------------------------------------
    # /
    # Direct Division
    # ----------------------------------------------------

    def divide(self, a, b):

        return a / b

    # ----------------------------------------------------
    # ⊘
    # Recursive Division
    # ----------------------------------------------------

    def recursive_divide(
        self,
        start,
        value,
        repetitions
    ):

        result = start

        for _ in range(repetitions):

            result /= value

        return result

    # ----------------------------------------------------
    # √
    # Square Root
    # ----------------------------------------------------

    def sqrt(self, value):

        return math.sqrt(value)

    # ----------------------------------------------------
    # ∛
    # Cube Root
    # ----------------------------------------------------

    def cbrt(self, value):

        return value ** (1 / 3)

    # ----------------------------------------------------
    # ⌋
    # Root Collapse Operator
    #
    # 256⌋2
    # 27⌋3
    # ----------------------------------------------------

    def root_collapse(
        self,
        value,
        root
    ):

        return value ** (1 / root)

    # ----------------------------------------------------
    # log
    # ----------------------------------------------------

    def logarithm(
        self,
        value,
        base
    ):

        return math.log(value, base)

    # ----------------------------------------------------
    # ln
    # ----------------------------------------------------

    def natural_log(self, value):

        return math.log(value)

    # ----------------------------------------------------
    # ↧
    # Compression Depth
    # ----------------------------------------------------

    def compression_depth(
        self,
        value,
        base
    ):

        return math.log(value, base)

    # ----------------------------------------------------
    # Σ
    # Sequence Summation
    # ----------------------------------------------------

    def sigma(self, n):

        return (n * (n + 1)) / 2

    # ----------------------------------------------------
    # Π
    # Multiplicative Collapse
    # ----------------------------------------------------

    def pi_operator(self, n):

        result = 1

        for i in range(1, n + 1):

            result *= i

        return result

    # ----------------------------------------------------
    # %
    # Modulo
    # ----------------------------------------------------

    def modulo(self, a, b):

        return a % b

    # ----------------------------------------------------
    # ≣
    # Computational Equivalence
    # ----------------------------------------------------

    def equivalent(self, a, b):

        return abs(a - b) < 0.000001

    # ----------------------------------------------------
    # ~=
    # Approximation
    # ----------------------------------------------------

    def approximately_equal(
        self,
        a,
        b,
        tolerance=0.001
    ):

        return abs(a - b) <= tolerance

    # ----------------------------------------------------
    # ∆
    # Transformation
    # ----------------------------------------------------

    def transform(
        self,
        value,
        operation
    ):

        return operation(value)

    # ----------------------------------------------------
    # ⊕
    # Merge Operator
    # ----------------------------------------------------

    def merge(self, a, b):

        return str(a) + str(b)

    # ----------------------------------------------------
    # ↺
    # Recursive Loop
    # ----------------------------------------------------

    def recursive_loop(
        self,
        function,
        iterations
    ):

        result = None

        for _ in range(iterations):

            result = function()

        return result

    # ----------------------------------------------------
    # ∫
    # Integration Approximation
    # ----------------------------------------------------

    def integrate(
        self,
        function,
        start,
        end,
        steps=1000
    ):

        width = (end - start) / steps

        area = 0

        x = start

        for _ in range(steps):

            area += function(x) * width
            x += width

        return area

    # ----------------------------------------------------
    # d/dx
    # Derivative Approximation
    # ----------------------------------------------------

    def derivative(
        self,
        function,
        x,
        h=0.0001
    ):

        return (
            function(x + h)
            - function(x)
        ) / h

    # ----------------------------------------------------
    # ⟦ ⟧
    # Execution Scope
    # ----------------------------------------------------

    def scope(self, expression):

        return expression

    # ----------------------------------------------------
    # ⊗
    # Matrix Merge
    # ----------------------------------------------------

    def matrix_merge(
        self,
        matrix_a,
        matrix_b
    ):

        result = []

        for row_a, row_b in zip(matrix_a, matrix_b):

            result.append(row_a + row_b)

        return result

    # ----------------------------------------------------
    # echo
    # ----------------------------------------------------

    def echo(self, value):

        print(value)

    # ----------------------------------------------------
    # sync
    # ----------------------------------------------------

    def sync(self, patron):

        print(
            f"[SYSTEM] Syncing with Patron {patron}"
        )

    # ----------------------------------------------------
    # invoke
    # ----------------------------------------------------

    def invoke(self, gate):

        print(
            f"[SYSTEM] Invoking Hell Gate {gate}"
        )

    # ----------------------------------------------------
    # administrator.access
    # ----------------------------------------------------

    def administrator_access(self):

        print(
            "[SYSTEM] Administrator Access Granted"
        )


"""
==========================================================
TEST ENGINE
==========================================================
"""

if __name__ == "__main__":

    ac = Aciium()

    print("\n================================")
    print("ACIIUM SYMBOLIC ENGINE v2.0")
    print("================================")

    # ----------------------------------------------
    # ADDITION
    # ----------------------------------------------

    print("\n5 + 3")
    print(ac.add(5, 3))

    # ----------------------------------------------
    # REPEATED ADDITION
    # ----------------------------------------------

    print("\n5^4")
    print(ac.repeat_add(5, 4))

    # ----------------------------------------------
    # RECURSIVE SUBTRACTION
    # ----------------------------------------------

    print("\n10 ⊖ 2^3")
    print(
        ac.recursive_subtract(
            10,
            2,
            3
        )
    )

    # ----------------------------------------------
    # MULTIPLICATION
    # ----------------------------------------------

    print("\n4 * 5")
    print(ac.multiply(4, 5))

    # ----------------------------------------------
    # REPEATED MULTIPLICATION
    # ----------------------------------------------

    print("\n2^^4")
    print(
        ac.repeat_multiply(
            2,
            4
        )
    )

    # ----------------------------------------------
    # RECURSIVE POWER
    # ----------------------------------------------

    print("\n2^^^3")
    print(
        ac.recursive_power(
            2,
            3
        )
    )

    # ----------------------------------------------
    # DIVISION
    # ----------------------------------------------

    print("\n20 / 4")
    print(ac.divide(20, 4))

    # ----------------------------------------------
    # RECURSIVE DIVISION
    # ----------------------------------------------

    print("\n64 ⊘ 2^^3")
    print(
        ac.recursive_divide(
            64,
            2,
            3
        )
    )

    # ----------------------------------------------
    # ROOTS
    # ----------------------------------------------

    print("\n√256")
    print(ac.sqrt(256))

    print("\n∛27")
    print(ac.cbrt(27))

    print("\n256⌋2")
    print(
        ac.root_collapse(
            256,
            2
        )
    )

    # ----------------------------------------------
    # LOGARITHMS
    # ----------------------------------------------

    print("\nlog₂(1024)")
    print(
        ac.logarithm(
            1024,
            2
        )
    )

    print("\nln(100)")
    print(ac.natural_log(100))

    # ----------------------------------------------
    # SIGMA
    # ----------------------------------------------

    print("\nΣ5")
    print(ac.sigma(5))

    # ----------------------------------------------
    # PI OPERATOR
    # ----------------------------------------------

    print("\nΠ5")
    print(ac.pi_operator(5))

    # ----------------------------------------------
    # MODULO
    # ----------------------------------------------

    print("\n10 % 3")
    print(ac.modulo(10, 3))

    # ----------------------------------------------
    # EQUIVALENCE
    # ----------------------------------------------

    print("\n2+2 ≣ 4")
    print(
        ac.equivalent(
            2 + 2,
            4
        )
    )

    # ----------------------------------------------
    # APPROXIMATION
    # ----------------------------------------------

    print("\n3.141 ~= 3.14")
    print(
        ac.approximately_equal(
            3.141,
            3.14
        )
    )

    # ----------------------------------------------
    # TRANSFORMATION
    # ----------------------------------------------

    print("\n∆")
    print(
        ac.transform(
            5,
            lambda x: x * 10
        )
    )

    # ----------------------------------------------
    # MERGE
    # ----------------------------------------------

    print("\n⊕")
    print(
        ac.merge(
            "Alex",
            "Vish"
        )
    )

    # ----------------------------------------------
    # DERIVATIVE
    # ----------------------------------------------

    print("\nDerivative of x² at x=3")

    print(
        ac.derivative(
            lambda x: x**2,
            3
        )
    )

    # ----------------------------------------------
    # INTEGRATION
    # ----------------------------------------------

    print("\nIntegral of x² from 0→3")

    print(
        ac.integrate(
            lambda x: x**2,
            0,
            3
        )
    )

    # ----------------------------------------------
    # SYSTEM COMMANDS
    # ----------------------------------------------

    ac.sync("Vishnu")

    ac.invoke(7)

    ac.administrator_access()

    print("\n================================")
    print("ACIIUM EXECUTION COMPLETE")
    print("================================")

