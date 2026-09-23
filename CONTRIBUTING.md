# Contributing Guidelines

Thank you for reviewing or contributing to this data science portfolio.

## Development Workflow
1. **Branching:** Work on dedicated feature branches (`feature/task-name`).
2. **Commit Style:** Adhere strictly to Conventional Commits:
   - `feat(...)`: New analytical feature or pipeline module
   - `docs(...)`: Documentation updates or report revisions
   - `test(...)`: Adding or updating test cases
   - `refactor(...)`: Restructuring code without changing functionality
   - `chore(...)`: Maintenance or configuration adjustments
3. **Reproducibility:** Fix random seeds using `random_state=42`.
4. **Testing:** Verify all test suites before committing:
   ```bash
   python scripts/run_all_tests.py
   ```
