from ..lib2to3 import fixer_base, pytree


class FixClassDecorators(fixer_base.BaseFix):
    """Removes class decorators.

    Example::

        @foo
        @bar
        class C(object):
            pass

    This will become::

        class C(object):
            pass
        C = bar(c)
        C = foo(c)

    """

    PATTERN = """
    decorated< ( decorator | decorators ) classdef >
    """

    BM_compatible = True

    def transform(self, node, results):
        """Transform the decorated class into assignments."""

        node = results['node']

        class_node = node.children[1].clone()

        if node.children[0].type == 275:  # 275, 'decorator'
            decorators = [node.children[0].clone()]
        else:  # 276, 'decorators'
            decorators = [node.clone() for node in node.children[0].children]

        class_name = class_node.children[1]

        children = [class_node]
        for decorator_node in reversed(decorators):
            del decorator_node.children[0]  # remove '@'
            decorator_node.children.insert(0,
                pytree.Leaf(1, class_name.value),
            )
            decorator_node.children.insert(1,
                pytree.Leaf(5, ' '),
            )
            decorator_node.children.insert(2,
                pytree.Leaf(22, '='),
            )
            decorator_node.children.insert(3,
                pytree.Leaf(5, ' '),
            )
            decorator_node.children.insert(-1,
                pytree.Leaf(7, '('),
            )
            decorator_node.children.insert(-1,
                pytree.Leaf(2, class_name.value),
            )
            decorator_node.children.insert(-1,
                pytree.Leaf(8, ')'),
            )
            children.append(decorator_node)

        return pytree.Node(node.type, children)
