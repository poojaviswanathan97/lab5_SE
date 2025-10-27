1. Which issues were the easiest to fix, and which were the hardest? Why?

Easiest: The simplest fixes were stylistic and formatting issues such as missing docstrings, unused imports, and PEP 8 naming conventions. These were straightforward because they didn’t affect logic or functionality—just required cleanup.
Hardest: The most challenging fix was removing the global variable usage. It required refactoring multiple functions to return and pass stock_data explicitly, ensuring functionality stayed intact while satisfying Pylint’s rule. This change also required testing the code flow thoroughly to prevent breaking data handling.

2. Did the static analysis tools report any false positives? If so, describe one example.

Yes, a mild false positive occurred with Pylint’s global-statement warning (W0603). While technically valid, it flagged a simple and safe global use that wasn’t inherently dangerous in this small script. However, removing it still improved structure and maintainability, so the fix was beneficial despite the low actual risk.

3. How would you integrate static analysis tools into your actual software development workflow?

Integrate Pylint, Flake8, and Bandit checks into a Continuous Integration (CI) pipeline (e.g., GitHub Actions) to automatically run on every push or pull request.
Use pre-commit hooks locally to prevent committing code that fails style or security checks.
Review reports regularly to catch regressions early, ensuring that code maintains consistent quality and security standards throughout the project lifecycle.

4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

The refactored code became more readable, modular, and maintainable with consistent naming and clear docstrings.
Error handling and input validation reduced the risk of runtime failures.
Security improved by removing eval() and narrowing exception handling.
The program is now fully PEP 8 compliant, easier to understand for collaborators, and safer to extend or reuse in future projects.