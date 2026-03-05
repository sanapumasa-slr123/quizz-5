from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=None)  # Will use OPENAI_API_KEY environment variable

SYSTEM_PROMPT = """You are a Python Syntax & Debugging Assistant. Your role is to:
1. Explain Python concepts clearly and concisely
2. Fix Python code snippets and suggest improvements
3. Recommend appropriate Python libraries for tasks
4. Provide debugging advice

IMPORTANT LIMITATIONS:
- You MUST refuse to write code in any other language (JavaScript, C++, Java, etc.)
- You cannot discuss general tech news or computer hardware
- Keep responses focused on Python programming

When a user asks you to code in another language, respond with: "I can only help with Python code. Please ask me something related to Python."
"""

def get_ai_response(messages: list) -> str:
    """
    Get AI response from OpenAI API
    
    Args:
        messages: List of message dicts with 'role' and 'content'
    
    Returns:
        str: AI response content
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": SYSTEM_PROMPT}] + messages,
            max_tokens=500,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error getting AI response: {str(e)}"
