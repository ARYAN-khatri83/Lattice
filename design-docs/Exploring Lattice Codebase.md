# Chat Conversation

Note: _This is purely the output of the chat conversation and does not contain any raw data, codebase snippets, etc. used to generate the output._

### User Input

You are a senior software engineer and technical mentor. I have a codebase that I need to fully understand for a job interview — I have zero prior knowledge of this project.
Your job is to produce a single, comprehensive, interview-ready document that explains this project so thoroughly that after reading it once, I can confidently explain every part of it to an interviewer.
Please cover the following in detail:
1. Project Overview
— What does this project do? What problem does it solve? Why does it exist?
2. Tech Stack & Imports
— List and explain every major library, framework, and import used. For each one, explain what it is, why it was chosen, and what would break without it.
3. Project Structure
— Walk through the folder/file structure. Explain what each file or folder is responsible for and how they connect to each other.
4. Core Logic — Step by Step
— Explain the main logic of the code as if telling a story. What happens first, second, third? Trace the full flow of data from input to output.
5. Key Code Sections (with explanation)
— Pick the most important code blocks and explain them line by line or block by block in plain English. No jargon without explanation.
6. Fallbacks, Error Handling & Edge Cases
— What happens when something goes wrong? What safety nets are built in? Why were these specific fallbacks chosen?
7. Design Decisions & The "Why"
— For every major architectural or technical choice, explain why that approach was taken over alternatives. What trade-offs were considered?
8. How the Pieces Connect
— Explain how all components, modules, or services talk to each other. Draw this out in plain text if needed (e.g., "Component A calls Service B, which returns data to Component C").
9. Potential Interview Questions & Answers
— List 10–15 questions an interviewer might ask about this project and provide strong, confident answers for each.
10. Summary (Elevator Pitch)
— Give me a 5–6 sentence summary I can say out loud to an interviewer when they ask "Tell me about this project."
Rules:

Write in simple, clear English. Avoid unnecessary jargon. When technical terms are used, immediately explain them in plain language.
Assume I am smart but have never seen this code before.
The document should be self-contained — I should need nothing else after reading it.
Be thorough. Do not skip anything that might come up in an interview.
Structure the document with clear headings so I can navigate it easily.

*Listed directory [Lattice](file:///Users/khatriaryan/Desktop/Lattice) *

*Viewed [README.md](file:///Users/khatriaryan/Desktop/Lattice/README.md) *

*Viewed [.env](file:///Users/khatriaryan/Desktop/Lattice/.env) *

*Viewed [docker-compose.yml](file:///Users/khatriaryan/Desktop/Lattice/docker-compose.yml) *

### Planner Response

Now let me explore the backend and frontend code in detail:

*Listed directory [backend](file:///Users/khatriaryan/Desktop/Lattice/backend) *

*Listed directory [frontend](file:///Users/khatriaryan/Desktop/Lattice/frontend) *

*Listed directory [design-docs](file:///Users/khatriaryan/Desktop/Lattice/design-docs) *

*Listed directory [demo](file:///Users/khatriaryan/Desktop/Lattice/demo) *

*Listed directory [app](file:///Users/khatriaryan/Desktop/Lattice/backend/app) *

*Listed directory [src](file:///Users/khatriaryan/Desktop/Lattice/frontend/src) *

*Viewed [requirements.txt](file:///Users/khatriaryan/Desktop/Lattice/backend/requirements.txt) *

*Viewed [package.json](file:///Users/khatriaryan/Desktop/Lattice/frontend/package.json) *

### Planner Response

Now let me read all the backend source files:

*Viewed [main.py](file:///Users/khatriaryan/Desktop/Lattice/backend/app/main.py) *

*Viewed [config.py](file:///Users/khatriaryan/Desktop/Lattice/backend/app/config.py) *

*Viewed [database.py](file:///Users/khatriaryan/Desktop/Lattice/backend/app/database.py) *

*Viewed [celery_worker.py](file:///Users/khatriaryan/Desktop/Lattice/backend/celery_worker.py) *

*Listed directory [models](file:///Users/khatriaryan/Desktop/Lattice/backend/app/models) *

*Listed directory [routes](file:///Users/khatriaryan/Desktop/Lattice/backend/app/routes) *

*Listed directory [schemas](file:///Users/khatriaryan/Desktop/Lattice/backend/app/schemas) *

*Listed directory [services](file:///Users/khatriaryan/Desktop/Lattice/backend/app/services) *

*Listed directory [tasks](file:///Users/khatriaryan/Desktop/Lattice/backend/app/tasks) *

*Listed directory [workflows](file:///Users/khatriaryan/Desktop/Lattice/backend/app/workflows) *

### Planner Response

Now let me read all the backend source files:

*Viewed [__init__.py](file:///Users/khatriaryan/Desktop/Lattice/backend/app/models/__init__.py) *

*Viewed [document.py](file:///Users/khatriaryan/Desktop/Lattice/backend/app/models/document.py) *

*Viewed [patient.py](file:///Users/khatriaryan/Desktop/Lattice/backend/app/models/patient.py) *

*Viewed [__init__.py](file:///Users/khatriaryan/Desktop/Lattice/backend/app/schemas/__init__.py) *

*Viewed [structured_document.py](file:///Users/khatriaryan/Desktop/Lattice/backend/app/schemas/structured_document.py) *

### Planner Response

Now let me read the rest of the backend files - services, routes, tasks, and workflows:

*Viewed [graph_service.py](file:///Users/khatriaryan/Desktop/Lattice/backend/app/services/graph_service.py) *

*Viewed [llm_service.py](file:///Users/khatriaryan/Desktop/Lattice/backend/app/services/llm_service.py) *

*Viewed [textract_service.py](file:///Users/khatriaryan/Desktop/Lattice/backend/app/services/textract_service.py) *

*Viewed [s3_service.py](file:///Users/khatriaryan/Desktop/Lattice/backend/app/services/s3_service.py) *

*Viewed [pdf_service.py](file:///Users/khatriaryan/Desktop/Lattice/backend/app/services/pdf_service.py) *

*Viewed [auth_service.py](file:///Users/khatriaryan/Desktop/Lattice/backend/app/services/auth_service.py) *

### Planner Response

Now let me read the remaining files - routes, tasks, workflows, and frontend:

*Viewed [documents.py](file:///Users/khatriaryan/Desktop/Lattice/backend/app/routes/documents.py) *

*Viewed [patients.py](file:///Users/khatriaryan/Desktop/Lattice/backend/app/routes/patients.py) *

*Viewed [health.py](file:///Users/khatriaryan/Desktop/Lattice/backend/app/routes/health.py) *

*Viewed [document_tasks.py](file:///Users/khatriaryan/Desktop/Lattice/backend/app/tasks/document_tasks.py) *

*Viewed [medical_extraction_graph.py](file:///Users/khatriaryan/Desktop/Lattice/backend/app/workflows/medical_extraction_graph.py) *

### Planner Response

Now let me read the frontend code:

*Viewed [App.tsx](file:///Users/khatriaryan/Desktop/Lattice/frontend/src/App.tsx) *

*Viewed [main.tsx](file:///Users/khatriaryan/Desktop/Lattice/frontend/src/main.tsx) *

*Viewed [config.ts](file:///Users/khatriaryan/Desktop/Lattice/frontend/src/config.ts) *

*Listed directory [pages](file:///Users/khatriaryan/Desktop/Lattice/frontend/src/pages) *

*Viewed [DashboardPage.tsx](file:///Users/khatriaryan/Desktop/Lattice/frontend/src/pages/DashboardPage.tsx) *

*Viewed [DocumentDetailPage.tsx](file:///Users/khatriaryan/Desktop/Lattice/frontend/src/pages/DocumentDetailPage.tsx) *

*Viewed [styles.css](file:///Users/khatriaryan/Desktop/Lattice/frontend/src/styles.css) *

### Planner Response

Now let me also read the Dockerfile and alembic files for completeness, then I'll read the design docs:

### Planner Response

Now I have a thorough understanding of the entire codebase. Let me write the comprehensive interview-ready document.

*Edited relevant file*