from llm_helper import llm
from few_shot import FewShotPosts

few_shot = FewShotPosts()


# ✅ Convert length type to readable string
def get_length_str(length):
    if length == "Short":
        return "1 to 5 lines"
    elif length == "Medium":
        return "6 to 10 lines"
    elif length == "Long":
        return "11 to 15 lines"
    else:
        return "6 to 10 lines"  # default fallback


# ✅ Main function to generate a LinkedIn post
def generate_post(length, language, tag):
    prompt = get_prompt(length, language, tag)

    # Get response from LLM
    response = llm.invoke(prompt)

    # Handle both dict-like and object-like responses
    if hasattr(response, "content"):
        return response.content
    elif isinstance(response, dict) and "content" in response:
        return response["content"]
    else:
        return str(response)


# ✅ Build the prompt dynamically
def get_prompt(length, language, tag):
    length_str = get_length_str(length)

    prompt = f"""
    Generate a LinkedIn post using the below information. No preamble.

    1) Topic: {tag}
    2) Length: {length_str}
    3) Language: {language}
    If Language is Hinglish then it means it is a mix of Hindi and English. 
    The script for the generated post should always be English.
    """

    # Add few-shot examples if available
    examples = few_shot.get_filtered_posts(length, language, tag)

    if len(examples) > 0:
        prompt += "\n\n4) Use the writing style as per the following examples."

    for i, post in enumerate(examples):
        post_text = post["text"]
        prompt += f"\n\nExample {i + 1}:\n\n{post_text}"

        if i == 1:  # Max two examples
            break

    return prompt


# ✅ Run directly
if __name__ == "__main__":
    print(generate_post("Medium", "English", "Mental Health"))
