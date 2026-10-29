# USIPs: Propostas de Melhoria do USI

🌐 [English](README.md) · **Português (Brasil)**

Uma **USIP** é um documento público que propõe uma mudança no desenho, na especificação ou na governança do USI, ou que registra uma decisão importante. Foi inspirada nos BIPs do Bitcoin e nas RFCs da IETF (seção 14.2 do whitepaper).

## Quando escrever uma

- Uma mudança na arquitetura, nos protocolos, nas escolhas criptográficas ou nos níveis de garantia.
- A inclusão de um perfil de país (seção 15.5 do whitepaper).
- Adotar, substituir ou abandonar um componente, ou firmar uma parceria (seções 5.2 e 5.5).
- Uma mudança na governança ou neste processo.

Erros de digitação, esclarecimentos e novas evidências não precisam de USIP: abra uma issue ou um pull request.

## Estados

`Rascunho` → `Em discussão` → `Aceita` ou `Rejeitada` (ou `Retirada`). Uma USIP aceita pode ser `Substituída` depois por outra.

## Processo

1. Discuta a ideia em uma issue antes.
2. Copie o [modelo](usip-template.pt-BR.md) para `usip-NNNN-short-title.pt-BR.md` (próximo número livre) e a versão em inglês para `usip-NNNN-short-title.md` (ou peça ajuda com a tradução), preencha e abra um pull request.
3. A USIP fica `Em discussão` por **pelo menos 14 dias**, publicamente.
4. As objeções devem ser respondidas no documento ou na discussão. Busca-se consenso aproximado, não unanimidade.
5. A pessoa responsável pela manutenção registra o resultado e os motivos. **Esse papel é provisório:** será substituído pela governança descrita na seção 14 do whitepaper (separação de poderes, limites de concentração, supermaioria para regras críticas).
6. Uma mudança que toque uma característica essencial (universal, colaborativo, seguro, sem fins lucrativos, sem dono; seção 5.3 do whitepaper) exige justificativa particularmente forte e discussão mais longa.

## Numeração

`usip-0001`, `usip-0002`, ... na ordem de abertura. `usip-0000` é reservada a este processo.
