🤖 AI Career Guidance Agent
An intelligent career assistant built with FastAPI, LangChain, and OpenAI GPT-4 that helps students discover:

🔍 Suitable career paths based on interests
💼 Skills & salary insights for each career
🎓 Free learning resources for upskilling
This project is designed for educational webinars, tech demos, and production-ready deployment on EC2.

🚀 Features
✅ Multi-step reasoning using LangChain RunnableSequence
✅ Modular architecture with clean, reusable chains
✅ OpenAI-powered insights and recommendations
✅ FastAPI backend ready for EC2 deployment
✅ Designed for scalability and future enhancements
🧠 Agent Workflow

graph TD
    A[User Input: Interests] --> B[CareerChain]
    B --> C[SkillChain]
    B --> D[ResourceChain]
    C --> E[Return Skills & Salaries]
    D --> F[Return Learning Resources]
📁 Folder Structure
bash
Copy
Edit
ai-career-agent/
│
├── app/
│   ├── main.py                  # FastAPI app entrypoint
│   ├── config.py                # Env loader
│   ├── utils/
│   │   └── llm_config.py        # OpenAI model setup
│   ├── chains/
│   │   ├── interest_chain.py
│   │   ├── skill_chain.py
│   │   └── resource_chain.py
│   ├── agent/
│   │   └── career_agent.py      # Final composed chain logic
│   └── schemas/
│       └── request.py           # Pydantic request model
├── .env                         # 🔐 Add your API keys here (not committed)
├── .gitignore
├── requirements.txt
└── README.md
⚙️ Setup Instructions
1. Clone the Repo
bash
Copy
Edit
git clone https://github.com/your-username/ai-career-agent.git
cd ai-career-agent
2. Create & Activate Virtual Environment
bash
Copy
Edit
python3.10 -m venv venv
source venv/bin/activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Add Your .env File
Create a .env file in the root directory with:
ini
Copy
Edit
OPENAI_API_KEY=your-openai-key
5. Run the App Locally
bash
Copy
Edit
uvicorn app.main:app --reload
Visit: http://127.0.0.1:8000/docs for Swagger UI

📦 Example Request
json
Copy
Edit
POST /suggest
{
  "interests": "biology, psychology"
}
🛠️ Tech Stack
Backend: FastAPI

AI Reasoning: LangChain

LLM: OpenAI GPT-4

Language: Python 3.10+

Deployment Ready: EC2 with gunicorn + nginx

📬 Connect With Us
For questions, feedback, or collaborations:
📧 contact: shloksschauhan.works@gmail.com