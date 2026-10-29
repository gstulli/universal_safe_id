# Universal Safe ID (USI)

🌐 [English](README.md) · **Português (Brasil)**

**Uma identidade pessoal universal, única, privada e recuperável, construída como bem público, sobre código aberto e um registro público verificável.**

> **Status:** concepção, com a **primeira versão do [whitepaper](docs/whitepaper.pt-BR.md) publicada (v0.2.0)**. O whitepaper detalha o modelo de ameaças, a arquitetura, as alternativas em disputa e um plano de 20 experimentos para decidir entre elas. **É um rascunho aberto à colaboração**: críticas, correções e contribuições são bem-vindas (ver [Como contribuir](#15-como-contribuir)). Nada aqui é definitivo: as propostas são hipóteses a serem testadas, medidas e ajustadas à medida que o projeto amadurece.

**Documentos:**

| Documento | Português | English |
|---|---|---|
| Visão geral do projeto | [README.pt-BR.md](README.pt-BR.md) | [README.md](README.md) |
| Whitepaper v0.2.0 | [docs/whitepaper.pt-BR.md](docs/whitepaper.pt-BR.md) | [docs/whitepaper.md](docs/whitepaper.md) |

---

## Sumário

1. [O problema](#1-o-problema)
2. [A proposta](#2-a-proposta)
3. [Princípios](#3-princípios)
4. [Diferenciais do USI](#4-diferenciais-do-usi)
5. [Arquitetura proposta](#5-arquitetura-proposta)
6. [Uma pessoa, um USI: o modelo de unicidade](#6-uma-pessoa-um-usi-o-modelo-de-unicidade)
7. [Recuperação de acesso](#7-recuperação-de-acesso)
8. [Privacidade e segurança](#8-privacidade-e-segurança)
9. [Sustentabilidade sem dono e sem lucro](#9-sustentabilidade-sem-dono-e-sem-lucro)
10. [Governança](#10-governança)
11. [Stakeholders](#11-stakeholders)
12. [Casos de uso iniciais](#12-casos-de-uso-iniciais)
13. [Como começar](#13-como-começar)
14. [Questões em aberto](#14-questões-em-aberto)
15. [Como contribuir](#15-como-contribuir)
16. [Glossário](#16-glossário)

---

## 1. O problema

A identificação de pessoas, hoje, depende de dois modelos, e ambos têm falhas sérias.

**Identidade emitida por governos e entidades centralizadas**
- Bilhões de pessoas não têm documento reconhecido: refugiados, apátridas, populações vulneráveis.
- Cada país, órgão e empresa mantém sua própria base, gerando duplicidades, fraudes e vazamentos em massa.
- O cidadão não controla seus dados: não sabe quem os consulta, não escolhe o que revelar e não consegue revogar acessos.
- A identidade não atravessa fronteiras com facilidade e pode ser negada ou cancelada por decisão de uma única autoridade.

**Identidade digital emitida por plataformas privadas** (login com contas de grandes empresas)
- A conta pertence à empresa, não à pessoa, e pode ser bloqueada sem recurso.
- Serve de base para rastreamento e perfilamento comercial.
- Não garante que existe um ser humano real e único por trás da conta.

**Um problema novo e urgente:** com a popularização de agentes de inteligência artificial capazes de imitar pessoas, distinguir um humano real de um robô, e uma pessoa de mil contas falsas, tornou-se essencial para votações, redes sociais, distribuição de benefícios e qualquer espaço que dependa do princípio "uma pessoa, uma voz".

## 2. A proposta

O USI propõe uma infraestrutura aberta e sem dono que permita a qualquer pessoa:

1. **Obter gratuitamente um identificador único e permanente** (o USI), vinculado a ela e a mais ninguém.
2. **Provar que é um ser humano único** sem precisar revelar quem é.
3. **Guardar seus dados pessoais sob seu próprio controle**, compartilhando apenas o necessário, com quem quiser, pelo tempo que quiser.
4. **Nunca perder sua identidade** por esquecer uma senha ou perder um celular.
5. **Ser reconhecida** por serviços, instituições e outras pessoas por meio de padrões abertos e interoperáveis.

O USI não pretende substituir documentos oficiais. Ele pode conviver com eles, aproveitá-los como evidência quando existirem e oferecer uma alternativa a quem não os possui.

### A família USI: pessoas, organizações e assinatura

O projeto tem duas partes que compartilham o mesmo núcleo (registro, chaves, recuperação, transparência, criptografia ágil e governança):
- **USI-P:** identidade da **pessoa humana** (unicidade, atributos, privacidade).
- **USI-O:** identidade de **organizações** (pessoas jurídicas), com atributos, representação e poderes verificáveis. A relação entre a pessoa e a organização, hoje representada pelo e-CPF e pelo e-CNPJ, passa a ser um dado explícito: a pessoa assina, e uma credencial mostra que ela pode agir pela organização, dentro de limites.

Sobre esse núcleo, o USI oferece **assinatura digital de documentos** e **autenticação** em sistemas online, como alternativa transparente à hierarquia de autoridades certificadoras. O valor jurídico depende de lei e de aceitação: a estratégia é coexistir primeiro e buscar reconhecimento depois. Detalhes nas [seções 21 e 22 do whitepaper](docs/whitepaper.pt-BR.md).

### Alcance geográfico: começa no Brasil, pensado sem fronteiras

- O **piloto começará no Brasil**, onde o projeto nasce, onde a legislação e os documentos são conhecidos e onde será formada a primeira rede de parceiros.
- O **desenho não tem fronteiras**: nada no protocolo depende de um país. O que é específico de cada país (documentos aceitos, validadores, aspectos legais) fica em **perfis de país** plugáveis.
- A expansão é **gradual e por adesão**: novos países entram à medida que stakeholders locais (operadores, validadores, emissores, juristas e governos interessados) oferecem suporte à infraestrutura e à operação.
- **Governos podem apoiar, mas não controlam.** Um governo pode, por exemplo, ajudar a qualificar a verificação dos seus próprios documentos, o que reduz duplicidades dentro do país, sem ganhar voz privilegiada, veto ou acesso a dados de titulares (ver [seção 10.3](#103-governos-apoio-sem-controle)).

## 3. Princípios

| # | Princípio | O que significa na prática |
|---|---|---|
| 1 | **Bem público, sem dono** | Nenhuma pessoa, empresa ou governo controla o sistema. O fundador se retira da governança assim que critérios objetivos de descentralização forem atingidos. |
| 2 | **Gratuito para o cidadão** | Criar, manter e recuperar um USI nunca terá custo para a pessoa. |
| 3 | **Sem lucro, sem token** | Não há lucro para fundadores, investidores ou mantenedores. Não haverá criptomoeda própria. Os recursos necessários à operação são transparentes e destinados apenas à infraestrutura. |
| 4 | **Uma pessoa, um USI** | Cada ser humano tem um único identificador. Duplicidades podem ser contestadas e corrigidas. |
| 5 | **Identificador permanente, chaves substituíveis** | O USI não muda; as chaves que o controlam podem ser trocadas, revogadas e recuperadas. |
| 6 | **Nenhum dado pessoal no registro público** | Nem em texto aberto, nem criptografado. O registro guarda apenas chaves públicas, compromissos criptográficos e provas. |
| 7 | **Divulgação mínima** | Revela-se apenas o necessário. Exemplo: provar "sou maior de idade" sem revelar a data de nascimento. |
| 8 | **Robustez por combinação** | Nenhum mecanismo isolado é confiável o suficiente. Unicidade, segurança e recuperação são garantidas por várias camadas independentes operando em conjunto. |
| 9 | **Padrões abertos** | Compatibilidade com padrões reconhecidos (W3C DID, Verifiable Credentials, FIDO2/passkeys), evitando formatos proprietários. |
| 10 | **Inclusão** | O sistema deve funcionar para quem não tem documento, tem pouca familiaridade com tecnologia ou acesso limitado à internet. |
| 11 | **Transparência e auditabilidade** | Código aberto, decisões públicas, contas públicas, registro verificável por qualquer pessoa. |
| 12 | **Evolução baseada em evidências** | Cada mecanismo é tratado como hipótese, testado em ambiente controlado e ajustado com base em dados reais. |
| 13 | **Piloto local, desenho global** | O piloto começa no Brasil, mas nada no sistema pode depender de um país. A expansão é gradual, por adesão de stakeholders de outros países. |
| 14 | **Apoio de governos sem controle** | Governos podem apoiar (por exemplo, qualificando seus documentos), mas não têm voto especial, veto nem acesso a dados dos titulares. |
| 15 | **Atributos únicos e verificáveis** | Cada USI tem um único nome oficial e um único identificador por país, vinculados por compromisso criptográfico. A confiança cresce com a verificação de emissores independentes e cai se o valor for alterado. |
| 16 | **Colaborar, não competir** | O USI busca contribuir com iniciativas similares, interoperar e reaproveitar o que é aberto, sem abrir mão de ser universal, colaborativo, seguro, sem fins lucrativos e sem dono. |
| 17 | **Falha humana impossível por construção** | O sistema gera e valida chaves, senhas e códigos; chaves fracas são rejeitadas; chaves sensíveis só são ativadas após verificação independente. A segurança de terceiros nunca depende do cuidado de uma única pessoa. |
| 18 | **Agilidade criptográfica** | Troca de algoritmos sem trocar de identidade, desde o projeto, inclusive para a computação quântica. |

## 4. Diferenciais do USI

O USI não parte do zero: combina técnicas já testadas em identidade descentralizada, criptografia e infraestrutura pública, buscando evitar os pontos de falha observados em iniciativas anteriores. Seus diferenciais estão na combinação:

1. **Unicidade por múltiplas evidências, não por um único método.** Nem só biometria, nem só documentos oficiais, nem só validação social. Cada pessoa acumula evidências independentes, e a confiança cresce com a diversidade delas (ver [seção 6](#6-uma-pessoa-um-usi-o-modelo-de-unicidade)).

2. **Níveis de garantia escolhidos por quem verifica.** Um fórum online pode aceitar um nível básico; uma distribuição de benefícios pode exigir o nível mais alto. O mesmo USI atende a ambos.

3. **Recuperação em camadas paralelas.** Várias rotas de recuperação operam simultaneamente, com prazos de espera proporcionais à força da evidência e direito de veto pelo titular (ver [seção 7](#7-recuperação-de-acesso)).

4. **Universal, mas não rastreável.** O USI é universal *para o titular*, não para os serviços. Cada serviço enxerga um pseudônimo diferente, derivado do USI, e recebe apenas a prova de que se trata de um humano único. Serviços distintos não conseguem cruzar dados entre si para rastrear a pessoa.

5. **Zero dado pessoal no registro público.** Elimina o conflito entre imutabilidade e o direito à eliminação de dados (LGPD, GDPR) e protege contra a quebra futura da criptografia atual.

6. **Gratuito para o cidadão, sustentado por quem se beneficia.** Sem token especulativo e sem cobrança do titular. A infraestrutura é mantida por instituições interessadas e por quem consome as verificações (ver [seção 9](#9-sustentabilidade-sem-dono-e-sem-lucro)).

7. **Validadores responsáveis.** Quem atesta a identidade de outra pessoa coloca a própria reputação em jogo. Atestar uma conta falsa tem consequência.

8. **Descentralização progressiva e planejada.** Em vez de um sistema "sem dono" desde o primeiro dia, o que tende a gerar vácuo de governança, o USI define fases e critérios objetivos para a transferência de controle à comunidade.

### Colaborar, não competir

O USI **não pretende disputar espaço** com iniciativas similares: o objetivo é comum, que qualquer pessoa possa provar que é um ser humano único e controlar seus próprios dados. Existem projetos de prova de pessoa única, de identidade descentralizada e de padrões abertos, entre eles [Ğ1/Duniter](https://duniter.org/), [Encointer](https://encointer.org/), [BrightID](https://brightid.org/), [Proof of Humanity](https://gov.proofofhumanity.id/t/poh-origin-constitution-v2/3053), a [Decentralized Identity Foundation](https://learnworkecosystemlibrary.com/organizations/decentralized-identity-foundation/) e a [LF Decentralized Trust](https://www.linuxfoundation.org/press/linux-foundation-decentralized-trust-launches-with-17-projects-100-founding-members). O levantamento inicial (incompleto) está na [seção 5 do whitepaper](docs/whitepaper.pt-BR.md).

Nossa postura:
- **Pesquisar antes de construir** e conversar com essas comunidades antes de qualquer protótipo próprio.
- **Contribuir de volta,** **interoperar** por meio de padrões abertos e **reaproveitar** o que é aberto, com crédito.
- **Aceitar a convergência:** se uma iniciativa existente cumprir as características essenciais, o caminho é contribuir com ela, e não duplicar esforços.

O que **não** muda em nenhuma parceria: o USI deve continuar **universal, colaborativo, seguro, sem fins lucrativos e sem dono**. Cada uma dessas características tem um teste prático descrito na seção 5.3 do whitepaper.

## 5. Arquitetura proposta

O sistema é organizado em três camadas independentes. Cada uma pode evoluir sem quebrar as demais.

```
┌──────────────────────────────────────────────────────────────────┐
│  CAMADA 3 – Dados e credenciais (fora do registro público)       │
│  Carteira do titular · credenciais verificáveis · provas ZK      │
├──────────────────────────────────────────────────────────────────┤
│  CAMADA 2 – Unicidade e reputação                                │
│  Evidências · atestações · níveis de garantia · contestações     │
├──────────────────────────────────────────────────────────────────┤
│  CAMADA 1 – Registro público (âncora)                            │
│  USI · chaves públicas · rotações · revogações · nullifiers       │
└──────────────────────────────────────────────────────────────────┘
```

### 5.1 Identificador e chaves

- O USI segue o padrão **W3C DID** (Decentralized Identifier), com um método próprio proposto como `did:usi`.
- O identificador é permanente. As chaves que o controlam são substituíveis.
- **Pré-rotação de chaves** (inspirada no protocolo KERI): ao registrar a chave atual, o titular registra também o *hash* da próxima chave, que fica guardada offline. Mesmo que a chave atual seja roubada, o atacante não consegue tomar o controle definitivo da identidade.
- Suporte a **múltiplos dispositivos** e a **passkeys** (FIDO2), protegidas pelo chip seguro do celular ou por chaves físicas.
- **Criptografia pós-quântica** (como os algoritmos padronizados pelo NIST, a exemplo do ML-DSA) deve ser considerada desde o desenho, com mecanismo de migração de algoritmos previsto.

### 5.2 Registro público

O registro público funciona como **âncora de confiança**: guarda apenas o mínimo necessário para que qualquer pessoa verifique, de forma independente, o estado de um USI.

**O que vai para o registro:** o identificador, as chaves públicas vigentes, o compromisso das próximas chaves, eventos de rotação e revogação, *nullifiers* de unicidade e resumos criptográficos (*hashes*) de atestações.

**O que nunca vai:** nome, documentos, fotos, biometria, endereço, data de nascimento, ou qualquer outro dado pessoal, nem mesmo criptografado.

**Tamanho estimado:** com algumas centenas de bytes por pessoa, um registro com toda a população mundial ficaria na ordem de poucos terabytes. Além disso, os usuários comuns não precisam armazená-lo: usam **clientes leves** que verificam provas compactas. Apenas os nós completos guardam o registro inteiro.

**Opções a serem avaliadas** (a decisão deve vir de provas de conceito):

| Opção | Descrição | A favor | Contra |
|---|---|---|---|
| A. Âncoras em blockchain pública existente | Registrar apenas os eventos em uma rede consolidada (por exemplo, uma camada 2 do Ethereum) | Segurança herdada; sem rede própria para manter | Custo por transação; dependência de terceiros |
| B. Rede federada própria | Dezenas a centenas de operadores institucionais independentes, com consenso tolerante a falhas bizantinas (BFT) e logs auditáveis por qualquer pessoa, no modelo do *Certificate Transparency* | Custo baixo; controle sobre desempenho e regras | Exige atrair e diversificar operadores |
| C. Híbrida | Rede federada para a operação diária, com âncoras periódicas em blockchain pública como garantia adicional de integridade | Combina vantagens de A e B | Maior complexidade |

**Critérios de escolha:** independência, custo para o cidadão (que deve ser zero), durabilidade em décadas, resistência a censura, capacidade de auditoria pública e desempenho.

### 5.3 Dados pessoais e credenciais

- Os dados pessoais ficam na **carteira do titular** (aplicativo no celular), com backup cifrado em local escolhido por ele.
- Informações sobre a pessoa são representadas como **credenciais verificáveis** (W3C Verifiable Credentials) emitidas por quem tem autoridade sobre elas: uma universidade emite o diploma, um órgão emite o documento, um conselho profissional emite o registro.
- **Divulgação seletiva** (SD-JWT, assinaturas BBS+) permite revelar apenas alguns campos de uma credencial.
- **Provas de conhecimento zero** (*zero-knowledge proofs*) permitem provar afirmações sem revelar o dado: "tenho mais de 18 anos", "moro neste município", "sou um humano único neste serviço".
- **Compartilhamento por tempo limitado:** o titular concede acesso a dados com prazo e pode revogá-lo a qualquer momento. Limitação importante, que deve ficar clara ao usuário: só é possível limitar o *acesso contínuo*. Uma informação que já foi vista ou copiada não pode ser "desvista".
- **Registro de consentimentos:** o titular mantém o histórico de quem acessou o quê e quando, visível apenas para ele.

### 5.4 Assinatura, autenticação e autoridades certificadoras

Hoje, a confiança em assinaturas e certificados depende de uma hierarquia de autoridades certificadoras. No modelo do USI, não há hierarquia de emissão de chaves: o identificador é auto-certificado, a confiança nos atributos vem de vários emissores independentes e todos os eventos são públicos e verificáveis, com carimbo de tempo por ancoragem no registro. Um emissor isolado não eleva sozinho a confiança além de um limite, e o dano de uma chave comprometida fica restrito ao que ela atestou.

O USI **não afirma, hoje, valor jurídico equivalente** ao da assinatura qualificada da ICP-Brasil, e **não substitui a fé pública dos cartórios** sem mudança de lei. A estratégia é coexistir (assinatura avançada por aceitação das partes), buscar reconhecimento e, onde a lei permitir, substituir funções técnicas. Ver [seção 22 do whitepaper](docs/whitepaper.pt-BR.md).

### 5.5 Segurança por construção: falhas humanas não podem comprometer terceiros

Reportagens recentes descrevem oito certificados de autoridades intermediárias cujas chaves privadas tinham valores triviais (como 4), apesar do uso de um algoritmo forte. A corrente é tão forte quanto o seu elo mais fraco, e todos os que confiavam na cadeia ficaram expostos. O USI propõe tornar esse tipo de falha **impossível por construção**, e não apenas proibida:

- **O sistema gera e valida as chaves.** A pessoa nunca escolhe nem digita uma chave. Chaves fracas, repetidas ou conhecidas como comprometidas são rejeitadas pelo protocolo. O mesmo vale para frases-senha de backup, PINs e códigos de recuperação.
- **Publicar antes de usar:** chaves sensíveis (de emissores e operadores) ficam publicadas em estado pendente e só são ativadas após verificação independente por monitores públicos.
- **Monitoramento contínuo e prova de comprometimento:** qualquer pessoa que assine com a chave privada de outro USI aciona a revogação automática.
- **Frescor e falha fechada:** verificadores exigem prova atualizada do estado do registro; sem ela, operações sensíveis não são aceitas.
- **Sem hierarquia, com chaves de limiar e limite de poder** por emissor; **transparência obrigatória**; metas de resposta a incidentes; credenciamento revogável.

Isso não torna o USI imune a falhas: nenhum teste prova aleatoriedade, e bugs e engenharia social continuam possíveis. O objetivo é que as falhas sejam mais difíceis, detectadas mais cedo e contidas. Ver [seção 23 do whitepaper](docs/whitepaper.pt-BR.md).

### 5.6 Migração criptográfica e computação quântica

O projeto troca de algoritmos **sem trocar de identidade**. Desde o início: identificadores de algoritmo em todo evento, assinaturas híbridas (clássica e pós-quântica) na transição, pré-rotação de chaves por *hash* (resistente a computadores quânticos), estágios públicos de depreciação com gatilhos definidos, procedimento de emergência e renovação de selos de assinaturas de longa duração. Já existem algoritmos pós-quânticos padronizados, mas com custos maiores e menos tempo de escrutínio, por isso o desenho prevê que até o algoritmo escolhido possa ser trocado. Uma análise identificou também um risco no próprio desenho: a técnica prevista para a unicidade de identificadores não resiste a computadores quânticos e deve ser reavaliada. Ver [seção 24 do whitepaper](docs/whitepaper.pt-BR.md).

## 6. Uma pessoa, um USI: o modelo de unicidade

Garantir que cada pessoa tenha um único registro, com 100% de certeza, é impossível para qualquer sistema, inclusive os governamentais. O objetivo do USI é tornar a fraude **difícil, cara, detectável e reversível**.

### 6.1 Camadas de evidência

Cada USI acumula evidências de categorias diferentes. Nenhuma é obrigatória isoladamente; a força está na combinação.

| Camada | Como funciona | Observações |
|---|---|---|
| **Vínculo social** | Pessoas que já têm USI atestam que conhecem o titular. A confiança não é medida pelo *número* de atestações, mas pela **análise do grafo**: grupos de contas falsas tendem a ter muitas conexões entre si e poucas com a rede honesta. | Atestadores são responsáveis: se atestarem uma conta falsa, perdem reputação. |
| **Prova documental com conhecimento zero** | Para quem tem documento com chip ou assinatura digital (como passaportes com NFC), o titular prova a validade do documento **sem revelá-lo**. O sistema guarda apenas um *nullifier*, valor derivado do documento que impede um segundo cadastro com o mesmo documento, sem permitir descobrir qual é. | Aproveita a unicidade que já existe nos documentos oficiais sem depender operacionalmente dos governos. |
| **Presença física** | Cerimônias de verificação presenciais e simultâneas, organizadas por validadores comunitários ou instituições parceiras (bibliotecas, escolas, ONGs). Uma pessoa não pode estar em dois lugares ao mesmo tempo. | Especialmente importante para quem não tem documentos. |
| **Biometria (opcional, a investigar)** | Comparação biométrica para detectar duplicidade, **somente** se for possível fazê-la sem base centralizada, com técnicas como computação multipartidária ou criptografia homomórfica. | Uso sempre opcional. Só será adotada se resolver os riscos de privacidade de forma comprovada. |
| **Histórico e continuidade** | Tempo de existência do USI, uso consistente, credenciais emitidas por terceiros. | Contas recém-criadas têm naturalmente menos peso. |

### 6.2 Níveis de garantia

As evidências se convertem em **níveis de garantia** públicos e padronizados. Quem verifica escolhe o nível exigido. Exemplo inicial, a ser calibrado:

| Nível | Requisito indicativo | Uso típico |
|---|---|---|
| 1 – Básico | Vínculo social mínimo | Fóruns, comentários, filtros anti-robô |
| 2 – Intermediário | Vínculo social sólido **ou** prova documental | Enquetes, comunidades online, cadastros simples |
| 3 – Alto | Duas camadas de categorias diferentes | Votações comunitárias, doações |
| 4 – Máximo | Três ou mais camadas, incluindo presença física ou prova documental | Distribuição de benefícios, aplicações sensíveis |

### 6.3 Contestação e correção

- **Qualquer pessoa pode contestar** um USI suspeito, apresentando evidências.
- As contestações são julgadas por **júris sorteados** entre titulares de nível alto, com regras públicas e direito de defesa.
- Uma duplicidade confirmada resulta no cancelamento do registro excedente e em perda de reputação para quem o atestou.
- Isso substitui o conceito de "irrevogável" por **permanente, mas corrigível**: o USI legítimo nunca é perdido; o fraudulento pode ser desfeito.

### 6.4 Ciclo de vida

**Criação** → **Acúmulo de evidências** → **Uso** → **Rotação de chaves** → **Recuperação** (se necessário) → **Contestação** (se houver) → **Inatividade ou óbito**

O tratamento de óbito e de inatividade prolongada deve ser definido de modo a impedir o uso indevido de identidades de pessoas falecidas sem expor dados de ninguém.

### 6.5 Vínculo com nome e documentos: uma identidade, um conjunto de atributos

Ter um único USI por pessoa não basta: é preciso também evitar que a mesma pessoa use dois nomes ou dois CPFs e que um terceiro receba informações diferentes das verdadeiras. Como o registro não guarda dados pessoais, o modelo proposto é:

- **Atributos-chave** (nome oficial, data de nascimento, identificador nacional estável de cada país, como o CPF): cada USI tem **um único valor vigente** por tipo. O valor fica na carteira; o registro guarda apenas um compromisso criptográfico. O nome é único *para o USI*, mas não entre pessoas; identificadores do Estado (CPF, passaporte) são únicos entre USIs.
- **Documentos** (passaporte, RG, habilitação): podem ser vários e renovados, mas sempre coerentes com os atributos-chave.
- **Confiança do atributo (C0 a C4):** começa em "declarado" e sobe à medida que **emissores independentes** (bancos que verificam seus clientes, órgãos públicos, outras instituições) verificam e atestam o atributo. Exemplo: João informa nome e CPF; ao abrir conta no Banco A, o banco verifica e atesta; outros bancos repetem o processo; quando a confiança é alta, qualquer contraparte pode aceitar o CPF apresentado como verdadeiro.
- **Alterar um atributo-chave zera a confiança** dele e exige nova validação (o histórico de trocas é preservado). Antes da primeira atestação, o titular pode corrigir erros livremente.
- **Identidade falsa:** quem se registra com nome ou CPF falsos precisa enganar vários emissores independentes e depois fica preso a essa identidade: não pode ter outro USI nem voltar atrás sem perder a confiança.
- **Ocupação de identidade alheia:** vence a evidência mais forte (prova criptográfica do documento original, mais atestações), e não quem chegou primeiro. Disputas vão a júri.
- **Nome social e mudança legal de nome:** são tratados à parte e sempre apresentados com rótulo de tipo. A mudança por ato legal tem caminho próprio, preservando a continuidade do USI e sem expor o nome anterior a terceiros.

- **Unicidade do identificador em fases:** na rede inicial, identificadores como o CPF **não** são expostos no registro, e a possibilidade de duplicidade é aceita e mitigada por outras camadas (mais verificações, detecção pelo emissor, outras evidências de unicidade). Quando a rede for grande e descentralizada, uma técnica criptográfica (OPRF de limiar) será ativada como melhoria prevista.

O USI **não torna uma informação verdadeira**: garante que ela é única e mede o quanto se pode confiar nela. A veracidade é garantida por quem a verifica. Detalhes na [seção 9.7 do whitepaper](docs/whitepaper.pt-BR.md), inclusive a discussão de alternativas descartadas, aberta a novas ideias.

## 7. Recuperação de acesso

Perder o acesso à própria identidade não pode ser definitivo. Ao mesmo tempo, o processo de recuperação é a porta preferida dos atacantes para sequestrar contas. O modelo do USI resolve esse conflito com **várias rotas operando em paralelo**, cada uma com exigências e prazos proporcionais à força da evidência apresentada.

### 7.1 Rotas de recuperação

| Rota | Mecanismo | Prazo de espera indicativo |
|---|---|---|
| **A – Outro dispositivo** | Uma passkey ou chave já registrada em outro aparelho autoriza a nova chave | Imediato |
| **B – Chave pré-rotacionada** | A próxima chave, guardada offline (papel, cofre, chave física), assume o controle | Curto (ex.: 24 a 72 horas) |
| **C – Recuperação social** | Um quórum de **guardiões** escolhidos pelo titular (ex.: 3 de 5 entre família, amigos e instituições) autoriza a nova chave. Pode usar compartilhamento de segredo de Shamir. | Médio (ex.: 7 dias) |
| **D – Revalidação de identidade** | O titular prova novamente que é a mesma pessoa, por meio das camadas de evidência da seção 6 (prova documental, presença física, validadores) | Longo (ex.: 30 dias), **e** exige combinação com outra rota ou com evidência de nível alto |

Os prazos são hipóteses iniciais a serem calibradas em testes.

### 7.2 Regras que valem para todas as rotas

1. **Notificação imediata** de qualquer pedido de recuperação a todos os dispositivos, guardiões e canais registrados.
2. **Direito de veto:** durante o prazo de espera, qualquer chave legítima ainda ativa pode cancelar o pedido. Isso protege contra quem tenta sequestrar a conta.
3. **Rotas mais fortes encurtam o prazo:** combinar rotas (por exemplo, guardiões + revalidação) reduz a espera; usar só uma rota fraca a aumenta.
4. **Congelamento de emergência:** em caso de roubo do celular ou suspeita de invasão, o titular ou um quórum de guardiões pode congelar o USI imediatamente, até a recuperação.
5. **Rotação obrigatória após recuperação:** todas as chaves antigas são revogadas e uma nova chave pré-rotacionada é gerada.
6. **Revisão periódica de guardiões:** o aplicativo lembra o titular de confirmar se seus guardiões continuam disponíveis e confiáveis.

### 7.3 Exemplos

- *Perdi o celular, mas tenho o tablet:* rota A, imediata.
- *Perdi todos os aparelhos, mas guardei o papel de recuperação:* rota B, com espera curta.
- *Perdi tudo:* rota C, com meus guardiões, em cerca de uma semana.
- *Perdi tudo e meus guardiões não estão disponíveis:* rota D, combinada com evidência de nível alto, em cerca de um mês.
- *Alguém roubou meu celular e pediu recuperação:* recebo a notificação em outro canal e veto o pedido; congelo o USI e inicio a recuperação legítima.

### 7.4 Casos extremos: perda total sem preparo e tentativa de abuso

- **Boa-fé, aparelho único, sem backup.** A carteira guarda pouco: o que pode ser refeito a partir do mundo (documentos físicos, atestações dos emissores) não depende do aparelho. Para subir de nível, o titular precisa de ao menos uma **âncora de recuperação** (backup cifrado, folha impressa, guardião pessoal ou institucional). Quem não preparou nada pode recorrer à **revalidação assistida**: emissores que já o conhecem, como bancos, confirmam sua identidade com o próprio cadastro.
- **Má-fé ("perdi tudo, quero recomeçar").** **Recomeçar não cria um USI novo:** quem tem atributos atestados recupera o mesmo USI, e os emissores que já conhecem o vínculo recusam vincular um segundo USI ao mesmo cliente. Quem nunca teve nada atestado pode recomeçar, pois não há o que perder, e o USI antigo expira.
- **Proporcionalidade:** quanto mais confiança acumulada, mais exigente é a recuperação.
- A fase inicial deixa um resíduo (duas identidades de baixa confiança), que só se fecha com a técnica da rede madura.

Nada disso está testado: ver a [seção 10.8 do whitepaper](docs/whitepaper.pt-BR.md) e contribuir.

## 8. Privacidade e segurança

### 8.1 Proteções de privacidade

- Nenhum dado pessoal no registro público.
- **Pseudônimos por serviço:** cada serviço recebe um identificador diferente, derivado do USI, impossibilitando o cruzamento de dados entre serviços.
- **Nullifiers** permitem provar "sou um humano único neste serviço" sem revelar qual é o USI.
- Divulgação mínima e provas de conhecimento zero como padrão, não como exceção.
- Conformidade com a **LGPD** e legislações equivalentes desde a concepção (*privacy by design*).

### 8.2 Ameaças consideradas

| Ameaça | Mitigações previstas |
|---|---|
| Contas falsas em massa (ataque Sybil) | Múltiplas camadas de evidência, análise de grafo, responsabilização de atestadores, contestação |
| Sequestro de conta via recuperação | Prazos de espera, notificação, veto, combinação de rotas |
| Conluio de guardiões | Guardiões de círculos diferentes, prazo de espera, veto do titular |
| Coação (pessoa forçada a revelar dados ou ceder o acesso) | Divulgação mínima, possibilidade de modo de emergência a ser estudado |
| Vigilância e rastreamento | Pseudônimos por serviço, nenhum dado no registro, provas de conhecimento zero |
| Captura da governança | Descentralização progressiva, diversidade geográfica e institucional dos operadores, regras públicas |
| Comprometimento de operadores do registro | Consenso tolerante a falhas, auditoria pública, âncoras externas |
| Avanço da computação quântica | Algoritmos pós-quânticos e mecanismo de migração |
| Exclusão digital | Presença física, guardiões, carteiras simplificadas, operação assistida por instituições |

### 8.3 Auditorias

Componentes criptográficos e de segurança devem passar por **auditorias independentes** antes de qualquer uso real, com resultados publicados.

## 9. Sustentabilidade sem dono e sem lucro

### 9.1 Por que o USI não precisa do modelo do Bitcoin

O Bitcoin paga mineradores porque precisa de consenso entre desconhecidos sobre dinheiro, onde a fraude gera lucro imediato. O USI tem necessidades muito menores: um registro enxuto, que não precisa ser armazenado por cada usuário e pode ser mantido por **algumas centenas de operadores independentes e confiáveis**, em vez de milhões de voluntários. Infraestruturas públicas essenciais da internet, como os servidores raiz de DNS e os logs de *Certificate Transparency*, já funcionam assim, mantidas por instituições que se beneficiam de sua existência.

### 9.2 Custos reais

Mesmo sem lucro, há custos: operação dos nós, desenvolvimento, auditorias de segurança, eventos de verificação presencial, suporte e assessoria jurídica.

### 9.3 Fontes de sustentação a serem testadas

1. **Operadores institucionais que se beneficiam:** empresas que gastam com verificação de identidade e prevenção de fraude, universidades, ONGs, bibliotecas, órgãos públicos. Operar um nó é mais barato do que manter suas próprias bases.
2. **Taxa de verificação paga por quem consome:** serviços que verificam USIs em larga escala podem pagar um valor mínimo por verificação, revertido aos operadores e à manutenção. **O cidadão nunca paga.**
3. **Bolsas, editais e doações** de fundações e programas de apoio a infraestrutura aberta e direitos digitais.
4. **Voluntariado em desenvolvimento,** motivado por propósito, reputação e aprendizado, como em outros grandes projetos de código aberto.

### 9.4 Por que não haverá token

Uma criptomoeda própria criaria incentivo financeiro para fraudar cadastros, atrairia especulação e desviaria o foco do projeto. A experiência de outras iniciativas mostra que tokens associados a identidade tendem a gerar compra e venda de cadastros e desconfiança pública.

### 9.5 Transparência financeira

Todos os recursos recebidos e gastos devem ser públicos, administrados por uma **fundação sem fins lucrativos**, com prestação de contas periódica.

## 10. Governança

### 10.1 Fases de descentralização

| Fase | Quem decide | Critério para avançar |
|---|---|---|
| **0 – Concepção** | Fundador e núcleo inicial de colaboradores | Whitepaper publicado e revisado por especialistas |
| **1 – Fundação** | Fundação sem fins lucrativos com conselho representando stakeholders (cidadãos, operadores, desenvolvedores, sociedade civil) | Rede em produção com operadores independentes em vários países |
| **2 – Comunidade** | Comunidade de titulares e contribuidores, por processo aberto de propostas | Nenhuma entidade isolada consegue alterar o sistema; o fundador se retira |

### 10.2 Mecanismos

- **Propostas de melhoria (USIPs):** qualquer pessoa pode propor mudanças, em processo público inspirado nos BIPs do Bitcoin e nas RFCs da IETF.
- **Consenso técnico aproximado** para decisões técnicas, com revisão por pares.
- **Voto "uma pessoa, um voto"** usando o próprio USI para decisões que afetem a comunidade, quando a rede estiver madura.
- **Separação de papéis:** quem desenvolve não opera sozinho, quem opera não decide sozinho, quem financia não controla.

### 10.3 Governos: apoio sem controle

Governos são aliados potencialmente valiosos e, ao mesmo tempo, os atores com maior capacidade de captura. Por isso valem regras iguais para qualquer governo:

- **Podem:** qualificar o perfil de país dos seus documentos (formatos, chaves públicas, listas de revogação, identificadores estáveis); operar nós como qualquer outro operador, sujeitos aos limites de concentração; ceder espaços públicos para cerimônias presenciais; reconhecer o USI para fins específicos; apoiar com financiamento ou assessoria jurídica.
- **Não podem:** ter voto especial, veto ou assento garantido; alterar regras ou o estado de qualquer USI; acessar dados dos titulares; condicionar o apoio a exclusividade, obrigatoriedade ou vigilância.
- **A verificação de documentos é local, com dados públicos e sem consulta online ao governo**, para que o Estado não saiba quem usa o USI nem onde.
- **O sistema continua funcionando se o apoio for retirado**; apenas o peso dos documentos daquele país diminui.
- Todos os acordos com governos são públicos, e o perfil de um país pode ser ponderado ou recusado por critérios públicos.

Os detalhes estão na [seção 14.5 do whitepaper](docs/whitepaper.pt-BR.md). No Brasil, o apoio do governo é bem-vindo, mas não é pré-requisito do piloto.

## 11. Stakeholders

| Stakeholder | Papel | Interesse |
|---|---|---|
| **Cidadãos (titulares)** | Criam e controlam seu USI | Identidade gratuita, privada e recuperável |
| **Pessoas sem documentação** (refugiados, apátridas, populações vulneráveis) | Titulares com necessidades específicas | Acesso a serviços e reconhecimento |
| **Atestadores e guardiões** | Validam pessoas que conhecem; ajudam na recuperação | Fortalecer a própria rede e comunidade |
| **Validadores comunitários e instituições parceiras** | Realizam verificações presenciais | Inclusão e serviço à comunidade |
| **Operadores de nós** | Mantêm o registro público | Infraestrutura confiável da qual dependem |
| **Verificadores** (plataformas, bancos, comércio, ONGs, órgãos públicos) | Aceitam e verificam USIs | Reduzir fraude, custos de verificação e contas falsas |
| **Emissores de credenciais e atestadores de atributos** (universidades, conselhos, órgãos públicos, empregadores, bancos e outras instituições que verificam clientes) | Emitem credenciais e atestam nome e documentos do titular | Credenciais à prova de falsificação; reaproveitar a verificação de clientes que já são obrigados a fazer |
| **Desenvolvedores e pesquisadores** | Constroem, auditam e evoluem o sistema | Propósito, reputação, pesquisa |
| **Reguladores e autoridades de proteção de dados** (como a ANPD) | Fiscalizam a conformidade | Proteção dos cidadãos |
| **Governos e órgãos públicos** (de qualquer país) | Apoio opcional: qualificar seus documentos, operar nós, ceder espaços, reconhecer o USI | Reduzir fraude e duplicidade, incluir pessoas sem documento. **Sem controle sobre o projeto** |
| **Iniciativas e organizações similares** (prova de pessoa única, identidade descentralizada, organizações de padrões) | Parceiros: compartilham pesquisa, padrões e componentes abertos | Objetivo comum; evitar duplicação de esforços |
| **Organizações** (empresas, associações, órgãos públicos) | Titulares de USI-O; agem por meio de representantes autorizados | Identidade, poderes e assinatura verificáveis, sem depender de um único responsável |
| **Autoridades certificadoras, cartórios e seus órgãos reguladores** | Interlocutores: coexistência, interoperação e eventual reconhecimento | Segurança jurídica e da infraestrutura; o USI busca dialogar antes de confrontar |
| **Financiadores** (fundações, programas de fomento, doadores) | Sustentam a fase inicial | Impacto social e infraestrutura aberta |
| **Sociedade civil e defensores de direitos digitais** | Fiscalizam e propõem melhorias | Privacidade, inclusão, transparência |

## 12. Casos de uso iniciais

Uma identidade só tem valor se for aceita, e só é aceita se as pessoas a tiverem. Para romper esse ciclo, o USI deve começar por nichos onde resolve uma dor real e imediata:

1. **Prova de humanidade:** distinguir pessoas de robôs e agentes de IA em redes sociais, fóruns, avaliações de produtos e formulários.
2. **Votações comunitárias e cooperativas:** garantir "uma pessoa, um voto" sem revelar quem votou.
3. **Distribuição de doações e benefícios:** evitar que a mesma pessoa receba várias vezes, com privacidade.
4. **Pessoas sem documentos:** em parceria com organizações humanitárias.
5. **Verificação de idade:** provar maioridade sem expor dados pessoais.
6. **Login sem senha:** acesso a serviços com o USI, sem depender de grandes plataformas.
7. **Credenciais acadêmicas e profissionais:** diplomas e registros verificáveis e infalsificáveis.
8. **Assinatura digital de documentos e autenticação em sistemas online,** para pessoas e organizações, com verificação por qualquer pessoa.

## 13. Como começar

Ações propostas para tirar o projeto do papel, em ordem aproximada:

### Etapa 1 – Whitepaper
- [x] Redigir a primeira versão do whitepaper ([v0.2.0](docs/whitepaper.pt-BR.md)), detalhando: modelo de ameaças, arquitetura das três camadas, modelo de unicidade e níveis de garantia, protocolo de recuperação, opções de registro público, modelo de sustentabilidade, plano de governança e plano de experimentos.
- [x] Publicar o rascunho neste repositório para comentários abertos.
- [ ] Aprofundar o levantamento da literatura e das experiências anteriores em identidade descentralizada e prova de pessoa única, com fontes primárias (a seção 5 do whitepaper é um resumo inicial e precisa ser verificada).
- [ ] Incorporar as contribuições recebidas e publicar a versão 0.2.

### Etapa 2 – Revisão e primeiros colaboradores
- [ ] Submeter o whitepaper à revisão de especialistas em criptografia, identidade digital, segurança e direito digital (LGPD).
- [ ] Contatar as iniciativas similares e as organizações de padrões (ver [seção 5 do whitepaper](docs/whitepaper.pt-BR.md)), propondo colaboração **antes** de qualquer protótipo próprio, e verificar o que ficou pendente no levantamento.
- [ ] Apresentar a proposta em comunidades de identidade descentralizada (como o W3C Credentials Community Group e a Decentralized Identity Foundation), em universidades e em grupos de pesquisa em segurança.
- [ ] Formar um núcleo inicial de colaboradores com perfis complementares: criptografia, desenvolvimento, direito, design de experiência, gestão de comunidade.

### Etapa 3 – Organização do repositório
- [x] Definir licenças: Apache-2.0 para código e CC BY 4.0 para documentação (podem ser revistas antes de o projeto aceitar as primeiras contribuições externas).
- [x] Criar `CONTRIBUTING.md`, código de conduta, política de segurança, o processo de propostas ([USIPs](docs/usips/README.pt-BR.md)), a página [Por onde começar](docs/start-here.pt-BR.md) e os modelos de issue e de pull request.
- [ ] Abrir uma *issue* para cada questão em aberto (ver [seção 14](#14-questões-em-aberto)) e habilitar *Discussions* para debates.
- [ ] Manter a pasta `docs/` para o whitepaper, decisões de arquitetura e atas.

### Etapa 4 – Provas de conceito
- [ ] Especificar e prototipar o método `did:usi`, com rotação e pré-rotação de chaves.
- [ ] Prototipar uma carteira mínima com credenciais verificáveis e divulgação seletiva.
- [ ] Implementar o protocolo de recuperação em camadas paralelas (rotas A a D, prazos, veto).
- [ ] Testar a prova documental com conhecimento zero e *nullifiers*.
- [ ] Simular ataques Sybil sobre o modelo de vínculo social para calibrar a análise de grafo.
- [ ] Comparar experimentalmente as opções de registro público (A, B e C).
- [ ] Levantar tecnicamente os documentos brasileiros candidatos (verificação criptográfica offline e identificador estável) e elaborar o primeiro perfil de país (experimento E13).
- [ ] Prototipar o vínculo de atributos (*slots* com compromisso, unicidade por OPRF de limiar, prova de vigência) e simular ataques de ocupação de identidade, conluio de emissores e identidade sintética (experimentos E14 e E15).
- [ ] Prototipar e testar a revalidação assistida por emissores e os cenários de perda total e de má-fé (experimento E16).
- [ ] Prototipar e testar a rejeição de chaves fracas, a ativação "publicar antes de usar" e a prova de comprometimento (experimento E17).
- [ ] Prototipar a migração criptográfica: identificadores de algoritmo, modo híbrido e simulação da "morte" de um algoritmo (experimento E18).
- [ ] Prototipar o USI-O com credenciais de representação e chave de limiar, em um piloto com uma associação ou cooperativa (experimento E19).
- [ ] Prototipar a assinatura de documentos e a verificação por terceiros (experimento E20).

### Etapa 5 – Análise jurídica e institucional
- [ ] Analisar conformidade com a LGPD e outras legislações relevantes.
- [ ] Estudar a forma jurídica da futura fundação e a viabilidade de reconhecimento do USI por instituições.
- [ ] Dialogar com a ANPD e, quando oportuno, com órgãos públicos brasileiros, pedindo apoio à qualificação dos documentos **sem contrapartida de controle**.
- [ ] Obter parecer jurídico sobre o enquadramento das assinaturas do USI (Lei 14.063/2020 e MP 2.200-2/2001) e sobre a relação com a fé pública dos cartórios.
- [ ] Definir o roteiro público de entrada de novos países (stakeholder local, perfil de país, análise jurídica, validadores, avaliação de riscos a direitos humanos).

### Etapa 6 – Financiamento e divulgação
- [ ] Mapear e submeter propostas a editais e programas de fomento a infraestrutura aberta e direitos digitais.
- [ ] Criar materiais de divulgação acessíveis (site, apresentação, vídeo curto) para atrair voluntários.
- [ ] Identificar instituições parceiras para o piloto e para operar os primeiros nós.

### Etapa 7 – Piloto
- [ ] Escolher um caso de uso inicial (ver [seção 12](#12-casos-de-uso-iniciais)) e uma comunidade parceira **no Brasil**.
- [ ] Executar um piloto controlado, com métricas de adesão, fraude detectada, sucesso de recuperação e satisfação.
- [ ] Publicar os resultados e ajustar o modelo.

### Etapa 8 – Institucionalização
- [ ] Constituir a fundação sem fins lucrativos.
- [ ] Iniciar a transição de governança para a fase 1.

## 14. Questões em aberto

Hipóteses e decisões que dependem de pesquisa e de testes:

- Qual opção de registro público (A, B ou C) oferece o melhor equilíbrio entre independência, custo e durabilidade?
- Como calibrar os pesos das camadas de evidência e os requisitos de cada nível de garantia?
- Qual a resistência real da análise de grafo social contra ataques Sybil organizados?
- É possível detectar duplicidade biométrica sem base centralizada, com custo e desempenho aceitáveis? Vale a pena?
- Quais prazos de espera equilibram segurança e conveniência na recuperação?
- Como organizar júris de contestação justos, resistentes a conluio e escaláveis?
- Como tratar óbito, inatividade e herança digital?
- Como proteger pessoas sob coação?
- Como tornar o sistema acessível a quem não tem smartphone ou internet estável?
- A taxa de verificação paga por serviços é viável e compatível com o princípio de não haver lucro?
- Quais critérios objetivos marcam cada transição de fase da governança?
- Como tratar a dupla nacionalidade entre países sem expor a dupla cidadania a nenhum Estado?
- Quais critérios públicos aceitam, ponderam ou recusam o perfil de um país?
- A fundação deve ter sede no Brasil ou numa jurisdição neutra?
- Como calcular a unicidade de CPFs e números de documento sem permitir ataque de dicionário?
- Como definir "emissor independente" e quem credencia os emissores?
- Como permitir a mudança legal de nome sem expor o histórico do titular?
- Que critérios ativam a técnica criptográfica de unicidade de identificadores na rede madura, e existe alternativa melhor?
- Como pessoas sem rede de apoio obtêm uma âncora de recuperação sem barreira excessiva, e como padronizar a revalidação assistida pelos emissores?
- Construir infraestrutura própria ou contribuir com uma iniciativa existente que cumpra as mesmas características? Quais componentes reaproveitar?
- Como o USI pode ser reconhecido juridicamente como assinatura sem perder as suas características essenciais, e como se relaciona com a fé pública dos cartórios?
- Como detectar geração fraca e sutil de aleatoriedade, e como credenciar emissores sem criar novos pontos de controle?
- Qual alternativa pós-quântica existe para a técnica de unicidade de identificadores e para as provas de conhecimento zero?

## 15. Como contribuir

O projeto está no início e toda contribuição é bem-vinda, **a começar pela leitura crítica do [whitepaper v0.2.0](docs/whitepaper.pt-BR.md)**. Especialmente de pessoas com experiência em:

- criptografia e protocolos de segurança;
- identidade digital e padrões W3C;
- sistemas distribuídos e consenso;
- direito digital e proteção de dados;
- design de experiência para públicos diversos;
- organização de comunidades e captação de recursos.

Para participar, abra uma *issue* com sua sugestão, dúvida ou crítica. Críticas fundamentadas são tão valiosas quanto ideias novas. Veja [Por onde começar](docs/start-here.pt-BR.md), o [guia de contribuição](CONTRIBUTING.pt-BR.md), o [código de conduta](CODE_OF_CONDUCT.pt-BR.md) e a [política de segurança](SECURITY.pt-BR.md).

### Política de idiomas

O repositório é **bilíngue**: cada documento existe em inglês (`nome.md`) e em português do Brasil (`nome.pt-BR.md`), com um link entre as versões no topo. Alterações devem ser feitas nas duas versões no mesmo commit sempre que possível; se houver divergência temporária, a versão em **inglês é a referência** até que as duas sejam sincronizadas. Contribuições em outros idiomas são bem-vindas como traduções adicionais (`nome.<código>.md`).

### Licenças

- **Código:** [Apache License 2.0](LICENSE).
- **Documentação** (whitepaper, READMEs e demais textos): [CC BY 4.0](LICENSE-docs).
- Não há cessão de direitos autorais: as pessoas autoras mantêm os seus direitos, e ninguém é dono do projeto ([NOTICE](NOTICE)).

## 16. Glossário

- **USI:** Universal Safe ID, o identificador pessoal único proposto por este projeto.
- **DID (Decentralized Identifier):** padrão W3C para identificadores que não dependem de uma autoridade central.
- **Credencial verificável:** documento digital assinado por um emissor, que o titular guarda e apresenta, e que qualquer pessoa pode verificar.
- **Prova de conhecimento zero (ZKP):** técnica criptográfica que permite provar que uma afirmação é verdadeira sem revelar a informação que a sustenta.
- **Nullifier:** valor derivado de um dado secreto que permite detectar uso repetido sem revelar o dado.
- **Ataque Sybil:** criação de muitas identidades falsas por uma mesma pessoa ou grupo.
- **Pré-rotação de chaves:** compromisso antecipado com a próxima chave, guardada offline, para recuperar o controle caso a chave atual seja comprometida.
- **Guardião:** pessoa ou instituição escolhida pelo titular para ajudar a recuperar seu acesso.
- **Compartilhamento de segredo de Shamir:** técnica que divide um segredo em partes, exigindo um número mínimo delas para reconstruí-lo.
- **Passkey:** credencial de acesso sem senha, baseada no padrão FIDO2, protegida pelo dispositivo do usuário.
- **Consenso BFT:** mecanismo de acordo entre nós de uma rede que tolera que parte deles falhe ou aja de má-fé.
- **Cliente leve:** software que verifica o registro sem precisar armazená-lo por completo.
- **Nível de garantia:** grau de confiança de que um USI corresponde a uma pessoa real e única.
- **USI-P / USI-O:** as duas partes do projeto: identidade da pessoa humana (P) e de organizações (O), sobre um núcleo comum.
- **Autoridade certificadora (AC):** entidade que emite certificados digitais ligando uma chave a uma identidade; opera em hierarquia (raiz, intermediárias).
- **Criptografia pós-quântica:** algoritmos desenhados para resistir a computadores quânticos.
- **Assinatura híbrida:** assinatura que combina um algoritmo clássico e um pós-quântico; só vale se ambos verificarem.
- **Agilidade criptográfica:** capacidade de trocar os algoritmos sem trocar a identidade.

---

*Este documento é vivo e será atualizado à medida que o projeto evoluir. Sugestões são bem-vindas por meio de issues.*
