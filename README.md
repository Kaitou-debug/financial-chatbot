FINANCIAL CHATBOT PROTOTYPE - DOCUMENTATION

OVERVIEW:
This is a rule-based prototype chatbot designed to answer specific financial queries regarding Microsoft, Apple, and Tesla. It uses data extracted from the Fiscal Year 2021-2024 10-K filings.

HOW IT WORKS:
The chatbot utilizes a simple Python script (`chatbot.py`) with a while-loop to continuously accept user input. It uses conditional logic (if-elif-else statements) to match the user's input string against a set of predefined valid queries. If a match is found, it returns the corresponding hardcoded financial insight derived from previous data analysis.

PREDEFINED QUERIES SUPPORTED:
1. "What is the total revenue?"
   - Provides the latest revenue figures for all three companies.
2. "How has net income changed over the last year?"
   - Summarizes the year-over-year percentage growth or decline in net income.
3. "Which company has the highest total assets?"
   - Identifies the company with the largest asset base (Microsoft).

LIMITATIONS:
1. Exact Matching: The chatbot currently requires exact string matching. It cannot interpret natural language variations (e.g., "Tell me about revenue" will fail).
2. Static Data: The responses are hardcoded based on a static dataset and do not update automatically from a live database.
3. Scope: It is limited to only three specific questions and three specific companies.

FUTURE IMPROVEMENTS:
- Integrate Natural Language Processing (NLP) to understand varied sentence structures.
- Connect to a SQL database or API to fetch real-time financial data.