# 🎯 verifica_coordenadas

> **Utilitário auxiliar para automações de GUI** — descubra as coordenadas exatas de qualquer ponto da tela em tempo real, sem complicação.

---

## 💡 Por que este projeto existe?

Projetos de automação com `pyautogui` — como o **automacao_IR** e o **Automatizador DIMOB** — exigem coordenadas precisas de campos e botões na tela. Descobrir esses valores manualmente é tedioso e impreciso.

O `verifica_coordenadas` resolve isso com uma janela flutuante que exibe, em tempo real e com atualização de 10ms, exatamente onde o seu cursor está. Simples, rápido e sem instalação complexa.

---

## ✨ Funcionalidades

- 📡 **Atualização em tempo real** — coordenadas X e Y atualizadas a cada 10ms
- 🪟 **Janela compacta e flutuante** — não atrapalha o fluxo de trabalho
- 🔒 **Tamanho fixo** — não redimensionável, fica sempre no canto da tela
- ⚡ **Zero configuração** — abre e já funciona

---

## 🛠️ Tecnologias

| Biblioteca | Uso |
|---|---|
| `tkinter` | Interface gráfica nativa do Python |
| `pyautogui` | Captura da posição do cursor |

---

## 🚀 Como usar

### 1. Instale as dependências

```bash
pip install pyautogui
```

> `tkinter` já vem incluído no Python. Nenhuma outra instalação necessária.

### 2. Execute o script

```bash
python verifica_coordenadas.py
```

### 3. Mova o cursor até o campo desejado

Uma janela pequena abrirá exibindo as coordenadas em tempo real:

```
X: 323, Y: 613
```

Anote os valores e use-os nas configurações do seu script de automação.

---

## 🔗 Projetos que usam este utilitário

Este script foi criado como ferramenta de apoio para:

- [automacao_IR](../automacao_IR) — Automação de preenchimento do Imposto de Renda
- [Automatizador DIMOB](../automacao_dimob) — Automação da declaração DIMOB na Receita Federal

---

## 📁 Estrutura

```
verifica_coordenadas/
└── verifica_coordenadas.py   # Script principal
```

---

## 📄 Licença

MIT — use, modifique e distribua à vontade.
