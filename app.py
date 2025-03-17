from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import numpy as np  
import google.generativeai as genai
import uvicorn
from dotenv import load_dotenv
import os

load_dotenv()

# Near the top of your file after imports
api_key = os.getenv("GOOGLE_API_KEY")
port = int(os.getenv("PORT", 8000))

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000", "https://rahul-nahar-github-io.vercel.app/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello World!"}

resume_data = { "Education": [
        {
            "Institution": "Purdue University",
            "Degree": "M.S Computer Science",
            "Location": "West Lafayette, IN",
            "Graduation": "May 2025",
            "Coursework": [
                "Robotics",
                "Foundations of Deep Learning",
                "Compiling and Programming Systems",
                "Parallel Computing",
                "Algorithm Design, Analysis, and Implementation",
                "Data Networks and Communications",
                "Information Security"
            ]
        },
        {
            "Institution": "University of Wollongong",
            "Degree": "BSc. Computer Science (Big Data)",
            "Location": "Wollongong, Australia",
            "Graduation": "Oct 2022",
            "Coursework": [
                "Project Development",
                "Software Development Methodology",
                "Object-Oriented Design and Programming",
                "Data Management and Security",
                "Big Data Mining Implementation"
            ]
        }
    ],
    "Skills": {
        "Languages": [
            "Python", "Java", "C++", "C", "JavaScript",
            "HTML/CSS", "R", "SQL (Postgres)", "MongoDB",
            "PL/SQL", "Golang", "PHP", "Scala"
        ],
        "Frameworks & Tools": [
            "React", "Node.js", "Flask", "Django", "RestAPI",
            "Pandas", "PySpark", "PyTorch", "TensorFlow", "MapReduce",
            "Pig Latin", "Hive", "Scikit Learn", "Postman", "Numpy",
            "Next.js", "Nest.js", "AWS", "Spark", "Hadoop", "MapReduce", "Redis"
        ],
        "Organizations": [
            "IDEAS Lab", "Li Group", "CSGSB [Graduate Committee Representative]",
            "Toastmasters", "Frontera"
        ]
    },
    "Experience": [
        {
            "Role": "Teaching Assistant",
            "Company": "Purdue University",
            "Location": "West Lafayette, IN",
            "Duration": "August 2024 - Present",
            "Responsibilities": [
                "Conducted Data Structures and Algorithms doubt-clearing sessions and coursework assessment.",
                "Led students in designing and implementing a Deepfake Detection capstone project, ensuring 100% milestone completion."
            ]
        },
        {
            "Role": "Software Engineer",
            "Company": "Tekbrics",
            "Location": "New Jersey, United States",
            "Duration": "January 2022 - July 2023",
            "Responsibilities": [
                "Enhanced product capabilities by integrating ML algorithms into web-based applications using the MERN stack.",
                "Developed high-performance data pipelines using Python and SQL, accelerating data retrieval speed by 50%.",
                "Collaborated with software engineering and data science teams to incorporate AI features, improving functionality and user interaction."
            ]
        },
        {
            "Role": "Researcher",
            "Company": "Purdue University",
            "Location": "West Lafayette, United States",
            "Duration": "August 2023 - Present",
            "Projects": [
                {
                    "Title": "The Data Mine",
                    "Description": "Developed an AI-based predictive model leveraging supplier KPI’s to forecast potential constraints, managing supplier performance and enterprise risk."
                },
                {
                    "Title": "IDEAS Lab",
                    "Description": "Designed a deep reinforcement learning (dRL)-based system for persistent monitoring, enabling a single robot to balance search and tracking behaviors in dynamic environments."
                }
            ]
        }
    ],
    "Publications": [
        {
            "Title": "FaultExplainer",
            "Description": "Leveraging Large Language Models for Interpretable Fault Detection and Diagnosis, improving fault detection accuracy by 70%."
        },
        {
            "Title": "scChat",
            "Description": "A Large Language Model-Powered Co-Pilot for Contextualized Single-Cell RNA Sequencing Analysis, reducing LLM costs by 54%."
        }
    ],
    "Projects": [
        {
            "Title": "Distributed File System",
            "Tech Stack": ["Golang", "PostgreSQL", "React.js"],
            "Description": "Executed secure session-based authentication using OIDC for data privacy. Developed robust APIs using Gorilla Mux."
        },
        {
            "Title": "Full-Stack Project Discovery Platform",
            "Tech Stack": ["NestJS", "MongoDB", "Elasticsearch", "Next.js", "Google Cloud"],
            "Description": "Built a project discovery platform using Elasticsearch and semantic search, increasing discovery efficiency by 70%."
        },
        {
            "Title": "Deep Learning Network",
            "Tech Stack": ["Python", "PyTorch", "NumPy"],
            "Description": "Implemented a feed-forward neural network from scratch, incorporating backpropagation, activation functions, and group-invariant CNNs, achieving 95% accuracy on the MNIST dataset."
        },
        {
            "Title": "Web-Spam Detection",
            "Tech Stack": ["SVM", "Decision Trees", "Random Forest", "Naïve Bayes", "KNN"],
            "Description": "Developed a web-spam classification model with PCA and SOM for feature reduction, enhancing detection accuracy to 68%."
        },
        {
            "Title": "Vulnerabilities and Attacks",
            "Tech Stack": ["C", "GDB"],
            "Description": "Investigated vulnerabilities like buffer overflow, DEP bypass, XSS, CSRF, and Padding Oracle attacks."
        },
        {
            "Title": "Compiler Optimization",
            "Tech Stack": ["CMake", "C++", "LLVM"],
            "Description": "Developed LLVM IR optimizations by implementing control and data flow analysis, including SSA and register allocation."
        },
        {
            "Title": "SDN & Network Protocols",
            "Tech Stack": ["P4", "Mininet", "ARP", "TCP", "Python"],
            "Description": "Developed a P4-based learning switch for optimized packet forwarding using match-action tables (MATs)."
        },
        {
            "Title": "Real-Time Alert System for Listings",
            "Tech Stack": ["Python", "Selenium", "BeautifulSoup", "Flask"],
            "Description": "Automated web scraping and alerting via Telegram bot, reducing manual search time by 10 minutes per query."
        }
    ],
    "Contact": {
        "Email": "rahulnpre@gmail.com",
        "LinkedIn": "https://www.linkedin.com/in/rahulnahar2610/",
        "GitHub": "https://github.com/rahulrocksn"
    }
}
print("Server Started", resume_data)

def generate_text(prompt, api_key, model_name="gemini-1.5-pro"):
    """Generates text using the specified Gemini model.

    Args:
        prompt: The text prompt to send to the model.
        api_key: Your Google AI Studio API key.
        model_name: The name of the Gemini model to use (e.g., "gemini-pro").

    Returns:
        The generated text, or None if an error occurs.
    """
    try:
        genai.configure(api_key=api_key) #configure inside the function for safety.
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


    
print("Server Started")

@app.get("/query")
def query_resume(question: str, num_results: int = 3):  # Allow specifying the number of results
    
    text_prompt = "Give a short answer to the question based on the following information: " + question + " " + json.dumps(resume_data) + ". I will be using this for my portfolio website, so give me a short answer, probably 5-7 lines for it.. If the retrieved information is not relevant, say 'No relevant information found, but please listen to a software joke.'"
    generated_text = generate_text(text_prompt, api_key)

    if generated_text:
        print("Generated Text:")
        print(generated_text)

    return {"responses": generated_text}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=port)



# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# import faiss
# import json
# from sentence_transformers import SentenceTransformer
# import numpy as np  
# import torch
# from transformers import AutoModelForCausalLM, AutoTokenizer
# import google.generativeai as genai

# from dotenv import load_dotenv
# import os

# load_dotenv()

# # Near the top of your file after imports
# api_key = os.getenv("GOOGLE_API_KEY")

# app = FastAPI()
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],  # Allow both localhost and IP
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# print("Server Started1")
# # Load Model
# model = SentenceTransformer("all-MiniLM-L6-v2")

# resume_data = { "Education": [
#         {
#             "Institution": "Purdue University",
#             "Degree": "M.S Computer Science",
#             "Location": "West Lafayette, IN",
#             "Graduation": "May 2025",
#             "Coursework": [
#                 "Robotics",
#                 "Foundations of Deep Learning",
#                 "Compiling and Programming Systems",
#                 "Parallel Computing",
#                 "Algorithm Design, Analysis, and Implementation",
#                 "Data Networks and Communications",
#                 "Information Security"
#             ]
#         },
#         {
#             "Institution": "University of Wollongong",
#             "Degree": "BSc. Computer Science (Big Data)",
#             "Location": "Wollongong, Australia",
#             "Graduation": "Oct 2022",
#             "Coursework": [
#                 "Project Development",
#                 "Software Development Methodology",
#                 "Object-Oriented Design and Programming",
#                 "Data Management and Security",
#                 "Big Data Mining Implementation"
#             ]
#         }
#     ],
#     "Skills": {
#         "Languages": [
#             "Python", "Java", "C++", "C", "JavaScript",
#             "HTML/CSS", "R", "SQL (Postgres)", "MongoDB",
#             "PL/SQL", "Golang", "PHP", "Scala"
#         ],
#         "Frameworks & Tools": [
#             "React", "Node.js", "Flask", "Django", "RestAPI",
#             "Pandas", "PySpark", "PyTorch", "TensorFlow", "MapReduce",
#             "Pig Latin", "Hive", "Scikit Learn", "Postman", "Numpy",
#             "Next.js", "Nest.js", "AWS", "Spark", "Hadoop", "MapReduce", "Redis"
#         ],
#         "Organizations": [
#             "IDEAS Lab", "Li Group", "CSGSB [Graduate Committee Representative]",
#             "Toastmasters", "Frontera"
#         ]
#     },
#     "Experience": [
#         {
#             "Role": "Teaching Assistant",
#             "Company": "Purdue University",
#             "Location": "West Lafayette, IN",
#             "Duration": "August 2024 - Present",
#             "Responsibilities": [
#                 "Conducted Data Structures and Algorithms doubt-clearing sessions and coursework assessment.",
#                 "Led students in designing and implementing a Deepfake Detection capstone project, ensuring 100% milestone completion."
#             ]
#         },
#         {
#             "Role": "Software Engineer",
#             "Company": "Tekbrics",
#             "Location": "New Jersey, United States",
#             "Duration": "January 2022 - July 2023",
#             "Responsibilities": [
#                 "Enhanced product capabilities by integrating ML algorithms into web-based applications using the MERN stack.",
#                 "Developed high-performance data pipelines using Python and SQL, accelerating data retrieval speed by 50%.",
#                 "Collaborated with software engineering and data science teams to incorporate AI features, improving functionality and user interaction."
#             ]
#         },
#         {
#             "Role": "Researcher",
#             "Company": "Purdue University",
#             "Location": "West Lafayette, United States",
#             "Duration": "August 2023 - Present",
#             "Projects": [
#                 {
#                     "Title": "The Data Mine",
#                     "Description": "Developed an AI-based predictive model leveraging supplier KPI’s to forecast potential constraints, managing supplier performance and enterprise risk."
#                 },
#                 {
#                     "Title": "IDEAS Lab",
#                     "Description": "Designed a deep reinforcement learning (dRL)-based system for persistent monitoring, enabling a single robot to balance search and tracking behaviors in dynamic environments."
#                 }
#             ]
#         }
#     ],
#     "Publications": [
#         {
#             "Title": "FaultExplainer",
#             "Description": "Leveraging Large Language Models for Interpretable Fault Detection and Diagnosis, improving fault detection accuracy by 70%."
#         },
#         {
#             "Title": "scChat",
#             "Description": "A Large Language Model-Powered Co-Pilot for Contextualized Single-Cell RNA Sequencing Analysis, reducing LLM costs by 54%."
#         }
#     ],
#     "Projects": [
#         {
#             "Title": "Distributed File System",
#             "Tech Stack": ["Golang", "PostgreSQL", "React.js"],
#             "Description": "Executed secure session-based authentication using OIDC for data privacy. Developed robust APIs using Gorilla Mux."
#         },
#         {
#             "Title": "Full-Stack Project Discovery Platform",
#             "Tech Stack": ["NestJS", "MongoDB", "Elasticsearch", "Next.js", "Google Cloud"],
#             "Description": "Built a project discovery platform using Elasticsearch and semantic search, increasing discovery efficiency by 70%."
#         },
#         {
#             "Title": "Deep Learning Network",
#             "Tech Stack": ["Python", "PyTorch", "NumPy"],
#             "Description": "Implemented a feed-forward neural network from scratch, incorporating backpropagation, activation functions, and group-invariant CNNs, achieving 95% accuracy on the MNIST dataset."
#         },
#         {
#             "Title": "Web-Spam Detection",
#             "Tech Stack": ["SVM", "Decision Trees", "Random Forest", "Naïve Bayes", "KNN"],
#             "Description": "Developed a web-spam classification model with PCA and SOM for feature reduction, enhancing detection accuracy to 68%."
#         },
#         {
#             "Title": "Vulnerabilities and Attacks",
#             "Tech Stack": ["C", "GDB"],
#             "Description": "Investigated vulnerabilities like buffer overflow, DEP bypass, XSS, CSRF, and Padding Oracle attacks."
#         },
#         {
#             "Title": "Compiler Optimization",
#             "Tech Stack": ["CMake", "C++", "LLVM"],
#             "Description": "Developed LLVM IR optimizations by implementing control and data flow analysis, including SSA and register allocation."
#         },
#         {
#             "Title": "SDN & Network Protocols",
#             "Tech Stack": ["P4", "Mininet", "ARP", "TCP", "Python"],
#             "Description": "Developed a P4-based learning switch for optimized packet forwarding using match-action tables (MATs)."
#         },
#         {
#             "Title": "Real-Time Alert System for Listings",
#             "Tech Stack": ["Python", "Selenium", "BeautifulSoup", "Flask"],
#             "Description": "Automated web scraping and alerting via Telegram bot, reducing manual search time by 10 minutes per query."
#         }
#     ],
#     "Contact": {
#         "Email": "rahulnpre@gmail.com",
#         "LinkedIn": "https://www.linkedin.com/in/rahulnahar2610/",
#         "GitHub": "https://github.com/rahulrocksn"
#     }
# }
# print("Server Started", resume_data)

# # Step 1: Create category-level embeddings
# category_names = list(resume_data.keys())  # ["Education", "Skills", "Experience", "Projects", etc.]
# category_embeddings = model.encode(category_names)

# category_index = faiss.IndexFlatL2(category_embeddings.shape[1])
# category_index.add(category_embeddings)

# # Step 2: Create sub-section embeddings for fine-grained search
# subsection_texts = []
# subsection_keys = []
# subsection_to_category = []

# for category, entries in resume_data.items():
#     if isinstance(entries, list):
#         for entry in entries:
#             text = json.dumps(entry)
#             subsection_texts.append(text)
#             subsection_keys.append(category)
#             subsection_to_category.append(category)
#     else:
#         subsection_texts.append(str(entries))
#         subsection_keys.append(category)
#         subsection_to_category.append(category)

# subsection_embeddings = model.encode(subsection_texts)
# subsection_index = faiss.IndexFlatL2(subsection_embeddings.shape[1])
# subsection_index.add(subsection_embeddings)

# def generate_text(prompt, api_key, model_name="gemini-1.5-pro"):
#     """Generates text using the specified Gemini model.

#     Args:
#         prompt: The text prompt to send to the model.
#         api_key: Your Google AI Studio API key.
#         model_name: The name of the Gemini model to use (e.g., "gemini-pro").

#     Returns:
#         The generated text, or None if an error occurs.
#     """
#     try:
#         genai.configure(api_key=api_key) #configure inside the function for safety.
#         model = genai.GenerativeModel(model_name)
#         response = model.generate_content(prompt)
#         return response.text
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return None


    
# print("Server Started")

# @app.get("/query")
# def query_resume(question: str, num_results: int = 3):  # Allow specifying the number of results
#     # Step 1: Find the most relevant category
#     query_embedding = model.encode([question])
#     _, category_idx = category_index.search(query_embedding, 1)
#     selected_category = category_names[category_idx[0][0]]
    
#     print(f"🔹 Detected Category: {selected_category}")

#     # Step 2: Search within the selected category's values
#     relevant_indices = [i for i, cat in enumerate(subsection_to_category) if cat == selected_category]
#     relevant_embeddings = [subsection_embeddings[i] for i in relevant_indices]

#     if not relevant_embeddings:  # No relevant data found
#         return {"category": selected_category, "response": "No relevant information found."}

#     # Create a temporary FAISS index for searching within the category
#     temp_index = faiss.IndexFlatL2(len(relevant_embeddings[0]))
#     relevant_embeddings_array = np.array(relevant_embeddings, dtype=np.float32)
#     temp_index.add(relevant_embeddings_array)

#     # Search for multiple relevant results (default: top 3)
#     _, subsection_idxs = temp_index.search(query_embedding, min(num_results, len(relevant_embeddings)))

#     # Retrieve multiple relevant responses
#     retrieved_texts = [subsection_texts[relevant_indices[idx]] for idx in subsection_idxs[0]]
    
#     print("🔹 Retrieved Entries:", retrieved_texts)
    
#     text_prompt = "Give a short answer to the question based on the following information: " + question + " " + " ".join(retrieved_texts) + ". I will be using this for my portfolio website, so give me a short answer, probably 5-7 lines for it. If the retrieved information is not relevant, say 'No relevant information found, but please listen to a software joke.'"
#     print("Generating text...", text_prompt)
#     generated_text = generate_text(text_prompt, api_key)

#     if generated_text:
#         print("Generated Text:")
#         print(generated_text)

#     return {"category": selected_category, "responses": generated_text}

