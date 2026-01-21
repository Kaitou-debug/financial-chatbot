def simple_chatbot():
    print("--- Financial Analysis Chatbot ---")
    print("I can answer questions about Microsoft, Apple, and Tesla based on their latest 10-K filings.")
    print("Valid queries you can ask:")
    print("1. What is the total revenue?")
    print("2. How has net income changed over the last year?")
    print("3. Which company has the highest total assets?")
    print("(Type 'exit' to close the chatbot)")
    print("-" * 40)

    while True:
        user_input = input("User: ").strip()
        
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        
        # Query 1: Total Revenue
        elif user_input == "What is the total revenue?":
            response = (
                "Chatbot: Here is the total revenue for the most recent fiscal year:\n"
                "- Microsoft (2024): $245,122 Million\n"
                "- Apple (2024): $391,035 Million\n"
                "- Tesla (2023): $96,773 Million"
            )
            print(response)

        # Query 2: Net Income Growth
        elif user_input == "How has net income changed over the last year?":
            response = (
                "Chatbot: Based on the data analysis:\n"
                "- Microsoft: Net Income increased by ~21.8% (from $72.4B to $88.1B).\n"
                "- Apple: Net Income decreased by ~3.4% (from $97.0B to $93.7B).\n"
                "- Tesla: Net Income increased by ~19.4% (from $12.6B to $15.0B)."
            )
            print(response)

        # Query 3: Total Assets
        elif user_input == "Which company has the highest total assets?":
            response = (
                "Chatbot: Microsoft has the highest total assets at $512,163 Million (FY2024), "
                "followed by Apple ($364,980M) and Tesla ($106,618M)."
            )
            print(response)

        # Fallback for unknown queries
        else:
            print("Chatbot: Sorry, I can only respond to the specific predefined queries listed above.")

if __name__ == "__main__":
    simple_chatbot()