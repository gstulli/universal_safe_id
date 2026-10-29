# Experiments

🌐 **English** · [Português (Brasil)](README.pt-BR.md)

> ⚠️ **Research prototypes.** Nothing here is production software. **Never use real keys, real documents or real personal data.** Passing a check here does not mean a key or design is secure.

Each experiment answers **one question** from the whitepaper (section 16, E1 to E20). The goal is evidence, including negative evidence, not a product.

## Convention

One folder per experiment: `E<NN>-<short-name>/`. Start from [`_template`](_template/README.md). Each folder has a `README.md` (and `README.pt-BR.md`) with:

1. **Hypothesis** and the whitepaper section it relates to.
2. **Method** and **success criterion** (decided *before* running).
3. **Status:** `planned`, `in progress`, `done`, `abandoned`.
4. **Result:** what happened, with data. **Negative results are published.**
5. **How to reproduce.**
6. **Limitations** and what the result does not show.
7. A banner stating that it is a research prototype.

Keep experiments small (one to two weeks of work), disposable and behind simple interfaces, so that a result can change the design without rewriting everything. Cite and credit existing work you reuse (whitepaper section 5.2).

## Index

| ID | Experiment | Status | Folder |
|---|---|---|---|
| E13 | Country profile: Brazil (research, no code) | in progress | [docs/research/E13-brazilian-documents.md](../docs/research/E13-brazilian-documents.md) |
| E17 | Key quality: weak-key checker (first prototype) | in progress | [E17-weak-key-linter](E17-weak-key-linter/README.md) |

The full list, with hypotheses and success criteria, is in whitepaper section 16. Each experiment has an issue labelled `experiment`.
