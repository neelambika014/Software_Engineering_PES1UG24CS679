\# Lab 5: Static Code Analysis



\## Objective



To improve Python code quality, security, and formatting using Pylint, Bandit, and Flake8.



\## Issues Identified and Fixes Applied



| Tool | Issue identified | Fix applied |

|---|---|---|

| Pylint | Missing module and function docstrings | Added docstrings |

| Pylint | Function names did not follow snake\_case | Renamed functions using snake\_case |

| Pylint | Unused import and argument | Removed unused import and argument |

| Pylint | Unnecessary else after return | Simplified conditional logic |

| Bandit | Hardcoded password | Removed the hardcoded password |

| Bandit | Potential SQL injection | Used parameterized SQL queries |

| Bandit | Unsafe subprocess usage | Replaced the shell command with print() |

| Flake8 | Lines exceeded the allowed length | Reformatted long statements |

| Flake8 | Missing whitespace and excess blank lines | Corrected formatting |



\## Final Analysis Results



\- Pylint score: 10.00/10

\- Bandit: No issues identified

\- Flake8: No style violations reported



\## Reflection



\### 1. What is static code analysis?



Static code analysis examines source code without executing it to identify potential bugs, security vulnerabilities, and style violations.



\### 2. What did the three tools help identify?



Pylint identified code-quality and naming issues. Bandit identified potentially unsafe coding patterns. Flake8 identified formatting and style violations.



\### 3. Why are parameterized SQL queries important?



They separate SQL commands from user-provided values, reducing the risk of SQL injection.



\### 4. How does static analysis improve software quality?



It helps developers identify problems early, improve maintainability, follow coding standards, and reduce security risks.



\### 5. What did you learn from this lab?



I learned how to run Pylint, Bandit, and Flake8, interpret their reports, fix code-quality and security issues, and verify improvements by running the tools again.

