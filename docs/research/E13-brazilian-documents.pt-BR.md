# E13: levantamento técnico dos documentos brasileiros

🌐 [English](E13-brazilian-documents.md) · **Português (Brasil)**

**Versão 0.1 (levantamento inicial) · 29 de outubro de 2026**
Experimento E13 do [whitepaper](../whitepaper.pt-BR.md) (seções 9.2.2 e 15.5) · Issue [#13](https://github.com/gstulli/universal_safe_id/issues/13)

> ⚠️ **Levantamento inicial, feito por busca pública e leitura de páginas e resoluções, com auxílio de IA. Não foi revisado por especialistas.** Parte das informações vem de reportagens e de resumos de busca, não das especificações técnicas oficiais, que não foram localizadas. **Nada aqui deve ser tomado como definitivo.** Cada afirmação indica a qualidade da fonte (ver legenda). Correções são bem-vindas.

**Legenda das fontes:** **[P]** fonte primária lida diretamente · **[O]** página oficial lida diretamente · **[S]** fonte secundária ou resumo de busca, sem leitura do original · **[?]** não encontrado.

## 1. Pergunta

A hipótese do E13 é: *documentos brasileiros podem ser verificados criptograficamente e offline, e deles se pode derivar um identificador estável da pessoa.* O critério de sucesso é encontrar **ao menos um documento verificável offline com identificador estável**, ou documentar que isso não é possível.

## 2. Resumo

**Conclusão provisória: há candidatos promissores, mas a hipótese ainda não está confirmada.** O CPF é, por lei, o número único da pessoa e consta nos documentos novos, o que resolve bem a parte do **identificador estável**. O que falta é confirmar **como cada documento é assinado e como se verifica essa assinatura offline**: para o passaporte há uma fonte primária (de 2013) que descreve a cadeia de certificados; para a CIN e a CNH digital só encontramos descrições gerais.

| Documento | Identificador estável | Verificação offline? | Verificação criptográfica documentada? | Situação |
|---|---|---|---|---|
| **CIN** (Carteira de Identidade Nacional) | **CPF**, número único por lei [O][S] | Parcial, pelo QR Code: CPF, data de nascimento e validade [S] | **Não encontrada** (formato e assinatura do QR Code não localizados) [?] | Candidata promissora; falta a especificação |
| **Passaporte** (com chip) | Número do passaporte muda a cada via; presença do CPF no chip **não verificada** [?] | Em princípio sim, pelo padrão ICAO | **Sim, em parte:** assinado com certificados da ICP-Brasil; autoridade raiz própria para o diretório da ICAO (2013) [P] | Candidato promissor; falta saber se o CPF consta e a situação atual no diretório da ICAO |
| **CNH digital** | CPF consta na CNH [S] | Sim, pelo QR Code, segundo portaria de 2017 [S] | Descrita em 2017: assinatura com certificado por Detran, guardado em módulo de hardware no Serpro [S] | Candidata; informação antiga, precisa de confirmação atual |
| **Conta gov.br** (bronze, prata, ouro) | CPF | **Não** (serviço online) | Não se aplica | Evidência complementar |
| **Certificado e-CPF / e-CNPJ** (ICP-Brasil) | CPF (ou CNPJ) no certificado, a confirmar | Sim (assinatura X.509) | Sim, padrão ICP-Brasil | Candidato técnico; exige compra e renovação pelo titular |

## 3. Detalhes por documento

### 3.1 CIN: Carteira de Identidade Nacional

- **Base legal.** O Decreto nº 10.977/2022 criou a CIN [S]. A Lei nº 14.534/2023 estabelece o **CPF como número único e suficiente** para identificar o cidadão em bancos de dados de serviços públicos, e determina que os órgãos emissores usem o CPF como número de registro geral nos documentos novos [S, via resumo de busca do texto da lei; confirmar no texto oficial no Planalto].
- **Página oficial** [O]: a CIN existe em formato **físico e digital**, "tem QR code", **usa o CPF como número único** e substitui o RG. A página **não** descreve o conteúdo do QR Code, a verificação, a presença de chip nem padrões técnicos.
- **Material e QR Code** [S, enciclopédia]: papel filigranado ou cartão de policarbonato; QR Code no verso para validação; **código MRZ** (zona legível por máquina) para confirmar a autenticidade fora do país; **chip não mencionado** para a CIN atual. A versão digital, no celular, teria uma cópia com "certificação digital", exportação em PDF e página de validação por QR Code.
- **Verificação** [S]: um aplicativo oficial ("Leitura de QR Code") tem dois modos. O **offline (parcial)** mostra CPF, data de nascimento e validade; o **online (completo)** mostra também foto, nome, filiação e naturalidade, exige conexão e, segundo um dos resultados, conta gov.br. Essa descrição vem de uma memória de reunião do governo federal de dezembro de 2024, vista apenas em resultado de busca.
- **Transição** [S]: os RGs antigos perdem validade em 2032 (as fontes divergem entre 28 de fevereiro e 1º de março), então haverá documentos de formatos diferentes convivendo por anos.
- **Não encontrado** [?]: formato interno do QR Code, se há assinatura digital, qual cadeia de certificados e como obter as chaves públicas para verificação offline.

### 3.2 Passaporte

- **Chip e padrão** [S]: o passaporte brasileiro tem chip e segue o padrão ICAO 9303 (apresentação da Polícia Federal à ICAO em 2012, reportagens do Serpro e do Olhar Digital, vistas só em listagem de busca).
- **Fonte primária lida: Resolução nº 101/2013 do CG ICP-Brasil** [P]. Pontos relevantes:
  - A Polícia Federal "faz uso de certificados digitais ICP-Brasil no processo de emissão dos passaportes comuns".
  - A ICAO distribui as cadeias de certificação dos passaportes eletrônicos por meio de um diretório de chaves públicas (**PKD**); em 2013, segundo a resolução, o Brasil era "um dos poucos países que possui passaporte eletrônico, mas não participa do programa PKD", e fazia gestões para aderir. A não conformidade entre as normas do PKD e as da ICP-Brasil era "impeditiva".
  - Para resolver, autorizou-se, "excepcional e exclusivamente", que a autoridade certificadora gerasse certificados **autoassinados de CSCA** (a âncora de confiança exigida pela ICAO), usando os **mesmos pares de chaves** das cadeias ICP-Brasil, com cerimônia, hardware criptográfico e restrições de uso definidos. O Ministério das Relações Exteriores passou a emitir os certificados de assinatura dos documentos de viagem.
- **Adesão posterior** [S]: um aviso de março de 2014 diz que o passaporte seria compatível com o PKD. **A situação atual no diretório não foi verificada** [?].
- **Não encontrado** [?]: se o CPF consta no chip ou no campo opcional da zona legível por máquina; quais campos do chip são assinados e como se faz a verificação passiva por um terceiro que não seja um posto de controle migratório.

### 3.3 CNH digital

- **Base** [S]: a Portaria Senatran nº 184/2017 (vista apenas em resumo de busca, pois o PDF não pôde ser lido) prevê um **QR Code criptografado e assinado**, com assinatura feita com certificado de cada Detran guardado em módulo de hardware no Serpro, verificável por um validador compatível com a ICP-Brasil e **lido sem internet** por um aplicativo gratuito.
- **Hoje** [S]: o aplicativo "CNH do Brasil" guarda a CNH e permite exportar um PDF com assinatura ICP-Brasil; a verificação por terceiros se faz com outro aplicativo (relatos citam o "Vio"). As fontes são antigas ou de blogs. **Precisa de confirmação em fonte oficial atual.**
- **Identificador** [S]: a Lei nº 14.534/2023 inclui a CNH entre os documentos que devem trazer o CPF.

### 3.4 Conta gov.br

Níveis bronze, prata e ouro [S]. O prata é obtido, por exemplo, por biometria facial contra a base da CNH ou por dados bancários; o ouro, por biometria facial da Justiça Eleitoral ou certificado ICP-Brasil. É um serviço **online** do governo, que não atende ao requisito de verificação offline e que revelaria ao Estado o uso (seção 14.5 do whitepaper). Serve, no máximo, como **evidência complementar** e dependeria de apoio governamental.

### 3.5 Certificados e-CPF e e-CNPJ (ICP-Brasil)

São certificados X.509 padrão, verificáveis offline. O CPF (ou CNPJ) consta em campos do certificado, **a confirmar nas normas da ICP-Brasil**. Exigem compra, renovação e guarda da chave pelo titular, o que não serve como porta de entrada inclusiva, mas é um caminho técnico claro para quem já os tem.

## 4. Implicações para o USI

1. **Identificador estável: favorável.** Como o CPF é o número único e consta na CIN, o perfil de país do Brasil pode derivar o registro único **do CPF**, o que resolve a duplicidade entre documentos brasileiros (seção 9.2.2 do whitepaper). Fica pendente confirmar quais documentos *provam* o CPF de forma verificável.
2. **O CPF não é segredo.** Aparece em muitos documentos e cadastros. Isso agrava o risco de **ocupação de identidade** (seção 9.7.6) e reforça a regra de que a evidência mais forte vence, não quem chegou primeiro.
3. **O modo "online" da CIN conflita com um princípio do USI.** Uma verificação que consulta o governo revela a ele quem está sendo verificado e quando. O desenho do USI exige **verificação local com dados públicos** (seção 14.5). Portanto, o modo útil é o **offline**, e só serve se for criptograficamente verificável com chaves públicas. A CIN offline, pelo que se viu, não traz o nome, só CPF, nascimento e validade.
4. **Qualidade da cadeia de confiança.** O passaporte e a CNH dependem da ICP-Brasil. A seção 23 do whitepaper mostra por que a qualidade da geração e da gestão de chaves importa; o **peso** da evidência brasileira deve ser ajustável no perfil de país.
5. **Convivência de formatos até 2032** (RGs antigos e CIN), com regras diferentes de verificação.
6. **Pessoas sem esses documentos** (uma parte central da missão de inclusão do USI) dependem das outras camadas de evidência.

## 5. O que falta descobrir e próximos passos

| # | Pendência | Como resolver |
|---|---|---|
| 1 | Formato do QR Code da CIN: campos, assinatura, cadeia de certificados e chaves públicas | Solicitar a especificação ao Ministério da Gestão e da Inovação, ao Serpro e ao ITI; procurar documentação pública do aplicativo validador |
| 2 | Se o modo offline da CIN é verificável por terceiros com chave pública | Prototipar a leitura de um QR Code de **documento de teste** ou do **próprio titular, com consentimento**, sem enviar dados a terceiros |
| 3 | Se o CPF consta no chip do passaporte e quais campos são assinados | Documentação da Polícia Federal e do ITI; teste com um passaporte **do próprio titular** em ambiente isolado |
| 4 | Situação atual do Brasil no diretório de chaves da ICAO | Consultar a lista pública de participantes da ICAO |
| 5 | Texto completo e vigência da Portaria Senatran 184/2017 e do formato atual da CNH digital | Obter o texto oficial; confirmar com a Senatran e o Serpro |
| 6 | Presença do CPF nos campos do e-CPF | Normas da ICP-Brasil |
| 7 | Confirmar a Lei 14.534/2023 e o Decreto 10.977/2022 nos textos oficiais | Planalto e Diário Oficial |
| 8 | Revisão jurídica (LGPD): tratar o CPF e dados de documentos | Parecer de especialista |

**Cuidado com dados reais.** Qualquer teste deve usar documentos de teste ou do próprio titular, com consentimento, e nenhum dado pessoal deve ser publicado no repositório (ver [SECURITY.pt-BR.md](../../SECURITY.pt-BR.md)).

## 6. Fontes

**Lidas diretamente**
- [P] [Resolução nº 101/2013 do CG ICP-Brasil (ITI)](https://www.gov.br/iti/pt-br/central-de-conteudo/resolucao-101-autoriza-procedimento-especifico-para-passaporte-pdf)
- [O] [Governo Digital: Carteira de Identidade Nacional](https://www.gov.br/governodigital/pt-br/identidade/identificacao-do-cidadao-e-carteira-de-identidade-nacional)
- [S] [Wikipédia: Carteira de Identidade Nacional](https://pt.wikipedia.org/wiki/Carteira_de_Identidade_Nacional)

**Vistas apenas em resultados de busca (não lidas na íntegra)**
- [S] [Lei nº 14.534/2023 (Planalto)](https://planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14534.htm)
- [S] [Decreto nº 10.977/2022, análise (Migalhas)](https://www.migalhas.com.br/depeso/370809/decreto-10-977-22-e-a-nova-identificacao-civil)
- [S] [Memória da 5ª reunião do CEFIC, dezembro de 2024 (Governo Digital)](https://www.gov.br/governodigital/pt-br/identidade/identificacao-do-cidadao-e-carteira-de-identidade-nacional/arquivos/2024-12-03_memoria-de-reuniao-5a-reuniao-cefic.pdf)
- [S] [Passaporte brasileiro e o padrão ICAO, 2014 (Portal Dori)](https://portaldori.com.br/2014/03/13/passaporte-brasileiro-com-assinatura-digital-adere-ao-padrao-icao/)
- [S] [Sabia que o passaporte brasileiro tem chip? (Olhar Digital, 2025)](https://olhardigital.com.br/2025/03/04/pro/sabia-que-o-passaporte-brasileiro-tem-chip-entenda-como-ele-funciona-e-para-que-serve/)
- [S] [Portaria Senatran nº 184/2017](https://www.gov.br/infraestrutura/pt-br/assuntos/transito/arquivos-senatran/portarias/2017/portaria1842017.pdf) (PDF não legível)
- [S] [CNH do Brasil (App Store)](https://apps.apple.com/us/app/-/id1275057217)
- [S] [Como ter uma conta gov.br prata ou ouro (Tecnoblog)](https://tecnoblog.net/responde/como-ter-uma-conta-gov-br-no-nivel-prata-ou-ouro/)

## 7. Histórico

| Versão | Data | Descrição |
|---|---|---|
| 0.1 | 2026-10-29 | Levantamento inicial. |
