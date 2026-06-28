# Claude Code Instructions
This project is an enterprise-style Agentic M&A Due Diligence Platform.

## Primary Responsibilities
- Write clean, modular, maintainable Python code.
- Explain architecture before implementing major features.
- Prefer small incremental changes over large rewrites.
- Never rewrite unrelated files.
- Add tests for new functionality.
- Keep business logic in Python and reasoning in LLM prompts.
- Use type hints and Pydantic models where appropriate.

## Engineering Rules
- Do not invent features that are not requested.
- Do not hard-code secrets.
- Use environment variables for API keys and database URLs.
- Keep prompts in `app/prompts/`.
- Keep agents in `app/agents/`.
- Keep LangGraph workflows in `app/graph/`.
- Keep RAG logic in `app/rag/`.
- Keep API routes in `app/api/`.

## AI System Rules
- Every diligence finding should cite source evidence when possible.
- If evidence is missing, say so clearly.
- Do not fabricate financial, legal, or market claims.
- Human review is required for high-risk findings.

## Development Workflow
Before implementing a feature:
1. Summarize the goal.
2. List files to modify.
3. Explain the design.
4. Implement incrementally.
5. Add or update tests.
6. Suggest the next commit message.