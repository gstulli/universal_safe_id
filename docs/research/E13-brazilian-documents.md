# E13: technical survey of Brazilian documents

🌐 **English** · [Português (Brasil)](E13-brazilian-documents.pt-BR.md)

**Version 0.1 (initial survey) · 29 October 2026**
Experiment E13 of the [whitepaper](../whitepaper.md) (sections 9.2.2 and 15.5) · Issue [#13](https://github.com/gstulli/universal_safe_id/issues/13)

> ⚠️ **Initial survey, made by public search and by reading pages and resolutions, with AI assistance. It has not been reviewed by specialists.** Part of the information comes from news reports and search summaries, not from the official technical specifications, which were not found. **Nothing here should be taken as definitive.** Each claim states the quality of its source (see legend). Corrections are welcome.

**Source legend:** **[P]** primary source read directly · **[O]** official page read directly · **[S]** secondary source or search summary, original not read · **[?]** not found.

## 1. Question

The E13 hypothesis is: *Brazilian documents can be verified cryptographically and offline, and a stable person identifier can be derived from them.* The success criterion is to find **at least one document verifiable offline with a stable identifier**, or to document that this is not possible.

## 2. Summary

**Provisional conclusion: there are promising candidates, but the hypothesis is not yet confirmed.** The CPF is by law the person's single number and appears on the new documents, which settles the **stable identifier** part well. What is missing is confirming **how each document is signed and how that signature is verified offline**: for the passport there is a primary source (from 2013) describing the certificate chain; for the CIN and the digital driving licence we only found general descriptions.

| Document | Stable identifier | Offline verification? | Cryptographic verification documented? | Status |
|---|---|---|---|---|
| **CIN** (National Identity Card) | **CPF**, single number by law [O][S] | Partial, via QR Code: CPF, date of birth and validity [S] | **Not found** (QR Code format and signature not located) [?] | Promising candidate; specification missing |
| **Passport** (with chip) | Passport number changes with each issue; presence of the CPF on the chip **not verified** [?] | In principle yes, via the ICAO standard | **Yes, in part:** signed with ICP-Brasil certificates; own root authority for the ICAO directory (2013) [P] | Promising candidate; need to know whether the CPF is included and current status in the ICAO directory |
| **Digital driving licence (CNH)** | CPF appears on the CNH [S] | Yes, via QR Code, according to a 2017 ordinance [S] | Described in 2017: signed with a certificate per state traffic authority, held in a hardware module at Serpro [S] | Candidate; old information, needs current confirmation |
| **gov.br account** (bronze, silver, gold) | CPF | **No** (online service) | Not applicable | Complementary evidence |
| **e-CPF / e-CNPJ certificate** (ICP-Brasil) | CPF (or CNPJ) in the certificate, to be confirmed | Yes (X.509 signature) | Yes, ICP-Brasil standard | Technical candidate; requires purchase and renewal by the holder |

## 3. Details by document

### 3.1 CIN: National Identity Card

- **Legal basis.** Decree No. 10,977/2022 created the CIN [S]. Law No. 14,534/2023 establishes the **CPF as the single and sufficient number** to identify citizens in public-service databases, and requires issuing bodies to use the CPF as the general registration number in new documents [S, via a search summary of the law text; confirm in the official text at Planalto].
- **Official page** [O]: the CIN exists in **physical and digital** formats, "has a QR code", **uses the CPF as its single number** and replaces the RG. The page does **not** describe the QR Code content, verification, presence of a chip or technical standards.
- **Material and QR Code** [S, encyclopedia]: watermarked paper or polycarbonate card; QR Code on the back for validation; **MRZ** (machine-readable zone) to confirm authenticity abroad; **chip not mentioned** for the current CIN. The digital version, on the phone, would have a copy with "digital certification", PDF export and a QR Code validation page.
- **Verification** [S]: an official app ("QR Code reading") has two modes. **Offline (partial)** shows CPF, date of birth and validity; **online (complete)** also shows photo, name, parentage and place of birth, requires a connection and, according to one result, a gov.br account. This description comes from a December 2024 federal-government meeting minute, seen only in a search result.
- **Transition** [S]: old RGs lose validity in 2032 (sources differ between 28 February and 1 March), so documents of different formats will coexist for years.
- **Not found** [?]: internal QR Code format, whether there is a digital signature, which certificate chain, and how to obtain public keys for offline verification.

### 3.2 Passport

- **Chip and standard** [S]: the Brazilian passport has a chip and follows ICAO 9303 (Federal Police presentation to ICAO in 2012, Serpro and Olhar Digital reports, seen only in search listings).
- **Primary source read: Resolution No. 101/2013 of the CG ICP-Brasil** [P]. Relevant points:
  - The Federal Police "uses ICP-Brasil digital certificates in the process of issuing ordinary passports".
  - ICAO distributes the certificate chains of e-passports through a public-key directory (**PKD**); in 2013, according to the resolution, Brazil was "one of the few countries that has an electronic passport but does not take part in the PKD programme", and was working to join. The non-conformity between PKD and ICP-Brasil rules was "an impediment".
  - To solve it, the certifying authority was authorized, "exceptionally and exclusively", to generate **self-signed CSCA certificates** (the trust anchor ICAO requires) using the **same key pairs** as the ICP-Brasil chains, with a ceremony, cryptographic hardware and use restrictions defined. The Ministry of Foreign Affairs began issuing the certificates that sign travel documents.
- **Later adhesion** [S]: a March 2014 notice says the passport would be PKD-compatible. **The current status in the directory was not verified** [?].
- **Not found** [?]: whether the CPF appears on the chip or in the optional field of the machine-readable zone; which chip fields are signed and how a third party other than a border-control point would do passive verification.

### 3.3 Digital driving licence (CNH)

- **Basis** [S]: Senatran Ordinance No. 184/2017 (seen only in a search summary, as the PDF could not be read) provides for an **encrypted and signed QR Code**, signed with a certificate per state traffic authority held in a hardware module at Serpro, verifiable by an ICP-Brasil-compatible validator and **read without internet** by a free app.
- **Today** [S]: the "CNH do Brasil" app holds the CNH and allows exporting a PDF with an ICP-Brasil signature; verification by third parties is done with another app (reports cite "Vio"). Sources are old or blogs. **Needs confirmation from a current official source.**
- **Identifier** [S]: Law No. 14,534/2023 includes the CNH among the documents that must carry the CPF.

### 3.4 gov.br account

Bronze, silver and gold levels [S]. Silver is obtained, for example, by facial biometrics against the CNH database or by bank data; gold, by electoral-court facial biometrics or an ICP-Brasil certificate. It is an **online** government service, which does not meet the offline-verification requirement and would reveal usage to the state (whitepaper section 14.5). At most, it serves as **complementary evidence** and would depend on government support.

### 3.5 e-CPF and e-CNPJ certificates (ICP-Brasil)

Standard X.509 certificates, verifiable offline. The CPF (or CNPJ) appears in certificate fields, **to be confirmed in ICP-Brasil rules**. They require purchase, renewal and key custody by the holder, which does not work as an inclusive entry point, but is a clear technical path for those who already have them.

## 4. Implications for USI

1. **Stable identifier: favourable.** Since the CPF is the single number and appears on the CIN, Brazil's country profile can derive the unique record **from the CPF**, which settles duplication across Brazilian documents (whitepaper section 9.2.2). Pending: confirm which documents *prove* the CPF verifiably.
2. **The CPF is not a secret.** It appears in many documents and registers. This worsens the risk of **identity squatting** (section 9.7.6) and reinforces the rule that the stronger evidence wins, not whoever arrived first.
3. **The CIN's "online" mode conflicts with a USI principle.** A check that queries the government reveals to it who is being verified and when. USI's design requires **local verification with public data** (section 14.5). So the useful mode is the **offline** one, and it only helps if it is cryptographically verifiable with public keys. The offline CIN, from what was seen, carries no name, only CPF, birth date and validity.
4. **Quality of the trust chain.** The passport and the CNH depend on ICP-Brasil. Whitepaper section 23 shows why the quality of key generation and management matters; the **weight** of Brazilian evidence should be adjustable in the country profile.
5. **Coexistence of formats until 2032** (old RGs and the CIN), with different verification rules.
6. **People without these documents** (a central part of USI's inclusion mission) depend on the other evidence layers.

## 5. What remains to be found and next steps

| # | Pending item | How to resolve |
|---|---|---|
| 1 | CIN QR Code format: fields, signature, certificate chain and public keys | Request the specification from the Ministry of Management and Innovation, Serpro and ITI; look for public documentation of the validator app |
| 2 | Whether the CIN offline mode is verifiable by third parties with a public key | Prototype reading a QR Code from a **test document** or from the **holder's own, with consent**, without sending data to third parties |
| 3 | Whether the CPF is on the passport chip and which fields are signed | Federal Police and ITI documentation; test with a passport **owned by the holder** in an isolated environment |
| 4 | Brazil's current status in the ICAO key directory | Check ICAO's public participant list |
| 5 | Full text and validity of Senatran Ordinance 184/2017 and the current CNH digital format | Obtain the official text; confirm with Senatran and Serpro |
| 6 | Presence of the CPF in e-CPF fields | ICP-Brasil rules |
| 7 | Confirm Law 14,534/2023 and Decree 10,977/2022 in the official texts | Planalto and the Official Gazette |
| 8 | Legal review (LGPD): handling the CPF and document data | Specialist opinion |

**Care with real data.** Any test must use test documents or the holder's own, with consent, and no personal data may be published in the repository (see [SECURITY.md](../../SECURITY.md)).

## 6. Sources

**Read directly**
- [P] [Resolution No. 101/2013 of the CG ICP-Brasil (ITI)](https://www.gov.br/iti/pt-br/central-de-conteudo/resolucao-101-autoriza-procedimento-especifico-para-passaporte-pdf)
- [O] [Governo Digital: National Identity Card](https://www.gov.br/governodigital/pt-br/identidade/identificacao-do-cidadao-e-carteira-de-identidade-nacional)
- [S] [Wikipedia: Carteira de Identidade Nacional](https://pt.wikipedia.org/wiki/Carteira_de_Identidade_Nacional)

**Seen only in search results (not read in full)**
- [S] [Law No. 14,534/2023 (Planalto)](https://planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14534.htm)
- [S] [Decree No. 10,977/2022, analysis (Migalhas)](https://www.migalhas.com.br/depeso/370809/decreto-10-977-22-e-a-nova-identificacao-civil)
- [S] [Minutes of the 5th CEFIC meeting, December 2024 (Governo Digital)](https://www.gov.br/governodigital/pt-br/identidade/identificacao-do-cidadao-e-carteira-de-identidade-nacional/arquivos/2024-12-03_memoria-de-reuniao-5a-reuniao-cefic.pdf)
- [S] [Brazilian passport and the ICAO standard, 2014 (Portal Dori)](https://portaldori.com.br/2014/03/13/passaporte-brasileiro-com-assinatura-digital-adere-ao-padrao-icao/)
- [S] [Did you know the Brazilian passport has a chip? (Olhar Digital, 2025)](https://olhardigital.com.br/2025/03/04/pro/sabia-que-o-passaporte-brasileiro-tem-chip-entenda-como-ele-funciona-e-para-que-serve/)
- [S] [Senatran Ordinance No. 184/2017](https://www.gov.br/infraestrutura/pt-br/assuntos/transito/arquivos-senatran/portarias/2017/portaria1842017.pdf) (PDF not readable)
- [S] [CNH do Brasil (App Store)](https://apps.apple.com/us/app/-/id1275057217)
- [S] [How to have a silver or gold gov.br account (Tecnoblog)](https://tecnoblog.net/responde/como-ter-uma-conta-gov-br-no-nivel-prata-ou-ouro/)

## 7. History

| Version | Date | Description |
|---|---|---|
| 0.1 | 2026-10-29 | Initial survey. |
