# Cloud Optimization Engine

## Project Overview

The Cloud Optimization Engine is a Django-based platform designed to intelligently analyze AWS EC2 instance performance and provide actionable, cost-saving recommendations. By integrating with AWS CloudWatch and a Large Language Model (LLM), the application helps users make informed decisions about their cloud infrastructure, reducing unnecessary spending and improving resource efficiency.

---

## Key Features

1. **API-Driven**
    Exposes a secure REST API endpoint to receive and process requests.

2. **AWS Integration**
    Utilizes Boto3 to collect real-time EC2 metrics (e.g., CPU Utilization) from AWS CloudWatch.

3. **LLM-Powered Insights**
    Sends collected data to an LLM to generate plain-language recommendations for instance type optimization.

4. **Secure Credential Management**
    Implements best practices for handling sensitive API keys using python-dotenv for environment-isolated configuration.

---

## Technology Stack

- Backend: Python, Django, Django REST Framework
- Cloud Services: Boto3, AWS EC2, AWS CloudWatch
- Artificial Intelligence: OpenAI API (or a local LLM like Ollama)
- Security: python-dotenv
- Tools: Postman

---

## Setup and Installation

    Follow these steps to get a local copy of the project up and running.

### 1. Clone the Repository

```bash
    git clone https://github.com/anagha0704/Cloud_Optimization_Engine.git
    cd Cloud_Optimization_Engine
```

---

### 2. Create a Virtual Environment

```bash
    python -m venv venv
    source venv/bin/activate
```

---

### 3. Install Dependencies
```bash
    pip install -r requirements.txt
```

### 4. Configure Environment Variables
    Create a file named .env in the project's root directory and add your credentials and keys.

```bash
    # Django
    DJANGO_SECRET_KEY='your-super-secret-key-goes-here'

    # AWS Credentials
    AWS_ACCESS_KEY_ID='your-aws-access-key-id'
    AWS_SECRET_ACCESS_KEY='your-aws-secret-access-key'
    AWS_REGION='your-aws-region'

    # OpenAI API Key
    OPENAI_API_KEY='your-openai-api-key'
```

---

### 5. Run Migrations

```bash
    python manage.py makemigrations optimization
    python manage.py migrate
```

Usage
Once the server is running and you have an EC2 instance in your AWS account, you can test the API.

1. Start the Server

    ```bash
        python manage.py runserver
    ```

2. Send a POST Request
Use a tool like Postman or the curl command to send an EC2 instance ID to your API.

    ```bash
        http://127.0.0.1:8000/api/optimize/
    ```

## Future Enhancements

1. Build a frontend to provide a user-friendly interface for instance management.
2. Integrate additional AWS metrics (e.g., NetworkIn, DiskReadBytes) for more comprehensive recommendations.
3. Add support for other AWS services, such as S3 or RDS
4. Implement a history of recommendations for long-term analysis.