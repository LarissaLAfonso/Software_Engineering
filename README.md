<div align="center">

# Árvore de Decisão Mock — Demonstração de Padrões de Projeto

Projeto acadêmico em Python que mostra como estruturar uma **árvore de decisão simplificada** apenas com comportamentos mockados (prints) para destacar o uso coordenado de quatro padrões clássicos: **Composite, Iterator, Visitor e State**. Não há treinamento real nem cálculo estatístico; o objetivo é tornar o design e a comunicação entre objetos o mais clara possível.

</div>

---

## Sumário

- [Motivação e Objetivos](#motivação-e-objetivos)
- [Principais Padrões e Responsabilidades](#principais-padrões-e-responsabilidades)
- [Estrutura do Repositório](#estrutura-do-repositório)
- [Fluxo da Demonstração](#fluxo-da-demonstração)
- [Como Executar](#como-executar)
- [Diagrama de Classes](#diagrama-de-classes)

---

## Motivação e Objetivos

1. **Comunicar arquitetura**: mostrar como diferentes padrões podem ser combinados em um único domínio (árvore de decisão).
2. **Separar preocupações**: cada padrão resolve um problema específico (composição, iteração, extensibilidade de operações, mudança de comportamento).
3. **Facilitar apresentações**: por ser totalmente mockado, o código roda em qualquer ambiente com Python ≥ 3.10 e evidencia o fluxo via mensagens no console.

---

## Principais Padrões e Responsabilidades

| Padrão   | Onde vive              | Por que é importante aqui? |
|----------|------------------------|----------------------------|
| Composite | `Node`, `DecisionNode`, `LeafNode` | Modela a árvore como hierarquia de nós reutilizável. |
| Iterator  | `PreOrderIterator`    | Percorre a estrutura sem expor detalhes internos dos nós. |
| Visitor   | `Visitor`, `CountLeavesVisitor`, `DepthVisitor` | Adiciona novas operações (contagem, profundidade) sem tocar na estrutura base. |
| State     | `TreeState` + `SplittingState`, `StoppingState`, `PruningState`, `TreeBuilder` | Simula fases do pipeline de construção da árvore mudando comportamento em tempo de execução. |

Cada classe imprime mensagens prefixadas (`[Composite]`, `[Iterator]`, `[Visitor]`, `[State]`, etc.) para deixar evidente qual padrão está atuando em cada passo, facilitando rastrear o fluxo pela saída do terminal.

---

## Estrutura do Repositório

```
├── tree_design.py      # Todas as classes da árvore e dos padrões
├── tree_demo.py        # Script principal de demonstração
├── class_diagram.png   # Diagrama UML (Composite + State + Visitor)
└── README.md           # Este guia
```

- `tree_design.py`: concentra toda a modelagem. Pode ser importado em outros projetos para reutilizar a estrutura mock.
- `tree_demo.py`: ponto de entrada que constrói uma árvore simples, aciona o `TreeBuilder` (State) e depois percorre a árvore com iterador + visitantes.
- `class_diagram.png`: boa referência visual para apresentação rápida do design antes de olhar o código.

---

## Fluxo da Demonstração

1. **Construção da árvore mock (`build_mock_tree`)**
   - Cria uma raiz `DecisionNode` com duas subárvores.
   - Usa `add_child` para conectar as instâncias, disparando logs do Composite.

2. **Ciclo de estados (`demo_state_pattern`)**
   - Instancia `TreeBuilder`, define o nó raiz e chama `build_step()` três vezes.
   - Os estados `SplittingState → StoppingState → PruningState → SplittingState` são encadeados via `set_state`, evidenciando o padrão State.

3. **Iteração + Visitantes (`demo_iterator_and_visitors`)**
   - `PreOrderIterator` percorre os nós em pré-ordem, emitindo logs de pilha.
   - `CountLeavesVisitor` é aplicado nó a nó para simular contagem de folhas.
   - `DepthVisitor` executa um percurso recursivo próprio (`compute`) e mantém um contador mock de profundidade máxima.

O script `main()` apenas orquestra essas etapas em sequência, o que permite usar o projeto tanto para demonstrações em aula quanto para testes locais rápidos.

---

## Como Executar

1. **Pré-requisitos**
   - Python 3.10+ (nenhuma dependência externa).

2. **Clonar ou baixar o repositório**
   ```bash
   git clone https://github.com/LarissaLAfonso/Software_Engineering.git
   cd Software_Engineering
   ```

3. **Executar a demonstração**
   ```bash
   python tree_demo.py
   ```

4. **Esperar a saída**
   - O terminal exibirá mensagens organizadas pelos prefixos dos padrões, ajudando a relacionar cada trecho de código ao conceito teórico correspondente.

---

## Diagrama de Classes

O arquivo `class_diagram.png` resume graficamente, usando a sintaxe Mermaid:

- a hierarquia `Node` (Composite),
- os visitantes conectados à interface `Visitor`,
- o contexto `TreeBuilder` alternando entre os diferentes estados.

Sugiro abrir o diagrama antes da execução para contextualizar nomes de classes e responsabilidades.


