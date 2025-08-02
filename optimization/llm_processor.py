import openai # or another LLM library

def get_llm_recommendation(instance_id, metric_data):
    # Format the data into a clear prompt for the LLM
    prompt = f"""
    Analyze the following CPU utilization data for an EC2 instance with ID {instance_id}:
    {metric_data}

    The data points represent the average CPU utilization over hourly periods in the last 24 hours.
    Provide a recommendation for this instance based on its usage pattern. 
    If the utilization is consistently low (e.g., below 10%), suggest a smaller instance type.
    If the utilization is consistently high (e.g., above 80%), suggest a larger instance type.
    The output should be a clear, concise recommendation text.
    """

    # Make the API call to the LLM
    response = openai.chat.completions.create(
        model="gpt-4o",  # or your preferred model
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150
    )
    return response.choices[0].message.content.strip()