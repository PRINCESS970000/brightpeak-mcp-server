# 🎓 BrightPeak Academy MCP Server

A FastMCP-based academic management system that demonstrates how a client and server communicate using the Model Context Protocol (MCP).

The project simulates a university management platform where the client interacts with the server to retrieve student information, manage grades, generate reports, and request AI-powered academic evaluations using MCP Sampling.

---

# 🚀 Features

- 📚 List all available courses
- 👨‍🎓 Retrieve student profiles
- 📝 Enroll students in courses
- ✏️ Update student grades with role-based authorization
- 📊 Generate academic reports with progress notifications
- 🤖 AI-powered student evaluation using MCP Sampling

---

# 🛠 Technologies

- Python 3.13
- FastMCP
- SQLite
- asyncio

---

# 📁 Project Structure

```
brightpeak-mcp-server/
│
├── Mcp-Server/
│   ├── server.py
│   ├── database.db
│   └── ...
│
├── client/
│   ├── client.py
│   └── test.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/brightpeak-mcp-server.git
```

Navigate into the project

```bash
cd brightpeak-mcp-server
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

#  Run the Project

Run the client

```bash
python client/client.py
```

The client automatically starts the MCP server using PythonStdioTransport.

---

#  Available MCP Tools

| Tool | Description |
|------|-------------|
| list_all_courses | Returns all available courses |
| get_student_profile | Retrieves a student's profile |
| enroll_student | Enrolls a student in a course |
| update_student_grade | Updates grades with authorization |
| generate_academic_report | Generates an academic report with progress tracking |
| request_student_evaluation | Requests an AI evaluation through MCP Sampling |

---

#  Progress Notifications

The server sends progress updates while generating reports.

Example:

```
Progress: 0%
Collecting student records...

Progress: 30%
Analyzing grades...

Progress: 70%
Generating final report...

Progress: 100%
Done
```

---

#  MCP Sampling

The project demonstrates MCP Sampling.

Instead of generating an academic evaluation inside the server, the server sends a prompt to the client.

The client (AI) generates the response and sends it back to the server.

Flow:

```
Client
    │
    │ call_tool()
    ▼
Server
    │
    │ ctx.sample(...)
    ▼
Client AI
    │
    │ Generate Evaluation
    ▼
Server
    │
    ▼
Client
```

---

#  Authorization

Grade updates require one of the following roles:

- INSTRUCTOR
- ADMIN

Unauthorized requests are rejected.

---

#  Example Output

========== Calling generate_academic_report ==========

Progress: 0%
Collecting student records...

Progress: 30%
Analyzing grades...

Progress: 70%
Generating final report...

Progress: 100%

Academic report generated successfully.

