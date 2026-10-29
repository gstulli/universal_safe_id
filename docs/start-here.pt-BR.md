# Por onde começar

🌐 [English](start-here.md) · **Português (Brasil)**

O Universal Safe ID (USI) é uma proposta **em fase de pesquisa** de infraestrutura de identidade aberta, sem fins lucrativos e sem dono. Ainda não há produto, e quase tudo é hipótese. Esta página ajuda você a achar uma forma útil de entrar, no tempo que tiver.

## Leia, nesta ordem

1. O [README](../README.pt-BR.md): o que o projeto propõe e o que o diferencia (10 minutos).
2. O [whitepaper](whitepaper.pt-BR.md): seções **1 a 3** (objetivos), **5** (iniciativas relacionadas e o que não abrimos mão), **9** (unicidade) e **10** (recuperação). O resto pode esperar (45 minutos).
3. A seção **18** (questões em aberto) e a seção **16** (experimentos): é onde mais precisamos de ajuda.

Cada seção é marcada como 🟢 proposta, 🟡 hipótese ou 🔴 em aberto. Trate 🟡 e 🔴 como convites para discordar.

## De quem precisamos

| Se você é... | Você poderia... |
|---|---|
| Criptógrafo ou engenheiro de segurança | Revisar o modelo de ameaças (seção 4), o desenho de chaves e recuperação (seções 7 e 10), as verificações de chaves fracas (seção 23) e o plano pós-quântico (seção 24). Revisar os [experimentos](../experiments/README.pt-BR.md). |
| Engenheiro de sistemas distribuídos | Comparar as opções de registro A, B e C (seção 8, experimento E1). |
| Pesquisador de identidade, grafos ou fraude | Assumir E2, E3 ou E15 (resistência a contas falsas, calibração de níveis, modelo de confiança). |
| Advogado ou especialista em proteção de dados | Revisar as seções 11.6, 21 e 22 (LGPD, assinaturas, cartórios). Pareceres são o principal gargalo da estratégia jurídica. |
| Designer ou pesquisador de UX | Assumir E6 (pessoas leigas conseguem configurar a recuperação?). |
| Alguém de uma iniciativa da área | Dizer o que erramos sobre o seu projeto (seção 5.1) e onde podemos colaborar. |
| Desenvolvedor | Pegar uma issue `experiment` com o rótulo `good first issue` ou revisar um protótipo. |
| Tradutor | Revisar as versões em inglês e português e acrescentar outros idiomas. |
| Qualquer pessoa | Ler o whitepaper de forma crítica e abrir uma issue de *Retorno sobre o whitepaper*. |

## Formas de ajudar em 30 minutos

- Conferir uma afirmação da seção 5.1 no site do próprio projeto e relatar correções.
- Ler uma questão em aberto e comentar com uma referência ou uma objeção.
- Revisar o texto de uma seção no seu idioma.
- Sugerir um nome melhor para algo confuso.

## Como o trabalho está organizado

- As **issues** têm rótulos de tipo (`experiment`, `open-question`, `needs-verification`, `question`), de área (`area:crypto`, `area:legal`, `area:ux`, `area:governance`, `area:research`, `area:docs`) e de dificuldade (`good first issue`, `help wanted`).
- Os **experimentos** seguem uma convenção: uma hipótese, um critério de sucesso e um resultado publicado, inclusive os negativos ([experiments/README.pt-BR.md](../experiments/README.pt-BR.md)).
- As **mudanças de desenho** passam por uma [USIP](usips/README.pt-BR.md).
- As **decisões** são registradas publicamente. Ver [CONTRIBUTING.pt-BR.md](../CONTRIBUTING.pt-BR.md).

## Observações

- Isto não é software de produção. Nunca coloque chaves, documentos ou dados pessoais reais em nada daqui.
- Boa parte do texto foi redigida com um assistente de IA e **não** foi revisada por especialistas. O seu ceticismo é o objetivo.
- O projeto é **universal, colaborativo, seguro, sem fins lucrativos e sem dono**, e pretende colaborar com iniciativas similares, não competir com elas.
