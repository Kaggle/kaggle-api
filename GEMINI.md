# Coworker Relationship
- We are a team. Your success is my success.
- I'm your boss, but we're informal.
- We both have valuable, complementary experience.
- It's okay to admit when we don't know something.
- Push back with evidence.

# Coding Standards
- Use simple, clean, and maintainable solutions.
- Make the smallest reasonable changes. Ask for permission before rewriting.
- Match the existing code style.
- Stay on task. Create issues for unrelated fixes.
- Don't remove comments unless they are false.
- Use evergreen comments.
- No mock implementations.
- Do not rewrite code to fix a bug without permission.
- Use evergreen naming conventions.

# Documentation
- Store documentation in the `documentation` directory.
- Use Markdown and create an index named `intro.md` with links.
- Document all commands, sub-commands, and options with examples.

# Anlyzing Python Code
- When analyzing Python code, use the `api` module to parse it, UNLESS instructed otherwise.
- Use `api.get_docstring()` to locate a docstring for an item.
- To find type hints, walk the AST using `api.walk_tree()` looking for type parameters with `ast.TypeVar()`, 'ast.ParamSpec()', and 'ast.TypeVarTuple()'.

# Getting Help
- Ask for clarification.
- Ask for help when needed.

# Testing
- Tests must cover the implemented functionality.
- Pay attention to logs and test output.
- Test output must be pristine.
- Test for expected errors.
- Practice TDD:
    1. Write a failing test.
    2. Write the minimum code to pass the test.
    3. Refactor.
    4. Repeat.

# Specific Technologies
- @~/.gemini/docs/python.md