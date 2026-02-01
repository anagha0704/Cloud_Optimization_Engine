# Cloud Optimization Engine

## Project Overview

Scalable Django platform that analyzes AWS EC2 performance metrics and delivers actionable cost-optimization recommendations. Using AWS CloudWatch and an LLM, the system synthesizes instance performance data into clear insights that support cost reduction and resource efficiency.

---

## Key Capabilities

1. **REST API interface**: Secure endpoints to accept AWS instance identifiers and return optimization recommendations.
2. **Real-time AWS telemetry**: Collects EC2 performance metrics (e.g., CPU utilization) via Boto3 from CloudWatch for data-driven analysis.
3. **LLM-driven recommendations**: Converts performance data into plain-language suggestions for instance sizing or cost savings.
4. **Credential security**: Manages AWS and OpenAI keys securely using python-dotenv for environment isolation.

---

## Technology Stack

- Backend: Python, Django, Django REST Framework
- Cloud Services: Boto3, AWS EC2, AWS CloudWatch
- Artificial Intelligence: OpenAI API (or a local LLM like Ollama)
- Security: python-dotenv
- Tools: Postman

---

## Setup and Installation

    Local Deployment Instructions

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

### 6. Usage

**Run & Test the API**

1. Start the Server

    ```bash
        python manage.py runserver
    ```

2. Send a POST Request
Use a tool like Postman or the curl command to send an EC2 instance ID to your API.

    ```bash
        http://127.0.0.1:8000/api/optimize/
    ```

## Planned Enhancements

* Develop a user interface for interactive instance management and visualization.
* Expand metric coverage (Network, Disk I/O) to strengthen recommendation accuracy.
* Extend optimization support to additional AWS services (e.g., S3, RDS).
* Add recommendation history tracking to analyze trends over time.
