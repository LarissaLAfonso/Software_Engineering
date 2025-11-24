from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Iterator, Optional


# ===========================
# VISITOR PATTERN - Interface
# ===========================

class Visitor(ABC):
    """
    Interface base para visitantes.

    Cada visitante define o que fazer quando encontra:
    - um DecisionNode
    - um LeafNode

    Isso permite adicionar novas operações sobre a árvore
    sem modificar as classes dos nós (Open/Closed Principle).
    """

    @abstractmethod
    def visit_decision_node(self, node: DecisionNode) -> None:
        ...

    @abstractmethod
    def visit_leaf(self, leaf: LeafNode) -> None:
        ...


# ===========================
# COMPOSITE PATTERN - Component
# ===========================

class Node(ABC):
    """
    Classe base do Composite.

    Representa um nó genérico da árvore (com ou sem filhos).
    DecisionNode e LeafNode herdam desta classe.
    """

    def __init__(self, name: str) -> None:
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    def add_child(self, child: Node) -> None:
        """
        Por padrão, um Node genérico não suporta filhos.
        DecisionNode sobrescreve este método para aceitar filhos.
        """
        raise NotImplementedError(f"Node {self._name} does not support children")

    def get_children(self) -> List[Node]:
        """
        Por padrão, um Node genérico não tem filhos.
        LeafNode usa essa implementação.
        """
        return []

    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        """
        Método usado pelo Visitor.

        Em cada subclasse, chamamos o método apropriado
        do Visitor (visit_decision_node ou visit_leaf).
        """
        ...


# ===========================
# COMPOSITE PATTERN - Composite
# ===========================

class DecisionNode(Node):
    """
    Nó interno (decisão) da árvore.

    Pode ter filhos, representando subárvores.
    """

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._children: List[Node] = []

    def add_child(self, child: Node) -> None:
        print(f"[Composite] Adding child {child.name} to decision node {self.name}")
        self._children.append(child)

    def get_children(self) -> List[Node]:
        return list(self._children)

    def accept(self, visitor: Visitor) -> None:
        """
        Parte do Visitor Pattern: delega para visitor.visit_decision_node.
        """
        print(f"[Visitor] DecisionNode.accept called for {self.name}")
        visitor.visit_decision_node(self)


# ===========================
# COMPOSITE PATTERN - Leaf
# ===========================

class LeafNode(Node):
    """
    Nó folha da árvore.

    Não possui filhos e representa uma classificação / valor final.
    """

    def accept(self, visitor: Visitor) -> None:
        """
        Parte do Visitor Pattern: delega para visitor.visit_leaf.
        """
        print(f"[Visitor] LeafNode.accept called for {self.name}")
        visitor.visit_leaf(self)


# ===========================
# ITERATOR PATTERN
# ===========================

class PreOrderIterator(Iterator[Node]):
    """
    Iterador em pré-ordem (root, filhos da esquerda para a direita, recursivamente).

    Implementa o padrão Iterator para percorrer a árvore
    sem expor a estrutura interna dos nós.
    """

    def __init__(self, root: Node) -> None:
        # Usamos uma pilha para simular a recursão da pré-ordem.
        self._stack: List[Node] = [root]

    def __iter__(self) -> PreOrderIterator:
        return self

    def __next__(self) -> Node:
        if not self._stack:
            raise StopIteration

        # Retira o próximo nó a ser visitado
        node = self._stack.pop()

        # Em pré-ordem: empilha os filhos na ordem inversa,
        # para que o primeiro filho seja visitado primeiro.
        children = list(reversed(node.get_children()))
        if children:
            print(f"[Iterator] Pushing children of {node.name} on stack")
        self._stack.extend(children)

        print(f"[Iterator] Yielding node {node.name}")
        return node


# ===========================
# STATE PATTERN - Interface
# ===========================

class TreeState(ABC):
    """
    Interface para estados do TreeBuilder.

    Cada estado define como tratar um passo de construção da árvore.
    """

    @abstractmethod
    def handle(self, builder: TreeBuilder) -> None:
        ...


# ===========================
# STATE PATTERN - Estados Concretos
# ===========================

class SplittingState(TreeState):
    """
    Estado que simula a fase de "split" (divisão de nós).
    """

    def handle(self, builder: TreeBuilder) -> None:
        print("[State] SplittingState: simulando divisão de nós da árvore")
        # Após dividir, mudamos para o estado de parada (mock)
        builder.set_state(StoppingState())


class StoppingState(TreeState):
    """
    Estado que simula o critério de parada do crescimento da árvore.
    """

    def handle(self, builder: TreeBuilder) -> None:
        print("[State] StoppingState: simulando critério de parada")
        # Após "parar", mudamos para um estado de poda (mock)
        builder.set_state(PruningState())


class PruningState(TreeState):
    """
    Estado que simula a fase de poda da árvore.
    """

    def handle(self, builder: TreeBuilder) -> None:
        print("[State] PruningState: simulando poda da árvore")
        # Após podar, voltamos para o estado de split (mock)
        builder.set_state(SplittingState())


# ===========================
# STATE PATTERN - Context
# ===========================

class TreeBuilder:
    """
    Contexto do padrão State.

    Mantém a referência para o estado atual e delega a ele
    o comportamento de cada 'build_step'.
    """

    def __init__(self, root: Optional[Node] = None) -> None:
        self.root: Optional[Node] = root
        # Estado inicial: SplittingState
        self._state: TreeState = SplittingState()

    def set_root(self, root: Node) -> None:
        print(f"[TreeBuilder] Root set to {root.name}")
        self.root = root

    def set_state(self, state: TreeState) -> None:
        """
        Troca o estado interno do builder.
        """
        print(f"[TreeBuilder] Transitioning to {state.__class__.__name__}")
        self._state = state

    def build_step(self) -> None:
        """
        Executa um passo de construção, delegando o comportamento ao estado atual.
        """
        print(f"[TreeBuilder] build_step using {self._state.__class__.__name__}")
        self._state.handle(self)


# ===========================
# VISITOR CONCRETO - DepthVisitor
# ===========================

class DepthVisitor(Visitor):
    """
    Visitor que "calcula" (mock) a profundidade máxima da árvore.

    Aqui não há cálculo real de profundidade, só prints e atualizações
    de um contador interno para fins de demonstração.
    """

    def __init__(self) -> None:
        self.max_depth: int = 0
        self._current_depth: int = 0

    def _update_depth(self, depth: int) -> None:
        self._current_depth = depth
        if depth > self.max_depth:
            self.max_depth = depth

    def compute(self, root: Node) -> None:
        """
        Percorre a árvore recursivamente, chamando accept em cada nó.
        """
        print("[DepthVisitor] Starting mock depth computation")
        self.max_depth = 0
        self._compute_recursive(root, 0)
        print(f"[DepthVisitor] Finished. Mock max depth = {self.max_depth}")

    def _compute_recursive(self, node: Node, depth: int) -> None:
        self._update_depth(depth)
        node.accept(self)
        for child in node.get_children():
            self._compute_recursive(child, depth + 1)

    def visit_decision_node(self, node: DecisionNode) -> None:
        print(f"[DepthVisitor] Visiting decision node {node.name} at mock depth {self._current_depth}")

    def visit_leaf(self, leaf: LeafNode) -> None:
        print(f"[DepthVisitor] Visiting leaf {leaf.name} at mock depth {self._current_depth}")


# ===========================
# VISITOR CONCRETO - CountLeavesVisitor
# ===========================

class CountLeavesVisitor(Visitor):
    """
    Visitor que conta (mock) quantas folhas existem na árvore.
    """

    def __init__(self) -> None:
        self.leaf_count: int = 0

    def visit_decision_node(self, node: DecisionNode) -> None:
        # Em nó de decisão não alteramos a contagem.
        print(f"[CountLeavesVisitor] Visiting decision node {node.name} (no count change)")

    def visit_leaf(self, leaf: LeafNode) -> None:
        self.leaf_count += 1
        print(f"[CountLeavesVisitor] Visiting leaf {leaf.name}. Mock leaf_count = {self.leaf_count}")
