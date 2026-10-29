# Como contribuir com o Universal Safe ID

🌐 [English](CONTRIBUTING.md) · **Português (Brasil)**

Obrigado pelo interesse. O USI é um projeto **em fase de pesquisa, sem fins lucrativos e sem dono**. Neste momento, as contribuições mais valiosas são **crítica, evidências e experimentos**, mais do que código. Se não souber por onde começar, leia [docs/start-here.pt-BR.md](docs/start-here.pt-BR.md).

Ao participar, você concorda em seguir o [Código de Conduta](CODE_OF_CONDUCT.pt-BR.md).

## Formas de contribuir

| Você pode... | Como |
|---|---|
| **Criticar o whitepaper** | Abra uma issue com o formulário *Retorno sobre o whitepaper*. Indique a seção, diga o que está errado ou falta e, se puder, cite uma fonte. |
| **Responder a uma questão em aberto** | Cada questão em aberto da [seção 18](docs/whitepaper.pt-BR.md#18-questões-em-aberto) tem uma issue com o rótulo `open-question`. Comente com ideias, referências ou objeções. |
| **Executar um experimento** | Cada experimento de E1 a E20 tem uma issue com o rótulo `experiment`. Diga que quer assumi-lo e siga a [convenção de experimentos](experiments/README.pt-BR.md). |
| **Verificar fatos** | A seção 5 (iniciativas relacionadas) e as seções jurídicas precisam de fontes primárias. Issues com o rótulo `needs-verification`. |
| **Traduzir e revisar o texto** | Mantenha as versões em inglês e português sincronizadas (ver abaixo). Outros idiomas são bem-vindos. |
| **Revisar código e criptografia** | Revise os protótipos em [experiments/](experiments/). A revisão independente é o que de mais útil uma pessoa especialista pode fazer. |
| **Propor uma mudança no desenho** | Escreva uma USIP (ver [docs/usips/](docs/usips/README.pt-BR.md)). |

## Regras básicas

1. **Apenas protótipos de pesquisa.** Nada aqui é software de produção. Nunca use chaves, documentos ou dados pessoais reais nos protótipos, nem peça a outras pessoas que usem.
2. **Evidência acima de opinião.** Hipóteses são marcadas como tais. Resultados negativos são tão valiosos quanto os positivos e devem ser publicados.
3. **As características essenciais são inegociáveis:** o projeto deve continuar **universal, colaborativo, seguro, sem fins lucrativos e sem dono** (seção 5.3 do whitepaper). Propostas que as contrariem exigem uma USIP e forte justificativa.
4. **Colaborar, não competir** (seção 5.2 do whitepaper). Verifique o que já existe e dê o crédito.
5. **Declare o uso de IA.** Boa parte deste repositório foi redigida com um assistente de IA e **ainda não foi revisada por especialistas**. Se você usou IA em uma contribuição, diga isso no pull request.
6. **Mudanças sensíveis à segurança** (criptografia, manuseio de chaves, recuperação) exigem revisão de pelo menos duas pessoas, uma delas com experiência relevante.

## Pull requests

1. Abra ou comente uma issue antes de qualquer mudança maior que um erro de digitação.
2. Crie uma branch, faça mudanças focadas e abra um pull request usando o modelo.
3. Mantenha os documentos **bilíngues:** cada documento existe em inglês (`nome.md`) e em português do Brasil (`nome.pt-BR.md`). Atualize os dois no mesmo pull request sempre que possível; se só puder escrever em um, diga isso e alguém do projeto ou voluntário traduz. Se houver divergência temporária, a **versão em inglês é a referência**.
4. No whitepaper, acrescente uma linha ao histórico de versões (seção 26) para mudanças significativas.
5. Assine seus commits (`git commit -s`) para confirmar o [Certificado de Origem do Desenvolvedor](https://developercertificate.org/): você escreveu a contribuição ou tem o direito de enviá-la sob as licenças do projeto.

## Licenças

- **Código:** [Apache License 2.0](LICENSE).
- **Documentação** (whitepaper, READMEs e outros textos): [CC BY 4.0](LICENSE-docs).
- As contribuições são aceitas sob as mesmas licenças (*entrada = saída*). **Não há cessão de direitos autorais nem acordo de licença de contribuidor:** as pessoas autoras mantêm os seus direitos, e nenhuma pessoa ou empresa é dona do projeto.

## Decisões

Até o projeto ter participantes suficientes, a pessoa responsável pela manutenção registra as decisões após uma discussão pública de pelo menos 14 dias e as explica na issue ou na USIP. **Esse papel é provisório** e será substituído pela governança descrita na seção 14 do whitepaper.

## Dúvidas

Abra uma issue com o rótulo `question`. Ainda não há um canal privado; um endereço de contato dedicado será publicado quando existir.
