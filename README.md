# Árvore de Decisão Mock - Padrões de Projeto

Este projeto modela uma **árvore de decisão simplificada** usando **padrões de projeto**, sem implementar o algoritmo real de aprendizado.  
Todo o comportamento é **mockado** por meio de `print`s, conforme as restrições do trabalho.

O foco é mostrar, de forma clara, o uso dos seguintes padrões:

- **Composite**
- **Iterator**
- **Visitor**
- **State**

---

## Estrutura do Projeto

`
.
├── tree_design.py                  # Implementação dos padrões de projeto e da estrutura da árvore
├── tree_demo.py                    # Script de demonstração (monta a árvore e executa operações)
├── README.md                       # Arquivo com as descrições e instruções do projeto
└── class_diagram.png               # Diagrama de classes feito usando Mermaid`

## `tree_design.py`

Arquivo principal de design. Aqui ficam todas as classes que modelam a árvore e os padrões de projeto.

### 1. Composite – Estrutura da Árvore

Objetivo: representar a árvore de decisão como uma estrutura hierárquica de nós internos e folhas.

- Node (abstrata)
  Representa um nó genérico da árvore.
  Define a interface comum:
    - `add_child(child: Node)`
    - `get_children() -> List[Node]`
    - `accept(visitor: Visitor)`
  Serve como componente base do padrão Composite.

- DecisionNode(Node)
  Nó interno da árvore (nó de decisão).
  Pode ter vários filhos (`children: List[Node]`).
  Implementa a lógica de:
    - `add_child` (adiciona filhos)
    - `get_children` (retorna a lista de filhos)
  Chama o `Visitor` via `accept`.

- LeafNode(Node)
  Nó folha da árvore. Não possui filhos.
  Representa um resultado final (classe, valor, etc.) de forma mockada.
  Chama o `Visitor` via `accept`.
