# Memória do Projeto

## Contexto

Aplicação acadêmica em Python para organizar contêineres recém-chegados em um pátio logístico. O estado do pátio é representado por uma matriz de 5 linhas por 6 colunas, com 30 posições.

## Decisões de implementação

- ocupacao é a matriz principal: 0 indica posição livre e 1 indica posição ocupada.
- identificacoes é uma matriz paralela que armazena o código do contêiner na mesma coordenada.
- Um clique em posição livre registra chegada; um clique em posição ocupada pede confirmação de saída.
- O total de chegadas é acumulado somente durante a execução atual do programa.
- A interface usa tkinter, ttk, ttk.Style, grid, pack e messagebox.
- O código foi mantido estritamente procedural, com funções e variáveis globais compartilhadas pela interface.

## Restrições pedagógicas

- Não criar classes próprias.
- Evidenciar sequência, seleção e repetição com comentários no código.
- Explicar nos comentários o uso de recursos de alto nível e métodos utilitários.
- Não adicionar recursos fora das regras do cenário.

## Privacidade

Não registrar neste repositório dados de integrantes, matrículas, documentos da instituição, imagens da entrega ou credenciais.
