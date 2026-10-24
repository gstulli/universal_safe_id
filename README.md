# Universal Safe ID (USI)

🌐 **English** · [Português (Brasil)](README.pt-BR.md)

**A universal personal identity that is unique, private and recoverable, built as a public good on open source code and a verifiable public registry.**

> **Status:** conception phase, with the **first version of the [whitepaper](docs/whitepaper.md) published (v0.1.2)**. The whitepaper details the threat model, the architecture, the alternatives still in dispute and a plan of 15 experiments to decide among them. **It is an open draft, open to collaboration**: criticism, corrections and contributions are welcome (see [How to contribute](#15-how-to-contribute)). Nothing here is final: the proposals are hypotheses to be tested, measured and adjusted as the project matures.

**Documents:**

| Document | English | Português |
|---|---|---|
| Project overview | [README.md](README.md) | [README.pt-BR.md](README.pt-BR.md) |
| Whitepaper v0.1.2 | [docs/whitepaper.md](docs/whitepaper.md) | [docs/whitepaper.pt-BR.md](docs/whitepaper.pt-BR.md) |

---

## Contents

1. [The problem](#1-the-problem)
2. [The proposal](#2-the-proposal)
3. [Principles](#3-principles)
4. [What sets USI apart](#4-what-sets-usi-apart)
5. [Proposed architecture](#5-proposed-architecture)
6. [One person, one USI: the uniqueness model](#6-one-person-one-usi-the-uniqueness-model)
7. [Access recovery](#7-access-recovery)
8. [Privacy and security](#8-privacy-and-security)
9. [Sustainability without owners or profit](#9-sustainability-without-owners-or-profit)
10. [Governance](#10-governance)
11. [Stakeholders](#11-stakeholders)
12. [Initial use cases](#12-initial-use-cases)
13. [Getting started](#13-getting-started)
14. [Open questions](#14-open-questions)
15. [How to contribute](#15-how-to-contribute)
16. [Glossary](#16-glossary)

---

## 1. The problem

Identifying people today depends on two models, and both have serious flaws.

**Identity issued by governments and centralized certifying bodies**
- Billions of people have no recognized document: refugees, stateless people, vulnerable populations.
- Each country, agency and company keeps its own database, producing duplicates, fraud and mass leaks.
- Citizens do not control their data: they do not know who queries it, cannot choose what to reveal and cannot revoke access.
- The identity does not cross borders easily and can be denied or cancelled by a single authority's decision.

**Digital identity issued by private platforms** (logging in with accounts from large companies)
- The account belongs to the company, not the person, and can be blocked with no recourse.
- It serves as a basis for tracking and commercial profiling.
- It does not guarantee that a real, unique human is behind the account.

**A new and urgent problem:** with the spread of AI agents able to imitate people, telling a real human from a bot — and one person from a thousand fake accounts — has become essential for voting, social networks, benefit distribution and any space that relies on the principle of "one person, one voice".

## 2. The proposal

USI proposes open, ownerless infrastructure that lets anyone:

1. **Obtain, free of charge, a unique and permanent identifier** (the USI), tied to them and nobody else.
2. **Prove they are a unique human being** without having to reveal who they are.
3. **Keep their personal data under their own control**, sharing only what is needed, with whom they choose, for as long as they choose.
4. **Never lose their identity** by forgetting a password or losing a phone.
5. **Be recognized** by services, institutions and other people through open, interoperable standards.

USI does not aim to replace official documents. It can coexist with them, use them as evidence where they exist, and offer an alternative to those who do not have them.

### Geographic scope: starts in Brazil, designed without borders

- The **pilot will start in Brazil**, where the project is born, where legislation and documents are known and where the first network of partners will be formed.
- The **design has no borders**: nothing in the protocol depends on one country. What is specific to each country (accepted documents, validators, legal aspects) lives in pluggable **country profiles**.
- Expansion is **gradual and by adhesion**: new countries join as local stakeholders (operators, validators, issuers, lawyers and interested governments) provide support for infrastructure and operation.
- **Governments may support, but do not control.** A government can, for example, help qualify verification of its own documents, which reduces duplicates within the country, without gaining a privileged voice, veto or access to holders' data (see [section 10.3](#103-governments-support-without-control)).

## 3. Principles

| # | Principle | In practice |
|---|---|---|
| 1 | **Public good, no owner** | No person, company or government controls the system. The founder steps away from governance once objective decentralization criteria are met. |
| 2 | **Free for the citizen** | Creating, maintaining and recovering a USI will never cost the person anything. |
| 3 | **No profit, no token** | No profit for founders, investors or maintainers. There will be no cryptocurrency of its own. Resources needed for operation are transparent and used only for infrastructure. |
| 4 | **One person, one USI** | Each human being has a single identifier. Duplicates can be challenged and corrected. |
| 5 | **Permanent identifier, replaceable keys** | The USI does not change; the keys that control it can be swapped, revoked and recovered. |
| 6 | **No personal data in the public registry** | Not in clear text, not even encrypted. The registry keeps only public keys, cryptographic commitments and proofs. |
| 7 | **Minimal disclosure** | Reveal only what is necessary. Example: prove "I am an adult" without revealing the date of birth. |
| 8 | **Robustness through combination** | No single mechanism is reliable enough. Uniqueness, security and recovery are ensured by several independent layers working together. |
| 9 | **Open standards** | Compatibility with recognized standards (W3C DID, Verifiable Credentials, FIDO2/passkeys), avoiding proprietary formats. |
| 10 | **Inclusion** | The system must work for people without documents, with little technical familiarity or limited internet access. |
| 11 | **Transparency and auditability** | Open source, public decisions, public accounts, a registry anyone can verify. |
| 12 | **Evidence-based evolution** | Each mechanism is treated as a hypothesis, tested in a controlled setting and adjusted from real data. |
| 13 | **Local pilot, global design** | The pilot starts in Brazil, but nothing in the system may depend on one country. Expansion is gradual, as stakeholders from other countries join. |
| 14 | **Government support without control** | Governments may support (for example, by qualifying their documents) but have no special vote, veto or access to holders' data. |
| 15 | **Unique, verifiable attributes** | Each USI has a single official name and a single identifier per country, bound by a cryptographic commitment. Trust grows as independent issuers verify, and drops if the value is changed. |

## 4. What sets USI apart

USI does not start from scratch: it combines techniques already proven in decentralized identity, cryptography and public infrastructure, seeking to avoid the failure points seen in earlier initiatives. Its distinguishing features lie in the combination:

1. **Uniqueness from multiple pieces of evidence, not a single method.** Not only biometrics, not only official documents, not only social vouching. Each person accumulates independent evidence, and confidence grows with its diversity (see [section 6](#6-one-person-one-usi-the-uniqueness-model)).

2. **Assurance levels chosen by the verifier.** An online forum may accept a basic level; a benefit distribution may require the highest. The same USI serves both.

3. **Recovery through parallel layers.** Several recovery routes operate at once, with waiting periods proportional to the strength of the evidence and a right of veto for the holder (see [section 7](#7-access-recovery)).

4. **Universal, but not traceable.** The USI is universal *for the holder*, not for services. Each service sees a different pseudonym derived from the USI and receives only proof that it is a unique human. Different services cannot cross-reference data to track the person.

5. **Zero personal data in the public registry.** Removes the conflict between immutability and the right to data erasure (LGPD, GDPR) and protects against future breaking of today's cryptography.

6. **Free for the citizen, funded by those who benefit.** No speculative token and no charge to the holder. Infrastructure is maintained by interested institutions and by those who consume verifications (see [section 9](#9-sustainability-without-owners-or-profit)).

7. **Accountable vouchers.** Anyone who attests to another person's identity puts their own reputation at stake. Vouching for a fake account has consequences.

8. **Progressive, planned decentralization.** Instead of an "ownerless" system from day one, which tends to create a governance vacuum, USI defines phases and objective criteria for handing control to the community.

## 5. Proposed architecture

The system is organized into three independent layers. Each can evolve without breaking the others.

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

### 5.1 Identifier and keys

- The USI follows the **W3C DID** (Decentralized Identifier) standard, with a proposed dedicated method, `did:usi`.
- The identifier is permanent. The keys that control it are replaceable.
- **Key pre-rotation** (inspired by the KERI protocol): when registering the current key, the holder also registers the *hash* of the next key, kept offline. Even if the current key is stolen, the attacker cannot take definitive control of the identity.
- Support for **multiple devices** and **passkeys** (FIDO2), protected by the phone's secure chip or by physical keys.
- **Post-quantum cryptography** (such as the NIST-standardized algorithms, e.g. ML-DSA) must be considered from the design stage, with a mechanism to migrate algorithms.

### 5.2 Public registry

The public registry works as a **trust anchor**: it stores only the minimum needed for anyone to independently verify the state of a USI.

**What goes into the registry:** the identifier, current public keys, commitments to next keys, rotation and revocation events, uniqueness *nullifiers* and cryptographic digests (*hashes*) of attestations.

**What never goes in:** name, documents, photos, biometrics, address, date of birth or any other personal data, not even encrypted.

**Estimated size:** with a few hundred bytes per person, a registry covering the entire world population would be on the order of a few terabytes. Moreover, ordinary users do not need to store it: they use **light clients** that verify compact proofs. Only full nodes keep the entire registry.

**Options to evaluate** (the decision should come from proofs of concept):

| Option | Description | Pros | Cons |
|---|---|---|---|
| A. Anchors on an existing public blockchain | Record only the events on an established network (for example, an Ethereum layer 2) | Inherited security; no own network to maintain | Per-transaction cost; third-party dependence |
| B. Own federated network | Tens to hundreds of independent institutional operators, with Byzantine-fault-tolerant (BFT) consensus and auditable logs anyone can check, in the style of *Certificate Transparency* | Low cost; control over performance and rules | Requires attracting and diversifying operators |
| C. Hybrid | Federated network for daily operation, with periodic anchors on a public blockchain as an extra integrity guarantee | Combines the advantages of A and B | Greater complexity |

**Selection criteria:** independence, cost to the citizen (which must be zero), durability over decades, censorship resistance, public auditability and performance.

### 5.3 Personal data and credentials

- Personal data lives in the **holder's wallet** (a phone app), with an encrypted backup in a place the holder chooses.
- Information about a person is represented as **verifiable credentials** (W3C Verifiable Credentials) issued by whoever has authority over it: a university issues the diploma, an agency issues the document, a professional council issues the registration.
- **Selective disclosure** (SD-JWT, BBS+ signatures) lets the holder reveal only some fields of a credential.
- **Zero-knowledge proofs** let the holder prove statements without revealing the data: "I am over 18", "I live in this municipality", "I am a unique human on this service".
- **Time-limited sharing:** the holder grants access to data with a deadline and can revoke it at any time. An important limitation that must be made clear to users: only *continued access* can be limited. Information that has already been seen or copied cannot be "unseen".
- **Consent log:** the holder keeps the history of who accessed what and when, visible only to them.

## 6. One person, one USI: the uniqueness model

Guaranteeing that each person has a single record with 100% certainty is impossible for any system, including government ones. USI's goal is to make fraud **hard, costly, detectable and reversible**.

### 6.1 Evidence layers

Each USI accumulates evidence from different categories. None is mandatory on its own; strength lies in the combination.

| Layer | How it works | Notes |
|---|---|---|
| **Social vouching** | People who already hold a USI attest that they know the holder. Trust is not measured by the *number* of attestations but by **graph analysis**: clusters of fake accounts tend to have many connections among themselves and few with the honest network. | Attesters are accountable: if they vouch for a fake account, they lose reputation. |
| **Zero-knowledge document proof** | For those with a document with a chip or digital signature (such as NFC passports), the holder proves the document is valid **without revealing it**. The system stores only a *nullifier*, a value derived from the document that prevents a second registration with the same document without revealing which document it is. | Leverages the uniqueness that official documents already offer without depending operationally on governments. |
| **Physical presence** | Simultaneous in-person verification ceremonies, organized by community validators or partner institutions (libraries, schools, NGOs). A person cannot be in two places at once. | Especially important for people without documents. |
| **Biometrics (optional, to be investigated)** | Biometric comparison to detect duplicates, **only** if it can be done without a centralized database, using techniques such as multi-party computation or homomorphic encryption. | Always optional. Adopted only if it demonstrably solves the privacy risks. |
| **History and continuity** | Age of the USI, consistent use, credentials issued by third parties. | Newly created accounts naturally carry less weight. |

### 6.2 Assurance levels

Evidence is converted into public, standardized **assurance levels**. Verifiers choose the level they require. Initial example, to be calibrated:

| Level | Indicative requirement | Typical use |
|---|---|---|
| 1 – Basic | Minimal social vouching | Forums, comments, anti-bot filters |
| 2 – Intermediate | Solid social vouching **or** document proof | Polls, online communities, simple sign-ups |
| 3 – High | Two layers from different categories | Community voting, donations |
| 4 – Maximum | Three or more layers, including physical presence or document proof | Benefit distribution, sensitive applications |

### 6.3 Challenge and correction

- **Anyone may challenge** a suspicious USI, presenting evidence.
- Challenges are judged by **randomly drawn juries** from high-level holders, under public rules and with a right of defence.
- A confirmed duplicate results in cancelling the surplus record and a reputation loss for those who vouched for it.
- This replaces the concept of "irrevocable" with **permanent, but correctable**: the legitimate USI is never lost; the fraudulent one can be undone.

### 6.4 Lifecycle

**Creation** → **Evidence accumulation** → **Use** → **Key rotation** → **Recovery** (if needed) → **Challenge** (if any) → **Inactivity or death**

Handling death and long-term inactivity must be defined so as to prevent misuse of deceased people's identities without exposing anyone's data.

### 6.5 Binding to name and documents: one identity, one set of attributes

Having a single USI per person is not enough: we must also prevent the same person from using two names or two CPFs, and prevent a third party from receiving information that differs from the truth. Since the registry stores no personal data, the proposed model is:

- **Key attributes** (official name, date of birth, each country's stable national identifier, such as the CPF): each USI has **one current value** per type. The value stays in the wallet; the registry keeps only a cryptographic commitment. The name is unique *to the USI*, but not across people; state identifiers (CPF, passport) are unique across USIs.
- **Documents** (passport, ID card, driving licence): there may be several, renewed over time, but always consistent with the key attributes.
- **Attribute trust (C0 to C4):** starts at "declared" and rises as **independent issuers** (banks that verify their customers, public bodies, other institutions) verify and attest the attribute. Example: John enters his name and CPF; on opening an account at Bank A, the bank verifies and attests; other banks repeat the process; once trust is high, any counterparty can accept the CPF presented as true.
- **Changing a key attribute resets its trust** and requires new validation (the change history is preserved). Before the first attestation, the holder can correct mistakes freely.
- **False identity:** someone who registers a false name or CPF must deceive several independent issuers and is then stuck with that identity: they cannot hold another USI or go back without losing trust.
- **Squatting on someone else's identity:** the stronger evidence wins (cryptographic proof of the original document, plus attestations), not whoever arrived first. Disputes go to a jury.
- **Social name and legal name change:** handled separately and always presented with a type label. A change by legal act has its own path, preserving USI continuity and without exposing the previous name to third parties.

USI **does not make information true**: it guarantees it is unique and measures how far it can be trusted. Truth is guaranteed by whoever verifies it. Details in [section 9.7 of the whitepaper](docs/whitepaper.md).

## 7. Access recovery

Losing access to one's own identity cannot be permanent. At the same time, the recovery process is attackers' preferred door for hijacking accounts. USI resolves this conflict with **several routes operating in parallel**, each with requirements and waiting periods proportional to the strength of the evidence presented.

### 7.1 Recovery routes

| Route | Mechanism | Indicative waiting period |
|---|---|---|
| **A – Another device** | A passkey or key already registered on another device authorizes the new key | Immediate |
| **B – Pre-rotated key** | The next key, kept offline (paper, safe, physical key), takes over | Short (e.g. 24 to 72 hours) |
| **C – Social recovery** | A quorum of **guardians** chosen by the holder (e.g. 3 of 5 among family, friends and institutions) authorizes the new key. May use Shamir secret sharing. | Medium (e.g. 7 days) |
| **D – Identity re-validation** | The holder proves again that they are the same person, through the evidence layers of section 6 (document proof, physical presence, validators) | Long (e.g. 30 days), **and** requires combination with another route or high-level evidence |

The waiting periods are initial hypotheses to be calibrated in tests.

### 7.2 Rules that apply to every route

1. **Immediate notification** of any recovery request to all devices, guardians and registered channels.
2. **Right of veto:** during the waiting period, any legitimate key that is still active can cancel the request. This protects against anyone trying to hijack the account.
3. **Stronger routes shorten the wait:** combining routes (for example, guardians + re-validation) reduces the wait; using a single weak route increases it.
4. **Emergency freeze:** in case of phone theft or suspected intrusion, the holder or a guardian quorum can freeze the USI immediately, until recovery.
5. **Mandatory rotation after recovery:** all old keys are revoked and a new pre-rotated key is generated.
6. **Periodic guardian review:** the app reminds the holder to confirm that guardians are still available and trustworthy.

### 7.3 Examples

- *I lost my phone but I have my tablet:* route A, immediate.
- *I lost every device but kept the recovery paper:* route B, short wait.
- *I lost everything:* route C, with my guardians, in about a week.
- *I lost everything and my guardians are unavailable:* route D, combined with high-level evidence, in about a month.
- *Someone stole my phone and requested recovery:* I get the notification on another channel and veto the request; I freeze the USI and start the legitimate recovery.

## 8. Privacy and security

### 8.1 Privacy protections

- No personal data in the public registry.
- **Per-service pseudonyms:** each service receives a different identifier derived from the USI, making cross-service data matching impossible.
- **Nullifiers** let a holder prove "I am a unique human on this service" without revealing which USI it is.
- Minimal disclosure and zero-knowledge proofs as the default, not the exception.
- Compliance with the **LGPD** and equivalent laws from the design stage (*privacy by design*).

### 8.2 Threats considered

| Threat | Planned mitigations |
|---|---|
| Mass fake accounts (Sybil attack) | Multiple evidence layers, graph analysis, attester accountability, challenge |
| Account hijack through recovery | Waiting periods, notification, veto, route combination |
| Guardian collusion | Guardians from different circles, waiting period, holder veto |
| Coercion (person forced to reveal data or give up access) | Minimal disclosure, an emergency mode to be studied |
| Surveillance and tracking | Per-service pseudonyms, no data in the registry, zero-knowledge proofs |
| Governance capture | Progressive decentralization, geographic and institutional diversity of operators, public rules |
| Compromise of registry operators | Fault-tolerant consensus, public audit, external anchors |
| Advances in quantum computing | Post-quantum algorithms and a migration mechanism |
| Digital exclusion | Physical presence, guardians, simplified wallets, institution-assisted operation |

### 8.3 Audits

Cryptographic and security components must undergo **independent audits** before any real use, with published results.

## 9. Sustainability without owners or profit

### 9.1 Why USI does not need Bitcoin's model

Bitcoin pays miners because it needs consensus among strangers about money, where fraud yields immediate profit. USI's needs are far smaller: a lean registry that need not be stored by each user and can be maintained by **a few hundred independent, trustworthy operators**, instead of millions of volunteers. Essential public Internet infrastructure, such as DNS root servers and *Certificate Transparency* logs, already works this way, maintained by institutions that benefit from its existence.

### 9.2 Real costs

Even without profit there are costs: running nodes, development, security audits, in-person verification events, support and legal advice.

### 9.3 Funding sources to test

1. **Institutional operators who benefit:** companies that spend on identity verification and fraud prevention, universities, NGOs, libraries, public bodies. Running a node is cheaper than maintaining their own databases.
2. **Verification fee paid by those who consume it:** services that verify USIs at scale can pay a minimal amount, earmarked for operators and maintenance. **The citizen never pays.**
3. **Grants, calls for proposals and donations** from foundations and programmes supporting open infrastructure and digital rights.
4. **Volunteer development,** motivated by purpose, reputation and learning, as in other large open source projects.

### 9.4 Why there will be no token

A token of its own would create a financial incentive to defraud registration, attract speculation and divert focus from the project. The experience of other initiatives shows that tokens tied to identity tend to generate buying and selling of registrations and public distrust.

### 9.5 Financial transparency

All resources received and spent must be public, managed by a **non-profit foundation**, with periodic accountability.

## 10. Governance

### 10.1 Decentralization phases

| Phase | Who decides | Criterion to advance |
|---|---|---|
| **0 – Conception** | Founder and initial core of collaborators | Whitepaper published and reviewed by specialists |
| **1 – Foundation** | Non-profit foundation with a board representing stakeholders (citizens, operators, developers, civil society) | Network in production with independent operators in several countries |
| **2 – Community** | Community of holders and contributors, through an open proposal process | No single entity can change the system; the founder steps away |

### 10.2 Mechanisms

- **Improvement proposals (USIPs):** anyone may propose changes, in a public process inspired by Bitcoin's BIPs and the IETF's RFCs.
- **Rough technical consensus** for technical decisions, with peer review.
- **"One person, one vote"** using the USI itself for decisions that affect the community, once the network is mature.
- **Separation of roles:** those who develop do not operate alone, those who operate do not decide alone, those who fund do not control.

### 10.3 Governments: support without control

Governments are potentially valuable allies and also the actors with the greatest capacity for capture. The same rules therefore apply to every government:

- **They may:** qualify the country profile for their documents (formats, public keys, revocation lists, stable identifiers); run nodes like any other operator, subject to concentration limits; provide public spaces for in-person ceremonies; recognize USI for specific purposes; support with funding or legal advice.
- **They may not:** hold a special vote, veto or guaranteed seat; alter rules or the state of any USI; access holders' data; make support conditional on exclusivity, mandatory use or surveillance.
- **Document verification is local, using public data and with no online query to the government**, so the state does not learn who uses USI or where.
- **The system keeps working if support is withdrawn**; only the weight of that country's documents decreases.
- All agreements with governments are public, and a country's profile can be weighted or refused by public criteria.

Details are in [section 14.5 of the whitepaper](docs/whitepaper.md). In Brazil, government support is welcome but not a prerequisite for the pilot.

## 11. Stakeholders

| Stakeholder | Role | Interest |
|---|---|---|
| **Citizens (holders)** | Create and control their USI | Free, private, recoverable identity |
| **People without documentation** (refugees, stateless, vulnerable populations) | Holders with specific needs | Access to services and recognition |
| **Attesters and guardians** | Vouch for people they know; help with recovery | Strengthen their own network and community |
| **Community validators and partner institutions** | Run in-person verifications | Inclusion and community service |
| **Node operators** | Maintain the public registry | Reliable infrastructure they depend on |
| **Verifiers** (platforms, banks, retail, NGOs, public bodies) | Accept and verify USIs | Reduce fraud, verification costs and fake accounts |
| **Credential issuers and attribute attesters** (universities, councils, public bodies, employers, banks and other institutions that verify customers) | Issue credentials and attest the holder's name and documents | Forgery-proof credentials; reuse the customer verification they are already required to do |
| **Developers and researchers** | Build, audit and evolve the system | Purpose, reputation, research |
| **Regulators and data protection authorities** (such as Brazil's ANPD) | Oversee compliance | Citizen protection |
| **Governments and public bodies** (of any country) | Optional support: qualify their documents, run nodes, provide spaces, recognize the USI | Reduce fraud and duplication, include people without documents. **No control over the project** |
| **Funders** (foundations, grant programmes, donors) | Sustain the initial phase | Social impact and open infrastructure |
| **Civil society and digital rights advocates** | Oversee and propose improvements | Privacy, inclusion, transparency |

## 12. Initial use cases

An identity is only valuable if accepted, and only accepted if people hold it. To break this cycle, USI should start with niches where it solves a real and immediate pain:

1. **Proof of humanity:** telling people from bots and AI agents in social networks, forums, product reviews and forms.
2. **Community and cooperative voting:** ensuring "one person, one vote" without revealing who voted.
3. **Donation and benefit distribution:** preventing the same person from receiving several times, with privacy.
4. **People without documents:** in partnership with humanitarian organizations.
5. **Age verification:** proving adulthood without exposing personal data.
6. **Passwordless login:** access to services with the USI, without depending on large platforms.
7. **Academic and professional credentials:** verifiable, forgery-proof diplomas and registrations.

## 13. Getting started

Proposed actions to get the project off the ground, in approximate order:

### Stage 1 – Whitepaper
- [x] Write the first version of the whitepaper ([v0.1.2](docs/whitepaper.md)), detailing: threat model, three-layer architecture, uniqueness model and assurance levels, recovery protocol, public registry options, sustainability model, governance plan and experiment plan.
- [x] Publish the draft in this repository for open comments.
- [ ] Deepen the survey of literature and prior experience in decentralized identity and proof of personhood, with primary sources (section 5 of the whitepaper is an initial summary and needs verification).
- [ ] Incorporate the contributions received and publish version 0.2.

### Stage 2 – Review and first collaborators
- [ ] Submit the whitepaper for review by specialists in cryptography, digital identity, security and digital law (LGPD).
- [ ] Present the proposal in decentralized identity communities (such as the W3C Credentials Community Group and the Decentralized Identity Foundation), universities and security research groups.
- [ ] Form an initial core of collaborators with complementary profiles: cryptography, development, law, experience design, community management.

### Stage 3 – Repository organization
- [ ] Define licences (suggestion: Apache-2.0 for code and CC BY 4.0 for documentation).
- [ ] Create `CONTRIBUTING.md`, a code of conduct and the proposal process (USIPs).
- [ ] Open an *issue* for each open question (see [section 14](#14-open-questions)) and enable *Discussions* for debate.
- [ ] Keep the `docs/` folder for the whitepaper, architecture decisions and minutes.

### Stage 4 – Proofs of concept
- [ ] Specify and prototype the `did:usi` method, with rotation and pre-rotation of keys.
- [ ] Prototype a minimal wallet with verifiable credentials and selective disclosure.
- [ ] Implement the layered parallel recovery protocol (routes A to D, waiting periods, veto).
- [ ] Test the zero-knowledge document proof and *nullifiers*.
- [ ] Simulate Sybil attacks on the social vouching model to calibrate graph analysis.
- [ ] Experimentally compare the public registry options (A, B and C).
- [ ] Technically survey the candidate Brazilian documents (offline cryptographic verification and stable identifier) and write the first country profile (experiment E13).
- [ ] Prototype attribute binding (slots with commitment, threshold-OPRF uniqueness, proof of currency) and simulate identity squatting, issuer collusion and synthetic identity attacks (experiments E14 and E15).

### Stage 5 – Legal and institutional analysis
- [ ] Analyse compliance with the LGPD and other relevant legislation.
- [ ] Study the legal form of the future foundation and the feasibility of institutional recognition of the USI.
- [ ] Engage the ANPD and, when appropriate, Brazilian public bodies, asking for support in qualifying documents **with no control in return**.
- [ ] Define the public checklist for admitting new countries (local stakeholder, country profile, legal analysis, validators, human-rights risk assessment).

### Stage 6 – Funding and outreach
- [ ] Map and submit proposals to calls and programmes supporting open infrastructure and digital rights.
- [ ] Create accessible outreach material (website, presentation, short video) to attract volunteers.
- [ ] Identify partner institutions for the pilot and to run the first nodes.

### Stage 7 – Pilot
- [ ] Choose an initial use case (see [section 12](#12-initial-use-cases)) and a partner community **in Brazil**.
- [ ] Run a controlled pilot, with metrics for sign-ups, fraud detected, recovery success and satisfaction.
- [ ] Publish the results and adjust the model.

### Stage 8 – Institutionalization
- [ ] Incorporate the non-profit foundation.
- [ ] Begin the transition to governance phase 1.

## 14. Open questions

Hypotheses and decisions that depend on research and testing:

- Which public registry option (A, B or C) offers the best balance of independence, cost and durability?
- How should the weights of the evidence layers and the requirements of each assurance level be calibrated?
- How resistant is graph analysis to organized Sybil attacks in practice?
- Can biometric duplicates be detected without a central database, at acceptable cost and performance? Is it worth it?
- Which waiting periods balance security and convenience in recovery?
- How can fair challenge juries be organized that resist collusion and scale?
- How should death, inactivity and digital inheritance be handled?
- How can people under coercion be protected?
- How can the system be made accessible to people without a smartphone or stable internet?
- Is the verification fee paid by services viable and compatible with the no-profit principle?
- Which objective criteria mark each governance phase transition?
- How should dual nationality across countries be handled without exposing the dual citizenship to any state?
- Which public criteria accept, weight or refuse a country's profile?
- Should the foundation be based in Brazil or in a neutral jurisdiction?
- How can uniqueness of CPFs and document numbers be computed without allowing a dictionary attack?
- How should "independent issuer" be defined, and who accredits issuers?
- How can a legal name change be allowed without exposing the holder's history?

## 15. How to contribute

The project is at an early stage and every contribution is welcome, **starting with a critical reading of the [whitepaper v0.1.2](docs/whitepaper.md)**. Especially from people with experience in:

- cryptography and security protocols;
- digital identity and W3C standards;
- distributed systems and consensus;
- digital law and data protection;
- experience design for diverse audiences;
- community organizing and fundraising.

To take part, open an *issue* with your suggestion, question or criticism. Well-founded criticism is as valuable as new ideas.

### Language policy

The repository is **bilingual**: every document exists in English (`name.md`) and Brazilian Portuguese (`name.pt-BR.md`), with a link between the versions at the top. Changes should be made to both versions in the same commit whenever possible; if they temporarily diverge, the **English version is the reference** until both are synchronized. Contributions in other languages are welcome as additional translations (`name.<code>.md`).

## 16. Glossary

- **USI:** Universal Safe ID, the unique personal identifier proposed by this project.
- **DID (Decentralized Identifier):** a W3C standard for identifiers that do not depend on a central authority.
- **Verifiable credential:** a digital document signed by an issuer, held by the holder and presented by them, which anyone can verify.
- **Zero-knowledge proof (ZKP):** a cryptographic technique that proves a statement is true without revealing the information behind it.
- **Nullifier:** a value derived from a secret that allows detecting repeated use without revealing the secret.
- **Sybil attack:** creation of many fake identities by one person or group.
- **Key pre-rotation:** advance commitment to the next key, kept offline, to regain control if the current key is compromised.
- **Guardian:** a person or institution chosen by the holder to help recover their access.
- **Shamir secret sharing:** a technique that splits a secret into parts, requiring a minimum number of them to reconstruct it.
- **Passkey:** a passwordless credential based on the FIDO2 standard, protected by the user's device.
- **BFT consensus:** an agreement mechanism among network nodes that tolerates some of them failing or acting maliciously.
- **Light client:** software that verifies the registry without storing it in full.
- **Assurance level:** degree of confidence that a USI corresponds to a real and unique person.

---

*This document is alive and will be updated as the project evolves. Suggestions are welcome through issues.*
