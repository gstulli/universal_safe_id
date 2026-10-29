# USIPs: USI Improvement Proposals

🌐 **English** · [Português (Brasil)](README.pt-BR.md)

A **USIP** is a public document proposing a change to the design, the specification or the governance of USI, or recording an important decision. It is inspired by Bitcoin's BIPs and the IETF's RFCs (whitepaper section 14.2).

## When to write one

- A change to the architecture, protocols, cryptographic choices or assurance levels.
- Adding a country profile (whitepaper section 15.5).
- Adopting, replacing or dropping a component, or a partnership (sections 5.2 and 5.5).
- A change to governance or to this process.

Typos, clarifications and new evidence do not need a USIP: open an issue or a pull request.

## States

`Draft` → `Under discussion` → `Accepted` or `Rejected` (or `Withdrawn`). An accepted USIP may later be `Superseded` by another.

## Process

1. Discuss the idea in an issue first.
2. Copy [usip-template.md](usip-template.md) to `usip-NNNN-short-title.md` (next free number), fill it in and open a pull request. Add the Portuguese version `usip-NNNN-short-title.pt-BR.md` (or ask for help).
3. The USIP stays `Under discussion` for **at least 14 days**, publicly.
4. Objections must be answered in the document or in the thread. Rough consensus is sought, not unanimity.
5. The maintainer records the outcome and the reasons. **This role is provisional**: it will be replaced by the governance described in whitepaper section 14 (separation of powers, concentration limits, supermajority for critical rules).
6. A change that touches an essential characteristic (universal, collaborative, secure, non-profit, ownerless; whitepaper section 5.3) needs particularly strong justification and a longer discussion.

## Numbering

`usip-0001`, `usip-0002`, ... in order of opening. `usip-0000` is reserved for this process.
