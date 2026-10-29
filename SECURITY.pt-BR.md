# Política de segurança

🌐 [English](SECURITY.md) · **Português (Brasil)**

## Situação do projeto

O Universal Safe ID está em **fase de pesquisa**. Tudo neste repositório (documentos e protótipos) é **experimental**:

- **Não use** nenhum código daqui para proteger chaves, documentos ou dados pessoais reais.
- **Não envie** dados pessoais reais, chaves privadas reais ou credenciais reais a este repositório, em issues, pull requests ou discussões. Se isso acontecer por engano, avise para que seja removido.
- Passar em uma verificação de um protótipo (por exemplo, a verificação de chaves fracas) **não significa** que uma chave ou um desenho seja seguro.

## Como relatar uma vulnerabilidade

Recebemos com gratidão relatos de problemas de segurança nos **protótipos** e de fragilidades no **desenho** descrito no whitepaper.

1. **Preferencial:** use o relato privado de vulnerabilidades do GitHub (aba *Security* do repositório, *Report a vulnerability*), se estiver habilitado.
2. Se o relato privado não estiver disponível, abra uma issue pública com o rótulo `security` descrevendo **apenas a área e o impacto**, sem detalhes de exploração, e peça um canal privado. Um endereço de contato dedicado será publicado quando existir.

Inclua: o que é afetado, como reproduzir, o impacto esperado e uma sugestão de correção, se houver.

## O que esperar

- Confirmação do recebimento, no melhor esforço (o projeto é mantido hoje por voluntários).
- Divulgação coordenada: sugerimos uma janela de **90 dias** antes de divulgar detalhes, ajustável por acordo.
- Crédito na correção ou no aviso, se você quiser.

## Escopo

No escopo: código em `experiments/` e falhas nos protocolos, procedimentos e escolhas criptográficas do whitepaper.
Fora do escopo: vulnerabilidades em projetos de terceiros (relate às pessoas responsáveis por eles) e engenharia social contra participantes do projeto.

Fragilidades de desenho que não sejam urgentes (por exemplo, um ataque melhor contra uma hipótese) são melhor tratadas em uma issue pública com o rótulo `open-question` ou `whitepaper-feedback`, para que a comunidade possa discuti-las.
