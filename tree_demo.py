from __future__ import annotations

# Importa todas as classes definidas no arquivo de design
from tree_design import (
    DecisionNode,
    LeafNode,
    TreeBuilder,
    PreOrderIterator,
    DepthVisitor,
    CountLeavesVisitor,
    Node,
)


def build_mock_tree() -> Node:
    """
    Constrói uma árvore de decisão (mock) para demonstração.

    Estrutura (conceitual):

        Root: feature_1 <= 10
        ├── Left: feature_2 > 5
        │   ├── Left-Left Leaf: class A
        │   └── Left-Right Leaf: class C
        └── Right Leaf: class B
    """

    # Cria o nó raiz (decisão)
    root = DecisionNode("Root: feature_1 <= 10")

    # Cria subárvore da esquerda (decisão + folhas)
    left = DecisionNode("Left: feature_2 > 5")

    # Cria folha da direita da raiz
    right = LeafNode("Right Leaf: class B")

    # Cria folhas filhas de "left"
    left_left = LeafNode("Left-Left Leaf: class A")
    left_right = LeafNode("Left-Right Leaf: class C")

    # Conecta a árvore usando o padrão Composite
    root.add_child(left)
    root.add_child(right)
    left.add_child(left_left)
    left.add_child(left_right)

    print("[Demo] Mock decision tree built")
    return root


def demo_state_pattern(root: Node) -> None:
    """
    Demonstra o uso do padrão State com a classe TreeBuilder.

    Apenas simula a transição entre os estados:
    SplittingState -> StoppingState -> PruningState -> SplittingState ...
    """

    print("\n=== Demo: State pattern with TreeBuilder ===")

    # Cria o TreeBuilder e define o root
    builder = TreeBuilder(root)

    # Chama alguns passos de construção (mock)
    builder.build_step()  # SplittingState
    builder.build_step()  # StoppingState
    builder.build_step()  # PruningState


def demo_iterator_and_visitors(root: Node) -> None:
    """
    Demonstra o uso conjunto de:

    - Iterator (PreOrderIterator) para percorrer a árvore
    - Visitors (CountLeavesVisitor e DepthVisitor) para operações independentes
    """

    print("\n=== Demo: Iterator + Visitor (count leaves) ===")

    # Cria o iterador em pré-ordem
    iterator = PreOrderIterator(root)

    # Cria o visitante que conta folhas
    count_visitor = CountLeavesVisitor()

    # Percorre a árvore com o iterador e visita cada nó
    for node in iterator:
        node.accept(count_visitor)

    print(f"[Demo] Final mock leaf count = {count_visitor.leaf_count}")

    print("\n=== Demo: DepthVisitor (mock depth computation) ===")

    # Cria o visitante que "calcula" profundidade
    depth_visitor = DepthVisitor()
    depth_visitor.compute(root)
    print(f"[Demo] Final mock max depth = {depth_visitor.max_depth}")


def main() -> None:
    """
    Ponto de entrada da demonstração.

    - Constrói a árvore mock
    - Demonstra o padrão State
    - Demonstra Iterator + Visitors
    """
    root = build_mock_tree()
    demo_state_pattern(root)
    demo_iterator_and_visitors(root)


if __name__ == "__main__":
    main()
