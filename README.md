# FAQ Retrieval System

The FAQ Retrieval System is built using **FastAPI** for the backend and **HTMX** for dynamic front-end interactions. The application leverages a machine-learning model to find the most relevant answer to a given question from a pre-defined FAQ dataset.

## Setup Instructions

Follow these steps to set up and run the project locally.

---

### 1. Clone the Repository
First, clone the project repository from GitHub and navigate into the project directory:

```bash
git clone https://github.com/ouerghi01/aziz-werghi_Tak2.git
cd aziz-werghi_Tak2
```

---

### 2. Run the Setup Script

Run the provided setup script to prepare your environment.

#### On Linux/macOS:
```bash
bash setup.sh
```

#### On Windows:
```bash
setup.bat
```

---

### 3. Activate the Virtual Environment

Activate the Python virtual environment created by the setup script.

#### On Linux/macOS:
```bash
source venv/bin/activate
```

#### On Windows:
```bash
venv\Scripts\activate
```

---



### 4. Run the Application

Start the FastAPI server to run the application:

```bash
uvicorn main:app --reload
```

The application will be accessible at `http://127.0.0.1:8000/` by default.

---

## Application Logic

### Core Functionality
- The application uses the **SentenceTransformer** model (`all-MiniLM-L6-v2`) to encode and compare question embeddings.
- A CSV file (`Data/questions_and_answers.csv`) containing predefined questions and answers is read and processed.
- The system identifies the most relevant answer by calculating the similarity between the user’s query and the dataset questions.

### API Endpoints
- **`GET /`**: Serves the main page of the application with a simple interface to ask questions.
- **`POST /answer_to_question`**: Accepts a question from the user, processes it, and returns the best-matched answer from the dataset.

### Frontend Integration
- The application uses **HTMX** for seamless interaction between the client-side and server-side without requiring full-page reloads.

---

## Notes
- Ensure that the `Data/questions_and_answers.csv` file is in the correct directory with the appropriate structure (columns: `Question` and `Answer`).
- The application automatically handles CORS and serves static files from the `static` directory.
- Templates for the UI are located in the `templates` directory and rendered using **Jinja2**.
