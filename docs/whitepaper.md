# Universal Safe ID (USI) — Whitepaper

🌐 **English** · [Português (Brasil)](whitepaper.pt-BR.md)

**Version 0.2.0 — open draft, open to collaboration** · October 2026
Companion to the [README](../README.md).

> **How to read this document.** USI is in the conception phase. This whitepaper gathers what is known, proposes paths and states what is still unknown. Each section is tagged with its maturity:
>
> - 🟢 **Proposed**: a direction the project intends to follow, subject to peer review.
> - 🟡 **Hypothesis**: a plausible idea that must be tested or measured before adoption.
> - 🔴 **Open**: a question with no known answer; needs research.
>
> Numeric values (waiting periods, thresholds, sizes) are **illustrative** until calibrated in the proofs of concept (section 16). Criticism, corrections and contributions are welcome (section 20).

---

## Table of contents

1. [Abstract](#1-abstract)
2. [Introduction and motivation](#2-introduction-and-motivation)
3. [Goals and non-goals](#3-goals-and-non-goals)
4. [Threat model](#4-threat-model)
5. [Lessons from prior initiatives](#5-lessons-from-prior-initiatives)
6. [Architecture overview](#6-architecture-overview)
7. [Identifier and key management](#7-identifier-and-key-management)
8. [Public registry](#8-public-registry)
9. [Uniqueness: one person, one USI](#9-uniqueness-one-person-one-usi)
10. [Access recovery](#10-access-recovery)
11. [Privacy](#11-privacy)
12. [Operational security and cryptography](#12-operational-security-and-cryptography)
13. [Sustainability](#13-sustainability)
14. [Governance](#14-governance)
15. [Adoption and entry strategy](#15-adoption-and-entry-strategy)
16. [Experimental validation plan](#16-experimental-validation-plan)
17. [Project risks](#17-project-risks)
18. [Open questions](#18-open-questions)
19. [Roadmap](#19-roadmap)
20. [How to contribute to this document](#20-how-to-contribute-to-this-document)
21. [USI-O: identity of organizations](#21-usi-o-identity-of-organizations)
22. [Digital signature and authentication: an alternative to certificate authority hierarchies](#22-digital-signature-and-authentication-an-alternative-to-certificate-authority-hierarchies)
23. [Lessons from real failures and procedures that prevent human error](#23-lessons-from-real-failures-and-procedures-that-prevent-human-error)
24. [Cryptographic migration and quantum computing](#24-cryptographic-migration-and-quantum-computing)
25. [References](#25-references)
26. [Version history](#26-version-history)

---

## 1. Abstract

Universal Safe ID (USI) is a proposal for open, ownerless, non-profit infrastructure through which anyone can obtain, free of charge, **a unique and permanent identifier** that proves they are **a distinct human being** without revealing who they are, and that lets them **control their own data**, sharing it selectively and for limited periods.

No technical component of USI is new. The proposed contribution is the **deliberate combination** of techniques already studied in decentralized identity, cryptography and public infrastructure, so that the weaknesses of each are covered by the others:

1. **Uniqueness from multiple independent evidence layers** (social vouching analysed as a graph, zero-knowledge document proofs, physical presence and, optionally, biometrics), translated into **assurance levels** that each verifier chooses.
2. **Access recovery through parallel routes** (another device, pre-rotated key, guardians, re-validation), with waiting periods and a right of veto proportional to the strength of the evidence.
3. **A minimal public registry** that stores only public keys, cryptographic commitments and proofs, **never personal data**.
4. **Per-service pseudonyms**, which prevent the universal identifier from becoming a tracking tool.
5. **Funding by those who benefit**, with no token and no charge to citizens, and governance that decentralizes in measurable phases.

This document describes the problem, the threat model, the proposed architecture, the alternatives still in dispute, an experiment plan to decide among them, and the project's risks. Part II (sections 21 to 24) extends the proposal to organizations, digital signature and authentication, the lessons from real failures in key infrastructure, and cryptographic migration.

## 2. Introduction and motivation

### 2.1 The problem

Systems for identifying people currently depend on two families of solutions, both problematic:

- **Identity issued by states and certifying bodies.** It leaves billions of people without recognized documents; produces centralized databases exposed to mass leaks and duplicates; does not cross borders easily; and can be denied or cancelled by a single authority.
- **Identity issued by private platforms** (accounts at large companies used to sign in elsewhere). The account belongs to the platform, can be blocked with no recourse, feeds commercial profiling and does not guarantee a real, unique human behind it.

### 2.2 An aggravated problem: humans and AI agents

The growing ability of AI agents to produce human-like text, voice, images and behaviour at scale makes it ever harder to sustain the principle of "one person, one voice" in social networks, reviews, surveys, community voting and benefit distribution. Traditional checks (CAPTCHAs, e-mail, phone numbers) are cheap to circumvent. There is growing demand for privacy-preserving **proof of personhood**.

### 2.3 What USI proposes

A third path: an identity that **does not depend on a single authority**, **does not require revealing personal data** to be proven, and **cannot be lost** through a simple lapse of memory, and whose trust is built from **independent evidence** rather than a single method.

## 3. Goals and non-goals

### 3.1 Goals 🟢

| # | Goal |
|---|---|
| G1 | Assign at most one active USI to each human being, making fraud hard, costly, detectable and reversible. |
| G2 | Let holders prove "I am a unique human" and "I have assurance level N" without revealing who they are. |
| G3 | Keep personal data under the holder's exclusive control, with minimal, selective and temporary disclosure. |
| G4 | Make lost access recoverable without creating an easy door for account takeover. |
| G5 | Prevent USI from being used to correlate or track the same person across services. |
| G6 | Be free for the holder and sustainable without a token or profit. |
| G7 | Be inclusive: work for people without documents, with older smartphones or unstable connections. |
| G8 | Be publicly verifiable and auditable, using open source and open standards. |
| G9 | Decentralize governance in a planned way, until no one — including the founder — has unilateral power. |
| G10 | Ensure each USI has a single current set of key attributes (official name, identifiers) and that third parties know how far to trust them. |
| G11 | Collaborate with similar initiatives, reusing open standards and components, without giving up the essential characteristics: universal, collaborative, secure, non-profit and ownerless (section 5). |
| G12 | Also serve organizations (USI-O), with verifiable representation and powers, sharing the same core as USI-P (section 21). |
| G13 | Offer verifiable digital signature and authentication, as an alternative to certificate authority hierarchies (section 22). |
| G14 | Make human security failures impossible by construction and prepare cryptographic migration, including for quantum computing (sections 23 and 24). |

### 3.2 Non-goals 🟢

- **It is not a currency, token or financial asset.**
- **It does not replace official documents.** It coexists with them and uses them as evidence where they exist.
- **It does not guarantee absolute uniqueness.** No system does; the aim is a cost of fraud far above its benefit.
- **It does not guarantee the truth of information**, only that it is unique and how far it can be trusted. Whoever verifies it answers for its truth (section 9.7).
- **It does not claim, today, a legal value** equivalent to the ICP-Brasil qualified signature, nor does it replace notarial public faith. Legal recognition is a long-term goal (section 22.4).
- **It is not a social credit, public reputation or citizen scoring system.** Internal reputation only weights attestations.
- **It does not store personal data** in the public registry, in any form.
- **It is not a surveillance mechanism**, nor compulsory identification.
- **It does not solve authorization by itself** (what a person may do), only authentication and proof of uniqueness.

### 3.3 Geographic premise: pilot in Brazil, design without borders 🟢

- **Pilot in Brazil.** The first real deployment will be in Brazil: it is where the project is born, where knowledge of documents and legislation (LGPD) is available and where the first network of partners will be formed.
- **Design without borders.** The protocol, the registry and the uniqueness model **must not presuppose any one country**. Everything country-specific lives in pluggable modules, the **country profiles** (section 9.2.2). Shortcuts that only work in Brazil (for example, hard-wiring a specific national number into the protocol) are technical debt and must be avoided.
- **Gradual expansion by adhesion.** New countries join as local stakeholders (node operators, validators, credential issuers, lawyers, translators and interested governments) sign on and provide support for infrastructure and operation. Joining is voluntary and non-exclusive; no country gets governance priority for having been first.
- **Government support without control.** Governments may support the project, including by qualifying verification of their own documents, but gain no control over it (section 14.5).

## 4. Threat model

### 4.1 Adversaries considered

| Adversary | Capability and motivation |
|---|---|
| **Sybil fraudster** [10] | Wants many identities to multiply votes, benefits or influence. May use automation, AI and paid labour. |
| **Identity marketplace** | Buys and sells registrations or attestations. Exploits paying real people to act as "humans for hire". |
| **Account hijacker** | Tries to take control of someone else's USI, preferably through the recovery route. |
| **Malicious operator** | Controls part of the registry nodes and tries to censor, reorder or forge events. |
| **Governance capturer** | Tries to gain control of the system's rules through money, political influence or collusion. |
| **Surveillant (state, company or passive observer)** | Wants to track people across services or build profiles from metadata. |
| **Coercer** | Physically or legally forces the holder to surrender access, keys or data. |
| **Future adversary** | Stores today's data to break it once quantum computing or new techniques arrive. |
| **Insider** | A developer, validator or juror who abuses their position. |
| **Identity squatter** | Registers someone else's name or CPF first to block them from registering their own identity, or builds a synthetic identity with fake documents (section 9.7). |

### 4.2 Trust assumptions 🟡

- A relevant share of holders and attesters acts honestly, and the honest network is larger than any fraudulent group (an assumption required by graph analysis).
- A qualified majority of registry operators does not collude (the assumption of any Byzantine-fault-tolerant consensus).
- Standardized cryptographic primitives remain secure, with a migration plan if they stop being so.
- Personal devices may be lost or stolen, but are not **all** compromised at the same time.

### 4.3 Out of scope for protection 🟢

- **Total compromise of the holder's device** by advanced malware at signing time.
- **A human who voluntarily and without coercion hands their USI to someone else** (identity sale). USI mitigates this (section 9.6) but cannot eliminate it; no system can.
- **Information already seen:** once revealed, data cannot be "unrevealed".

## 5. Lessons from prior initiatives

This section summarizes patterns observed in existing approaches, focusing on **design lessons** rather than criticism of specific initiatives. The observations are general and must be verified and detailed in future versions with primary sources.

| Approach | What works | What tends to fail | Consequence for USI |
|---|---|---|---|
| **Mandatory biometrics on dedicated hardware** | Strong duplicate detection; hard to fool at scale | Privacy concerns, hardware centralization, regulatory scrutiny, dependence on a single manufacturer | Biometrics, if adopted, will be **optional**, with no central database and an architecture that does not need a single manufacturer |
| **Social graph** | No hardware or documents; inclusive | Well-connected fake groups; low adoption; little motivation to vouch | Use the graph as **one** piece of evidence, with structural analysis and attester accountability |
| **Deposit, video and jury challenge** | Creates a cost to cheat and a corrective mechanism | Slow, expensive onboarding; dependence on a financial asset | Keep **challenge and jury**, but with no mandatory financial deposit from the citizen |
| **Synchronized tests to prove humanity** | No documents needed | Outsourcing: people taking the test for others for pay | Do not rely on isolated tests; combine with other evidence |
| **Simultaneous in-person meetings** | Strong against Sybil: nobody is in two places at once | Hard to scale; requires coordination and accessibility | Use physical presence as **high-level** evidence, backed by local partners |
| **Open identity standards (DID, VC)** | Interoperability, tooling ecosystem | No uniqueness solution of their own; uniqueness comes from a state | Adopt the standards; **add** the uniqueness layer |
| **State digital identity wallets** | Legal recognition, high potential adoption | Dependence on one issuer and its policy | Accept state credentials as **evidence**, never as the sole requirement |

**Three cross-cutting lessons:**

1. No single piece of evidence holds up; the most fragile approaches rely on one signal.
2. The most attacked point tends to be the **identity marketplace** (paying real people), not technical brute force.
3. Financial tokens attract fraud and speculation and distort the incentives of those who should vouch.

### 5.1 Overview of related initiatives (initial survey, October 2026) 🟡

This survey was made with public searches and by reading the projects' websites. **It is incomplete:** it does not cover initiatives outside the cryptocurrency world or in other languages, and several details (legal form, governance, current status) could not be confirmed. It must be verified and expanded with primary sources (section 5.6).

| Initiative | Main scope | Nature, as found | Possible collaboration with USI |
|---|---|---|---|
| [Ğ1 / Duniter](https://duniter.org/) | Currency with basic income; identities through a web of trust, one per living person | Free software maintained by a community; more than 6,000 participants. Legal form and governance not found | Analysis of resistance to fake accounts in a web of trust ([2025 study](https://www.arxiv.org/pdf/2512.07897)); share simulations (E2) |
| [Encointer](https://encointer.org/) | Local currencies; uniqueness through random in-person meetings | Protocol on the Kusama network, in use in Tanzania and Nigeria; an association is linked to the project (to be confirmed); [operation funded by an on-chain treasury](https://kusama-static.polkassembly.io/referenda/645). Licence to be confirmed | In-person ceremonies (E10); field experience with people without documents |
| [BrightID](https://brightid.org/) | Proof of uniqueness through a social graph | Presents itself as an open public good; the site indicates a company (BrightID Main LLC) | Graph analysis, operating lessons (E2) |
| [Proof of Humanity](https://gov.proofofhumanity.id/t/poh-origin-constitution-v2/3053) | Registration with video, vouching and challenge | Community governance through proposals, with Kleros as arbitrator; [fork discussion](https://gov.proofofhumanity.id/t/hip-74-peaceful-fork-status-thread/2695). Current status to be confirmed | Challenge and jury (E8) |
| [Decentralized Identity Foundation](https://learnworkecosystemlibrary.com/organizations/decentralized-identity-foundation/) | Standards and tools for decentralized identity | Non-profit organization, according to a secondary source (to be confirmed) | Review of the `did:usi` specification and credentials |
| [LF Decentralized Trust](https://www.linuxfoundation.org/press/linux-foundation-decentralized-trust-launches-with-17-projects-100-founding-members) and [OpenWallet](https://www.ledgerinsights.com/openwallet-foundation-to-merge-into-lf-decentralized-trust/) | Open software for wallets, credentials and trust | Open-source foundation (launched 2024); OpenWallet is due to merge into it in 2027 (to be confirmed) | Reusable wallets and libraries; possible home for the specification |
| Self and [ZKPassport](https://itbrief.co.uk/story/aztec-labs-acquires-obsidion-for-zkpassport-identity) | Zero-knowledge passport proofs | Open source but maintained by companies; ZKPassport was acquired by Aztec Labs in June 2026 | Reuse document proofs (E4) |
| [Human Passport](https://human.tech/blog/human-tech-launch-acquisition-gitcoin-passport) | Humanity scoring | Acquired by Holonym Foundation in February 2025; tied to human.tech and a network with a token | Learning reference |
| World ID | Uniqueness through iris scans, on dedicated hardware | Commercial. In Brazil, the [ANPD banned payment for iris collection](https://olhardigital.com.br/2025/08/06/reviews/world-brasil-mantem-proibicao-de-pagamento-por-escaneamento-de-olhos/) | Learning reference (privacy and regulation); reuse of components not envisaged |
| Idena | Uniqueness through synchronized tests | Current status not found | Not found |

**Survey conclusion.** None of the projects found combines, at once, the five characteristics of USI (section 5.3) and the full scope of the proposal (layered uniqueness, access recovery, verifiable attribute binding, a pilot with LGPD compliance). Some are close in spirit (Ğ1/Duniter, Encointer) but have a different main scope; others are uniqueness projects tied to companies or tokens; and others are standards bodies that provide the technical base. This **does not prove** that the gap exists: the survey is partial.

### 5.2 Stance: collaborate, do not compete 🟢

USI does not intend to compete with similar initiatives. The goal is shared: that anyone can prove they are a unique human being and control their own data. If an existing initiative already fulfils USI's essential characteristics (section 5.3), the path is to **contribute to it** rather than build parallel infrastructure. Commitments:

1. **Research before building.** Check what already exists and talk to the communities before any prototype of our own.
2. **Contribute back.** Publish research, experiment results (including negative ones), fixes and code for anyone who can use them.
3. **Interoperate.** Adopt open standards and build bridges, so that people using another initiative need not choose.
4. **Reuse what is open,** with credit and within the licences.
5. **Acknowledge and respect** the work of other initiatives, without treating them as adversaries.
6. **Accept convergence.** If, after the survey and conversations, joining forces proves more effective (joining, merging or another initiative adopting the specification) and the essential characteristics are preserved, that decision will be discussed and recorded through a USIP (section 14.2).

### 5.3 What USI does not give up 🟢

Collaborating does not mean diluting. These five characteristics are **non-negotiable** in any partnership, merger or reuse:

| Characteristic | What it means | Test when assessing a collaboration |
|---|---|---|
| **Universal** | No borders: open to any person and country, not depending on one country, language or infrastructure (section 3.3) | Does the solution exclude regions, languages or people without documents? |
| **Collaborative** | Open proposal process and community governance; anyone can contribute (section 14.2) | Are decisions open, or do they depend on a closed entity? |
| **Secure** | Privacy and security by design; no personal data in the registry; independent audits; access recovery (sections 8, 10, 11 and 12) | Does it require centralized personal data or mandatory biometrics? Has it been audited? |
| **Non-profit** | No token, no profit for founders, investors or maintainers; revenue only covers costs (section 13) | Is there a mandatory token, equity stake or value extraction? |
| **Ownerless** | Progressive decentralization; nobody, including the founder and partners, has unilateral power (section 14) | Does anyone gain a special vote, veto or control over the rules? |

### 5.4 Forms of collaboration 🟡

| Level | Examples |
|---|---|
| **Knowledge** | Share research, simulations and experiment data (E2, E8, E10); cross-review of specifications |
| **Standards** | Adopt and contribute to DID, verifiable credentials and presentation protocols |
| **Components** | Reuse open-source code (wallets, credential libraries, document proofs) instead of rewriting it |
| **Integration** | Accept evidence from other proof-of-personhood initiatives as one of the evidence layers (section 9.2), and let them accept USI. Hypothesis to evaluate |
| **Institutional** | Partnerships, joint projects, joint funding applications and, where appropriate, joining or merging |

### 5.5 Criteria for reusing a component or entering a partnership 🟡

1. A recognized open-source licence.
2. No dependence on a mandatory token or on a single maintainer or company.
3. It does not impose control, a special vote or a veto on USI.
4. Compatible with USI's privacy (no personal data in the registry, no mandatory biometrics).
5. Auditable and open to independent audit; possibility of an honest fork (section 14.3).
6. Project health: active maintenance and ownership stability. Several initiatives were acquired or changed course; dependencies should therefore sit behind interfaces that allow swapping one component for another.

### 5.6 What still needs to be verified 🔴

- Current legal form, governance and funding of Ğ1/Duniter, Encointer, BrightID and Proof of Humanity.
- Current status of Idena and of proof-of-personhood initiatives outside the cryptocurrency world.
- Government digital-identity initiatives (for example, the European digital identity wallets) and how they relate to USI.
- Projects in other languages and regions, including Latin America.
- Whether any initiative has **verifiable binding of name and documents by independent issuers** (section 9.7). We did not find one, but that does not prove none exists.

Contributions to this survey are especially welcome.

## 6. Architecture overview

### 6.1 Layers 🟢

```
┌──────────────────────────────────────────────────────────────────┐
│  LAYER 3 – Data and credentials (off the public registry)        │
│  Holder's wallet · verifiable credentials · ZK proofs            │
├──────────────────────────────────────────────────────────────────┤
│  LAYER 2 – Uniqueness and reputation                             │
│  Evidence · attestations · assurance levels · challenges         │
├──────────────────────────────────────────────────────────────────┤
│  LAYER 1 – Public registry (anchor)                              │
│  USI · public keys · rotations · revocations · nullifiers        │
└──────────────────────────────────────────────────────────────────┘
```

The layers are independent and should evolve separately: replacing the public registry should not require changing the credential format, and recalibrating the uniqueness model should not alter the key protocol.

### 6.2 Components and flows

| Component | Role |
|---|---|
| **Wallet** | The holder's app. Stores keys, identity secrets, credentials and consents. Generates proofs. |
| **Public registry** | Stores and orders events (creation, rotation, revocation, freeze, nullifiers, attestation digests). |
| **Uniqueness service** | Rules and processes that convert evidence into an assurance level. Partly *on-chain* (hashes, nullifiers), partly *off-chain* (graph, juries). |
| **Country profiles** | Public, versioned modules holding what is country-specific: accepted documents and how to verify them, stable identifier, evidence weight, validators and legal aspects (section 9.2.2). |
| **Attesters** | Existing holders who vouch for another holder. |
| **Guardians** | People or institutions chosen by the holder to assist recovery. |
| **In-person validators** | Partners who run physical verification ceremonies. |
| **Issuers** | Institutions that issue verifiable credentials (diplomas, registrations) and **attest attributes** of the holder (name, documents), such as banks that verify their customers (section 9.7). |
| **Verifiers** | Services that request and check USI proofs. |
| **Juries** | Randomly drawn groups that decide challenges. |

**Typical use flow (simplified).** A verifier asks for "unique human with level ≥ 2". The wallet computes a pseudonym and a *nullifier* specific to that verifier and generates a zero-knowledge proof that (a) an active USI exists in the registry, (b) with level ≥ 2, (c) to which the pseudonym and the *nullifier* belong. The verifier checks the proof and the *nullifier*, without learning which USI it is.

## 7. Identifier and key management

### 7.1 Identifier 🟢

USI follows the **W3C DID** standard [1]. A dedicated method, `did:usi`, is proposed, whose identifier is derived deterministically from data in the creation event (for example, the hash of the first event), making it self-certifying and independent of any naming authority.

### 7.2 Keys and secrets: separate roles 🟢

A common mistake is using one key for everything. USI proposes **separating functions**:

| Material | Function | Rotatable? | Note |
|---|---|---|---|
| **Control key(s)** | Sign registry events (rotation, revocation, freeze) | Yes | May be FIDO2 passkeys [2] or hardware keys |
| **Pre-rotated key** | Takes over if control keys are lost or compromised | Yes, on each use | Only its *hash* is registered; the key stays offline |
| **Identity secret** | Basis for deriving per-service pseudonyms and *nullifiers* | **Should not change** (see 11.3) | Must be recoverable without being revealed to third parties |
| **Credential keys** | Sign credential presentations | Yes | May be derived per service |

### 7.3 Key event log 🟢

Inspired by KERI [3], each USI's state is the result of a **chained log of events**: creation, rotation, device add/remove, freeze, unfreeze, recovery start/veto/completion, revocation by jury decision. Each event is signed by the current keys and references the previous event.

### 7.4 Pre-rotation 🟢

When registering the current key, the holder also registers the *hash* of the next one. If the current key is compromised, the attacker **cannot** name a key of their choosing as successor, since the successor is already committed in advance. The holder keeps the next key offline (paper, safe, hardware key).

### 7.5 Cryptographic agility and post-quantum 🟡

Events must identify the algorithm used. Migration to standardized post-quantum algorithms (such as ML-DSA, FIPS 204 [4]) must be possible without changing USI. Since post-quantum keys and signatures are considerably larger, the registry should store **commitments (hashes)** of keys, revealing the full key only when needed (in the event that uses it). This affects sizing (section 8.3). The full migration plan is in section 24.

### 7.6 Multiple devices 🟢

A USI may have several authorized devices, each with its own key, under a configurable policy (for example, "any one may sign everyday acts; security changes require two").

## 8. Public registry

### 8.1 Requirements 🟢

| Requirement | Description |
|---|---|
| R1 | **Independence**: no single entity can alter, censor or erase events. |
| R2 | **Durability**: survive for decades, including the end of any organization. |
| R3 | **Zero cost to the holder.** |
| R4 | **Public auditability**: anyone can verify the registry's integrity. |
| R5 | **Privacy**: no personal data; minimal correlatable metadata. |
| R6 | **Light verification**: modest devices check compact proofs without downloading the whole registry. |
| R7 | **Sufficient performance** for the target scale. |
| R8 | **Jurisdictional neutrality**: operators in several jurisdictions. |

### 8.2 What is and is not recorded 🟢

**Recorded:** USI, key commitments, key events, uniqueness *nullifiers*, attestation digests (*hashes*), jury decisions (in minimal form).
**Never recorded:** name, documents, photos, biometrics, address, date of birth or any personal data, **not even encrypted**.

Encrypted data on a ledger is a risk: today's cryptography may be broken in the future ("harvest now, decrypt later"), and a registry is by nature impossible to erase, which clashes with the right to erasure under the Brazilian LGPD [5].

### 8.3 Sizing 🟡

Order-of-magnitude estimate (to be validated in a prototype):

| Scenario | Data per person in the registry | Total for 8 billion |
|---|---|---|
| Full classical keys (e.g. 32-byte elliptic curve) + basic events | ~200–300 B | ~1.6–2.4 TB |
| Full post-quantum keys in the registry (order of kB) | ~2–4 kB | ~16–32 TB |
| Only key **commitments (hashes)**; keys revealed in events | ~200–400 B | ~1.6–3.2 TB |

Notes:
- Eight billion is a **theoretical ceiling**, not a target. Each key rotation adds events; real growth depends on usage.
- The estimate justifies the principle of storing **commitments**, not full post-quantum keys.
- History may be **pruned or archived** by light nodes, keeping only current state and the proofs needed.
- Ordinary users do **not** store the registry: they use a light client and compact inclusion proofs.

### 8.4 Implementation options 🔴

The decision must come from proofs of concept (section 16). Options:

| | **A. Anchors on an existing public blockchain** | **B. Own federated network (BFT) with auditable logs** | **C. Hybrid** |
|---|---|---|---|
| Description | Events (or Merkle tree roots) published on an established public network, e.g. an Ethereum layer 2 | Tens to hundreds of independent operators run Byzantine-fault-tolerant consensus; auditable logs in the style of *Certificate Transparency* [6] | Federated network for daily operation; periodic anchors (Merkle roots) on a public blockchain |
| Security | Inherited from a battle-tested network | Depends on operator diversity and honesty | Dual: federation + external anchor |
| Cost | Per-transaction cost (mitigable by batching) | Operating cost spread among operators | Sum of both, but anchor cost is small |
| Dependency | Third parties and their rules and fees | Finding and keeping operators | Both, to a lesser degree |
| Main risk | Rule changes, congestion, fees | Capture or collapse of the operator set | Complexity |
| Privacy | Permanent public metadata | Better control over what is exposed | Same as B + opaque anchors |

**Working hypothesis:** option **C** tends to balance requirements R1–R8 best: operate through a federation, with Merkle roots anchored on a public network so that tampering is detectable by anyone. This is a **hypothesis**, not a decision.

**Batching.** Whichever option is chosen, events should be aggregated in batches and committed by Merkle root, so that the per-holder cost is a tiny fraction.

## 9. Uniqueness: one person, one USI

### 9.1 Design principle 🟢

Absolute uniqueness is impossible. The aim is that **the marginal cost of a fake identity always exceeds its benefit**, that fraud is **detectable**, and that it is **reversible** without harming the legitimate holder.

### 9.2 Evidence layers 🟢

Each USI accumulates evidence from distinct categories. None is mandatory on its own; strength comes from combination and from independence among them.

#### 9.2.1 Social vouching 🟡

- **Mechanism:** existing holders attest that they know the candidate as a real, unique person.
- **The number of attestations is not what is measured**, but the **structure of the graph**. Clusters of fake accounts tend to form regions densely connected to each other and sparsely connected to the honest network; algorithms such as SybilRank [7] exploit this.
- **Attesters answer for what they attest:** vouching for a USI later judged fraudulent lowers the attester's reputation (and, in serious cases, temporarily removes them from the role). This makes careless attestation costly.
- **Attester limits:** a maximum number of active attestations per period; attestation requires a real link (e.g. prior interaction, a meeting, verifiable context).
- **Weaknesses:** vulnerable to "humans for hire" and to real people induced to attest fraud; slow initial network effect; reinforces connection inequalities.

#### 9.2.2 Zero-knowledge document proof 🟡

- **Mechanism:** for those holding a document with a chip and verifiable digital signature (such as e-passports), the holder proves, inside a zero-knowledge proof, that (a) the document is authentic, (b) it is valid and (c) a deterministic ***nullifier*** derives from it. The registry stores only the *nullifier*; a second registration with the same document yields the same *nullifier* and is refused. *In the initial phase of the network, the *nullifier* is not published, and duplication is mitigated in other ways (section 9.7.10).*
- **Advantage:** leverages the uniqueness states already establish, without creating a document database and without revealing data.
- **Limitations that must be acknowledged:**
  - Uniqueness is **per document**, not **per person**. People with several documents (dual nationality, a renewed passport with a new number) could in principle produce several *nullifiers*. Mitigations to investigate: deriving the *nullifier* from stable personal fields (not the document number), which requires careful privacy analysis; and cross-checking with other layers. See **country profiles**, below.
  - It depends on **trust in issuing authorities** (each country's certificate chains). Malicious states could in theory issue fake documents en masse. Mitigation: the document layer's weight is adjusted per country and can be reduced by a governance decision if abuse is evidenced.
  - It covers only those who **have** the document. For everyone else, the other layers apply.

**Country profiles: qualifying documents 🟡**

Each country that joins the project has a public, versioned and reviewable **country profile** containing:

1. the **accepted documents** (e-passport, national identity document, driving licence, etc.) and **how to verify them cryptographically**: formats, public keys and certificate chains, revocation lists;
2. the **stable identifier of the person** in that country, where one exists (for example, a unique national number), and how to derive the *nullifier* from it, so that **all documents from the same country (passport, ID card, licence, reissues and renewals) yield the same *nullifier***;
3. the **weight** of the country's document evidence, set by public criteria;
4. local in-person validators and partners, local legal analysis and languages.

*Who writes the profile.* The community, from public specifications. When the country's government supports the project, it can **qualify** the profile (confirm formats, publish keys and revocation lists, clarify which fields are stable), but the profile is public and adopted through an open process (USIP), not by government decision (section 14.5). Revocation lists published by the issuer (lost, stolen, or deceased holders' documents) also help the USI lifecycle (section 9.5).

*Effect on duplicates.*
- **Within a country:** a well-qualified profile solves the case of people with several documents from the same country (renewed passport, ID card and licence): all lead to the same *nullifier*.
- **Across countries (dual nationality):** still not fully solved. Two countries produce two *nullifiers*. Linking documents from different countries would require cooperation between states and would reveal the dual citizenship to them, which is a privacy risk and must not be assumed. Mitigations: levels 3 and 4 require **non-document** evidence (physical presence, social vouching) that a second passport does not duplicate; challenge and jury; and conscious acceptance of a residue, since dual nationals are a minority and the gain from a second identity is limited at the higher levels. 🔴 *Open.*

*Minimal structure.* In the pilot, Brazil will have the first country profile (section 15.5). It serves as a template for the following ones and lets us test from the start that nothing in the protocol depends on it.

#### 9.2.3 Physical presence 🟡

- **Mechanism:** simultaneous in-person ceremonies with community validators and partner institutions (libraries, schools, NGOs). Each participant is verified by other participants and by accredited validators, at the same time, at several locations. A person cannot be in two places at once.
- **Strong** against Sybil; **essential** for people without documents.
- **Weaknesses:** cost and logistics; risk of collusion among local validators; accessibility needs. Mitigations: rotating and randomly drawn validators, audited sampling of ceremonies, signed records.

#### 9.2.4 Biometrics (optional) 🔴

- **Project position:** biometrics will only be adopted if duplicates can be detected **without a centralized biometric database** and without exposing data to any operator. Candidate techniques: multi-party computation and homomorphic encryption over biometric templates.
- **Risks:** biometric data cannot be revoked; imprecision (false positives grow with scale); demographic bias; coercion.
- **Stance:** always **optional**, never a minimum-level requirement, and subject to independent audit approval. It may be dropped if risks outweigh benefits.

#### 9.2.5 Continuity and history 🟡

Age of the USI, consistent use, credentials issued by recognized third parties. New accounts weigh less. Weak evidence in isolation, but it raises the cost of attacks that need fast results.

### 9.3 Assurance levels 🟡

Evidence is converted into public, standardized levels. The verifier chooses the level it requires.

| Level | Indicative requirement | Typical use |
|---|---|---|
| **1 – Basic** | Minimal social vouching | Forums, comments, anti-bot filter |
| **2 – Intermediate** | Solid social vouching **or** document proof | Polls, online communities, simple sign-ups |
| **3 – High** | Evidence from **two different categories** | Community voting, donations |
| **4 – Maximum** | **Three or more** categories, including physical presence or document proof | Benefit distribution, sensitive applications |

Calibration (weights, thresholds, time decay) is an experimental matter (section 16, experiments E2 and E3). A more refined model may replace the table with a continuous score while keeping levels as the interface.

### 9.4 Challenge and correction 🟡

- **Any holder may challenge** a suspicious USI by presenting evidence, possibly with a cap on simultaneous challenges to prevent harassment.
- **Randomly drawn juries** from high-level holders decide, under public rules, with a right of defence for the challenged party and a minimal record of the decision.
- **Effects of a confirmed duplicate:** the surplus record is cancelled; the legitimate USI remains; the attesters of the fraudulent USI lose reputation.
- **Safeguards against abuse:** repeated unfounded challenges cost the challenger reputation; decisions can be appealed.
- **Open questions:** jury resistance to collusion and vote buying; verifiably random drawing; workload.

This mechanism is what replaces the idea of "irrevocable" with **"permanent, but correctable"**.

### 9.5 Lifecycle 🟡

**Creation → evidence accumulation → use → key rotation → recovery (if needed) → challenge (if any) → inactivity or death.**

Handling death and inactivity must prevent use of deceased people's identities without exposing anyone's data. Hypotheses: marking inactivity after a long period without signs of life from the holder, with a challenge window; optionally naming a digital heir who can close (but not take over) the USI.

### 9.6 Identity sale and rental 🔴

The hardest attack to eliminate is the real person who **sells** their USI or acts as a "human for hire". Measures that make it harder without eliminating it:

- **Detecting control transfer:** key rotation followed by an abrupt change in usage pattern raises alerts.
- **Waiting periods and limits on sensitive operations**, which prevent fast monetization at scale.
- **Reputational cost to the holder** who cedes control, when the transfer is proven.
- **Periodic, optional "liveness" proofs** for high-level uses.
- **Resistance to coercion and vote buying:** in voting, schemes that prevent holders from proving to third parties how they voted.

This is a permanent research topic.

### 9.7 Binding between the USI and identity attributes (name and documents) 🟡

**The problem.** Guaranteeing a single USI per person (sections 9.1 to 9.6) is not enough. We must also prevent the same person from using two names or two CPFs, and prevent a third party who checks a USI from receiving information that differs from the truth. Since the public registry stores no personal data, the obvious path of writing "USI → name, CPF" on the ledger is ruled out.

**Principle.** USI guarantees two distinct things:
1. that the information is **unique** for that USI (there are no two current versions);
2. **how far it can be trusted** (how many independent issuers have verified it).

USI **does not make information true**. Whoever verifies it answers for its truth (section 9.7.5).

**9.7.1 Two kinds of information**

| Type | Examples | Rule |
|---|---|---|
| **Key attributes** | official name, date of birth, each country's stable national identifier (for example, the CPF) | **One current value** per type (and per country, for the identifier). Changing a value that has already been attested resets its trust. |
| **Documents** | passport, ID card, driving licence | Several may exist and be renewed or reissued (even by different bodies in the same country), but all must be **consistent** with the key attributes: same stable identifier and a compatible name. |

The **name is a key in the sense of being immutable and bound to the USI**, but it is **not unique across people** (there are many "John Smiths"). Uniqueness *across USIs* only applies to identifiers that the state guarantees to be unique (CPF, passport with country). Name matching (accents, abbreviations, transliteration from other alphabets) must be defined in the country profile. 🔴

**9.7.2 How the binding is recorded**
- For each USI and attribute type there is a single **slot**. The current value stays in the holder's wallet. The registry keeps only a **cryptographic commitment** to the value and minimal metadata (type, country, date, change counter).
- **Uniqueness across USIs.** To prevent the same CPF from being bound to two USIs, the registry stores a *nullifier* of the identifier. Caution: CPFs and document numbers have a small space of possible values, and a plain hash would be reversed by brute force (dictionary attack). Hypothesis: compute the *nullifier* with an **oblivious pseudorandom function (OPRF) whose key is split among several operators** (threshold cryptography), with query limits, so that no single operator can test CPFs. 🔴 This also applies to the document *nullifier* (section 9.2.2). The discarded alternative and the phased rollout, with the OPRF only in the mature network, are in section 9.7.10. Caution: known OPRFs use elliptic curves and do not resist quantum computers (section 24.2).
- **Presentation.** The holder reveals whichever value they choose (for example, the CPF) and proves, in zero knowledge, that it is the current value in the slot of their USI, with trust at or above the level required, revealing nothing else.

**9.7.3 Attribute trust**

This is a dimension **separate** from the uniqueness assurance levels (section 9.3): those say "this is a unique human"; this one says "this name/CPF can be accepted as true". Indicative levels, to be calibrated:

| Level | Name | Indicative requirement |
|---|---|---|
| **C0** | Declared | Provided by the holder, unverified |
| **C1** | Verified | One qualified issuer verified and attested |
| **C2** | Corroborated | Two or more **independent** issuers |
| **C3** | Trusted | Three or more independent issuers, or two plus cryptographic document proof |
| **C4** | Authoritative | Cryptographic proof from the primary source (for example, a state-issued chip document) plus corroboration |

The score depends on:
- **how many independent issuers** attested (independent = no common ownership or operational control);
- **the type of issuer**: primary source (whoever created the identifier, such as the state), a regulated institution with a legal duty to verify customers (such as banks), others;
- **the verification method** stated in the attestation: lookup in an official source, document check, self-declaration;
- **time** (attestations age and may require renewal);
- **revocations and challenges**: an issuer that discovers fraud can withdraw its attestation, and trust drops.

*Privacy of attestations.* Showing publicly that "Bank X attested the CPF of USI Y" would reveal which institutions the person deals with. Hypothesis: anonymous attestations, where the holder proves that an accredited issuer attested the attribute, without revealing which, and a per-issuer *nullifier* prevents double counting. 🔴

**9.7.4 Worked example: John**
1. **Registration.** John enters his name, date of birth, CPF and documents. The wallet reads chip documents whenever possible, to reduce typing errors, and **clearly warns that these attributes are keys and cannot be changed without losing trust**. While no issuer has attested (C0), John can correct mistakes freely.
2. **First attestation.** On opening an account (or linking his USI to his account) at Bank A, John presents his name and CPF. The bank, already legally required to verify its customers, checks them and issues a signed attestation. The attribute moves to C1.
3. **Corroboration.** Other banks and institutions repeat the process. With enough independent issuers, the attribute reaches C2 and C3.
4. **Use.** From then on, when presenting his USI with the CPF, any counterparty can accept the CPF and name as true, according to the level it requires. Another bank would not be told that John is called "Joseph" or has another CPF, because only one current value exists per slot.
5. **Change.** If John tries to change the CPF after it was attested, the new value is born at C0, the change history is preserved (counter) and he must go through the whole process again. Verifiers may require "no recent changes".

**9.7.5 What USI guarantees and what it does not**
- It guarantees **uniqueness** (one current value per type and one holder per identifier) and **measures trust** from independent issuers.
- It **does not guarantee truth**. If independent issuers are fooled by high-quality fake documents, a **synthetic identity** may reach high trust. Defences: issuer quality and accountability (each answers legally and reputationally for what it attests), cryptographic proof wherever it exists, and challenge (section 9.4).
- Someone who registers a false name or CPF (the "Joseph who wants to be Paul") must deceive several independent issuers and then **is stuck with that identity**: they cannot hold another USI and cannot go back to being recognized as Joseph without losing the trust earned.

**9.7.6 Identity squatting attack**

CPFs and document numbers are not secrets. A fraudster may try to register someone else's CPF first. If "first come" prevailed, the victim would be blocked from registering their own identity. Proposed rule: **stronger evidence wins, not order of arrival**.
- A merely declared attribute (C0) **does not block** the identifier. Whoever presents cryptographic proof of the original document (section 9.2.2), or reaches higher trust, takes the slot; the previous record is marked as disputed and suspended.
- Disputes between comparable evidence go to a **jury**, with physical presence when needed (section 9.4).
- The attesters of the overturned record lose reputation.

**9.7.7 Special cases: social name and legal name change**
- **Official name and social name** are distinct attributes. The social name is declared, **never reaches "official" trust** and is always presented with a **type label**, so that the verifier knows whether it received the official or the social name.
- **Legal change** (court or administrative decision, marriage, rectification). There is a dedicated path, **official change**: the holder presents evidence of the legal act (a new document issued by the authority, through the country profile). The new name is born with trust proportional to the strength of that evidence (chip document: high; paper only: rises with issuers' attestations), and the USI keeps **continuity** (same USI and other attributes). During the transition period, trust in the new name keeps rising.
- **Dignity and protection (🔴).** A legal name change must not expose the previous name or reveal to third parties that a change occurred. That could endanger trans people, victims of violence who change names for protection, among others. Hypothesis: change history is visible only to the holder and, in case of challenge, to the jury; the "recent changes" counter verifiers see counts only changes **without** a legal act. This design must be discussed with human-rights organizations before adoption.

**9.7.8 Relation to country profiles and governments**

Where a government supports the project (section 14.5), credentials signed by the **primary source** (chip document, official credential) reach high trust levels directly (C3 or C4). Where it does not, trust is built by secondary issuers, such as banks. In both cases the issuer is just an issuer: it gains no power over the system's rules.

**9.7.9 Limits**
- It depends on trustworthy and **independent** issuers. A cartel or collusion of issuers can inflate trust. Mitigations: public independence criteria, transparent accreditation, sampled audits and loss of accreditation.
- Who accredits issuers and under what criteria is an open governance question (section 14).
- The wallet must communicate clearly that key attributes are permanent, to avoid holder frustration.

**9.7.10 Identifier uniqueness: discarded alternative and phased rollout**

*Alternative considered and discarded: individual random key.* Combining the CPF with a random number that only the holder keeps (a hiding cryptographic commitment) protects against dictionary attacks: without the random number, nobody can test CPFs. It is exactly what the attribute slot already uses to hide the value. But it **cannot detect duplicates**: two registrations of the same CPF, with different random numbers, produce completely different values, and the system does not notice the repetition.

The deadlock is fundamental:
- to detect duplicates, **everyone must compute the same value** from the same CPF;
- if everyone computes the same value, **anyone who knows the computation** can test every possible CPF.

The known way out is the threshold OPRF (section 9.7.2): a secret common to the system but which no single operator holds. It is the soundest hypothesis identified so far, not a certainty. **Better alternatives are welcome** (open question 19).

*Phased rollout.* A public registry is permanent. Any value derived from a CPF that is written before the network is large and diverse stays exposed forever if the OPRF secret is ever compromised, and the security of a threshold OPRF depends on having many independent operators. Therefore the proposal is:

**Phase A: initial network (pilot and growth)** 🟡
- **No *nullifier* of a unique identifier** (CPF, passport number) is written to the registry. The slot holds only the hiding commitment, with the holder's random number.
- **It is explicitly accepted that identifier duplication is possible.** Combined mitigations:
  1. the other person-uniqueness layers (social vouching, physical presence, challenge);
  2. **more verifications:** high attribute-trust levels require more independent issuers;
  3. **local detection by the issuer,** who sees the CPF in clear: a bank notices, within its own customer base, that the same CPF was presented by two USIs, and may refuse to attest or flag the case;
  4. **government verification,** where supported (section 14.5): the primary-source credential guarantees the **truth** of the data (C4). Note: it does **not** guarantee that only one USI is bound to the CPF, because that would require the government to hold the USI↔CPF relationship, contradicting the principle that the state does not learn who uses USI.
- The attribute carries an explicit **"global uniqueness not verified"** mark, so no verifier assumes it. Duplicate-sensitive uses (such as benefit distribution) should rely on the other layers.
- The document layer (section 9.2.2) proves document authenticity but **publishes no *nullifier*** in this phase; its weight as uniqueness evidence is reduced.

**Phase B: mature network** 🟡
- The threshold OPRF is activated as an **already planned improvement**, under objective, public criteria:
  1. experiment E14 completed successfully and the protocol independently audited;
  2. a minimum number of independent operators, in diverse jurisdictions, respecting concentration limits (section 14.3);
  3. governance at least at phase 1 (section 14.1);
  4. approval through a USIP.
- **Migration.** Each holder, through the wallet, re-presents the slot value and generates the *nullifier* without exposing it. Duplicates accumulated in phase A surface at that moment and follow the challenge process (sections 9.4 and 9.7.6): the stronger evidence wins and the others lose trust in that identifier. Migration has a deadline window; unmigrated slots are capped at lower trust (for example, at most C2) and marked accordingly.
- **Rotating the system key** requires a re-derivation protocol for the values. 🔴 *Open.*

*Costs accepted in phase A:* possible duplication, more friction to reach high trust and a future migration with possible conflicts. *Benefit:* nothing that could be reversed by brute force is permanently recorded before the network has the diversity needed to protect it.

## 10. Access recovery

### 10.1 Principle 🟢

Losing access to one's identity cannot be permanent, but recovery is the attackers' preferred path. USI resolves the dilemma with **parallel routes**, each with requirements and waiting periods proportional to the strength of the evidence, always subject to **notification and veto**.

### 10.2 Routes 🟡

| Route | Mechanism | Requirement | Indicative wait |
|---|---|---|---|
| **A – Another device** | A key or passkey on another already-authorized device signs the key change | Possession of a valid device | Immediate |
| **B – Pre-rotated key** | The backup key, kept offline, takes over | Possession of the backup material | Short (24–72 h) |
| **C – Social recovery** | A quorum of **guardians** chosen by the holder (e.g. 3 of 5) authorizes the new key; the identity secret may be reconstructed through Shamir secret sharing [8] | Guardian quorum | Medium (≈ 7 days) |
| **D – Identity re-validation** | The holder redoes the proof of being the same person, through the evidence layers (section 9) | High-level evidence **and** combination with another route | Long (≈ 30 days) |

### 10.3 Common rules 🟢

1. Immediate, redundant **notification** (all devices, guardians and registered channels) on every request.
2. **Veto:** during the wait, any still-active legitimate key can cancel the request.
3. **Combining routes shortens the wait.** Example: guardians (C) + re-validation (D) reduce the wait; a single weak route increases it.
4. **Emergency freeze**, by the holder or a guardian quorum, suspends the USI until recovery.
5. **Mandatory rotation** after recovery: all old keys are revoked and a new backup key is registered.
6. **Periodic guardian review** by the wallet.
7. **Attempt limits** and growing delays after denied requests.

### 10.4 State machine (summary) 🟡

```
ACTIVE ──(recovery request)──► WAITING ──(period elapsed, no veto)──► RECOVERED ──► ACTIVE (new keys)
   │                              │
   │                              └──(veto by legitimate key)──► ACTIVE (request cancelled, alert)
   └──(freeze)──► FROZEN ──(unfreeze by quorum or valid key)──► ACTIVE
```

### 10.5 Attack analysis 🟡

| Attack | Defence |
|---|---|
| Attacker steals a device and starts recovery | Notification on independent channels; veto by other keys; waiting period |
| Attacker compromises guardians (collusion or social engineering) | Quorum from different circles; waiting period; holder veto; guardians who do not know each other (option) |
| Attacker forges re-validation | Requires high-level evidence **and** combination with another route; longer wait |
| Holder loses everything and has no guardians | Route D, slower |
| Coercion of the holder | Freeze by third parties and an emergency mode (🔴 open) |
| Denial of service against recovery | Multiple independent channels and routes |

### 10.6 Which secret is recovered? 🔴

Recovery swaps **control keys**. But the **identity secret**, the basis of pseudonyms and *nullifiers* (section 11.3), must also survive. If lost, the holder would get new pseudonyms and could in theory circumvent the "one account per person" limit at each service. Hypotheses to evaluate: splitting the identity secret among guardians (Shamir) and/or in an encrypted backup under the holder's control; or recording secret "epochs" in the registry, with rules so services handle transitions without allowing duplicate accounts. This is one of the protocol's most important design questions. The same applies to the random numbers that open the attribute commitments (section 9.7.2): the proposal is to derive them from the identity secret, so that recovering the latter recovers the former (section 10.8).

### 10.7 User experience 🟡

The security of any recovery scheme depends on people being able to use it. The wallet must guide initial setup (choosing guardians, backing up the backup key), periodically test recovery (a "drill") and be understandable to people with low technical familiarity.

### 10.8 Extreme scenarios: total loss without preparation and attempted abuse 🟡

This section records two scenarios identified in the project discussion and the hypotheses for handling them. **None has been tested.** The aim is to have them documented so the community can critique them and propose better solutions.

**10.8.1 Scenario 1: good faith, single device, no backup**

*The situation.* The person has a single phone, which holds everything. It is stolen or lost. They have no computer, backup or configured guardians.

*What is lost and what is not.*

| Lost (existed only on the device) | Not lost |
|---|---|
| Control keys and identity secret | The USI itself, which is in the public registry |
| Random numbers that open the attribute commitments (section 9.7.2) | Attestations held by issuers (for example, the bank knows that USI is linked to its customer) |
| Credentials stored in the wallet | Physical documents, if the person has them (the chip can be read again) |

*Diagnosis of current routes.* Routes A (another device) and B (offline backup key) do not exist for this person. Route C (guardians) exists only if configured. Route D remains, which requires high-level evidence **and** another route, and in practice is infeasible for someone who prepared nothing. The result is a **real risk of permanent loss of identity**, contrary to goal G4. There is an additional problem: without the random numbers, even a person who regains access cannot prove the attributes already registered.

*Treatment hypotheses* 🟡

1. **The wallet stores little: the phone holds the essentials, the world holds the rest.** The attributes' random numbers are **derived from the identity secret** (rather than drawn and stored separately), so recovering the secret recovers all commitments. Credentials are reissued by issuers, documents are read again from the physical chip, and attestations already sit in issuers' records.
2. **Recovery anchor to move up a level.** Without at least one anchor, the USI stays at level 1 and attributes at C0, when there is little to lose. Creating a USI remains free and unrestricted. Possible anchors are:
   - **encrypted backup** kept in the device maker's cloud, protected by a passphrase the holder chooses (this is the route B material). For someone with a single phone it is probably the most realistic path;
   - a **recovery sheet**, written or printed (libraries and community validators can help print it);
   - a **personal guardian**;
   - an **institutional guardian** (bank, library, NGO, public service), for people without a network of trusted individuals.

   *Trade-offs:* the maker's cloud reintroduces a dependency (reduced by local encryption); passphrases get forgotten; and any friction at sign-up can deter exactly those who need it most. The requirement applies to moving up a level, not to creating the USI.
3. **Issuer-assisted re-validation (a refinement of route D).** Those who prepared nothing turn to issuers that already attested their attributes and, where possible, to a physical presence point. Each issuer checks the person against its own records, which contain the link between the USI and the customer, and issues a signed **recovery confirmation**. Indicative requirement: two or more confirmations from independent issuers, or one confirmation plus an in-person validator. The more confirmations, the shorter the wait.
   *Risks and costs:* the issuer must offer the service (cost and liability; see section 13.3 on who funds it); social engineering against issuer staff requires a standardized procedure and strong verification; the issuer learns that the USI was recovered.
4. **Issuer-assisted quick freeze.** The person alerts an issuer, which may request that the USI be frozen after verifying them. The freeze has a **maximum duration** and expires if re-validation is not started, which limits abuse (someone pretending to be the victim to freeze another person's account).
5. **Full rotation after recovery** (section 10.3). The consequences for pseudonyms at services are in section 10.6.

**10.8.2 Scenario 2: bad faith ("I lost everything, I need to start over")**

*The situation.* The person has backups and every means of recovering, but claims total loss. The aim may be to obtain a second USI, to wipe a history (attribute changes, recoveries, reputation penalties) or to open a second account at a service.

*The loophole.* If "starting over" means creating a **new, independent USI**, the person ends up with two. In phase A there is no unique-identifier record in the public registry (section 9.7.10).

*Proposed rule: starting over does not create a new USI.* 🟡
- Those with attested attributes (C1 or higher) or person level 2 or higher must use **recovery of the same USI** (item 3 above). Creating a new USI is not an open path in this case. Issuers that already know the link **refuse** to bind a second USI to the same customer.
- Those who **never had anything attested** and are at level 1 have nothing to lose. For them, opening a new USI is acceptable. The old USI becomes orphaned and is marked inactive after a period. The abuser's gain in this case is a second USI with zero trust. This residue is accepted in phase A.

*Layers that hinder abuse*
1. **Detection by the issuer.** The bank that already linked the CPF to USI 1 notices the attempt to link USI 2 to the same customer. For two USIs to reach C3 without any issuer seeing both, the person needs at least **twice as many independent issuers**, which raises the cost considerably.
2. **Public recovery counter,** without identifying the person. Sensitive verifiers may require "no recent recoveries". Repeating "I lost everything" becomes a risk signal.
3. **High levels require evidence that is hard to duplicate** (physical presence, several independent issuers).
4. **Veto.** If the old device is still in the person's possession, the old key itself can veto the request.
5. **Proven consequences.** A proven fraudulent recovery (for example, when it turns out the backup existed) reduces the USI's trust and may go to a jury (section 9.4).

*Residue.* A person may hold two low-trust USIs, using issuers that never overlap. This residue is closed in phase B, when the unique-identifier record refuses the second USI (section 9.7.10).

**10.8.3 Proportionality** 🟡

The demands of recovery grow with what is at stake.

| Situation | What is at stake | Indicative handling |
|---|---|---|
| USI with no attested attributes, level 1 | Almost nothing | Simple restart; the old USI expires |
| Attributes C1 to C2 | Medium | Assisted re-validation with two confirmations; short to medium wait |
| Attributes C3 to C4 or level 3 to 4 | High | Re-validation with physical presence and issuers; long wait; veto |

**10.8.4 Pseudonyms and phase B** 🔴

Recovering the USI but losing the identity secret yields new pseudonyms at services (section 10.6). A hypothesis, not yet carefully analysed: in phase B, the value used to ensure "one account per person" at each service could be derived from a secret computed from the physical document through the technique in section 9.7.2, and so be rebuilt without a backup. It needs privacy analysis before being considered.

**10.8.5 Limits and invitations to the community**

There is a fundamental tension: recovery that is too easy opens the door to hijacking and abuse; too hard destroys the identity of those who acted in good faith. This design tries to make the demands proportional, to lean on institutions that already know the person and to prepare the holder from the start. **It does not eliminate the residue.** Points where better ideas are sought:
- alternatives to depending on issuers and institutions for people who are isolated;
- how to accredit institutional guardians without creating new control points;
- how to protect assisted re-validation against social engineering;
- how to tell, without exposing anyone, a legitimate restart from an attempt to obtain a second USI;
- how to preserve the privacy of the link between USI and issuer during recovery.

## 11. Privacy

### 11.1 Principles 🟢

- **No personal data in the public registry.**
- **Minimal disclosure** by default: reveal only what the verifier needs.
- **Unlinkability** across services.
- **Privacy by design** and by default.

### 11.2 Selective disclosure and zero-knowledge proofs 🟢

- **Verifiable credentials** (W3C VC [9]) issued by whoever has authority over the fact.
- **Selective disclosure** (for example, SD-JWT or BBS signatures) to reveal only specific fields.
- **Zero-knowledge proofs** for derived claims: "I am over 18", "I live in this municipality", "I am a unique human on this service".
- **Presentation protocols** compatible with open standards (for example, OpenID for Verifiable Presentations), easing integration with existing services.

### 11.3 Per-service pseudonyms and *nullifiers* 🟡

For each verifier (identified by a public identifier), the wallet computes:

- a **pseudonym** `P = PRF(identity_secret, verifier_id)`, stable for that service but with no apparent relation to those at other services;
- an associated ***nullifier***, which the verifier uses to detect that the same holder has not opened two accounts.

The zero-knowledge proof shows that `P` was correctly derived from an active USI at the required level, **without revealing the USI**. Two verifiers comparing their data cannot conclude that it is the same person.

**Important caveat:** unlinkability depends on **implementation discipline** (for example, not leaking the USI in network metadata, credential keys or presentation timing) and must be the subject of specific review.

### 11.4 Time-limited sharing 🟡

The holder grants access to data with a term, purpose and scope; revocation ends continued access. **Explicit limitation**: what has already been seen or copied cannot be withdrawn. The interface must make this clear. Mechanisms such as short-lived credentials and proofs instead of copies reduce the exposure surface.

### 11.5 Consent log 🟢

The wallet keeps, under the holder's exclusive control, a history of who accessed what, when and for what purpose.

### 11.6 Legal compliance 🟡

From the start the project considers the LGPD [5] and equivalent laws (for example, the European GDPR):

| Topic | Approach |
|---|---|
| **Minimization** | No personal data in the registry; credentials off-chain |
| **Erasure** | Possible, since data sits in the wallet and with issuers, not in the immutable registry |
| **Consent and purpose** | Sharing always by the holder's act, with a stated purpose |
| **Sensitive data (biometrics)** | Optional; only with reinforced safeguards and audit |
| **Controller and processors** | Analysis needed: do registry operators process personal data? The design aims for **no**, but this requires legal advice |
| **Impact assessment** | Prepare and publish a data protection impact assessment before the pilot |
| **International transfer** | Compliance analysis for each operator jurisdiction |

This section requires **review by digital law specialists**.

### 11.7 Metadata and network 🔴

Even without personal data, **metadata** (network addresses, timing, usage patterns) can identify people. To study: presentation without direct contact with the registry, use of relays and anonymity networks, batching events to reduce temporal correlation.

## 12. Operational security and cryptography

### 12.1 Required good practice 🟢

- Reference implementations in memory-safe languages wherever possible.
- Exclusive use of standardized primitives and reviewed libraries; **never home-made cryptography**.
- New cryptographic constructions (zero-knowledge circuits, nullifier protocols, pseudonym derivation) must have a **formal specification** and **independent review**.
- **Reproducible builds** and signed releases.
- Responsible vulnerability disclosure programme.

### 12.2 Audits 🟢

No component will be used with real people before an **independent audit**, with a public report. Audits repeat after each significant change.

### 12.3 Key custody and experience 🟡

Most digital-identity losses stem from usability failures. The project will use secure-chip storage on the device, **local** biometric authentication (which never leaves the device), optional encrypted backup and clear guidance.

### 12.4 Cryptographic migration 🟡

The protocol provides for deactivating compromised algorithms by governance decision, with a transition period and coordinated key rotation, without changing the USI. Details are in section 24.

## 13. Sustainability

### 13.1 Why not replicate Bitcoin's model 🟢

Bitcoin pays miners because it needs consensus, among hostile strangers, on something whose fraud yields immediate profit (money). USI is not money; its registry is lean (section 8.3), can be checked by light clients and **does not require millions of people to store a copy**. A **moderate set of independent operators** suffices, as with public Internet infrastructure (DNS root servers, Certificate Transparency logs [6], time synchronization and others).

### 13.2 Costs 🟡

| Category | Note |
|---|---|
| Registry node operation | Spread among operators; moderate per-operator cost, to be measured |
| Anchors on a public network (if applicable) | Mitigated by batching |
| Development and maintenance | Volunteer and/or grant-funded |
| Security audits | Significant and recurring cost |
| In-person ceremonies and validator support | Logistics, training, accessibility |
| Support, documentation and translation | Ongoing effort |
| Legal advice | Especially early on |

One step of the plan is to **put numbers on these costs**, including the annual cost per node operator (experiment E1).

### 13.3 Funding sources to test 🟡

1. **Institutional operators who benefit:** companies that spend on KYC and fraud, universities, NGOs, libraries, public bodies.
2. **Verification fee paid by verifiers (never by citizens):** services that consume verifications at high volume pay a minimal amount, earmarked for maintenance and transparent.
3. **Grants, calls for proposals and donations** from foundations and programmes supporting open infrastructure and digital rights.
4. **Volunteering** in development, motivated by purpose, learning and reputation.

**Reconciling with the "no profit" principle:** what the project forbids is profit for founders, investors and maintainers, and the creation of a financial asset. Revenue that covers **operating costs**, managed transparently by a non-profit foundation, is compatible with that principle.

### 13.4 Why there will be no token 🟢

A token would create a financial incentive to defraud registration and to sell identities, would attract speculation and would shift focus to price. It would also expose holders to tax and regulatory obligations. USI's incentives are institutional and reputational, not monetary.

### 13.5 Transparency 🟢

Revenue, expenses and pay (if any, for contracted services) are public, with periodic accountability and external audit.

## 14. Governance

### 14.1 Phases 🟡

| Phase | Who decides | Objective criteria to advance (to be defined) |
|---|---|---|
| **0 – Conception** | Founder and initial core | Whitepaper published and reviewed by independent specialists |
| **1 – Foundation** | Non-profit foundation with a board representing stakeholder groups | Network in production with independent operators in at least *N* countries; audits completed; successful pilot |
| **2 – Community** | Community of holders and contributors, through an open process | No single entity (including the foundation) can change rules unilaterally; the founder steps away |

The founder's departure is **objective** and **metric-conditional** (for example, number of independent maintainers, operator diversity, absence of a single point of decision failure), avoiding both a governance vacuum and perpetuation.

### 14.2 Mechanisms 🟡

- **Improvement proposals (USIPs):** public, versioned documents in the repository, with states (draft, under discussion, accepted, rejected), inspired by BIPs and IETF RFCs.
- **Rough technical consensus** on specification decisions, with peer review.
- **"One person, one vote"** with the USI itself, for decisions that affect the community, once the network is mature. Before that, no USI-based voting.
- **Separation of powers:** those who develop do not operate alone; those who operate do not decide alone; those who fund do not control.
- **Mandatory transparency:** meetings, decisions and votes are public (with security exceptions).

### 14.3 Capture resistance 🟡

- Concentration limits: no operator, country or organization may control more than a fraction of the operator set (for example, below 1/3).
- Required geographic, legal and institutional diversity.
- Limited terms and rotation in key roles.
- Changes to critical rules require a supermajority and a public waiting period.
- A plan for an honest **fork**: if governance fails, the community must be able to reproduce the system from open code and data.

### 14.4 Tension between "ownerless" and accountability 🔴

An ownerless system still needs some legal entity to sign contracts, receive donations, answer to authorities and commission audits. The foundation fills that role but must be designed **not** to become a control point. Legal form and jurisdiction are open questions, including whether the foundation should sit in the pilot's jurisdiction (Brazil) or a neutral one, to avoid the perception of national control.

### 14.5 Role of governments: support without control 🟡

Governments can be valuable allies and are also the actors with the greatest capacity for capture. USI adopts the stance **support yes, control no**, on equal terms for any government.

**What a government may do (optional):**
- qualify the country profile for its documents: publish formats, public keys and revocation lists, clarify stable identifiers;
- run nodes **like any other operator**, subject to the concentration limits (section 14.3);
- provide public spaces (libraries, service offices) for in-person ceremonies;
- recognize USI for specific purposes, and support the project with funding or legal advice.

**What a government may not do:**
- hold a special vote, veto, guaranteed seat or any other privilege in governance;
- alter rules, events or the state of any USI;
- access holders' data. The system is designed so that document verification is done **locally, using public data** (keys and revocation lists), **with no online query to the government**, so that the state does not learn who uses USI or where;
- make its support conditional on exclusivity, mandatory use or surveillance features.

**Safeguards:**
1. The system keeps working if support is withdrawn: only that country's document-layer weight drops, and the other layers compensate.
2. All agreements, contributions and communications with governments are public.
3. There are public criteria for accepting, weighting or refusing a country profile, including when the state issues documents abusively, uses its support for surveillance or could put holders at risk.
4. Concentration limits apply to entities tied to the same state.
5. A government's support does not make the project "Brazilian" or belonging to any other country.

In Brazil, government support is welcome but **not a prerequisite** for the pilot.

## 15. Adoption and entry strategy

### 15.1 The chicken-and-egg problem 🟢

An identity is only valuable if accepted, and only accepted if widely held. Strategy: start with **niches where USI solves a real pain that alternatives do not**, and grow from there.

### 15.2 Priority niches 🟡

| Priority | Use case | Why |
|---|---|---|
| 1 | **Proof of humanity** (anti-bot and anti-agent) | Immediate, growing pain; needs little personal information; tolerates basic levels |
| 2 | **Community and cooperative voting** | "One person, one vote" is an explicit need |
| 3 | **Donation and benefit distribution** without duplication | Partnership with humanitarian organizations |
| 4 | **Age verification** without data exposure | Growing regulatory demand |
| 5 | **People without documents** | Project mission; depends on field partners |
| 6 | **Passwordless login** | Reduces dependence on platforms |
| 7 | **Academic and professional credentials** | Added value once a user base exists |

### 15.3 Easing integration 🟡

- Bridges to widely used standards (for example, an OpenID Connect-compatible bridge), so a service can integrate USI without rewriting its authentication.
- Open libraries and SDKs, documentation and examples.
- Translation of documentation and interfaces (the repository's bilingual policy is the first step).

### 15.4 Growth strategy 🟡

1. **Closed pilot** with one partner community and one use case.
2. **Expansion through communities** (cooperatives, associations, open-source projects).
3. **Integrations** with low-friction platforms.
4. **Institutional recognition** (universities, NGOs, public bodies) once robustness is demonstrated.

Always measure: sign-ups, retention, fraud detected, successful recovery rate, onboarding time, cost per holder.

### 15.5 Pilot in Brazil and international expansion 🟡

**Pilot in Brazil.**
- Survey candidate Brazilian documents (for example, the national identity card, the chip passport and the digital driving licence) and check, for each, **whether offline cryptographic verification is possible** and **what the person's stable identifier is**. Accounts on digital government services may be assessed as complementary evidence. *All of these points need technical confirmation from the official specifications.*
- Engage the data protection authority (ANPD) and, when appropriate, public bodies, asking for support in qualifying the country profile **with no control in return** (section 14.5).
- Form the first network of partners: universities, libraries, cooperatives, civil society organizations.

**International expansion.** The order in which countries join is determined by the adhesion of local stakeholders, not by a central plan. For a country to be included, a public checklist is proposed:
1. at least one local stakeholder committed to support;
2. a country profile written and reviewed, with cryptographic verification of the documents tested;
3. local legal analysis (data protection, identity regulation);
4. local in-person validators;
5. translation and adaptation of interface and documentation;
6. human-rights risk assessment (countries where using USI could endanger holders);
7. approval through a USIP.

## 16. Experimental validation plan

To avoid decisions based on guesses, the project proposes a series of experiments, each with a **hypothesis, method and success criterion**.

| ID | Experiment | Hypothesis | Brief method | Success criterion (indicative) |
|---|---|---|---|---|
| E1 | **Registry cost and performance** | Option C meets R1–R8 at viable cost | Prototypes of options A, B and C under simulated load; measure cost per event, latency, size and operating cost | Negligible cost per holder; acceptable latency; light verification on modest devices |
| E2 | **Graph resistance to Sybil** | Structural analysis detects fake groups with high precision | Simulate honest networks and attacks (clusters, infiltration, humans for hire) and measure detection | High detection with low false-positive rate in defined scenarios |
| E3 | **Level calibration** | Levels can balance inclusion and security | Simulation with different weights; sensitivity analysis | Levels stable under reasonable parameter variation |
| E4 | **ZK document proof** | Proving authenticity and generating a *nullifier* is viable on ordinary devices | Prototype with test documents and phone verification | Acceptable proving time; no leakage; handling of the "multiple documents" case |
| E5 | **Recovery protocol** | The four routes work in parallel without opening gaps | Implementation, red-team testing with a simulated adversary, device-loss simulation | No successful hijack in defined scenarios; high legitimate recovery rate |
| E6 | **Recovery usability** | Lay people can set up guardians and backups | Usability tests with diverse participants, including low technical familiarity | High rate of correct setup; low abandonment |
| E7 | **Pseudonyms and unlinkability** | Distinct services cannot correlate the same holder | Formal analysis and correlation tests, including via metadata | No practical correlation vector identified |
| E8 | **Challenge jury** | Randomly drawn juries decide well and resist collusion | Simulations and a pilot with synthetic cases | Error and manipulation rates below the set limit |
| E9 | **Identity secret in recovery** | The secret can be recovered without allowing duplicate accounts | Compare variants (Shamir, encrypted backup, epochs) | A variant that preserves pseudonyms and prevents duplication |
| E10 | **In-person ceremonies** | Ceremonies scale and resist local collusion | Pilot in one partner community | Viable cost per person; collusion detected in sampled audit |
| E11 | **Biometrics without a central database** (optional) | Viable with demonstrated privacy | Feasibility study and expert review | If no secure, accurate variant exists, **drop it** |
| E12 | **Sustainability** | Verification fees cover operating costs | Financial model and consultation with potential operators and verifiers | Cost coverage without requiring payment from holders |
| E13 | **Country profile: Brazil** | Brazilian documents can be verified cryptographically and offline and a stable person identifier derived | Survey of official specifications; verification prototype; expert consultation | At least one document verifiable offline with a stable identifier, or a documented conclusion that it is not possible |
| E14 | **Attribute binding (cryptography)** | Slots with commitment, threshold-OPRF uniqueness and zero-knowledge proof of currency can be built at viable cost | Prototype of the slot, of the *nullifier* with OPRF split among operators and of presentation; dictionary-attack and attestation-privacy tests | No leakage of values by brute force in tested scenarios; proofs in acceptable time on a phone |
| E15 | **Attribute trust model** | Independent issuers raise trust reliably and the model resists squatting, collusion and synthetic identity | Simulation of honest and fraudulent issuers, squatting attacks, cartels and synthetic identities; tests with legal name-change cases | High detection with low false positives; no squatting path without a possible challenge |
| E16 | **Unprepared recovery and abuse** | Issuer-assisted re-validation recovers good-faith people at a high success rate, and a red team can neither hijack a USI nor obtain a second high-trust USI | Pilot of assisted re-validation with partner institutions; total-loss simulation; social-engineering attacks against issuers; attempts to obtain two USIs with disjoint issuers | High legitimate recovery rate; no hijack or second USI at C3 or above in the defined scenarios |
| E17 | **Key quality and failure-proof activation** | Rejection by construction, monitors and "publish before use" detect weak keys and block their activation | Inject weak keys (small scalars, invalid points, repeated) in a test environment; measure detection and blocking time; test the proof of compromise; red-team attack on ceremonies | All known weak keys rejected; detection in minutes; no activation without independent verification |
| E18 | **Cryptographic migration** | Algorithm swaps, hybrid signatures and mass rotation work without changing USI and at viable cost | Prototype of events with algorithm identifiers; classical plus post-quantum hybrid mode; simulation of an algorithm "dying"; measure sizes, latency and cost; evaluate post-quantum alternatives for OPRF and zero-knowledge proofs | Full simulated migration within target; acceptable cost and size; plan for OPRF and proofs |
| E19 | **USI-O: representation and powers** | Representation credentials, threshold key and succession work in real organizations | Pilot with a partner association or cooperative; scenarios of representative departure, collusion and succession | Powers applied correctly; immediate revocation; recovery by quorum |
| E20 | **Document signing and recognition** | USI signatures are verifiable by third parties, accepted by private parties and compatible with the legal framing of an advanced signature | Signing pilot in real workflows; legal opinion on Law 14,063/2020 and PM 2,200-2/2001; third-party verification test | Third-party verification without our help; favourable opinion on advanced-signature framing; acceptance by at least one institution |

Results and data from the experiments will be **published**, including negative ones.

## 17. Project risks

| Risk | Likelihood | Impact | Response |
|---|---|---|---|
| Low adoption (chicken and egg) | High | High | Initial niches, easy integration, partners |
| Shortage of volunteers and funding | High | High | Focus on grants/calls, lean scope, institutional partnerships |
| Legal incompatibility (LGPD, identity regulation, biometrics) | Medium | High | Early legal advice, privacy by design, controlled pilot |
| Sophisticated Sybil attacks and identity marketplaces | High | High | Multiple layers, challenge, levels, monitoring |
| Security flaw in a cryptographic component | Medium | Very high | Review, audit, formal specification, vulnerability programme |
| Governance capture | Medium | High | Phases, concentration limits, transparency |
| Scope creep | High | Medium | Start with a restricted MVP (proof of humanity), cut what is not essential |
| Perception of "compulsory ID" or surveillance | Medium | High | Non-mandatory use, clear communication, per-service pseudonyms |
| Dependence on third parties (public network, state certificate chains) | Medium | Medium | Hybrid option, per-country weighting, contingency plan |
| Coercion of vulnerable users | Medium | High | Emergency mode (under study), freeze by third parties |
| Perception of control by one government, or capture by a supporting state | Medium | High | Support without control (section 14.5), concentration limits, public agreements, neutral jurisdiction to be considered |
| Withdrawal of government support or policy change | Medium | Medium | System works without the support; document-layer weight adjustable |
| Brazil-specific shortcuts that do not generalize | Medium | Medium | Pluggable country profiles; architecture review before expansion |
| Squatting on other people's identifiers | High | High | Stronger evidence wins, not order of arrival; challenge and jury (section 9.7.6) |
| Synthetic identity built with high-quality fake documents | Medium | High | Accountable issuers, cryptographic proof, challenge, revocation of attestations |
| Collusion or cartel of issuers | Medium | High | Public independence criteria, transparent accreditation, audit |
| Exposure of people through name-change history | Medium | Very high | History visible only to the holder and jury; consultation with human-rights organizations |
| Identifier duplication in the initial phase (no global *nullifier*) | High | Medium | "Global uniqueness not verified" mark; more independent issuers; local detection by the issuer; other uniqueness layers; future OPRF activation (section 9.7.10) |
| Permanent loss of identity by unprepared people | High | High | Recovery anchors to move up a level; issuer-assisted re-validation (section 10.8) |
| Social engineering against issuers in assisted re-validation | Medium | High | Standardized procedure, strong verification, several independent confirmations |
| Fraudulent recovery to obtain a second identity | Medium | Medium | "Starting over does not create a new USI", detection by the issuer, recovery counter, proportionality |
| Duplicated effort or competition with similar initiatives | Medium | Medium | Collaboration stance (section 5.2); research and talk before building; interoperate |
| Dependence on a third-party project that changes course, is acquired or shut down | Medium | Medium | Reuse criteria (section 5.5); dependencies behind replaceable interfaces |
| Key-generation failure (weak randomness) in wallets or issuers | Medium | Very high | Rejection by construction, mixing of sources, monitors, "publish before use" (section 23) |
| Compromise of an accredited issuer | Medium | High | Power limit per issuer, threshold keys, automatic revocation, several independent issuers (sections 9.7.3 and 23) |
| Legal and political barrier to recognizing signatures and replacing certificate authorities and notaries | High | High | Phased strategy, coexistence, dialogue with regulators, legal opinion (section 22) |
| Cryptographic break or quantum advance before migration | Low to medium | Very high | Cryptographic agility, hybrid mode, hash pre-rotation, emergency procedure, drills (section 24) |
| Shell organizations using USI-O for fraud | Medium | High | Trust through independent issuers, power limits, challenge (section 21.8) |
| Loss of control of a USI-O through departure or collusion of representatives | Medium | High | Threshold key, quorum, veto, succession (section 21.5) |

## 18. Open questions

1. Which registry option (A, B or C) is best? (E1)
2. How should weights and thresholds of the assurance levels be calibrated? (E3)
3. How resistant is the social graph to organized attacks? (E2)
4. How should people with several valid documents be handled? (E4)
5. Are biometrics without a central database viable and desirable? (E11)
6. Which waiting periods balance security and convenience in recovery? (E5, E6)
7. How can the identity secret be protected during recovery without allowing duplicate accounts? (E9)
8. How should juries be structured to resist collusion and scale? (E8)
9. How to handle death, inactivity and digital inheritance?
10. How to protect people under coercion?
11. How to reduce exposure through network metadata?
12. What legal form and jurisdiction for the foundation?
13. Which numeric criteria mark the governance phase transitions?
14. How to include people without smartphones or with limited connectivity?
15. Is the verification-fee model compatible with the non-profit principle and with system neutrality?
16. How should dual nationality across countries be handled without exposing the dual citizenship to any state? (E4, E13)
17. Which public criteria accept, weight or refuse a country's profile, including on human-rights grounds?
18. Should the foundation be based in the pilot's jurisdiction (Brazil) or a neutral one?
19. How can uniqueness of small-space identifiers (CPF, document numbers) be computed without allowing a dictionary attack? (E14)
20. How can attestations be recorded without revealing the holder's relationship with each issuer? (E14)
21. How should "independent issuer" be defined, who accredits issuers, and how is collusion avoided? (E15)
22. How can a legal name change be allowed without exposing the holder's history? (E15)
23. How should names be matched across documents (accents, abbreviations, transliteration)?
24. Which objective criteria activate the threshold OPRF (phase B), and how should phase A records be migrated, including accumulated duplicates? (E14)
25. Is there a better alternative to the threshold OPRF for detecting duplicates of small-space identifiers without exposing them?
26. How can people without a support network obtain a recovery anchor without an excessive entry barrier? (E6, E16)
27. How can assisted re-validation by issuers be incentivised and standardized (cost, liability, defence against social engineering)? (E16)
28. How can the identity secret and the attributes' random numbers be derived so that they are recoverable without compromising privacy? (E9, E16)
29. How can a legitimate restart be told apart, without exposing anyone, from an attempt to obtain a second USI?
30. Build our own infrastructure or contribute to an existing initiative that meets the same characteristics? Which components to reuse and with which projects to partner? (section 5)
31. How can we collaborate with initiatives that have a token, a company or different governance without compromising the absence of an owner and of profit?
32. How should legal orders (judicial and administrative) over a USI or USI-O be handled without creating a unilateral power? (sections 14.4 and 21.5)
33. What is the possible legal framing of USI signatures, and the path to recognition without losing the essential characteristics? (E20)
34. How does USI relate to the public faith of notaries without improperly replacing it? (section 22.4)
35. How can issuers and institutional guardians be accredited without creating new control points? (section 23.9)
36. How can a subtle weak randomness generation, which passes the known tests, be detected? (E17)
37. How can automatic revocation on proof of compromise be reconciled with non-repudiation? (section 23.6)
38. What post-quantum alternative exists for the threshold OPRF and for current zero-knowledge proofs? (E18)
39. How can partners and beneficial owners in a USI-O be protected without losing the necessary transparency? (section 21.7)
40. What are the calendar and triggers for deprecating algorithms? (section 24.4)

## 19. Roadmap

| Stage | Deliverables |
|---|---|
| **1. Whitepaper** | Version 0.1 (this document); open review; version 0.2 with contributions |
| **2. Community and review** | Expert review; contact with similar projects for collaboration (section 5.2); presentation to decentralized identity communities; initial core of collaborators |
| **3. Repository organization** | Licences, `CONTRIBUTING`, code of conduct, USIP process, issues for each open question |
| **4. Proofs of concept** | Experiments E1–E20 by priority |
| **5. Legal and institutional analysis** | Opinion on LGPD and other rules; foundation design |
| **6. Funding and outreach** | Grant applications; outreach material; partner search |
| **7. Pilot (Brazil)** | Initial use case with a partner community in Brazil; metrics; public report; checklist for admitting new countries |
| **8. Institutionalization** | Foundation incorporated; transition to governance phase 1 |

There are no fixed dates in this version: the schedule depends on community formation and funding.

## 20. How to contribute to this document

This is an open draft. To contribute:

- **Critical review:** open an issue pointing out errors, gaps or missing risks. Well-founded criticism is welcome.
- **Source references:** section 5 and the technical claims need primary sources; help verify and add them.
- **Survey of initiatives:** help verify and expand the survey in section 5.1, including projects outside the cryptocurrency world and in other languages.
- **Specialists:** cryptography, distributed systems, digital identity, data protection law, experience design, anthropology/social sciences (for inclusion), ethics.
- **Experiments:** take on one of experiments E1–E20.
- **Translation and language review:** keep the Portuguese and English versions in sync.

All significant changes must be recorded in the version history (section 26).

## 21. USI-O: identity of organizations

> **Part II.** Sections 21 to 24 extend the proposal of Part I (people) to organizations, digital signature and authentication, and cover the lessons from real failures in key infrastructure and cryptographic migration. This part is **more preliminary** than the previous ones: almost everything here is 🟡 or 🔴. If it grows, it will be split into its own document.

### 21.1 The USI family 🟢

The project now has two parts that share one core:

| Component | Description | Where described |
|---|---|---|
| **Common core (USI Core)** | Public registry, key events, recovery, transparency, cryptographic agility and governance | Sections 6, 7, 8, 10, 12, 14 and 24 |
| **USI-P (person)** | Identity of the human being: uniqueness, attributes and privacy | Sections 9 and 11 |
| **USI-O (organization)** | Identity of legal entities and other organizations: attributes, representation and powers | This section |
| **Trust services** | Document signing, authentication and timestamping, for people and organizations | Section 22 |

The split recognizes that people and organizations have different problems of uniqueness, privacy and control. The core, however, is one: the same registry, the same key and recovery rules, and the same governance.

### 21.2 What is different about organizations 🟡

| Aspect | USI-P | USI-O |
|---|---|---|
| What is guaranteed unique | One human being, one USI | One legal entity, one USI-O (by national identifier) |
| Primary source | State-issued identity documents | Official registers of legal entities (for example, the Federal Revenue Service and the commercial boards, in Brazil) |
| Main threat | Fake human accounts | Shell companies, representatives without authority, power-of-attorney fraud |
| Who acts | The person | Authorized people, within powers and limits |
| Privacy | Personal data, protected | Generally public data; exception for natural persons tied to the entity (partners, sole proprietors), subject to the LGPD |
| Key | The person's; recoverable by them | The organization's, with a control and succession policy |

**A USI-O is never proof of humanity.** One person may legitimately control several organizations. Therefore any use that depends on "one person, one vote" (section 12) accepts only USI-P.

### 21.3 Identifier and attributes 🟡

- The USI-O has its own permanent identifier (`did:usi`), with the same rules for keys, rotation and recovery.
- **Key attributes:** the entity's national identifier (the CNPJ, in Brazil), corporate name, legal nature, date of incorporation and registration status. They follow the *slot* model and **attribute trust (C0 to C4)** of section 9.7, with independent issuers.
- **Primary source:** where a government supports the project (section 14.5), extracts and credentials signed by the official registers lead directly to high trust levels. Where there is none, trust is built by independent secondary issuers.
- **Uniqueness:** since an entity's identifier is generally **public**, the unique record does not need the protection technique used for people's identifiers (OPRF, section 9.7.2). **Exception:** sole proprietors and micro-entrepreneurs have a CNPJ tied to a natural person and must be handled with USI-P's protections.
- **Changes** (corporate name, address, legal nature) follow the "official change" path of section 9.7.7, with evidence from the register.

### 21.4 Representation and powers: the relation between e-CPF and e-CNPJ 🟡

Today, in ICP-Brasil, the e-CPF and the e-CNPJ are distinct certificates, used in government and private applications [15]. In USI, the relation between the person and the organization is an explicit, verifiable piece of data:

- **An act on behalf of the organization** is a signature by the **person** (USI-P) accompanied by a **representation credential** from the **organization** (USI-O). The verifier checks both.
- **The representation credential** states: the role (managing partner, director, attorney, accountant, user), the scope (types of act), the limits (amount, term), any requirement of joint signature (for example, two of three directors), whether sub-delegation is possible (with limited depth), the validity and how it is revoked.
- **Who issues the credential:** the official register (where supported), the registered corporate act, or the organization itself, by quorum decision.
- **Zero-knowledge proofs** make it possible to show, for example, "I am authorized to sign contracts up to R$ X for this organization", without revealing other data.
- **Power lives in the policy, not in a key.** When a representative leaves, the credential is revoked. There is no "company key" that walks out with the person, a common problem when a certificate is tied to a single responsible person.

### 21.5 Organization control and succession 🟡

- The USI-O control key is a **threshold key** among representatives (for example, 2 of 3), never a single person's key.
- Sensitive operations (changing the powers policy, appointing or removing representatives) require a quorum and a **waiting period with notification and veto**, as in section 10.3.
- **Recovery:** by quorum of the remaining representatives and re-validation with the official register or independent issuers (section 10.8).
- **Succession:** if no representative remains (for example, the death of the sole partner), recovery is by evidence of a legal act (probate, judicial or administrative appointment). 🔴 Open: how to handle legal orders without creating a unilateral power (section 14.4).

### 21.6 Lifecycle 🟡

**Incorporation → attribute attestation → operation → changes → merger, split or absorption (succession between USI-O) → suspension (for example, registration ineligibility) → closure.** On closure, the USI-O is ended but its history remains, and signatures made while it was active stay verifiable.

### 21.7 Privacy and transparency 🟡

- Entity data is public only to the minimum needed. Ownership structure and beneficial owners are sensitive and use **selective disclosure** and proofs ("there is a partner resident in country X", with no names), according to applicable regulation.
- The natural persons tied to the organization keep their privacy: when acting for it, they reveal only what the act requires.

### 21.8 Specific risks 🟡

| Risk | Response |
|---|---|
| Shell companies and use of straw owners | Trust through independent issuers and primary source; power limits; graph signals between organizations and people; challenge |
| Power-of-attorney or powers fraud | Credentials with scope, limit and term; joint signature; immediate revocation |
| Organizations used to circumvent "one person, one vote" | USI-O never counts as proof of humanity |
| Loss of control through departure or collusion of representatives | Threshold key, quorum, waiting period and veto |
| Exposure of partners and beneficial owners | Selective disclosure and zero-knowledge proofs |

### 21.9 Countries and official sources 🟡

**Country profiles** (section 9.2.2) now also include registers of legal entities: formats of signed extracts, registration-status lists and local rules. Government support remains optional and **without control** (section 14.5).

## 22. Digital signature and authentication: an alternative to certificate authority hierarchies

### 22.1 Two central uses 🟢

1. **Document signing:** proving authorship, integrity and time.
2. **Authentication and authorization:** proving the legitimacy of whoever accesses an online system, as a person or as a representative of an organization, with the role and powers they hold.

Both rest on the same core: USI keys, registry state and credentials. The document never goes into the registry; only its *hash* is anchored, when there is a need to prove the time.

### 22.2 How a USI signature is verified 🟡

1. The verifier receives the document (or its *hash*), the signature, the signer's identifier (or a pseudonym) and the necessary credentials (attributes, role).
2. It checks the signature against the signer's **key current at the time of signing**, using registry state and an inclusion proof (light client).
3. It checks that the key was not revoked or declared compromised, and that the proof is **fresh** enough (section 23.7).
4. It checks the **timestamp:** the *hash* was anchored in a batch in the registry, proving it existed at that time.
5. It checks the required levels: attribute trust (C), person assurance level and, where applicable, role and powers in the organization.
6. It applies the verifier's policy: accepted algorithms, validity, minimum level.

### 22.3 Comparison with the certificate authority hierarchy 🟡

| Aspect | CA hierarchy (current model) | USI model (proposed) |
|---|---|---|
| Trust structure | Root, intermediates and end certificates; roots are accepted by the trust programs of browsers, systems and governments | No key-issuing hierarchy: the USI is self-certifying; trust in attributes comes from several independent issuers, in levels |
| Who binds key to person | A CA, through its own validation or registration agents | Attestations from independent issuers and uniqueness evidence, recorded and auditable |
| Effect of a weak or compromised issuing key | Can forge identities of any holder in the chain | A single issuer cannot raise trust above C1 or C2 alone; damage is limited to what it attested and is detectable |
| Revocation | Lists and queries distributed heterogeneously; outdated trust stores | Single, public registry state, with freshness proof |
| Transparency | Partial (for example, the public certificate log for TLS [6]) | All events and attestations are public; without inclusion in the registry there is no validity |
| Time | Timestamping authority | Batch anchoring in the registry |
| Legal value | Legal presumption for documents signed with ICP-Brasil certificates [13] | By acceptance of the parties, until recognized (section 22.4) |
| Cost to the citizen | Purchase, validity and renewal of the certificate | Free |

### 22.4 Legal value and the role of notaries 🔴

This is the main barrier to replacement and needs legal advice (to be confirmed).

- **ICP-Brasil.** It was established by Provisional Measure No. 2,200-2/2001 [13], which, as commonly read, gives a presumption of validity to documents signed with ICP-Brasil certificates and admits other means of proving authorship and integrity, provided the parties accept them.
- **Law No. 14,063/2020 [14].** It defines simple, advanced and qualified electronic signatures. For the advanced one, requirements include a unique link to the signer, use of signature-creation data under the signer's control with a high level of confidence, and detection of any later modification.
- **Hypothesis:** USI signatures could qualify as **advanced** (and simple) electronic signatures, valid by acceptance of the parties. Equivalence to the **qualified** signature would require legal recognition.
- **Notaries.** Beyond technology, they perform a legal **public-faith** function, assigned by law to delegated officers (authenticity of acts, property registries, among others). USI can dematerialize the technical parts (identification, integrity, timestamping) but **does not replace public faith without a change in law**.

### 22.5 Phased strategy 🟡

| Phase | Goal |
|---|---|
| **1. Coexistence** | USI works as an advanced electronic signature by acceptance of the parties (private contracts, associations, internal workflows, communities). ICP-Brasil certificates are accepted as evidence, and there is interoperation. |
| **2. Recognition** | Dialogue with regulators and competent bodies (for example, the ITI, which administers the ICP-Brasil root, and those supervising notaries), legal opinions, sector rules and acceptance by institutions. |
| **3. Partial replacement** | Where the law allows, USI replaces technical functions currently provided by certificate authorities and notarial services. |

USI positions itself as a **technically more transparent alternative** and, in the long run, a **replacement for parts** of the current model. The collaboration stance of section 5.2 also applies here: seek dialogue and interoperability before confrontation.

### 22.6 Server (TLS) and code-signing certificates 🔴

The cases analysed in section 23 involve TLS and code-signing certificates. Replacing that ecosystem requires browser and operating-system vendors to adopt another model, which is **not a short-term goal**. Paths to study: using the USI-O as an additional signal of the identity of the organization that owns a domain (link between domain and USI-O); a transparent registry as an extra layer for detecting improper issuance; and participation in standardization forums.

### 22.7 Limits 🟡

- Legal value depends on law and acceptance, not on technology.
- For applications where the verifier demands an ICP-Brasil or equivalent certificate, USI alone is not enough.
- A signature proves control of a key by a USI, and the trust level comes from attestations; it does not make what the document states true.

## 23. Lessons from real failures and procedures that prevent human error

### 23.1 Cases analysed 🟡

This section starts from two recent reports on key-infrastructure failures [15][16]. **Caveats:** the data come from the reports, which differ in details (for example, one speaks of six intermediates for TLS and two for code signing, the other of eight intermediate TLS certificates); the cause of the weak key generation was not clarified in them; and official investigations may differ.

**Case 1: trivial private keys in intermediate authorities.** According to the reports, eight intermediate-authority certificates of eMudhra (operator of the emSign brand), tied to chains recognized by major trust programs, had private keys of tiny value (4, 56, 66, 115, 155, 156, 230 and 237), even though they used the NIST P-384 curve, which should offer about 192 bits of security. With so few possible values, about 255 attempts would suffice to recover any of them. A researcher reported the problem and proved possession of the keys by signing a message with them. The described risk is the issuance of fraudulent certificates for domains the attacker does not control, which would enable interception of connections. According to the reports, there is no public evidence of malicious exploitation.

**Response.** Mozilla blocked the intermediates in under three hours and removed the root from its store; Chrome and Apple also acted. But the response was uneven: according to one report, at the time of the original report Edge on Windows 10 kept connecting to 12 vulnerable hosts, and applications with their own trust stores remain exposed. According to the Chrome Root Program, no TLS certificates from the six TLS intermediates appeared in public certificate logs before the block, which reduced the risk.

**Case 2: ICP-Brasil and the Mozilla store.** According to the article [15], the ICP-Brasil root is not in Mozilla's store; an inclusion request made in 2020 pointed out, according to participants in the public discussion, certificates outside WebPKI requirements, invalid domain names and the extensive hierarchy of subordinate authorities. The author stresses that **it is not possible to conclude that ICP-Brasil is more or less secure** from the incident, and that being recognized is not the same as operating securely.

### 23.2 Lessons and USI's responses 🟡

| # | What the reports say | Underlying failure | USI response |
|---|---|---|---|
| 1 | Trivial private keys with a strong algorithm (the advertised size did not match actual security) | Key generation without validating the result | Rejection by construction of weak keys in the wallet, protocol and monitors (23.4); activation only after independent verification (23.5) |
| 2 | Discovered by a third party, who proved possession of the key by signing a message | Neither audit nor the issuer's monitoring detected it; a simple test was not run | Continuous monitoring by anyone; proof of compromise with automatic revocation (23.6) |
| 3 | A weak intermediate would allow forging certificates for other people's domains | Issuing power concentrated in few keys; very broad damage | No key-issuing hierarchy; threshold keys; trust requires several independent issuers (22.3, 23.5) |
| 4 | Fast response by some and slow or partial by others; outdated own trust stores | Trust and revocation distributed heterogeneously | Single source of truth in the registry; mandatory freshness proof; fail closed on sensitive operations (23.7) |
| 5 | Transparency of certificate logs reduced the risk | Transparency works as a safety net | Mandatory transparency for every event and attestation (22.3) |
| 6 | Slow recovery, compared to Heartbleed: many systems hard to update | Late cryptographic agility and inventory | Agility from the design and periodic drills (section 24) |
| 7 | Being in a trust program does not guarantee secure operation; control by audit and third-party notifications | Paper compliance instead of continuous technical verification | Automatic, continuous and public technical verification; revocable accreditation (23.6, 23.9) |
| 8 | Extensive hierarchy with compliance questions (according to participants in the public discussion) | Long hierarchies multiply points of failure and non-compliance | Flat structure and machine-checkable rules at each issuance (23.4). USI does not presume to be better; it aims to be easier to verify |

### 23.3 Principles 🟢

1. **A chain is only as strong as its weakest link.** The project must ensure no link can be weak without being detected and contained.
2. **Make error impossible, not merely forbidden.** People never choose or type keys: the system generates and validates them. There are no manual shortcuts.
3. **Automate control.** Machine checks at the creation of every key, rather than periodic paper audits.
4. **Independent and public verification.** Anyone can reproduce the tests.
5. **Mandatory transparency.** What is not in the registry does not count.
6. **Contain damage.** Short-lived keys, limited scope, threshold and no hierarchy.
7. **Respond quickly and auditably.**
8. **Learn from incidents,** with a public report.

### 23.4 Rejecting weak secrets 🟡

| Secret | Rule (indicative) |
|---|---|
| **Signing keys** (elliptic-curve and post-quantum) | Generated on the device (in a secure element where available) by an approved random generator; never imported by hand. The protocol rejects: keys whose private scalar may be small (testing whether the public key is one of the first multiples of the base point), points of small order or off the curve, keys in lists of known weak or compromised keys, and keys repeated across USIs. A simple test such as the first-multiples check would detect keys of the reported kind. |
| **Entropy** | Mixing of multiple sources (system, hardware, device events); generator health tests; device attestation where available |
| **Algorithms and parameters** | Closed, versioned list; minimum sizes; nothing outside the list |
| **Backup passphrases** (section 10.8) | Generated by the system (word list with minimum entropy) or, if chosen by the user, accepted only after entropy and leaked-password checks; derivation by a slow, hardware-resistant function (for example, Argon2id) |
| **PINs and local codes** | Attempt limit enforced by secure hardware; progressive lockout; obvious or sequential PINs rejected |
| **Recovery codes and seeds** | Randomly generated and shown once; never derived from personal data (date of birth, CPF) |
| **Issuer and operator keys** | Threshold custody among several custodians; generation in a recorded, verifiable ceremony; activation only after the publication period (section 23.5) |

### 23.5 Issuing and activating sensitive keys: publish before use 🟡

1. An issuer's or operator's key is generated in a **ceremony with threshold custody**: no person knows it in full.
2. Before activation, the public key is published in the registry in a **pending** state.
3. **Independent monitors** run the checks of section 23.4 and others; anyone can challenge with proof.
4. The key becomes active only after a **minimum period without challenge** (for example, 24 to 72 hours) and with a minimum number of independent monitors confirming.
5. Manual steps require **two or more responsible people** (four-eyes rule), with a public record of the ceremony where applicable.
6. There are no manual issuance paths outside this flow.

In principle, public verification before activation would allow detecting keys of the reported kind.

### 23.6 Continuous monitoring and proof of compromise 🟡

- **Public, reproducible monitors** continuously scan all registered keys: small values, invalid points, repetitions, lists of compromised keys and statistical anomalies.
- **Proof of compromise.** Anyone who can sign with another USI's private key (as the researcher in the case did by signing a message) can present that signature as proof. Verification is automatic and results in **immediate freezing and revocation**, forced rotation and re-validation of the affected attestations. There is a reward programme for responsible disclosure.
- **Beware of non-repudiation.** A holder could leak their own key on purpose to repudiate signatures. Signatures prior to the moment of revocation, proven by timestamp, remain valid, and repeated leaks are treated as a risk signal (section 23.10).

### 23.7 Revocation and verification with freshness 🟡

- Verifiers use registry state with **inclusion and freshness proofs**, with a maximum age per risk level (minutes for sensitive operations, hours for the rest).
- **Fail closed** on high-level operations: without a fresh proof, no acceptance. No silently accepting when the check fails.
- **Single source of trust**, derived from the registry, instead of divergent local stores. Applications that work offline use short-lived proofs and accept less power.
- Revocations propagate between nodes by a gossip protocol, to reduce dependence on a single channel.

### 23.8 Incident response 🟡

Indicative targets, to be calibrated:

| Step | Target |
|---|---|
| Automatic detection and confirmation | Minutes |
| Automatic freeze or revocation of a compromised key | Within 1 hour |
| Automatic suspension of a compromised issuer's power to attest and flagging of affected attestations for re-validation | Immediate |
| Public communication | Within 24 hours |
| Public post-incident report | Within 30 days |
| Simulated drills (revoking a fictitious issuer, mass rotation) | Periodic |

### 23.9 Accreditation and accountability of issuers 🟡

- **Public criteria** for accreditation, technical and governance-related.
- **Continuous technical verification** (23.6), not just a declaration of compliance.
- **Power limit:** a single issuer cannot raise an attribute's trust above C1 or C2 alone (section 9.7.3).
- **Automatic suspension or loss** of accreditation for proven technical failure, with a public record.
- **Legal and financial liability** where it exists (for example, regulated institutions).
- Who accredits and under what criteria is a governance matter (section 14) and a USIP matter. 🔴 Open.

### 23.10 Limits 🔴

- **No test proves randomness;** it only detects known bad patterns. A subtle weak generation (a partially predictable generator) may pass. Mitigations: mixing of sources, hardware attestation, audited libraries and bug rewards.
- **Bugs in the wallet or protocol,** and the software supply chain.
- **Social engineering:** people remain targets.
- **Tension with non-repudiation** (section 23.6).
- **The weak link may lie outside USI:** verifiers and legacy systems that ignore the rules.
- **Cost and friction** of rigid procedures.
- USI is **not immune** to failures like those reported; the aim is for them to be harder to occur, detected earlier, contained and fixed faster.

## 24. Cryptographic migration and quantum computing

### 24.1 Principle 🟢

The project is designed from the start to **change algorithms without changing identity**. Cryptographic agility is a design requirement, not a feature to add later.

A premise adjustment: post-quantum algorithms already standardized by NIST in 2024 exist (ML-KEM [11], ML-DSA [4] and SLH-DSA [12]). But they have larger keys and signatures, less time under scrutiny, and candidates were broken during the selection process (for example, SIKE and Rainbow, in 2022). The plan therefore combines **planned migration** with **hybrid use** (classical plus post-quantum algorithm) and allows that the chosen algorithm itself may need to be replaced.

### 24.2 Cryptographic inventory and vulnerability 🟡

The project keeps a **public inventory of primitives** (a cryptographic bill of materials), updated with each version.

| Primitive | Use in USI | Quantum threat | Path |
|---|---|---|---|
| Elliptic-curve signatures (for example, Ed25519, P-256) | Key events, document signatures, credentials | Breakable by Shor's algorithm | Standardized post-quantum signatures (ML-DSA, SLH-DSA; FN-DSA being standardized), in hybrid mode during transition |
| Key exchange and encryption of backups and channels | Encrypted backups, transport | Classical exchange breakable | ML-KEM in hybrid mode; 256-bit symmetric encryption |
| Hash functions (SHA-256, SHA-3) | Commitments, Merkle trees, pre-rotation | Grover's algorithm halves security; 256-bit outputs keep a margin | Keep outputs of at least 256 bits. Hash pre-rotation is already resistant |
| Symmetric encryption (AES-256) | Local protection | Margin kept with 256 bits | Keep |
| Zero-knowledge proofs based on curves or pairings | Level proofs, *nullifiers*, selective disclosure | Breakable | Hash-based (STARK-type) or lattice-based systems; research ongoing; higher cost |
| BBS signatures (selective disclosure) | Credentials | Pairing-based: breakable | Post-quantum alternatives still under research; SD-JWT with post-quantum signatures as an option |
| **Threshold OPRF** (elliptic curves) | Identifier uniqueness (section 9.7.2) | Breakable. If the protocol's public key is public, a quantum adversary could obtain the secret key and test identifiers against values already recorded in the registry ("harvest now, decrypt later" attack) | Do not publish the public key, or a post-quantum OPRF (research); **re-evaluate phase B** of section 9.7.10 |
| Attribute commitments | Slots (section 9.7.2) | Pedersen commitments hide perfectly, but binding is breakable; hash commitments resist | Prefer hash commitments |

**Identified risk:** the public registry is permanent, and anything in it protected only by classical assumptions may be exposed in the future. The registry should therefore contain only hash commitments, hashes and data that do not lose protection against quantum computers.

### 24.3 Migration mechanisms 🟡

1. **Algorithm identifiers and protocol version** in every event, signature and credential.
2. **Hybrid signatures** during transition: an event is valid only if it verifies under both the classical and the post-quantum algorithm.
3. **Hash pre-rotation** (section 7.4): the next key is committed by hash, which resists quantum computers. At rotation, a post-quantum key is revealed. This is the natural migration path without changing USI.
4. **Signed update in hybrid mode,** including that of the wallet itself.
5. **Agility tests:** each release is tested with algorithm swaps, and there are periodic drills of "killing" an algorithm.
6. **Capacity planning** for mass rotations (rate limit, batches, priority by risk level).

### 24.4 Deprecation stages and triggers 🟡

| Stage | Meaning |
|---|---|
| **Accepted** | May be used |
| **Preferred** | Recommended; the new algorithm starts being offered |
| **Required (hybrid)** | New events need both a classical and a post-quantum signature |
| **Obsolete** | Legacy verification only, for events before a date |
| **Prohibited** | Not accepted |

The change of stage is decided by USIP, based on public **triggers**: guidance from standards bodies, cryptanalysis results, quantum-computing milestones and the opinion of an open cryptography working group, which publishes an annual risk assessment.

### 24.5 Emergency procedure 🟡

If an algorithm is declared broken:
1. Its use in new events is suspended, **except for rotation**.
2. **Hash pre-rotated** keys (resistant) take over control.
3. Mass rotation follows priority by risk level.
4. Legacy verification is kept only for records with a timestamp earlier than the break date.
5. Immediate public communication and a later report.

### 24.6 Long-lived signatures 🟡

Documents signed today must remain verifiable for decades. The document's *hash* is anchored in the registry; before the algorithm weakens, the seal is **renewed** by new anchoring with the new algorithm, forming a chain of evidence. An old signature remains provable as "existed before date X" as long as it was anchored before the break.

### 24.7 Costs 🟡

Post-quantum sizes are larger: an ML-DSA signature is on the order of 2.4 kB and a public key on the order of 1.3 kB, and SLH-DSA signatures can range from about 8 to tens of kB, depending on parameters (approximate values, to be confirmed). This affects registry sizing (section 8.3), and device bandwidth and battery. Mitigations: record **hash commitments** instead of full keys, anchor in batches by Merkle root and use aggregated signatures where possible.

### 24.8 Open questions 🔴

- Quantum-resistant zero-knowledge proofs and credentials with selective disclosure, at viable cost on phones.
- A post-quantum alternative to the threshold OPRF, or a design that dispenses with the public key (section 9.7.10).
- Deprecation calendar, in a context where the time to quantum risk is uncertain.
- Cost and usability of post-quantum signatures on modest devices.

## 25. References

> Initial list; references must be checked and completed with links and exact versions in future editions.

1. W3C. *Decentralized Identifiers (DIDs) v1.0*. W3C Recommendation, 2022.
2. FIDO Alliance; W3C. *Web Authentication (WebAuthn)* and FIDO2 specifications.
3. S. Smith. *Key Event Receipt Infrastructure (KERI)*. arXiv:1907.02143.
4. NIST. *FIPS 204: Module-Lattice-Based Digital Signature Standard (ML-DSA)*. 2024.
5. Brazil. *Law No. 13,709/2018 (General Personal Data Protection Law, LGPD)*.
6. B. Laurie, A. Langley, E. Kasper. *RFC 6962: Certificate Transparency*. IETF, 2013.
7. Q. Cao, M. Sirivianos, X. Yang, T. Pregueiro. *Aiding the Detection of Fake Accounts in Large Scale Social Online Services* (SybilRank). NSDI, 2012.
8. A. Shamir. *How to Share a Secret*. Communications of the ACM, 1979.
9. W3C. *Verifiable Credentials Data Model*. W3C Recommendation.
10. J. Douceur. *The Sybil Attack*. IPTPS, 2002.
11. NIST. *FIPS 203: Module-Lattice-Based Key-Encapsulation Mechanism Standard (ML-KEM)*. 2024.
12. NIST. *FIPS 205: Stateless Hash-Based Digital Signature Standard (SLH-DSA)*. 2024.
13. Brazil. *Provisional Measure No. 2,200-2/2001* (establishes ICP-Brasil).
14. Brazil. *Law No. 14,063/2020* (electronic signatures).
15. TabNews (user augustresende). [A chave privada era literalmente 4: o Firefox confiava nela, a ICP-Brasil não confia](https://www.tabnews.com.br/augustresende/a-chave-privada-era-literalmente-4-o-firefox-confiava-nela-no-icp-brasil-nao-confia). October 2026.
16. Hardware.com.br. [Oito certificados TLS comprometidos colocam a segurança da internet em alerta](https://www.hardware.com.br/noticias/oito-certificados-tls-comprometidos-colocam-a-seguranca-da-internet-em-alerta/). 21 October 2026.

## 26. Version history

| Version | Date | Description |
|---|---|---|
| 0.1 | 2026-10-23 | First draft, open to collaboration. |
| 0.1.1 | 2026-10-23 | Geographic premise (pilot in Brazil, design without borders), country profiles, role of governments (support without control), experiment E13. |
| 0.1.2 | 2026-10-24 | Binding between USI and identity attributes (section 9.7): key attributes, attribute trust, identity squatting, social name and legal name change; experiments E14 and E15. |
| 0.1.3 | 2026-10-24 | Section 9.7.10: discarded alternative (individual random key) and phased rollout of identifier uniqueness (phase A without *nullifier*, phase B with threshold OPRF). |
| 0.1.4 | 2026-10-24 | Section 10.8: extreme recovery scenarios (total loss without preparation and attempted abuse), recovery anchors, issuer-assisted re-validation, the "starting over does not create a new USI" rule and proportionality; experiment E16. |
| 0.1.5 | 2026-10-27 | Section 5: overview of related initiatives, collaboration stance, non-negotiable characteristics, forms of collaboration and reuse criteria; goal G11. |
| 0.2.0 | 2026-10-29 | Part II (sections 21 to 24): USI-O (identity of organizations), digital signature and authentication as an alternative to certificate authority hierarchies, lessons from real failures and procedures that prevent human error, cryptographic migration and quantum computing; goals G12 to G14; experiments E17 to E20. |
