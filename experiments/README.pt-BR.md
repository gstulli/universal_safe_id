# Experimentos

🌐 [English](README.md) · **Português (Brasil)**

> ⚠️ **Protótipos de pesquisa.** Nada aqui é software de produção. **Nunca use chaves, documentos ou dados pessoais reais.** Passar em uma verificação daqui não significa que uma chave ou um desenho seja seguro.

Cada experimento responde a **uma pergunta** do whitepaper (seção 16, E1 a E20). O objetivo é obter evidências, inclusive negativas, e não um produto.

## Convenção

Uma pasta por experimento: `E<NN>-<nome-curto>/`. Comece pelo [`_template`](_template/README.pt-BR.md). Cada pasta tem um `README.md` (e `README.pt-BR.md`) com:

1. **Hipótese** e a seção do whitepaper a que se relaciona.
2. **Método** e **critério de sucesso** (definidos *antes* de executar).
3. **Estado:** `planejado`, `em andamento`, `concluído`, `abandonado`.
4. **Resultado:** o que aconteceu, com dados. **Resultados negativos são publicados.**
5. **Como reproduzir.**
6. **Limitações** e o que o resultado não mostra.
7. Um aviso de que é um protótipo de pesquisa.

Mantenha os experimentos pequenos (uma a duas semanas de trabalho), descartáveis e atrás de interfaces simples, para que um resultado possa mudar o desenho sem reescrever tudo. Cite e dê crédito ao trabalho existente que reaproveitar (seção 5.2 do whitepaper).

## Índice

| ID | Experimento | Estado | Pasta |
|---|---|---|---|
| E13 | Perfil de país: Brasil (pesquisa, sem código) | em andamento | [docs/research/E13-brazilian-documents.pt-BR.md](../docs/research/E13-brazilian-documents.pt-BR.md) |
| E17 | Qualidade de chaves: verificador de chaves fracas (primeiro protótipo) | em andamento | [E17-weak-key-linter](E17-weak-key-linter/README.pt-BR.md) |

A lista completa, com hipóteses e critérios de sucesso, está na seção 16 do whitepaper. Cada experimento tem uma issue com o rótulo `experiment`.
