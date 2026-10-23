# Universal Safe ID (USI) — Whitepaper

🌐 **English** · [Português (Brasil)](whitepaper.pt-BR.md)

**Version 0.1.1 — open draft, open to collaboration** · October 2026
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
21. [References](#21-references)
22. [Version history](#22-version-history)

---

## 1. Abstract

Universal Safe ID (USI) is a proposal for open, ownerless, non-profit infrastructure through which anyone can obtain, free of charge, **a unique and permanent identifier** that proves they are **a distinct human being** without revealing who they are, and that lets them **control their own data**, sharing it selectively and for limited periods.

No technical component of USI is new. The proposed contribution is the **deliberate combination** of techniques already studied in decentralized identity, cryptography and public infrastructure, so that the weaknesses of each are covered by the others:

1. **Uniqueness from multiple independent evidence layers** (social vouching analysed as a graph, zero-knowledge document proofs, physical presence and, optionally, biometrics), translated into **assurance levels** that each verifier chooses.
2. **Access recovery through parallel routes** (another device, pre-rotated key, guardians, re-validation), with waiting periods and a right of veto proportional to the strength of the evidence.
3. **A minimal public registry** that stores only public keys, cryptographic commitments and proofs, **never personal data**.
4. **Per-service pseudonyms**, which prevent the universal identifier from becoming a tracking tool.
5. **Funding by those who benefit**, with no token and no charge to citizens, and governance that decentralizes in measurable phases.

This document describes the problem, the threat model, the proposed architecture, the alternatives still in dispute, an experiment plan to decide among them, and the project's risks.

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

### 3.2 Non-goals 🟢

- **It is not a currency, token or financial asset.**
- **It does not replace official documents.** It coexists with them and uses them as evidence where they exist.
- **It does not guarantee absolute uniqueness.** No system does; the aim is a cost of fraud far above its benefit.
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
| **Issuers** | Institutions that issue verifiable credentials (diplomas, registrations). |
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

Events must identify the algorithm used. Migration to standardized post-quantum algorithms (such as ML-DSA, FIPS 204 [4]) must be possible without changing USI. Since post-quantum keys and signatures are considerably larger, the registry should store **commitments (hashes)** of keys, revealing the full key only when needed (in the event that uses it). This affects sizing (section 8.3).

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

- **Mechanism:** for those holding a document with a chip and verifiable digital signature (such as e-passports), the holder proves, inside a zero-knowledge proof, that (a) the document is authentic, (b) it is valid and (c) a deterministic ***nullifier*** derives from it. The registry stores only the *nullifier*; a second registration with the same document yields the same *nullifier* and is refused.
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

Recovery swaps **control keys**. But the **identity secret**, the basis of pseudonyms and *nullifiers* (section 11.3), must also survive. If lost, the holder would get new pseudonyms and could in theory circumvent the "one account per person" limit at each service. Hypotheses to evaluate: splitting the identity secret among guardians (Shamir) and/or in an encrypted backup under the holder's control; or recording secret "epochs" in the registry, with rules so services handle transitions without allowing duplicate accounts. This is one of the protocol's most important design questions.

### 10.7 User experience 🟡

The security of any recovery scheme depends on people being able to use it. The wallet must guide initial setup (choosing guardians, backing up the backup key), periodically test recovery (a "drill") and be understandable to people with low technical familiarity.

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

The protocol provides for deactivating compromised algorithms by governance decision, with a transition period and coordinated key rotation, without changing the USI.

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

## 19. Roadmap

| Stage | Deliverables |
|---|---|
| **1. Whitepaper** | Version 0.1 (this document); open review; version 0.2 with contributions |
| **2. Community and review** | Expert review; presentation to decentralized identity communities; initial core of collaborators |
| **3. Repository organization** | Licences, `CONTRIBUTING`, code of conduct, USIP process, issues for each open question |
| **4. Proofs of concept** | Experiments E1–E13 by priority |
| **5. Legal and institutional analysis** | Opinion on LGPD and other rules; foundation design |
| **6. Funding and outreach** | Grant applications; outreach material; partner search |
| **7. Pilot (Brazil)** | Initial use case with a partner community in Brazil; metrics; public report; checklist for admitting new countries |
| **8. Institutionalization** | Foundation incorporated; transition to governance phase 1 |

There are no fixed dates in this version: the schedule depends on community formation and funding.

## 20. How to contribute to this document

This is an open draft. To contribute:

- **Critical review:** open an issue pointing out errors, gaps or missing risks. Well-founded criticism is welcome.
- **Source references:** section 5 and the technical claims need primary sources; help verify and add them.
- **Specialists:** cryptography, distributed systems, digital identity, data protection law, experience design, anthropology/social sciences (for inclusion), ethics.
- **Experiments:** take on one of experiments E1–E13.
- **Translation and language review:** keep the Portuguese and English versions in sync.

All significant changes must be recorded in the version history (section 22).

## 21. References

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

## 22. Version history

| Version | Date | Description |
|---|---|---|
| 0.1 | 2026-10-23 | First draft, open to collaboration. |
| 0.1.1 | 2026-10-23 | Geographic premise (pilot in Brazil, design without borders), country profiles, role of governments (support without control), experiment E13. |
