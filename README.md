# Controle de Contêineres

Projeto acadêmico de Programação 2 para aplicar lógica estruturada/procedural, matrizes e interface gráfica em Python.

## Proposta

O programa representa um pátio logístico por uma matriz de 5 linhas e 6 colunas. Cada uma das 30 posições tem um estado:

- `0`: posição livre;
- `1`: posição ocupada.

Ao informar uma identificação e clicar em uma posição livre, o sistema registra a chegada do contêiner. Ao clicar em uma posição ocupada, solicita confirmação e registra a saída. Os totais são atualizados após cada operação e um resumo é exibido antes de encerrar.

## Requisitos atendidos

- Python com `tkinter` e `tkinter.ttk`;
- estilo nativo configurado com `ttk.Style`;
- paradigma procedural, sem classes próprias;
- matriz 5 x 6 como fonte de verdade do estado do pátio;
- validações por `messagebox`;
- layout organizado com `grid` e `pack`;
- comentários pedagógicos no código para estruturas de controle e recursos de alto nível.

## Como executar

O projeto não requer bibliotecas externas.

```powershell
git clone https://github.com/roberttavelino/checkpoint-conteineres.git
cd checkpoint-conteineres
py main.py
```

Também é possível executar com `python main.py` quando esse comando apontar para uma instalação do Python 3 com Tkinter.

## Estrutura

```text
checkpoint-conteineres/
├── MEMORY.md
├── ROADMAP.md
├── README.md
├── main.py
└── ia/
    └── Prompt Python.md
```

O arquivo `REGRA_DE_NEGOCIO.md` complementa a documentação com os fluxos Dado Quando Então usados pelo projeto.

## Privacidade

Esta versão pública não inclui nomes de integrantes, matrículas, documentos institucionais, capturas de tela, senhas, tokens ou chaves de API.

## Verificação técnica

Antes de cada entrega, execute:

```powershell
python -m py_compile main.py
```

Esse comando verifica a sintaxe do arquivo. A interface deve ser aberta em um ambiente gráfico para testar manualmente os cliques e as caixas de diálogo.
