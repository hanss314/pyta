"""
Assign astroid node

An assignment.

Attributes:
    - targets  (List[Name | Tuple[Name]])
        - A list of nodes.
    - value    (Node)
        - A single node.

Example 1:
    - targets  -> [Name(id='x', ctx=Store())]
    - value    -> Num(n=3)

Example 2:
    - targets  -> [Name(id='a', ctx=Store()),Name(id='b', ctx=Store())]
    - value    -> Num(n=1)

Example 3:
    - targets  -> [Tuple(elts=[Name(id='a', ctx=Store()),
                  Name(id='b', ctx=Store())]
    - value    -> Name(id='c', ctx=Load())

Type-checking:
    - Single identifiers are associated with the type of the expression on the RHS of the =.
    - For (unpacking) tuple assignment, the RHS must be an iterable of the same length as
      the number of identifiers on the LHS.
"""

# Example 1
x = 3

# Example 2
a = b = 1

# Example 3
a, b = c
