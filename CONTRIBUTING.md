# Contributing to Universal Safe ID

🌐 **English** · [Português (Brasil)](CONTRIBUTING.pt-BR.md)

Thank you for your interest. USI is a **research-stage, non-profit, ownerless** project. At this point the most valuable contributions are **critique, evidence and experiments**, more than code. If you are not sure where to start, read [docs/start-here.md](docs/start-here.md).

By taking part you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md).

## Ways to contribute

| You can... | How |
|---|---|
| **Critique the whitepaper** | Open an issue using the *Whitepaper feedback* form. Point to a section, say what is wrong or missing, and (if you can) cite a source. |
| **Answer an open question** | Each open question in [section 18](docs/whitepaper.md#18-open-questions) has an issue labelled `open-question`. Comment with ideas, references or objections. |
| **Run an experiment** | Each experiment E1 to E20 has an issue labelled `experiment`. Say you want to take it, then follow the [experiment convention](experiments/README.md). |
| **Verify facts** | Section 5 (related initiatives) and the legal sections need primary sources. Issues labelled `needs-verification`. |
| **Translate and review language** | Keep the English and Portuguese versions in sync (see below). Other languages are welcome. |
| **Review code and cryptography** | Review prototypes under [experiments/](experiments/). Independent review is the most useful thing a specialist can do. |
| **Propose a change to the design** | Write a USIP (see [docs/usips/](docs/usips/README.md)). |

## Ground rules

1. **Research prototypes only.** Nothing here is production software. Never use real keys, real documents or real personal data in the prototypes, and never ask others to.
2. **Evidence over opinion.** Hypotheses are labelled as such. Negative results are as valuable as positive ones and must be published.
3. **Essential characteristics are not negotiable:** the project must remain **universal, collaborative, secure, non-profit and ownerless** (whitepaper section 5.3). Proposals that conflict with them need a USIP and strong justification.
4. **Collaborate, do not compete** (whitepaper section 5.2). Check what already exists and credit it.
5. **Disclose AI assistance.** Much of this repository was drafted with an AI assistant and is **not yet reviewed by specialists**. If you used AI in a contribution, say so in the pull request.
6. **Security-sensitive changes** (cryptography, key handling, recovery) need review by at least two people, one of them with relevant experience.

## Pull requests

1. Open or comment on an issue first for anything bigger than a typo.
2. Create a branch, make focused changes, and open a pull request using the template.
3. Keep documents **bilingual**: every document exists in English (`name.md`) and Brazilian Portuguese (`name.pt-BR.md`). Update both in the same pull request when possible; if you can only write one, say so and a maintainer or volunteer will translate. If versions diverge temporarily, the **English version is the reference**.
4. For the whitepaper, add a line to the version history (section 26) for significant changes.
5. Sign off your commits (`git commit -s`) to confirm the [Developer Certificate of Origin](https://developercertificate.org/): you wrote the contribution or have the right to submit it under the project's licences.

## Licences

- **Code:** [Apache License 2.0](LICENSE).
- **Documentation** (whitepaper, READMEs and other texts): [CC BY 4.0](LICENSE-docs).
- Contributions are accepted under the same licences (*inbound = outbound*). **There is no copyright assignment and no contributor licence agreement**: authors keep their copyright, and no person or company owns the project.

## Decisions

Until the project has enough participants, the maintainer records decisions after a public discussion of at least 14 days, and explains them in the issue or USIP. **This is a provisional role**, to be replaced by the governance described in whitepaper section 14.

## Questions

Open an issue labelled `question`. There is no private channel yet; a dedicated contact address will be published when one exists.
