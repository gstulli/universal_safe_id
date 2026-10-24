# Universal Safe ID (USI) — Whitepaper

🌐 [English](whitepaper.md) · **Português (Brasil)**

**Versão 0.1.2 — rascunho aberto à colaboração** · Outubro de 2026
Documento complementar ao [README](../README.pt-BR.md).

> **Como ler este documento.** O USI está em fase de concepção. Este whitepaper reúne o que se sabe, propõe caminhos e declara o que ainda não se sabe. Cada seção indica o seu grau de maturidade:
>
> - 🟢 **Proposto**: direção que o projeto pretende seguir, sujeita a revisão por pares.
> - 🟡 **Hipótese**: ideia plausível que precisa ser testada ou medida antes de ser adotada.
> - 🔴 **Em aberto**: questão sem resposta conhecida; precisa de pesquisa.
>
> Valores numéricos (prazos, limiares, tamanhos) são **ilustrativos** até que sejam calibrados nas provas de conceito (seção 16). Críticas, correções e contribuições são bem-vindas (seção 20).

---

## Sumário

1. [Resumo](#1-resumo)
2. [Introdução e motivação](#2-introdução-e-motivação)
3. [Objetivos e não objetivos](#3-objetivos-e-não-objetivos)
4. [Modelo de ameaças](#4-modelo-de-ameaças)
5. [Aprendizados de iniciativas anteriores](#5-aprendizados-de-iniciativas-anteriores)
6. [Visão geral da arquitetura](#6-visão-geral-da-arquitetura)
7. [Identificador e gestão de chaves](#7-identificador-e-gestão-de-chaves)
8. [Registro público](#8-registro-público)
9. [Unicidade: uma pessoa, um USI](#9-unicidade-uma-pessoa-um-usi)
10. [Recuperação de acesso](#10-recuperação-de-acesso)
11. [Privacidade](#11-privacidade)
12. [Segurança operacional e criptografia](#12-segurança-operacional-e-criptografia)
13. [Sustentabilidade](#13-sustentabilidade)
14. [Governança](#14-governança)
15. [Adoção e estratégia de entrada](#15-adoção-e-estratégia-de-entrada)
16. [Plano de validação experimental](#16-plano-de-validação-experimental)
17. [Riscos do projeto](#17-riscos-do-projeto)
18. [Questões em aberto](#18-questões-em-aberto)
19. [Roteiro](#19-roteiro)
20. [Como contribuir com este documento](#20-como-contribuir-com-este-documento)
21. [Referências](#21-referências)
22. [Histórico de versões](#22-histórico-de-versões)

---

## 1. Resumo

O Universal Safe ID (USI) é uma proposta de infraestrutura aberta, sem dono e sem fins lucrativos para que qualquer pessoa obtenha, gratuitamente, **um identificador único e permanente**, capaz de provar que ela é **um ser humano distinto** sem revelar quem é, e que a permita **controlar seus próprios dados**, compartilhando-os de forma seletiva e temporária.

Nenhum componente técnico do USI é inédito. A contribuição proposta está na **combinação deliberada** de técnicas já estudadas em identidade descentralizada, criptografia e infraestrutura pública, de modo que as fraquezas de cada uma sejam cobertas pelas demais:

1. **Unicidade por múltiplas evidências independentes** (vínculo social analisado em grafo, prova documental com conhecimento zero, presença física, e opcionalmente biometria), traduzidas em **níveis de garantia** que cada verificador escolhe.
2. **Recuperação de acesso por rotas paralelas** (outro dispositivo, chave pré-rotacionada, guardiões, revalidação), com prazos de espera e direito de veto proporcionais à força da evidência.
3. **Registro público mínimo**, que guarda apenas chaves públicas, compromissos criptográficos e provas, **nunca dados pessoais**.
4. **Pseudônimos distintos por serviço**, que impedem que o identificador universal se torne instrumento de rastreamento.
5. **Sustentação por quem se beneficia**, sem token e sem cobrança do cidadão, com governança que se descentraliza em fases mensuráveis.

Este documento descreve o problema, o modelo de ameaças, a arquitetura proposta, as alternativas ainda em disputa, um plano de experimentos para decidir entre elas e os riscos do projeto.

## 2. Introdução e motivação

### 2.1 O problema

Sistemas de identificação de pessoas dependem hoje de duas famílias de soluções, ambas problemáticas:

- **Identidade emitida por Estados e entidades certificadoras.** Deixa bilhões de pessoas sem documento reconhecido; produz bases centralizadas sujeitas a vazamento em massa e a duplicidades; não atravessa fronteiras com facilidade; e pode ser negada ou cancelada por uma única autoridade.
- **Identidade emitida por plataformas privadas** (contas de grandes empresas usadas para entrar em outros serviços). A conta pertence à plataforma, pode ser bloqueada sem recurso, é base de perfilamento comercial e não garante que haja um humano real e único por trás dela.

### 2.2 Um problema agravado: humanos e agentes de IA

A capacidade crescente de agentes de IA de produzir texto, voz, imagens e comportamento humano em escala torna cada vez mais difícil sustentar o princípio "uma pessoa, uma voz" em redes sociais, avaliações, pesquisas, votações comunitárias e distribuição de benefícios. Mecanismos tradicionais de verificação (CAPTCHAs, e-mail, telefone) são baratos de contornar. Há uma demanda crescente por **prova de pessoa única** (*proof of personhood*) que preserve a privacidade.

### 2.3 O que o USI propõe

Um terceiro caminho: uma identidade que **não depende de uma única autoridade**, **não exige a revelação de dados pessoais** para ser comprovada e **não pode ser perdida** por um simples esquecimento, e cuja confiança é construída por **evidências independentes** e não por um único método.

## 3. Objetivos e não objetivos

### 3.1 Objetivos 🟢

| # | Objetivo |
|---|---|
| O1 | Atribuir no máximo um USI ativo a cada ser humano, com fraude difícil, cara, detectável e reversível. |
| O2 | Permitir que o titular prove "sou um humano único" e "tenho nível de garantia N" sem revelar quem é. |
| O3 | Manter os dados pessoais sob controle exclusivo do titular, com divulgação mínima, seletiva e temporária. |
| O4 | Tornar a perda de acesso recuperável sem criar uma porta fácil para sequestro de conta. |
| O5 | Impedir que o USI possa ser usado para correlacionar ou rastrear a mesma pessoa entre serviços. |
| O6 | Ser gratuito para o titular e sustentável sem token e sem lucro. |
| O7 | Ser inclusivo: funcionar para quem não tem documento, smartphone novo ou conexão estável. |
| O8 | Ser verificável e auditável publicamente, em código aberto e com padrões abertos. |
| O9 | Descentralizar a governança de forma planejada, até que ninguém, incluindo o fundador, tenha poder unilateral. |
| O10 | Garantir que cada USI tenha um único conjunto vigente de atributos-chave (nome oficial, identificadores) e que terceiros saibam o quanto confiar neles. |

### 3.2 Não objetivos 🟢

- **Não é uma moeda, um token ou um ativo financeiro.**
- **Não substitui documentos oficiais.** Convive com eles e os usa como evidência quando existirem.
- **Não garante unicidade absoluta.** Nenhum sistema garante; o objetivo é um custo de fraude muito superior ao benefício.
- **Não garante a veracidade das informações**, apenas que são únicas e o quanto são confiáveis. Quem responde pela veracidade é quem as verifica (seção 9.7).
- **Não é um sistema de crédito social, reputação pública ou pontuação de cidadãos.** Reputação interna serve apenas para ponderar atestações.
- **Não armazena dados pessoais** no registro público, em qualquer forma.
- **Não é um mecanismo de vigilância**, nem de identificação compulsória.
- **Não resolve, por si só, a autorização** (o que a pessoa pode fazer), apenas a autenticação e a prova de unicidade.

### 3.3 Premissa geográfica: piloto no Brasil, desenho sem fronteiras 🟢

- **Piloto no Brasil.** A primeira implantação real será no Brasil: é onde o projeto nasce, onde o conhecimento sobre documentos e legislação (LGPD) está disponível e onde será formada a primeira rede de parceiros.
- **Desenho sem fronteiras.** O protocolo, o registro e o modelo de unicidade **não podem pressupor um país**. Tudo o que é específico de um país fica em módulos plugáveis, os **perfis de país** (seção 9.2.2). Atalhos que só funcionam no Brasil (por exemplo, assumir um número nacional específico no protocolo) são dívida técnica e devem ser evitados.
- **Expansão gradual por adesão.** Novos países entram à medida que stakeholders locais (operadores de nós, validadores, emissores de credenciais, juristas, tradutores e governos interessados) aderem e oferecem suporte à infraestrutura e à operação. A adesão é voluntária e sem exclusividade; nenhum país tem prioridade de governança por ter sido o primeiro.
- **Apoio de governos sem controle.** Governos podem apoiar o projeto, inclusive qualificando a verificação dos seus próprios documentos, mas não adquirem qualquer controle sobre ele (seção 14.5).

## 4. Modelo de ameaças

### 4.1 Adversários considerados

| Adversário | Capacidade e motivação |
|---|---|
| **Fraudador Sybil** [10] | Quer múltiplas identidades para multiplicar votos, benefícios ou influência. Pode usar automação, IA e mão de obra paga. |
| **Mercado de identidades** | Compra e vende cadastros ou atestações. Explora o pagamento a pessoas reais para atuarem como "humanos de aluguel". |
| **Sequestrador de conta** | Tenta tomar o controle de um USI alheio, de preferência pela rota de recuperação. |
| **Operador malicioso** | Controla parte dos nós do registro e tenta censurar, reordenar ou falsificar eventos. |
| **Capturador de governança** | Tenta obter, por dinheiro, influência política ou conluio, o controle das regras do sistema. |
| **Vigilante (Estado, empresa ou observador passivo)** | Quer rastrear pessoas entre serviços, ou construir perfis a partir de metadados. |
| **Coator** | Força fisicamente ou legalmente o titular a ceder acesso, chaves ou dados. |
| **Adversário futuro** | Guarda dados de hoje para quebrá-los quando houver computação quântica ou novas técnicas. |
| **Insider** | Desenvolvedor, validador ou jurado que abusa da posição. |
| **Ocupante de identidade** | Registra primeiro o nome ou o CPF de outra pessoa para impedi-la de registrar a própria identidade, ou constrói uma identidade sintética com documentos falsos (seção 9.7). |

### 4.2 Premissas de confiança 🟡

- Parte relevante dos titulares e atestadores age de forma honesta, e a rede honesta é maior que qualquer grupo fraudulento (premissa necessária à análise de grafo).
- Mais da maioria qualificada dos operadores do registro não conspira (premissa de qualquer consenso tolerante a falhas bizantinas).
- Primitivas criptográficas padronizadas permanecem seguras, com plano de migração se deixarem de ser.
- Dispositivos pessoais podem ser perdidos ou roubados, mas não estão **todos** comprometidos ao mesmo tempo.

### 4.3 O que está fora do escopo de proteção 🟢

- **Comprometimento total do dispositivo do titular** por malware avançado, no momento da assinatura.
- **Um humano que, voluntariamente e sem coação, entrega seu USI a outro** (venda de identidade). O USI mitiga (seção 9.6), mas não elimina; nenhum sistema elimina.
- **Informação já vista:** uma vez revelado, um dado não pode ser "desrevelado".

## 5. Aprendizados de iniciativas anteriores

Esta seção resume padrões observados em abordagens existentes, com ênfase nas **lições de projeto**, e não na crítica a iniciativas específicas. As observações são gerais e devem ser verificadas e detalhadas em versões futuras, com fontes primárias.

| Abordagem | O que funciona | O que costuma falhar | Consequência para o USI |
|---|---|---|---|
| **Biometria obrigatória em hardware dedicado** | Alta capacidade de detectar duplicidade; difícil de enganar em larga escala | Preocupações de privacidade, centralização do hardware, escrutínio regulatório e dependência de um único fabricante | Biometria, se adotada, será **opcional**, sem base centralizada e com arquitetura que dispense um fabricante único |
| **Grafo social** | Sem hardware nem documento; inclusivo | Grupos falsos bem conectados; baixa adoção; pouca motivação para validar | Usar grafo como **uma** evidência, com análise estrutural e responsabilização dos atestadores |
| **Depósito, vídeo e contestação por júri** | Cria custo para fraudar e mecanismo corretivo | Cadastro lento e caro; dependência de ativo financeiro | Manter **contestação e júri**, mas sem depósito financeiro obrigatório para o cidadão |
| **Testes sincronizados para provar humanidade** | Dispensa documentos | Terceirização: pessoas que fazem o teste por outras em troca de pagamento | Não depender de testes isolados; combinar com outras evidências |
| **Encontros presenciais simultâneos** | Forte contra Sybil: ninguém está em dois lugares ao mesmo tempo | Difícil de escalar; exige coordenação e acessibilidade | Usar presença física como evidência de **alto nível**, apoiada por parceiros locais |
| **Padrões abertos de identidade (DID, VC)** | Interoperabilidade, ecossistema de ferramentas | Sem solução própria de unicidade; a unicidade vem de um Estado | Adotar os padrões; **acrescentar** a camada de unicidade |
| **Carteiras de identidade estatais** | Reconhecimento legal, alta adesão potencial | Dependência de um emissor e de sua política | Aceitar credenciais estatais como **evidência**, nunca como único requisito |

**Três lições transversais:**

1. Nenhuma evidência isolada resiste; as abordagens mais frágeis dependem de um único sinal.
2. O ponto mais atacado costuma ser o **mercado de identidades** (pagar pessoas reais), e não a força bruta técnica.
3. Tokens financeiros atraem fraude e especulação e distorcem os incentivos de quem deveria validar.

## 6. Visão geral da arquitetura

### 6.1 Camadas 🟢

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

As camadas são independentes e devem poder evoluir separadamente: trocar o registro público não deve exigir mudar o formato das credenciais, e recalibrar o modelo de unicidade não deve alterar o protocolo de chaves.

### 6.2 Componentes e fluxos

| Componente | Função |
|---|---|
| **Carteira (wallet)** | Aplicativo do titular. Guarda chaves, segredos de identidade, credenciais e consentimentos. Gera provas. |
| **Registro público** | Armazena e ordena eventos (criação, rotação, revogação, congelamento, nullifiers, resumos de atestações). |
| **Serviço de unicidade** | Conjunto de regras e processos que convertem evidências em nível de garantia. Em parte *on-chain* (hashes, nullifiers), em parte *off-chain* (grafo, júris). |
| **Perfis de país** | Módulos públicos e versionados com o que é específico de cada país: documentos aceitos e como verificá-los, identificador estável, peso da evidência, validadores e aspectos legais (seção 9.2.2). |
| **Atestadores** | Titulares existentes que atestam outro titular. |
| **Guardiões** | Pessoas ou instituições escolhidas pelo titular para auxiliar na recuperação. |
| **Validadores presenciais** | Parceiros que realizam cerimônias de verificação física. |
| **Emissores** | Instituições que emitem credenciais verificáveis (diplomas, registros) e **atestam atributos** do titular (nome, documentos), como bancos que verificam seus clientes (seção 9.7). |
| **Verificadores** | Serviços que pedem e conferem provas do USI. |
| **Júris** | Grupos sorteados que decidem contestações. |

**Fluxo de uso típico (simplificado).** Um verificador solicita "humano único com nível ≥ 2". A carteira calcula um pseudônimo e um *nullifier* específicos para aquele verificador e gera uma prova de conhecimento zero de que (a) existe um USI ativo no registro, (b) com nível ≥ 2, (c) ao qual o pseudônimo e o *nullifier* pertencem. O verificador confere a prova e o *nullifier*, sem saber qual é o USI.

## 7. Identificador e gestão de chaves

### 7.1 Identificador 🟢

O USI segue o padrão **W3C DID** [1]. Propõe-se um método próprio, `did:usi`, cujo identificador é derivado de forma determinística de dados do evento de criação (por exemplo, o hash do primeiro evento), de modo a ser auto-certificado e independente de uma autoridade de nomes.

### 7.2 Chaves e segredos: separar papéis 🟢

Um erro comum é usar uma única chave para tudo. O USI propõe **separar funções**:

| Material | Função | Rotacionável? | Observação |
|---|---|---|---|
| **Chave(s) de controle** | Assinam eventos do registro (rotação, revogação, congelamento) | Sim | Podem ser *passkeys* FIDO2 [2] ou chaves em hardware |
| **Chave pré-rotacionada** | Assume o controle se as chaves de controle forem perdidas ou comprometidas | Sim, a cada uso | Só o *hash* é registrado; a chave fica offline |
| **Segredo de identidade** | Base para derivar pseudônimos e *nullifiers* por serviço | **Não deve mudar** (ver 11.3) | Precisa ser recuperável sem ser revelado a terceiros |
| **Chaves de credencial** | Assinam apresentações de credenciais | Sim | Podem ser derivadas por serviço |

### 7.3 Registro de eventos de chaves 🟢

Inspirado em KERI [3], o estado de cada USI é o resultado de um **registro encadeado de eventos**: criação, rotação, adição/remoção de dispositivo, congelamento, descongelamento, início/veto/conclusão de recuperação, revogação por decisão de júri. Cada evento é assinado pelas chaves vigentes e referencia o evento anterior.

### 7.4 Pré-rotação 🟢

Ao registrar a chave atual, o titular registra o *hash* da próxima. Se a chave atual for comprometida, o atacante **não consegue** nomear uma chave de sua escolha como sucessora, pois ela já está comprometida com antecedência. O titular guarda a próxima chave offline (papel, cofre, chave física).

### 7.5 Agilidade criptográfica e pós-quântica 🟡

Os eventos devem identificar o algoritmo usado. A migração para algoritmos pós-quânticos padronizados (como ML-DSA, FIPS 204 [4]) deve ser possível sem trocar de USI. Como assinaturas e chaves pós-quânticas são significativamente maiores, o registro deve armazenar **compromissos (hashes)** de chaves, e revelar a chave completa somente quando necessário (no evento que a utiliza). Isso afeta o dimensionamento (seção 8.3).

### 7.6 Múltiplos dispositivos 🟢

Um USI pode ter vários dispositivos autorizados, cada um com sua chave, com política configurável (por exemplo, "qualquer um pode assinar atos cotidianos; mudanças de segurança exigem dois").

## 8. Registro público

### 8.1 Requisitos 🟢

| Requisito | Descrição |
|---|---|
| R1 | **Independência**: nenhuma entidade única pode alterar, censurar ou apagar eventos. |
| R2 | **Durabilidade**: sobreviver por décadas, inclusive ao fim de qualquer organização. |
| R3 | **Custo zero para o titular.** |
| R4 | **Auditabilidade pública**: qualquer pessoa pode verificar a integridade do registro. |
| R5 | **Privacidade**: nenhum dado pessoal; mínimo de metadados correlacionáveis. |
| R6 | **Verificabilidade leve**: dispositivos modestos verificam provas compactas, sem baixar o registro inteiro. |
| R7 | **Desempenho suficiente** para a escala-alvo. |
| R8 | **Neutralidade jurisdicional**: operadores em várias jurisdições. |

### 8.2 O que é e o que não é registrado 🟢

**Registrado:** USI, compromissos de chaves, eventos de chaves, *nullifiers* de unicidade, resumos (*hashes*) de atestações, decisões de júri (em forma mínima).
**Nunca registrado:** nome, documentos, fotos, biometria, endereço, data de nascimento, ou qualquer dado pessoal, **nem criptografado**.

Dados cifrados na cadeia são um risco: a criptografia de hoje pode ser quebrada no futuro (ataque "colete agora, decifre depois") e o registro é, por natureza, impossível de apagar, o que colide com o direito à eliminação previsto na LGPD [5].

### 8.3 Dimensionamento 🟡

Estimativa de ordem de grandeza (a validar em protótipo):

| Cenário | Dados por pessoa no registro | Total para 8 bilhões |
|---|---|---|
| Chaves clássicas completas (ex.: curvas elípticas de 32 bytes) + eventos básicos | ~200–300 B | ~1,6–2,4 TB |
| Chaves pós-quânticas completas no registro (ordem de kB) | ~2–4 kB | ~16–32 TB |
| Apenas **compromissos (hashes)** de chaves; chaves reveladas nos eventos | ~200–400 B | ~1,6–3,2 TB |

Observações:
- Oito bilhões é um **teto teórico**, não uma meta. Cada rotação de chave acrescenta eventos; o crescimento real depende do uso.
- A estimativa justifica o princípio de armazenar **compromissos**, não chaves pós-quânticas completas.
- Dados de histórico podem ser **podados ou arquivados** por nós leves, mantendo-se só o estado atual e as provas necessárias.
- O usuário comum **não** armazena o registro: usa cliente leve e provas de inclusão compactas.

### 8.4 Opções de implementação 🔴

A decisão deve vir de provas de conceito (seção 16). Opções:

| | **A. Âncoras em blockchain pública existente** | **B. Rede federada própria (BFT) com logs auditáveis** | **C. Híbrida** |
|---|---|---|---|
| Descrição | Eventos (ou raízes de árvores de Merkle) publicados em uma rede pública consolidada, por exemplo uma camada 2 de Ethereum | Dezenas a centenas de operadores independentes executam consenso tolerante a falhas bizantinas; logs auditáveis no estilo *Certificate Transparency* [6] | Rede federada para operação diária; âncoras periódicas (raízes de Merkle) em blockchain pública |
| Segurança | Herdada de uma rede já testada | Depende da diversidade e honestidade dos operadores | Dupla: federação + âncora externa |
| Custo | Custo por transação (mitigável com agregação em lotes) | Custo de operação distribuído entre operadores | Soma, mas custo de âncora é pequeno |
| Dependência | De terceiros e de suas regras e taxas | De conseguir e manter operadores | Das duas, em menor grau |
| Risco principal | Mudança de regras, congestionamento, taxas | Captura ou colapso do conjunto de operadores | Complexidade |
| Privacidade | Metadados públicos permanentes | Melhor controle sobre o que é exposto | Idem B + âncoras opacas |

**Hipótese de trabalho:** a opção **C** tende a equilibrar melhor os requisitos R1–R8: operar via federação, com raízes de Merkle ancoradas em rede pública para tornar a adulteração detectável por qualquer pessoa. Esta é uma **hipótese**, não uma decisão.

**Agregação em lotes.** Seja qual for a opção, os eventos devem ser agregados em lotes e comprometidos por raiz de Merkle, de modo que o custo por titular seja uma fração mínima.

## 9. Unicidade: uma pessoa, um USI

### 9.1 Princípio de projeto 🟢

Garantir unicidade absoluta é impossível. O objetivo é que **o custo marginal de uma identidade falsa seja sempre superior ao seu benefício**, que a fraude seja **detectável** e que seja **reversível** sem prejuízo ao titular legítimo.

### 9.2 Camadas de evidência 🟢

Cada USI acumula evidências de categorias distintas. Nenhuma é obrigatória isoladamente; a força vem da combinação e da independência entre elas.

#### 9.2.1 Vínculo social 🟡

- **Mecanismo:** titulares existentes atestam que conhecem o candidato como pessoa real e única.
- **Não se mede a quantidade de atestações**, mas a **estrutura do grafo**. Grupos de contas falsas tendem a formar regiões densamente conectadas entre si e escassamente conectadas à rede honesta; algoritmos como o SybilRank [7] exploram esse fato.
- **Atestadores respondem pelo que atestam:** atestar um USI posteriormente considerado fraudulento reduz a reputação do atestador (e, em casos graves, o remove temporariamente da função). Isso encarece a atestação irresponsável.
- **Limites do atestador:** número máximo de atestações ativas por período; atestação exige presença de vínculo real (ex.: interação prévia, encontro, contexto verificável).
- **Fraquezas:** vulnerável a "humanos de aluguel" e a pessoas reais induzidas a atestar fraudes; efeito de rede inicial lento; reforça desigualdades de conexão.

#### 9.2.2 Prova documental com conhecimento zero 🟡

- **Mecanismo:** para quem possui documento com chip e assinatura digital verificável (como passaportes eletrônicos), o titular prova, dentro de uma prova de conhecimento zero, que (a) o documento é autêntico, (b) está válido e (c) deriva dele um ***nullifier*** determinístico. O registro guarda apenas o *nullifier*; um segundo cadastro com o mesmo documento produz o mesmo *nullifier* e é recusado.
- **Vantagem:** aproveita a unicidade que Estados já estabelecem, sem criar base de documentos e sem revelar dados.
- **Limitações que precisam ser reconhecidas:**
  - A unicidade é **por documento**, não **por pessoa**. Quem tem múltiplos documentos (dupla nacionalidade, passaporte renovado com novo número) pode, em princípio, produzir múltiplos *nullifiers*. Mitigações a investigar: derivar o *nullifier* de campos estáveis da pessoa (e não do número do documento), o que exige análise cuidadosa de privacidade; e cruzamento com outras camadas. Ver **perfis de país**, a seguir.
  - Depende da **confiança nas autoridades emissoras** (cadeias de certificados de cada país). Estados maliciosos poderiam, em tese, emitir documentos falsos em massa. Mitigação: o peso da camada documental é ponderado por país e pode ser reduzido por decisão de governança se houver evidência de abuso.
  - Cobre apenas quem **tem** o documento. Para os demais, valem as outras camadas.

**Perfis de país: qualificação dos documentos 🟡**

Cada país que adere ao projeto tem um **perfil de país** público, versionado e revisável, contendo:

1. os **documentos aceitos** (passaporte eletrônico, documento nacional de identidade, habilitação etc.) e **como verificá-los criptograficamente**: formatos, chaves públicas e cadeias de certificados, listas de revogação;
2. o **identificador estável da pessoa** naquele país, quando existir (por exemplo, um número nacional único), e a forma de derivar dele o *nullifier*, de modo que **todos os documentos do mesmo país (passaporte, identidade, habilitação, reemissões e renovações) resultem no mesmo *nullifier***;
3. o **peso** da evidência documental do país, definido por critérios públicos;
4. validadores e parceiros presenciais locais, análise jurídica local e idiomas.

*Quem elabora o perfil.* A comunidade, a partir de especificações públicas. Quando o governo do país apoia o projeto, pode **qualificar** o perfil (confirmar formatos, publicar chaves e listas de revogação, esclarecer quais campos são estáveis), mas o perfil é público e adotado por processo aberto (USIP), não por decisão do governo (seção 14.5). Listas de revogação publicadas pelo emissor (documentos perdidos, roubados, de pessoas falecidas) também ajudam no ciclo de vida do USI (seção 9.5).

*Efeito sobre duplicidades.*
- **Dentro de um país:** um perfil bem qualificado resolve o caso de pessoas com vários documentos do mesmo país (passaporte renovado, identidade e habilitação): todos levam ao mesmo *nullifier*.
- **Entre países (dupla nacionalidade):** continua sem solução completa. Dois países produzem dois *nullifiers*. Ligar documentos de países diferentes exigiria cooperação entre Estados e revelaria a dupla cidadania a eles, o que é um risco de privacidade e não deve ser pressuposto. Mitigações: níveis 3 e 4 exigem evidências **não documentais** (presença física, vínculo social) que não se duplicam com um segundo passaporte; contestação e júri; e aceitação consciente de um resíduo, já que pessoas com dupla nacionalidade são minoria e o ganho de uma segunda identidade fica limitado nos níveis mais altos. 🔴 *Em aberto.*

*Estrutura mínima.* No piloto, o Brasil terá o primeiro perfil de país (seção 15.5). O perfil serve de modelo para os seguintes e permite testar, desde o início, que nada no protocolo depende dele.

#### 9.2.3 Presença física 🟡

- **Mecanismo:** cerimônias presenciais e simultâneas, com validadores comunitários e instituições parceiras (bibliotecas, escolas, ONGs). Cada participante é verificado por outros participantes e por validadores credenciados, ao mesmo tempo, em vários locais. Uma pessoa não pode estar em dois locais simultaneamente.
- **Forte** contra Sybil; **essencial** para quem não tem documento.
- **Fraquezas:** custo e logística; risco de conluio de validadores locais; requer acessibilidade. Mitigações: rotatividade e sorteio de validadores, amostragem auditada de cerimônias, registros assinados.

#### 9.2.4 Biometria (opcional) 🔴

- **Posição do projeto:** biometria só será adotada se for possível detectar duplicidade **sem base biométrica centralizada** e sem expor dados a nenhum operador. Técnicas candidatas: computação multipartidária e criptografia homomórfica sobre gabaritos biométricos.
- **Riscos:** dados biométricos são irrevogáveis; imprecisão (falsos positivos aumentam com a escala); viés demográfico; coerção.
- **Postura:** sempre **opcional**, nunca requisito de nível mínimo, e condicionada à aprovação em auditoria independente. Pode ser descartada se os riscos superarem os benefícios.

#### 9.2.5 Continuidade e histórico 🟡

Tempo de existência do USI, uso consistente, credenciais emitidas por terceiros reconhecidos. Contas recém-criadas pesam menos. É uma evidência fraca isoladamente, mas encarece ataques que precisam de resultados rápidos.

### 9.3 Níveis de garantia 🟡

Evidências são convertidas em níveis públicos e padronizados. O verificador escolhe o nível que exige.

| Nível | Requisito indicativo | Uso típico |
|---|---|---|
| **1 – Básico** | Vínculo social mínimo | Fóruns, comentários, filtro anti-robô |
| **2 – Intermediário** | Vínculo social sólido **ou** prova documental | Enquetes, comunidades online, cadastros simples |
| **3 – Alto** | Evidências de **duas categorias diferentes** | Votações comunitárias, doações |
| **4 – Máximo** | **Três ou mais** categorias, incluindo presença física ou prova documental | Distribuição de benefícios, aplicações sensíveis |

A calibração (pesos, limiares, decaimento no tempo) é uma questão experimental (seção 16, experimentos E2 e E3). Um modelo mais refinado poderá substituir a tabela por uma pontuação contínua, mantendo os níveis como interface.

### 9.4 Contestação e correção 🟡

- **Qualquer titular pode contestar** um USI suspeito, apresentando evidências, possivelmente com limite de contestações simultâneas para evitar assédio.
- **Júris sorteados** entre titulares de nível alto decidem, com regras públicas, direito de defesa para o contestado e registro mínimo da decisão.
- **Efeitos de uma duplicidade confirmada:** o registro excedente é cancelado; o USI legítimo permanece; os atestadores do USI fraudulento perdem reputação.
- **Salvaguardas contra abuso:** contestações infundadas reiteradas geram perda de reputação do contestante; decisões têm possibilidade de recurso.
- **Questões abertas:** resistência dos júris ao conluio e à compra de votos; sorteio verificavelmente aleatório; carga de trabalho.

Este mecanismo é o que permite substituir a ideia de "irrevogável" pela de **"permanente, mas corrigível"**.

### 9.5 Ciclo de vida 🟡

**Criação → acúmulo de evidências → uso → rotação de chaves → recuperação (se necessária) → contestação (se houver) → inatividade ou óbito.**

O tratamento de óbito e de inatividade precisa impedir o uso de identidades de falecidos sem expor dados de ninguém. Hipóteses: marcação de inatividade após longo período sem sinais de vida do titular, com período de contestação; designação opcional de um herdeiro digital que pode encerrar (mas não assumir) o USI.

### 9.6 Venda e aluguel de identidade 🔴

O ataque mais difícil de eliminar é o da pessoa real que **vende** seu USI ou atua como "humano de aluguel". Medidas que dificultam, sem eliminar:

- **Detecção de transferência de controle:** rotação de chaves seguida de mudança abrupta de padrão de uso eleva alertas.
- **Prazos e limites em operações sensíveis**, que impedem a monetização rápida em larga escala.
- **Custo reputacional ao titular** que cede o controle, quando a transferência é comprovada.
- **Provas de "vivacidade" periódicas e opcionais** em usos de alto nível.
- **Resistência à coerção e à compra de voto:** em votações, esquemas que impeçam o titular de provar a terceiros em quem votou.

Este é um tema de pesquisa permanente.

### 9.7 Vínculo entre o USI e os atributos de identidade (nome e documentos) 🟡

**O problema.** Garantir um único USI por pessoa (seções 9.1 a 9.6) não basta. É preciso também impedir que a mesma pessoa use dois nomes ou dois CPFs e que um terceiro, ao verificar um USI, receba informações diferentes das verdadeiras. Como o registro público não guarda dado pessoal, o caminho óbvio, gravar "USI → nome, CPF" na rede, está descartado.

**Princípio.** O USI garante duas coisas distintas:
1. que a informação é **única** para aquele USI (não existem duas versões vigentes);
2. **quanto se pode confiar** nela (quantos emissores independentes a verificaram).

O USI **não torna uma informação verdadeira**. Quem responde pela veracidade é quem a verifica (seção 9.7.5).

**9.7.1 Dois tipos de informação**

| Tipo | Exemplos | Regra |
|---|---|---|
| **Atributos-chave** | nome oficial, data de nascimento, identificador nacional estável de cada país (por exemplo, o CPF) | **Um único valor vigente** por tipo (e por país, no caso do identificador). Alterar um valor que já foi atestado zera a confiança dele. |
| **Documentos** | passaporte, RG, carteira de habilitação | Podem existir vários e ser renovados ou reemitidos (inclusive por entidades diferentes do mesmo país), mas todos devem ser **coerentes** com os atributos-chave: mesmo identificador estável e nome compatível. |

O **nome é chave no sentido de ser imutável e vinculado ao USI**, mas **não é único entre pessoas** (há muitos "João da Silva"). A unicidade *entre USIs* só se aplica aos identificadores que o Estado garante serem únicos (CPF, passaporte com país). A correspondência entre nomes (acentos, abreviações, transliteração de outros alfabetos) deve ser definida no perfil de país. 🔴

**9.7.2 Como o vínculo é registrado**
- Para cada USI e tipo de atributo existe um único **espaço (*slot*)**. O valor vigente fica na carteira do titular. O registro guarda apenas um **compromisso criptográfico** do valor e metadados mínimos (tipo, país, data, contador de trocas).
- **Unicidade entre USIs.** Para impedir que o mesmo CPF seja vinculado a dois USIs, o registro guarda um *nullifier* do identificador. Atenção: CPFs e números de documento têm um espaço pequeno de valores possíveis, e um *hash* simples seria revertido por força bruta (ataque de dicionário). Hipótese: calcular o *nullifier* com uma **função pseudoaleatória oblívia (OPRF) cuja chave é dividida entre vários operadores** (criptografia de limiar), com limite de consultas, de modo que nenhum operador, sozinho, consiga testar CPFs. 🔴 Isso vale também para o *nullifier* documental (seção 9.2.2).
- **Apresentação.** O titular revela o valor que quiser (por exemplo, o CPF) e prova, em conhecimento zero, que é o valor vigente no *slot* do seu USI, com confiança igual ou superior à exigida, sem revelar mais nada.

**9.7.3 Confiança do atributo**

É uma dimensão **separada** dos níveis de garantia de pessoa única (seção 9.3): aqueles dizem "é um humano único"; esta diz "este nome/CPF pode ser aceito como verdadeiro". Níveis indicativos, a calibrar:

| Nível | Nome | Requisito indicativo |
|---|---|---|
| **C0** | Declarado | Informado pelo titular, sem verificação |
| **C1** | Verificado | Um emissor qualificado verificou e atestou |
| **C2** | Corroborado | Dois ou mais emissores **independentes** |
| **C3** | Confiável | Três ou mais emissores independentes, ou dois mais prova documental criptográfica |
| **C4** | Autoritativo | Prova criptográfica da fonte primária (por exemplo, documento com chip emitido pelo Estado) mais corroboração |

A pontuação depende de:
- **quantos emissores independentes** atestaram (independente = sem controle societário ou operacional comum);
- **o tipo de emissor**: fonte primária (quem criou o identificador, como o Estado), instituição regulada com dever legal de verificar clientes (como bancos), outros;
- **o método de verificação** declarado na atestação: consulta a fonte oficial, conferência de documento, autodeclaração;
- **o tempo** (as atestações envelhecem e podem exigir renovação);
- **revogações e contestações**: um emissor que descobre fraude pode retirar a atestação, e a confiança cai.

*Privacidade das atestações.* Mostrar publicamente que "o Banco X atestou o CPF do USI Y" revelaria com que instituições a pessoa se relaciona. Hipótese: atestações anônimas, em que o titular prova que um emissor credenciado atestou o atributo, sem revelar qual, e um *nullifier* por emissor impede a contagem dupla. 🔴

**9.7.4 Fluxo de exemplo: João**
1. **Cadastro.** João informa nome, data de nascimento, CPF e documentos. A carteira lê documentos com chip sempre que possível, para reduzir erros de digitação, e **avisa claramente que esses atributos são chave e não podem ser alterados sem perder a confiança**. Enquanto nenhum emissor atestou (C0), João pode corrigir erros livremente.
2. **Primeira atestação.** Ao abrir conta (ou ao vincular seu USI à conta) no Banco A, João apresenta nome e CPF. O banco, que já é obrigado por lei a verificar o cliente, confere e emite uma atestação assinada. O atributo vai a C1.
3. **Corroboração.** Outros bancos e instituições repetem o processo. Com emissores independentes suficientes, o atributo chega a C2 e C3.
4. **Uso.** Dali em diante, ao apresentar seu USI com o CPF, qualquer contraparte pode aceitar o CPF e o nome como verdadeiros, conforme o nível que exigir. Outro banco não receberia a informação de que João se chama "José" ou tem outro CPF, porque só existe um valor vigente por *slot*.
5. **Alteração.** Se João tentar trocar o CPF depois de atestado, o novo valor nasce em C0, o histórico de trocas é preservado (contador) e ele precisa passar por todo o processo de novo. Verificadores podem exigir "sem trocas recentes".

**9.7.5 O que o USI garante e o que não garante**
- Garante a **unicidade** (um valor vigente por tipo e uma versão por identificador) e **mede a confiança** a partir de emissores independentes.
- **Não garante a veracidade.** Se emissores independentes forem enganados por documentos falsos de boa qualidade, uma **identidade sintética** pode atingir confiança alta. Defesas: qualidade e responsabilização dos emissores (cada um responde legal e reputacionalmente pelo que atesta), prova criptográfica sempre que existir, e contestação (seção 9.4).
- Quem registra um nome ou CPF falsos (o "José que quer ser Paulo") precisa enganar vários emissores independentes e depois **fica preso a essa identidade**: não pode ter outro USI e não consegue voltar a ser reconhecido como José sem perder a confiança ganha.

**9.7.6 Ataque de ocupação de identidade alheia (*squatting*)**

CPFs e números de documentos não são segredos. Um fraudador pode tentar registrar primeiro o CPF de outra pessoa. Se valesse "quem chegou primeiro", a vítima ficaria impedida de registrar a própria identidade. Regra proposta: **evidência mais forte vence, e não a ordem de chegada**.
- Um atributo apenas declarado (C0) **não bloqueia** o identificador. Quem apresentar prova criptográfica do documento original (seção 9.2.2), ou atingir confiança maior, assume o *slot*; o registro anterior é marcado como disputado e suspenso.
- Disputas entre evidências comparáveis vão a **júri**, com presença física quando necessário (seção 9.4).
- Os atestadores do registro derrubado perdem reputação.

**9.7.7 Casos especiais: nome social e mudança legal de nome**
- **Nome oficial e nome social** são atributos distintos. O nome social é declarado, **nunca atinge confiança "oficial"** e é sempre apresentado com um **rótulo de tipo**, de modo que o verificador saiba se recebeu o nome oficial ou o social.
- **Mudança legal** (decisão judicial ou administrativa, casamento, retificação). Há um caminho próprio, **alteração oficial**: o titular apresenta evidência do ato legal (novo documento emitido pela autoridade, via perfil de país). O novo nome nasce com confiança proporcional à força dessa evidência (documento com chip: alta; apenas papel: sobe com as atestações dos emissores), e o USI mantém **continuidade** (mesmo USI e demais atributos). Durante o período transitório, a confiança do novo nome vai subindo.
- **Dignidade e proteção (🔴).** Uma mudança legal de nome não deve expor o nome anterior nem revelar a terceiros que houve mudança. Isso pode colocar em risco pessoas trans, vítimas de violência que trocam de nome por proteção, entre outras. Hipótese: o histórico de trocas fica visível apenas ao titular e, em caso de contestação, ao júri; o contador "trocas recentes" que verificadores veem conta apenas as alterações **sem** ato legal. Esse desenho precisa ser discutido com organizações de direitos humanos antes de ser adotado.

**9.7.8 Relação com perfis de país e governos**

Onde há apoio de um governo (seção 14.5), credenciais assinadas pela **fonte primária** (documento com chip, credencial oficial) chegam diretamente a níveis altos de confiança (C3 ou C4). Onde não há, a confiança é construída por emissores secundários, como bancos. Em ambos os casos, o emissor é apenas um emissor: não adquire poder sobre as regras do sistema.

**9.7.9 Limites**
- Depende de emissores confiáveis e **independentes**. Um cartel ou conluio de emissores pode inflar a confiança. Mitigações: critérios públicos de independência, credenciamento transparente, auditoria amostral e perda de credenciamento.
- Quem credencia os emissores e com quais critérios é uma questão de governança em aberto (seção 14).
- Exige que a carteira comunique com clareza que os atributos-chave são permanentes, para evitar frustração do titular.

## 10. Recuperação de acesso

### 10.1 Princípio 🟢

Perder o acesso à identidade não pode ser definitivo, mas a recuperação é o caminho preferido dos atacantes. O USI resolve o dilema por **rotas paralelas**, cada uma com exigências e prazos de espera proporcionais à força da evidência, sempre sujeitas a **notificação e veto**.

### 10.2 Rotas 🟡

| Rota | Mecanismo | Exigência | Espera indicativa |
|---|---|---|---|
| **A – Outro dispositivo** | Chave ou passkey de outro aparelho já autorizado assina a troca de chave | Posse de dispositivo válido | Imediata |
| **B – Chave pré-rotacionada** | A chave de reserva, guardada offline, assume o controle | Posse do material de reserva | Curta (24–72 h) |
| **C – Recuperação social** | Quórum de **guardiões** escolhidos pelo titular (ex.: 3 de 5) autoriza a nova chave; o segredo de identidade pode ser reconstruído por compartilhamento de segredo de Shamir [8] | Quórum de guardiões | Média (≈ 7 dias) |
| **D – Revalidação de identidade** | O titular refaz a prova de que é a mesma pessoa, por meio das camadas de evidência (seção 9) | Evidência de nível alto **e** combinação com outra rota | Longa (≈ 30 dias) |

### 10.3 Regras comuns 🟢

1. **Notificação** imediata e redundante (todos os dispositivos, guardiões e canais cadastrados) a cada pedido.
2. **Veto:** durante a espera, qualquer chave legítima ainda ativa pode cancelar o pedido.
3. **Combinação encurta o prazo.** Exemplo: guardiões (C) + revalidação (D) reduzem a espera; rota única fraca aumenta.
4. **Congelamento de emergência**, pelo titular ou por quórum de guardiões, suspende o USI até a recuperação.
5. **Rotação obrigatória** após recuperação: todas as chaves antigas são revogadas e uma nova chave de reserva é registrada.
6. **Revisão periódica de guardiões** pela carteira.
7. **Limite de tentativas** e atraso crescente após pedidos negados.

### 10.4 Máquina de estados (resumo) 🟡

```
ATIVO ──(pedido de recuperação)──► EM_ESPERA ──(prazo cumprido, sem veto)──► RECUPERADO ──► ATIVO (chaves novas)
   │                                    │
   │                                    └──(veto de chave legítima)──► ATIVO (pedido cancelado, alerta)
   └──(congelamento)──► CONGELADO ──(descongelamento por quórum ou chave válida)──► ATIVO
```

### 10.5 Análise de ataques 🟡

| Ataque | Defesa |
|---|---|
| Atacante rouba um dispositivo e inicia recuperação | Notificação em canais independentes; veto por outras chaves; prazo de espera |
| Atacante compromete guardiões (conluio ou engenharia social) | Quórum com guardiões de círculos diferentes; prazo; veto do titular; guardiões não conhecem uns aos outros (opção) |
| Atacante forja revalidação | Exige evidência de nível alto **e** combinação com outra rota; prazo maior |
| Titular perde tudo e não tem guardiões | Rota D, mais lenta |
| Coação ao titular | Congelamento por terceiros e modo de emergência (🔴 em aberto) |
| Negação de serviço contra a recuperação | Múltiplos canais e rotas independentes |

### 10.6 Qual segredo se recupera? 🔴

A recuperação troca **chaves de controle**. Mas o **segredo de identidade**, base dos pseudônimos e *nullifiers* (seção 11.3), também precisa sobreviver. Se for perdido, o titular passaria a ter novos pseudônimos e poderia, em tese, burlar o limite de "uma conta por pessoa" em cada serviço. Hipóteses a avaliar: dividir o segredo de identidade entre guardiões (Shamir) e/ou em backup cifrado sob controle do titular; ou registrar "épocas" de segredo no registro, com regras para que serviços tratem transições sem permitir contas duplicadas. Esta é uma das questões de projeto mais importantes do protocolo.

### 10.7 Experiência de uso 🟡

A segurança de qualquer esquema de recuperação depende de que as pessoas consigam usá-lo. A carteira deve guiar a configuração inicial (escolha de guardiões, backup da chave de reserva), testar periodicamente a recuperação ("simulado") e ser compreensível para quem tem baixa familiaridade técnica.

## 11. Privacidade

### 11.1 Princípios 🟢

- **Nenhum dado pessoal no registro público.**
- **Divulgação mínima** como padrão: revelar só o que o verificador precisa.
- **Não correlacionabilidade** entre serviços.
- **Privacidade desde a concepção** (*privacy by design*) e por padrão.

### 11.2 Divulgação seletiva e provas de conhecimento zero 🟢

- **Credenciais verificáveis** (W3C VC [9]) emitidas por quem tem autoridade sobre o fato.
- **Divulgação seletiva** (por exemplo, SD-JWT ou assinaturas BBS) para revelar apenas campos específicos.
- **Provas de conhecimento zero** para afirmações derivadas: "tenho mais de 18 anos", "moro neste município", "sou um humano único neste serviço".
- **Protocolos de apresentação** compatíveis com padrões abertos (por exemplo, OpenID for Verifiable Presentations), facilitando integração com serviços existentes.

### 11.3 Pseudônimos e *nullifiers* por serviço 🟡

Para cada verificador (identificado por um identificador público), a carteira calcula:

- um **pseudônimo** `P = PRF(segredo_de_identidade, id_do_verificador)`, estável para aquele serviço, mas sem relação aparente com os de outros;
- um ***nullifier*** associado, que o verificador usa para detectar que o mesmo titular não abriu duas contas.

A prova de conhecimento zero demonstra que `P` foi derivado corretamente de um USI ativo, com o nível exigido, **sem revelar o USI**. Dois verificadores que comparem seus dados não conseguem concluir que se trata da mesma pessoa.

**Ressalva importante:** a não correlacionabilidade depende de **disciplina de implementação** (por exemplo, não vazar o USI em metadados de rede, em chaves de credenciais ou em tempo de apresentação), e deve ser objeto de revisão específica.

### 11.4 Compartilhamento por tempo limitado 🟡

O titular concede acesso a dados com prazo, finalidade e escopo; a revogação encerra o acesso contínuo. **Limitação explícita**: não é possível retirar o que já foi visto ou copiado. A interface deve deixar isso claro. Mecanismos como credenciais de curta duração e provas em vez de cópias reduzem a superfície de exposição.

### 11.5 Registro de consentimentos 🟢

A carteira mantém, sob controle exclusivo do titular, um histórico de quem acessou o quê, quando e com qual finalidade.

### 11.6 Conformidade legal 🟡

O projeto considera desde o início a LGPD [5] e legislações equivalentes (por exemplo, o GDPR europeu):

| Tema | Abordagem |
|---|---|
| **Minimização** | Nenhum dado pessoal no registro; credenciais fora da cadeia |
| **Eliminação** | Possível, pois os dados estão na carteira e em emissores, não no registro imutável |
| **Consentimento e finalidade** | Compartilhamento sempre por ato do titular, com finalidade declarada |
| **Dados sensíveis (biometria)** | Opcional; só com salvaguardas reforçadas e auditoria |
| **Controlador e operadores** | Análise necessária: os operadores do registro tratam dados pessoais? O desenho busca que **não**, mas isso exige parecer jurídico |
| **Relatório de impacto** | Elaborar e publicar relatório de impacto à proteção de dados antes do piloto |
| **Transferência internacional** | Análise de conformidade com cada jurisdição dos operadores |

Esta seção exige **revisão de especialistas em direito digital**.

### 11.7 Metadados e rede 🔴

Mesmo sem dados pessoais, **metadados** (endereços de rede, horários, padrões de uso) podem identificar pessoas. É preciso estudar: apresentação sem contato direto com o registro, uso de relays e redes de anonimato, agrupamento de eventos em lotes para reduzir a correlação temporal.

## 12. Segurança operacional e criptografia

### 12.1 Boas práticas exigidas 🟢

- Implementações de referência em linguagens seguras quanto à memória, sempre que possível.
- Uso exclusivo de primitivas padronizadas e bibliotecas revisadas; **nunca criptografia própria**.
- Construções criptográficas novas (circuitos de conhecimento zero, protocolos de nullifier, derivação de pseudônimos) devem ter **especificação formal** e **revisão independente**.
- **Compilações reproduzíveis** e assinatura de versões.
- Programa de divulgação responsável de vulnerabilidades.

### 12.2 Auditorias 🟢

Nenhum componente será usado com pessoas reais antes de **auditoria independente**, com relatório público. Auditorias se repetem a cada mudança significativa.

### 12.3 Custódia de chaves e experiência 🟡

A maior parte das perdas de identidade digital decorre de falhas de usabilidade. O projeto adotará armazenamento em chip seguro do dispositivo, autenticação biométrica **local** (que não deixa o aparelho), backup cifrado opcional e orientações claras.

### 12.4 Migração criptográfica 🟡

O protocolo prevê desativar algoritmos comprometidos por decisão de governança, com período de transição e rotação de chaves coordenada, sem alterar o USI.

## 13. Sustentabilidade

### 13.1 Por que não replicar o modelo do Bitcoin 🟢

O Bitcoin remunera mineradores porque precisa de consenso, entre desconhecidos hostis, sobre algo cuja fraude gera lucro imediato (dinheiro). O USI não é dinheiro; seu registro é enxuto (seção 8.3), pode ser verificado por clientes leves e **não exige que milhões de pessoas guardem uma cópia**. Basta um conjunto **moderado de operadores independentes**, como ocorre com infraestruturas públicas da internet (servidores raiz do DNS, logs de Certificate Transparency [6], sincronização de tempo, entre outras).

### 13.2 Custos 🟡

| Categoria | Observação |
|---|---|
| Operação de nós do registro | Distribuída entre operadores; custo por operador moderado, a medir |
| Âncoras em rede pública (se aplicável) | Mitigado por agregação em lotes |
| Desenvolvimento e manutenção | Voluntário e/ou financiado por bolsas |
| Auditorias de segurança | Custo relevante e recorrente |
| Cerimônias presenciais e apoio a validadores | Logística, treinamento, acessibilidade |
| Suporte, documentação e tradução | Esforço contínuo |
| Assessoria jurídica | Especialmente no início |

Uma etapa do plano é **estimar esses custos com números**, inclusive o custo anual por operador de nó (experimento E1).

### 13.3 Fontes de sustentação a testar 🟡

1. **Operadores institucionais que se beneficiam:** empresas que gastam com KYC e fraude, universidades, ONGs, bibliotecas, órgãos públicos.
2. **Taxa de verificação paga por quem verifica (nunca pelo cidadão):** serviços que consomem verificações em grande volume pagam um valor mínimo, destinado à manutenção e transparente.
3. **Bolsas, editais e doações** de fundações e programas de apoio à infraestrutura aberta e a direitos digitais.
4. **Voluntariado** no desenvolvimento, motivado por propósito, aprendizado e reputação.

**Compatibilização com o princípio "sem lucro":** o que o projeto veda é lucro para fundadores, investidores e mantenedores e a criação de ativo financeiro. Receitas que cubram **custos operacionais**, geridas de forma transparente por uma fundação sem fins lucrativos, são compatíveis com esse princípio.

### 13.4 Por que não haverá token 🟢

Um token criaria incentivo financeiro para fraudar o cadastro e para vender identidades, atrairia especulação e deslocaria o foco para o preço. Também deixaria o titular exposto a obrigações fiscais e regulatórias. Os incentivos do USI são institucionais e reputacionais, não monetários.

### 13.5 Transparência 🟢

Receitas, despesas e remunerações (se houver, para serviços contratados) são públicas, com prestação de contas periódica e auditoria externa.

## 14. Governança

### 14.1 Fases 🟡

| Fase | Quem decide | Critérios objetivos para avançar (a definir) |
|---|---|---|
| **0 – Concepção** | Fundador e núcleo inicial | Whitepaper publicado e revisado por especialistas independentes |
| **1 – Fundação** | Fundação sem fins lucrativos com conselho que representa grupos de stakeholders | Rede em produção com operadores independentes em ao menos *N* países; auditorias concluídas; piloto bem-sucedido |
| **2 – Comunidade** | Comunidade de titulares e contribuidores, via processo aberto | Nenhuma entidade isolada (incluindo a fundação) consegue alterar regras unilateralmente; o fundador se retira |

O desligamento do fundador é **objetivo** e **condicional a métricas** (por exemplo, quantidade de mantenedores independentes, diversidade de operadores, ausência de ponto único de falha de decisão), evitando tanto o vácuo de governança quanto a perpetuação.

### 14.2 Mecanismos 🟡

- **Propostas de melhoria (USIPs):** documentos públicos, versionados no repositório, com estados (rascunho, em discussão, aceita, rejeitada), inspirados em BIPs e RFCs da IETF.
- **Consenso técnico aproximado** em decisões de especificação, com revisão por pares.
- **Voto "uma pessoa, um voto"** com o próprio USI, para decisões que afetam a comunidade, quando a rede estiver madura. Antes disso, não há votação por USI.
- **Separação de poderes:** quem desenvolve não opera sozinho; quem opera não decide sozinho; quem financia não controla.
- **Transparência obrigatória:** reuniões, decisões e votos públicos (com ressalva para segurança).

### 14.3 Resistência à captura 🟡

- Limites de concentração: nenhum operador, país ou organização pode controlar mais que uma fração do conjunto de operadores (por exemplo, abaixo de 1/3).
- Diversidade geográfica, jurídica e institucional exigida.
- Mandatos limitados e rotatividade em funções-chave.
- Mudanças em regras críticas exigem supermaioria e período de espera público.
- Plano de **bifurcação** (*fork*) honesta: se a governança falhar, a comunidade deve conseguir reproduzir o sistema a partir do código e dos dados abertos.

### 14.4 Conflito entre "sem dono" e responsabilidade 🔴

Um sistema sem dono precisa de alguma entidade jurídica para firmar contratos, receber doações, responder a autoridades e contratar auditorias. A fundação cumpre esse papel, mas precisa ser projetada para **não** ser um ponto de controle. A forma jurídica e a jurisdição são questões em aberto, inclusive se a fundação deve ficar na jurisdição do piloto (Brasil) ou numa jurisdição neutra, para evitar a percepção de controle nacional.

### 14.5 Papel dos governos: apoio sem controle 🟡

Governos podem ser aliados valiosos e, ao mesmo tempo, são os atores com maior capacidade de captura. O USI adota a postura **apoio sim, controle não**, em termos iguais para qualquer governo.

**O que um governo pode fazer (opcional):**
- qualificar o perfil de país dos seus documentos: publicar formatos, chaves públicas e listas de revogação, esclarecer identificadores estáveis;
- operar nós **como qualquer outro operador**, sujeito aos limites de concentração (seção 14.3);
- ceder espaços públicos (bibliotecas, agências de atendimento) para cerimônias presenciais;
- reconhecer o USI para finalidades específicas, e apoiar o projeto com financiamento ou assessoria jurídica.

**O que um governo não pode fazer:**
- ter voto especial, veto, assento garantido ou qualquer outro privilégio na governança;
- alterar regras, eventos ou o estado de qualquer USI;
- acessar dados dos titulares. O sistema é concebido para que a verificação dos documentos seja feita **localmente, com dados públicos** (chaves e listas de revogação), **sem consulta online ao governo**, de modo que o Estado não saiba quem usa o USI nem onde;
- condicionar o apoio a exclusividade, a obrigatoriedade de uso ou a funcionalidades de vigilância.

**Salvaguardas:**
1. O sistema continua funcionando se o apoio for retirado: cai apenas o peso da camada documental daquele país, e as demais camadas compensam.
2. Todos os acordos, contribuições e comunicações com governos são públicos.
3. Há critérios públicos para aceitar, ponderar ou recusar o perfil de um país, inclusive quando o Estado emite documentos de forma abusiva, usa o apoio para vigilância ou pode colocar titulares em risco.
4. Os limites de concentração valem para entidades ligadas a um mesmo Estado.
5. O apoio de um governo não torna o projeto "brasileiro" ou de qualquer outro país.

No Brasil, o apoio do governo é bem-vindo, mas **não é pré-requisito** para o piloto.

## 15. Adoção e estratégia de entrada

### 15.1 O problema do ovo e da galinha 🟢

Uma identidade só tem valor se aceita, e só é aceita se for amplamente portada. Estratégia: começar por **nichos em que o USI resolve uma dor real que as alternativas não resolvem**, e crescer a partir deles.

### 15.2 Nichos prioritários 🟡

| Prioridade | Caso de uso | Por que |
|---|---|---|
| 1 | **Prova de humanidade** (anti-bot e anti-agente) | Dor imediata e crescente; exige pouca informação pessoal; tolera níveis básicos |
| 2 | **Votações comunitárias e cooperativas** | "Uma pessoa, um voto" é necessidade explícita |
| 3 | **Distribuição de doações e benefícios** sem duplicidade | Parceria com organizações humanitárias |
| 4 | **Verificação de idade** sem exposição de dados | Demanda regulatória crescente |
| 5 | **Pessoas sem documento** | Missão do projeto; depende de parceiros de campo |
| 6 | **Login sem senha** | Reduz dependência de plataformas |
| 7 | **Credenciais acadêmicas e profissionais** | Valor agregado após a base de usuários existir |

### 15.3 Facilitar a integração 🟡

- Pontes para padrões amplamente usados (por exemplo, ponte compatível com OpenID Connect), para que um serviço integre o USI sem reescrever sua autenticação.
- Bibliotecas e SDKs abertos, documentação e exemplos.
- Tradução de documentação e interfaces (a política bilíngue do repositório é o primeiro passo).

### 15.4 Estratégia de crescimento 🟡

1. **Piloto fechado** com uma comunidade parceira e um caso de uso.
2. **Expansão por comunidades** (cooperativas, associações, projetos de código aberto).
3. **Integrações** com plataformas de baixo atrito.
4. **Reconhecimento institucional** (universidades, ONGs, órgãos públicos) depois de demonstrada a robustez.

Medir sempre: adesão, retenção, fraude detectada, taxa de recuperação bem-sucedida, tempo de cadastro, custo por titular.

### 15.5 Piloto no Brasil e expansão internacional 🟡

**Piloto no Brasil.**
- Levantar os documentos brasileiros candidatos (por exemplo, a carteira de identidade nacional, o passaporte com chip e a habilitação digital) e verificar, para cada um, **se é possível a verificação criptográfica offline** e **qual é o identificador estável da pessoa**. Contas de serviços governamentais digitais podem ser avaliadas como evidência complementar. *Todos esses pontos precisam de confirmação técnica a partir das especificações oficiais.*
- Dialogar com a autoridade de proteção de dados (ANPD) e, quando oportuno, com órgãos públicos, pedindo apoio à qualificação do perfil de país **sem contrapartida de controle** (seção 14.5).
- Formar a primeira rede de parceiros: universidades, bibliotecas, cooperativas, organizações da sociedade civil.

**Expansão internacional.** A ordem de entrada dos países é determinada pela adesão de stakeholders locais, não por um plano central. Para que um país seja incluído, propõe-se um roteiro público:
1. ao menos um stakeholder local comprometido com o apoio;
2. perfil de país elaborado e revisado, com verificação criptográfica dos documentos testada;
3. análise jurídica local (proteção de dados, regulação de identidade);
4. validadores presenciais locais;
5. tradução e adaptação de interface e documentação;
6. avaliação de riscos a direitos humanos (países onde o uso do USI poderia colocar titulares em perigo);
7. aprovação por USIP.

## 16. Plano de validação experimental

Para evitar decisões baseadas em palpites, o projeto propõe uma série de experimentos, cada um com **hipótese, método e critério de sucesso**.

| ID | Experimento | Hipótese | Método resumido | Critério de sucesso (indicativo) |
|---|---|---|---|---|
| E1 | **Custo e desempenho do registro** | A opção C atende aos requisitos R1–R8 a custo viável | Protótipos das opções A, B e C com carga simulada; medir custo por evento, latência, tamanho e custo de operação | Custo por titular desprezível; latência aceitável; verificação leve em dispositivos modestos |
| E2 | **Resistência do grafo a Sybil** | Análise estrutural detecta grupos falsos com alta precisão | Simular redes honestas e ataques (agrupamentos, infiltração, humanos de aluguel) e medir detecção | Alta detecção com baixa taxa de falsos positivos em cenários definidos |
| E3 | **Calibração dos níveis** | É possível definir níveis que equilibrem inclusão e segurança | Simulação com diferentes pesos; análise de sensibilidade | Níveis estáveis sob variações razoáveis dos parâmetros |
| E4 | **Prova documental com ZK** | Provar autenticidade e gerar *nullifier* é viável em dispositivos comuns | Protótipo com documentos de teste e verificação em celular | Tempo de prova aceitável; sem vazamento; tratamento do caso "múltiplos documentos" |
| E5 | **Protocolo de recuperação** | As quatro rotas funcionam em paralelo sem abrir brechas | Implementação, testes com adversário simulado (red team), simulação de perda de dispositivos | Nenhum sequestro bem-sucedido nos cenários definidos; alta taxa de recuperação legítima |
| E6 | **Usabilidade da recuperação** | Pessoas leigas conseguem configurar guardiões e backups | Testes de usabilidade com participantes diversos, inclusive de baixa familiaridade técnica | Taxa alta de configuração correta; baixa taxa de abandono |
| E7 | **Pseudônimos e não correlacionabilidade** | Serviços distintos não conseguem correlacionar o mesmo titular | Análise formal e testes de correlação, inclusive por metadados | Nenhum vetor de correlação prático identificado |
| E8 | **Júri de contestação** | Júris sorteados decidem bem e resistem a conluio | Simulações e piloto com casos sintéticos | Taxas de erro e de manipulação abaixo do limite estabelecido |
| E9 | **Segredo de identidade na recuperação** | Dá para recuperar o segredo sem permitir contas duplicadas | Comparar variantes (Shamir, backup cifrado, épocas) | Variante que preserva pseudônimos e impede duplicação |
| E10 | **Cerimônias presenciais** | Cerimônias escalam e resistem a conluio local | Piloto em uma comunidade parceira | Custo por pessoa viável; conluio detectado em auditoria amostral |
| E11 | **Biometria sem base central** (opcional) | É viável com privacidade comprovada | Estudo de viabilidade e revisão por especialistas | Se não houver variante segura e precisa, **descartar** |
| E12 | **Sustentabilidade** | Taxas de verificação cobrem custos operacionais | Modelo financeiro e consulta a potenciais operadores e verificadores | Cobertura de custos sem exigir pagamento do titular |
| E13 | **Perfil de país: Brasil** | É possível verificar documentos brasileiros de forma criptográfica e offline e derivar um identificador estável da pessoa | Levantamento das especificações oficiais; protótipo de verificação; consulta a especialistas | Ao menos um documento verificável offline com identificador estável, ou conclusão documentada de que não é possível |
| E14 | **Vínculo de atributos (criptografia)** | É possível registrar *slots* com compromisso, unicidade por OPRF de limiar e prova de vigência em conhecimento zero, com custo viável | Protótipo do *slot*, do *nullifier* com OPRF dividida entre operadores e da apresentação; teste de ataque de dicionário e de privacidade das atestações | Nenhum vazamento de valores por força bruta nos cenários testados; provas em tempo aceitável em celular |
| E15 | **Modelo de confiança do atributo** | Emissores independentes elevam a confiança de forma confiável e o modelo resiste a ocupação, conluio e identidade sintética | Simulação de emissores honestos e fraudulentos, ataques de ocupação, cartéis e identidades sintéticas; teste com casos de mudança legal de nome | Alta detecção com baixos falsos positivos; nenhum caminho de ocupação sem contestação possível |

Resultados e dados dos experimentos serão **publicados**, inclusive os negativos.

## 17. Riscos do projeto

| Risco | Probabilidade | Impacto | Resposta |
|---|---|---|---|
| Baixa adoção (ovo e galinha) | Alta | Alto | Nichos iniciais, integração fácil, parceiros |
| Escassez de voluntários e de financiamento | Alta | Alto | Foco em bolsas/editais, escopo enxuto, parcerias institucionais |
| Incompatibilidade jurídica (LGPD, regulação de identidade, biometria) | Média | Alto | Parecer jurídico cedo, privacidade desde a concepção, piloto controlado |
| Ataques Sybil sofisticados e mercado de identidades | Alta | Alto | Múltiplas camadas, contestação, níveis, monitoramento |
| Falha de segurança em componente criptográfico | Média | Muito alto | Revisão, auditoria, especificação formal, programa de vulnerabilidades |
| Captura da governança | Média | Alto | Fases, limites de concentração, transparência |
| Excesso de escopo | Alta | Médio | Começar por MVP restrito (prova de humanidade), cortar o que não for essencial |
| Percepção de "identificação obrigatória" ou vigilância | Média | Alto | Não obrigatoriedade, comunicação clara, pseudônimos por serviço |
| Dependência de terceiros (rede pública, cadeias de certificados estatais) | Média | Médio | Opção híbrida, ponderação por país, plano de contingência |
| Coação de usuários vulneráveis | Média | Alto | Modo de emergência (em estudo), congelamento por terceiros |
| Percepção de controle por um governo, ou captura pelo Estado apoiador | Média | Alto | Apoio sem controle (seção 14.5), limites de concentração, acordos públicos, jurisdição neutra a considerar |
| Retirada do apoio governamental ou mudança de política | Média | Médio | Sistema funciona sem o apoio; peso da camada documental ajustável |
| Atalhos específicos do Brasil que não se generalizam | Média | Médio | Perfis de país plugáveis; revisão de arquitetura antes da expansão |
| Ocupação de identificadores alheios (*squatting*) | Alta | Alto | Evidência mais forte vence, não a ordem de chegada; contestação e júri (seção 9.7.6) |
| Identidade sintética com documentos falsos de boa qualidade | Média | Alto | Emissores responsáveis, prova criptográfica, contestação, revogação de atestações |
| Conluio ou cartel de emissores | Média | Alto | Critérios públicos de independência, credenciamento transparente, auditoria |
| Exposição de pessoas por histórico de mudança de nome | Média | Muito alto | Histórico visível só ao titular e ao júri; consulta a organizações de direitos humanos |

## 18. Questões em aberto

1. Qual opção de registro (A, B ou C) é a melhor? (E1)
2. Como calibrar pesos e limiares dos níveis de garantia? (E3)
3. Qual a resistência real do grafo social contra ataques organizados? (E2)
4. Como tratar quem tem múltiplos documentos válidos? (E4)
5. Biometria sem base central é viável e desejável? (E11)
6. Quais prazos equilibram segurança e conveniência na recuperação? (E5, E6)
7. Como proteger o segredo de identidade na recuperação, sem permitir contas duplicadas? (E9)
8. Como estruturar júris resistentes a conluio e escaláveis? (E8)
9. Como tratar óbito, inatividade e herança digital?
10. Como proteger pessoas sob coação?
11. Como reduzir a exposição por metadados de rede?
12. Qual forma jurídica e jurisdição para a fundação?
13. Quais critérios numéricos marcam as transições de fase da governança?
14. Como incluir pessoas sem smartphone ou com conectividade limitada?
15. O modelo de taxa de verificação é compatível com o princípio de não lucro e com a neutralidade do sistema?
16. Como tratar a dupla nacionalidade entre países sem expor a dupla cidadania a nenhum Estado? (E4, E13)
17. Quais critérios públicos aceitam, ponderam ou recusam o perfil de um país, inclusive por risco a direitos humanos?
18. A fundação deve ter sede na jurisdição do piloto (Brasil) ou numa jurisdição neutra?
19. Como calcular a unicidade de identificadores de espaço pequeno (CPF, números de documento) sem permitir ataque de dicionário? (E14)
20. Como registrar atestações sem revelar a relação do titular com cada emissor? (E14)
21. Como definir "emissor independente", quem credencia os emissores e como evitar conluio? (E15)
22. Como permitir a mudança legal de nome sem expor o histórico do titular? (E15)
23. Como corresponder nomes entre documentos (acentos, abreviações, transliteração)?

## 19. Roteiro

| Etapa | Entregas |
|---|---|
| **1. Whitepaper** | Versão 0.1 (este documento); revisão aberta; versão 0.2 com contribuições |
| **2. Comunidade e revisão** | Revisão por especialistas; apresentação a comunidades de identidade descentralizada; núcleo inicial de colaboradores |
| **3. Organização do repositório** | Licenças, `CONTRIBUTING`, código de conduta, processo de USIPs, *issues* para cada questão em aberto |
| **4. Provas de conceito** | Experimentos E1–E15 conforme prioridade |
| **5. Análise jurídica e institucional** | Parecer sobre LGPD e outras normas; desenho da fundação |
| **6. Financiamento e divulgação** | Submissão a editais; materiais de divulgação; busca de parceiros |
| **7. Piloto (Brasil)** | Caso de uso inicial com comunidade parceira no Brasil; métricas; relatório público; roteiro de entrada de novos países |
| **8. Institucionalização** | Fundação constituída; transição para a fase 1 de governança |

Não há datas fixas nesta versão: o cronograma depende da formação da comunidade e do financiamento.

## 20. Como contribuir com este documento

Este é um rascunho aberto. Para contribuir:

- **Revisão crítica:** abra uma *issue* apontando erros, lacunas ou riscos que faltam. Críticas fundamentadas são bem-vindas.
- **Referência a fontes:** a seção 5 e as afirmações técnicas precisam de fontes primárias; ajude a verificar e acrescentar.
- **Especialistas:** criptografia, sistemas distribuídos, identidade digital, direito de proteção de dados, design de experiência, antropologia/ciências sociais (para inclusão), ética.
- **Experimentos:** assuma um dos experimentos E1–E15.
- **Tradução e revisão linguística:** mantenha as versões em português e em inglês sincronizadas.

Todas as alterações significativas devem ser registradas no histórico de versões (seção 22).

## 21. Referências

> Lista inicial; as referências devem ser conferidas e completadas com links e versões exatas em edições futuras.

1. W3C. *Decentralized Identifiers (DIDs) v1.0*. Recomendação do W3C, 2022.
2. FIDO Alliance; W3C. *Web Authentication (WebAuthn)* e especificações FIDO2.
3. S. Smith. *Key Event Receipt Infrastructure (KERI)*. arXiv:1907.02143.
4. NIST. *FIPS 204: Module-Lattice-Based Digital Signature Standard (ML-DSA)*. 2024.
5. Brasil. *Lei nº 13.709/2018 (Lei Geral de Proteção de Dados Pessoais)*.
6. B. Laurie, A. Langley, E. Kasper. *RFC 6962: Certificate Transparency*. IETF, 2013.
7. Q. Cao, M. Sirivianos, X. Yang, T. Pregueiro. *Aiding the Detection of Fake Accounts in Large Scale Social Online Services* (SybilRank). NSDI, 2012.
8. A. Shamir. *How to Share a Secret*. Communications of the ACM, 1979.
9. W3C. *Verifiable Credentials Data Model*. Recomendação do W3C.
10. J. Douceur. *The Sybil Attack*. IPTPS, 2002.

## 22. Histórico de versões

| Versão | Data | Descrição |
|---|---|---|
| 0.1 | 2026-10-23 | Primeiro rascunho, aberto à colaboração. |
| 0.1.1 | 2026-10-23 | Premissa geográfica (piloto no Brasil, desenho sem fronteiras), perfis de país, papel dos governos (apoio sem controle), experimento E13. |
| 0.1.2 | 2026-10-24 | Vínculo entre USI e atributos de identidade (seção 9.7): atributos-chave, confiança do atributo, ocupação de identidade, nome social e mudança legal de nome; experimentos E14 e E15. |
