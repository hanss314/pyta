"""
Lambda astroid node

Lambda is a minimal function definition that can be used inside an expression.

Attributes:
    - args    (Arguments)
        - The arguments for function lambda.
    - body    (Node)
        - The body of function lambda. The body should be a single node.
    - locals  (Dict)
        - Contains the variables in the local scope.

Example:
    - args    -> x
    - body    -> 3
    - locals  -> {"args": x, "body": 3}

Type-checking:
    The inferred type is a Callable with arguments inferred from the body of the
    lambda expressions and whose return type is the inferred type of the body.
"""

fun = lambda: 3
fun2 = lambda x, y: x + y
