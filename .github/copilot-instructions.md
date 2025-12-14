<!-- Copilot instructions for AI coding agents -->
# eliza-bot — Copilot instructions

Short, actionable guide for AI code assistants working in this repository.

- **Big picture:** This repository is a tiny, single-file Python implementation of the ELIZA chatbot. The entire runtime logic lives in [eliza.py](eliza.py). The project intentionally avoids frameworks and external dependencies.

- **Primary files:**
  - [eliza.py](eliza.py) — single source of truth. Contains a `rules` mapping (pattern -> responses) and the matching/response logic.
  - [README.md](README.md) — project description; update when adding new behaviors or CLI flags.

- **What to change and how:**
  - Add conversational rules by editing the top-level `rules` dict in `eliza.py`. Use regular-expression keys (prefer raw strings) and values as a list of response templates. Example pattern entry:

    ```py
    rules[r"I need (.*)"] = ["Why do you need %s?", "Would getting %s help?"]
    ```

  - Keep logic inside `eliza.py` small and self-contained. If adding complexity (new modules, tests), add a short note in `README.md` describing how to run things.

- **Running & debugging:**
  - There is no build step. Run the bot interactively with `python3 eliza.py` from the repository root.
  - When modifying regex rules, test them locally by running the script and exercising the new patterns. Use small unit scripts or an interactive Python session to validate `re` behavior.

- **Project conventions & patterns:**
  - Minimalist, single-file design — avoid introducing heavy dependencies. Prefer standard library (`re`, `random`, etc.).
  - Response templates should use `%s` placeholders for captured groups (consistent with existing simple style) or Python f-strings if you refactor consistently.

- **When to create new files:**
  - If you add non-trivial parsing, multi-file structure, or tests, create a `tests/` folder and a brief `README.md` update explaining how to run tests (e.g., `pytest`).

- **Integration and external dependencies:**
  - Currently none. If adding integrations (APIs, databases), document required environment variables in `README.md` and avoid committing secrets.

- **Commit & PR guidance for agents:**
  - Keep changes small and focused (single behavioral change per PR).
  - Update `README.md` for any user-facing CLI or behavior change.

- **Examples in this repo:**
  - The `rules` dict in [eliza.py](eliza.py) is the canonical example of how input patterns map to responses. Follow its shape when extending behavior.

If anything above is unclear or you want examples converted to tests or a small CLI, tell me which area to expand.
