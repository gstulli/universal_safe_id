# Security policy

🌐 **English** · [Português (Brasil)](SECURITY.pt-BR.md)

## Project status

Universal Safe ID is in a **research stage**. Everything in this repository (documents and prototypes) is **experimental**:

- **Do not use** any code here to protect real keys, real documents or real personal data.
- **Do not submit** real personal data, real private keys or real credentials to this repository, in issues, pull requests or discussions. If you do by mistake, tell us so it can be removed.
- Passing a check in a prototype (for example, a weak-key check) **does not mean** a key or design is secure.

## Reporting a vulnerability

We welcome reports of security problems in the **prototypes**, and of weaknesses in the **design** described in the whitepaper.

1. **Preferred:** use GitHub's private vulnerability reporting (the *Security* tab of the repository, *Report a vulnerability*), if it is enabled.
2. If private reporting is not available, open a public issue with the label `security` that describes the **area and impact only**, without exploit details, and ask for a private channel. A dedicated contact address will be published when one exists.

Please include: what is affected, how to reproduce it, the expected impact, and any suggested fix.

## What to expect

- Acknowledgement of your report on a best-effort basis (the project is currently maintained by volunteers).
- A coordinated disclosure: we suggest a **90-day** window before public details, adjustable by agreement.
- Credit in the fix or advisory, if you wish.

## Scope

In scope: code under `experiments/`, and flaws in the protocols, procedures and cryptographic choices in the whitepaper.
Out of scope: vulnerabilities in third-party projects (report them to their maintainers), and social engineering of project participants.

Design weaknesses that are not urgent (for example, a better attack on a hypothesis) are best raised as a public issue labelled `open-question` or `whitepaper-feedback`, so the community can discuss them.
