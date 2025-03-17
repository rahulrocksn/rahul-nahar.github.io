from sentence_transformers import SentenceTransformer
import faiss
import json

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


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

# Convert text to embeddings
texts = []
keys = []
for section, content in resume_data.items():
    if isinstance(content, list):
        for entry in content:
            texts.append(json.dumps(entry))
            keys.append(section)
    else:
        texts.append(str(content))
        keys.append(section)

embeddings = model.encode(texts)

# Test: Verify embeddings are correctly generated
assert embeddings.shape[0] == len(texts), "Embedding count does not match text count!"

# Test: Check FAISS search retrieval
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

query_embedding = model.encode(["give me all the projects you have made"])
distances, indices = index.search(query_embedding, 1)

retrieved_text = texts[indices[0][0]]
print("Retrieved Section:", retrieved_text)

# Test: Ensure correct retrieval
assert "Languages" in retrieved_text, "Incorrect section retrieved!"

