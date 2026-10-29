# Start here

🌐 **English** · [Português (Brasil)](start-here.pt-BR.md)

Universal Safe ID (USI) is a **research-stage** proposal for an open, non-profit, ownerless identity infrastructure. There is no product yet, and almost everything is a hypothesis. This page helps you find a useful way in, in the time you have.

## Read, in this order

1. The [README](../README.md): what the project proposes and what makes it different (10 minutes).
2. The [whitepaper](whitepaper.md): sections **1 to 3** (goals), **5** (related initiatives and what we will not give up), **9** (uniqueness) and **10** (recovery). The rest can wait (45 minutes).
3. Section **18** (open questions) and section **16** (experiments): this is where help is most needed.

Each section is tagged 🟢 proposed, 🟡 hypothesis or 🔴 open. Treat 🟡 and 🔴 as invitations to disagree.

## Who we need

| If you are... | You could... |
|---|---|
| A cryptographer or security engineer | Review the threat model (section 4), the key and recovery design (sections 7 and 10), the weak-key checks (section 23) and the post-quantum plan (section 24). Review [experiments/](../experiments/README.md). |
| A distributed-systems engineer | Compare the registry options A, B and C (section 8, experiment E1). |
| A researcher in identity, graphs or fraud | Take E2, E3 or E15 (Sybil resistance, level calibration, trust model). |
| A lawyer or data-protection specialist | Review sections 11.6, 21 and 22 (LGPD, signatures, notaries). Opinions are the main blocker to the legal strategy. |
| A designer or UX researcher | Take E6 (can lay people configure recovery?). |
| Someone from an initiative in this field | Tell us what we got wrong about your project (section 5.1) and where we could collaborate. |
| A developer | Pick an `experiment` issue labelled `good first issue`, or review a prototype. |
| A translator | Review the English and Portuguese versions; add other languages. |
| Anyone | Read the whitepaper critically and open a *Whitepaper feedback* issue. |

## Ways to help in 30 minutes

- Check one claim in section 5.1 against the project's own site and report corrections.
- Read one open question and comment with a reference or an objection.
- Review the wording of one section in your native language.
- Find a better name for something confusing.

## How the work is organized

- **Issues** are labelled by type (`experiment`, `open-question`, `needs-verification`, `question`), by area (`area:crypto`, `area:legal`, `area:ux`, `area:governance`, `area:research`, `area:docs`) and by difficulty (`good first issue`, `help wanted`).
- **Experiments** follow a convention: a hypothesis, a success criterion and a published result, including negative ones ([experiments/README.md](../experiments/README.md)).
- **Design changes** go through a [USIP](usips/README.md).
- **Decisions** are recorded publicly. See [CONTRIBUTING.md](../CONTRIBUTING.md).

## Please note

- This is not production software. Never put real keys, documents or personal data in anything here.
- Much of the text was drafted with an AI assistant and has **not** been reviewed by specialists. Your scepticism is the point.
- The project is **universal, collaborative, secure, non-profit and ownerless**, and aims to collaborate with similar initiatives rather than compete with them.
