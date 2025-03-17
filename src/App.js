import React, { useState, useEffect } from 'react';
import { FaGithub, FaLinkedin, FaMoon, FaSun, FaBars, FaTimes } from 'react-icons/fa';
import './styles/globals.css';
import emailjs from '@emailjs/browser';


function App() {
  const [darkMode, setDarkMode] = useState(false);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [activeSection, setActiveSection] = useState('home');
  const [formStatus, setFormStatus] = useState('');

  const [query, setQuery] = useState('');
  const [queryResult, setQueryResult] = useState(null);
  const [isQuerying, setIsQuerying] = useState(false);

  // Add this new function
  const handleQuerySubmit = async (e) => {
    e.preventDefault();
    setIsQuerying(true);
    try {
      const API_URL = "https://rahul-nahar-github-io-1.onrender.com/";  // Replace with your Render URL
      // Update your fetch call
      const response = await fetch(`${API_URL}/query?question=${encodeURIComponent(query)}`);      const data = await response.json();
      console.log('Query result:', data);
      setQueryResult(data);
    } catch (error) {
      console.error('Error querying resume:', error);
    }
    setIsQuerying(false);
  };
  
  // Toggle dark mode
  const toggleDarkMode = () => {
    setDarkMode(!darkMode);
  };

  // Handle scroll to set active section
  useEffect(() => {
    const handleScroll = () => {
      const sections = document.querySelectorAll('section');
      let current = '';
      
      sections.forEach((section) => {
        const sectionTop = section.offsetTop;
        if (window.scrollY >= sectionTop - 200) {
          current = section.getAttribute('id');
        }
      });
      
      setActiveSection(current);
    };
    
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  // Scroll to section
  const scrollToSection = (sectionId) => {
    const element = document.getElementById(sectionId);
    window.scrollTo({
      top: element.offsetTop - 70,
      behavior: 'smooth'
    });
    setMobileMenuOpen(false);
  };

  // Resume data
  const data = {
    personalInfo: {
      name: "Rahul Nahar",
      title: "Software Engineer & ML Researcher",
      email: "rahulnpre@gmail.com",
      phone: "619-490-8724",
      github: "https://github.com/rahulrocksn",
      linkedin: "https://www.linkedin.com/in/rahulnahar2610/",
      bio: "I'm a Computer Science graduate student at Purdue University specializing in machine learning, software development, and data engineering. With experience in both research and industry, I develop innovative solutions at the intersection of AI and software engineering."
    },
    education: [
      {
        degree: "M.S Computer Science",
        institution: "Purdue University",
        location: "West Lafayette, IN",
        date: "May 2025",
        courses: "Robotics, Foundations of Deep Learning, Compiling and Programming Systems, Parallel Computing, Algo Design, Analysis and Implementation"
      },
      {
        degree: "BSc. Computer Science (Big Data)",
        institution: "University of Wollongong",
        location: "Wollongong, Australia",
        date: "October 2022",
        courses: "Project Development, Software Development Methodology, Object Oriented Design and Programming, Data Management and Security"
      }
    ],
    experiences: [
      {
        role: "Teaching Assistant",
        company: "Purdue University",
        location: "West Lafayette, IN",
        period: "August 2024 - Present",
        description: [
          "Familiarized students with Data Structures and Algorithms, conducting doubt-clearing sessions and assessing coursework.",
          "Led students in designing and implementing a Deepfake Detection capstone project, streamlining project workflows."
        ]
      },
      {
        role: "Software Engineer",
        company: "Tekbrics",
        location: "New Jersey, United States",
        period: "January 2022 - July 2023",
        description: [
          "Enhanced product capabilities by integrating ML algorithms into web-based applications using the MERN stack.",
          "Engineered high-performance data pipelines using Python and SQL, accelerating data retrieval speed by 50%."
        ]
      },
      {
        role: "Research Experience",
        company: "Purdue University",
        location: "West Lafayette, United States",
        period: "August 2023 - Present",
        description: [
          "The Data Mine: Collaborating with Caterpillar to develop an AI-based predictive model for supplier KPI's.",
          "IDEAS Lab: Designing and implementing a deep reinforcement learning (dRL)-based system for persistent monitoring."
        ]
      }
    ],
    publications: [
      {
        title: "FaultExplainer: Leveraging Large Language Models for Interpretable Fault Detection and Diagnosis",
        description: "Developed and maintained a website for fault monitoring in industrial settings using PCA and feature engineering, improving accuracy by 70%."
      },
      {
        title: "scChat: A Large Language Model-Powered Co-Pilot for Contextualized Single-Cell RNA Sequencing Analysis",
        description: "Built a ChatGPT-like platform to analyze and query custom RNA sequencing datasets using OpenAI API and RAG systems, reducing LLM costs by 54%."
      }
    ],
    projects: [
      {
        title: "Distributed File System",
        tech: "Golang, PostgreSQL, React.js",
        description: "Executed secure session-based authentication using OIDC in Golang for data privacy and access control. Developed and documented robust APIs using Gorilla Mux, integrating with the frontend via cross-functional hooks.",
        github: "https://github.com/OhanaFS",
      },
      {
        title: "Full-Stack Project Discovery Platform",
        tech: "NestJS, MongoDB, Elasticsearch, Next.js, Google Cloud",
        description: "Constructed and developed a project discovery platform using Elasticsearch and semantic search, increasing discovery efficiency by 70%.",
        github: "https://github.com/Front-era/project-finder",
      },
      {
        title: "Vulnerabilities and Attacks",
        tech: "C, GDB, Web Security",
        description: "Investigated vulnerable C code susceptible to stack-smashing attacks. Exploited diverse vulnerabilities including buffer overflow, DEP bypass, and analyzed security flaws."
      },
      {
        title: "Compiler Optimization",
        tech: "CMake, C++, LLVM",
        description: "Developed LLVM IR optimizations by implementing Control and Data Flow Analysis. Designed compiler passes for Live Variable Analysis and Dead Code Elimination."
      },
      {
        title: "SDN & Network Protocols",
        tech: "P4, Mininet, ARP, TCP, Python",
        description: "Developed a P4-based learning switch in Mininet for optimized packet forwarding using match-action tables (MATs). Formulated SDN switch migration strategies via clustering using cost functions, boosting network efficiency by 52%."
      },
      {
        title: "Real-Time Alert System for Listings",
        tech: "Python, Selenium, BeautifulSoup, Flask",
        description: "Scraped webpages changing dynamically while efficiently storing and processing data. Automated job execution using CRON jobs and Selenium for scheduled searches. Implemented Flask to acquire search criteria, scraped listings, and alerted users via a Telegram bot, improving user efficiency by reducing manual search time by 10 minutes per query."
        , github: "https://github.com/rahulrocksn/Carousell-new-listing-automation-web-scrapping-"
      },
      {
        title: "Deep Learning Network",
        tech: "Python, PyTorch, NumPy",
        description: "Implemented a feed-forward neural network from scratch, incorporating backpropagation, activation functions, and group-invariant CNNs. Designed an HMC sampler for MLP and optimized training, achieving 95% accuracy on the MNIST dataset."
        , github: "https://github.com/rahulrocksn/DeepLearning"
      },
      {
        title: "Web-Spam Detection",
        tech: "Python, Machine Learning, PCA",
        description: "Developed a web-spam classification model using SVM, Decision Trees, Random Forest, Naïve Bayes, and KNN. Applied PCA and SOM for feature reduction, enhancing detection accuracy to 68%."
        , github: "https://github.com/rahulrocksn/Web-spam-detection" 
      },
    ],
    skills: {
      languages: [
        "Python", "Java", "C++", "C", "JavaScript", "HTML/CSS", "R", "SQL (Postgres)", 
        "MongoDB", "PL/SQL", "Golang", "PHP", "Scala"
      ],
      frameworks: [
        "React", "Node.js", "Flask", "Django", "RestAPI", "Pandas", "PySpark", "PyTorch", 
        "Tensorflow", "MapReduce", "Scikit Learn", "Next.js", "AWS", "Spark", "Hadoop"
      ]
    }
  };

  return (
    <div className={`app ${darkMode ? 'dark-mode' : ''}`}>
      {/* Header */}
      <header className="header">
        <div className="container header-content">
          <h1 className="logo">RN</h1>
          
          <nav className={`nav-menu ${mobileMenuOpen ? 'active' : ''}`}>
            <ul>
              <li className={activeSection === 'home' ? 'active' : ''}>
                <a onClick={() => scrollToSection('home')}>Home</a>
              </li>
              <li className={activeSection === 'about' ? 'active' : ''}>
                <a onClick={() => scrollToSection('about')}>About</a>
              </li>
              <li className={activeSection === 'experience' ? 'active' : ''}>
                <a onClick={() => scrollToSection('experience')}>Experience</a>
              </li>
              <li className={activeSection === 'projects' ? 'active' : ''}>
                <a onClick={() => scrollToSection('projects')}>Projects</a>
              </li>
              <li className={activeSection === 'skills' ? 'active' : ''}>
                <a onClick={() => scrollToSection('skills')}>Skills</a>
              </li>
              <li className={activeSection === 'publications' ? 'active' : ''}>
                <a onClick={() => scrollToSection('publications')}>Publications</a>
              </li>
              <li className={activeSection === 'contact' ? 'active' : ''}>
                <a onClick={() => scrollToSection('contact')}>Contact</a>
              </li>
            </ul>
          </nav>
          
          <div className="header-right">
            <button className="theme-toggle" onClick={toggleDarkMode}>
              {darkMode ? <FaSun /> : <FaMoon />}
            </button>
            <button className="mobile-toggle" onClick={() => setMobileMenuOpen(!mobileMenuOpen)}>
              {mobileMenuOpen ? <FaTimes /> : <FaBars />}
            </button>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main>

        {/* Hero Section */}
        <section className="query-section">
          <div className="container">
            <div className="query-content">
              <h2 className="section-title">Ask me about my experience</h2>
              <form onSubmit={handleQuerySubmit} className="query-form">
                <input
                  type="text"
                  value={query}
                  onChange={(e) => setQuery(e.target.value)}
                  placeholder="e.g., What are your programming skills?"
                  className="query-input"
                />
                <button 
                  type="submit" 
                  className="btn btn-primary"
                  disabled={isQuerying}
                >
                  {isQuerying ? 'Cooking...' : 'Ask'}
                </button>
              </form>
              {queryResult && (
                <div className="query-result card">
                  <p>{queryResult.responses}</p>
                </div>
              )}
            </div>
          </div>
        </section>

        <section id="home" className="hero-section">
          <div className="container">
            <div className="hero-content">
              <h1 className="fade-in">
                Hi, I'm <span className="gradient-text">{data.personalInfo.name}</span>
              </h1>
              <h2 className="fade-in">{data.personalInfo.title}</h2>
              <p className="fade-in">{data.personalInfo.bio}</p>
              <div className="hero-buttons fade-in">
                <button className="btn btn-primary" onClick={() => scrollToSection('contact')}>
                  Contact Me
                </button>
                <button className="btn btn-outline" onClick={() => scrollToSection('projects')}>
                  View Projects
                </button>
              </div>
              <div className="social-links fade-in">
                <a href={data.personalInfo.github} target="_blank" rel="noopener noreferrer">
                  <FaGithub />
                </a>
                <a href={data.personalInfo.linkedin} target="_blank" rel="noopener noreferrer">
                  <FaLinkedin />
                </a>
              </div>
            </div>
          </div>
        </section>


        {/* About Section */}
        <section id="about" className="about-section">
          <div className="container">
            <h2 className="section-title">About Me</h2>
            <div className="about-content">
              <div className="about-text">
                <p>{data.personalInfo.bio}</p>
                <h3>Education</h3>
                <div className="education-cards">
                  {data.education.map((edu, index) => (
                    <div className="card education-card" key={index}>
                      <h3>{edu.degree}</h3>
                      <h4>{edu.institution}</h4>
                      <p className="location">{edu.location}</p>
                      <p className="date">{edu.date}</p>
                      <p className="courses"><strong>Courses:</strong> {edu.courses}</p>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* Experience Section */}
        <section id="experience" className="experience-section">
          <div className="container">
            <h2 className="section-title">Experience</h2>
            <div className="timeline">
              {data.experiences.map((exp, index) => (
                <div className="timeline-item" key={index}>
                  <div className="timeline-content card">
                    <h3>{exp.role}</h3>
                    <h4>{exp.company}</h4>
                    <p className="location">{exp.location}</p>
                    <p className="period">{exp.period}</p>
                    <ul>
                      {exp.description.map((item, i) => (
                        <li key={i}>{item}</li>
                      ))}
                    </ul>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* Projects Section */}
        <section id="projects" className="projects-section">
          <div className="container">
            <h2 className="section-title">Projects</h2>
            <div className="projects-grid">
          {data.projects.map((project, index) => (
            <div className="project-card card" key={index}>
              <h3>{project.title}</h3>
              <div className="tech-stack">
                <span>{project.tech}</span>
              </div>
              <p>{project.description}</p>
              {project.github && (
                <a 
                  href={project.github} 
                  target="_blank" 
                  rel="noopener noreferrer"
                  className="project-github-link"
                >
                  <FaGithub /> View Code
                </a>
              )}
            </div>
          ))}
        </div>
          </div>
        </section>

        {/* Skills Section */}
        <section id="skills" className="skills-section">
          <div className="container">
            <h2 className="section-title">Skills</h2>
            <div className="skills-content">
              <div className="skill-category">
                <h3>Languages</h3>
                <div className="skill-tags">
                  {data.skills.languages.map((lang, index) => (
                    <span className="skill-tag" key={index}>{lang}</span>
                  ))}
                </div>
              </div>
              <div className="skill-category">
                <h3>Frameworks & Tools</h3>
                <div className="skill-tags">
                  {data.skills.frameworks.map((framework, index) => (
                    <span className="skill-tag" key={index}>{framework}</span>
                  ))}
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* Publications Section */}
        <section id="publications" className="publications-section">
          <div className="container">
            <h2 className="section-title">Publications</h2>
            <div className="publications-list">
              {data.publications.map((pub, index) => (
                <div className="publication-card card" key={index}>
                  <h3>{pub.title}</h3>
                  <p>{pub.description}</p>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* Contact Section */}
        <section id="contact" className="contact-section">
          <div className="container">
            <h2 className="section-title">Contact Me</h2>
            <div className="contact-content">
              <div className="contact-info">
                <p>
                  <strong>Email:</strong> <a href={`mailto:${data.personalInfo.email}`}>{data.personalInfo.email}</a>
                </p>
                <p>
                  <strong>Phone:</strong> <a href={`tel:${data.personalInfo.phone}`}>{data.personalInfo.phone}</a>
                </p>
                <div className="social-links">
                  <a href={data.personalInfo.github} target="_blank" rel="noopener noreferrer">
                    <FaGithub /> GitHub
                  </a>
                  <a href={data.personalInfo.linkedin} target="_blank" rel="noopener noreferrer">
                    <FaLinkedin /> LinkedIn
                  </a>
                </div>
              </div>
              <form className="contact-form" onSubmit={(e) => {
    e.preventDefault();
    setFormStatus('sending');
    
    emailjs.sendForm(
      'service_i3hrxhf', // Replace with your EmailJS service ID
      'template_fln7xv6',    // Your template ID
      e.target,
      'y7Wx1aUzKlPBwwEFo'  // Replace with your EmailJS public key
    )
      .then(() => {
        setFormStatus('success');
        e.target.reset();
        setTimeout(() => setFormStatus(''), 5000);
      })
      .catch(() => {
        setFormStatus('error');
        setTimeout(() => setFormStatus(''), 5000);
      });
  }}>
    <div className="form-group">
      <label htmlFor="name">Name</label>
      <input type="text" id="name" name="user_name" required />
    </div>
    <div className="form-group">
      <label htmlFor="email">Email</label>
      <input type="email" id="email" name="user_email" required />
    </div>
    <div className="form-group">
      <label htmlFor="message">Message</label>
      <textarea id="message" name="message" rows="5" required></textarea>
    </div>
    <button type="submit" className="btn btn-primary" disabled={formStatus === 'sending'}>
      {formStatus === 'sending' ? 'Sending...' : 'Send Message'}
    </button>
    {formStatus === 'success' && (
      <p className="success-message">Message sent successfully!</p>
    )}
    {formStatus === 'error' && (
      <p className="error-message">Failed to send message. Please try again.</p>
    )}
  </form>
            </div>
          </div>
        </section>
      </main>

      {/* Footer */}
      <footer className="footer">
        <div className="container">
          <div className="footer-content">
            <p>&copy; {new Date().getFullYear()} {data.personalInfo.name}. All rights reserved.</p>
            <div className="social-links">
              <a href={data.personalInfo.github} target="_blank" rel="noopener noreferrer">
                <FaGithub />
              </a>
              <a href={data.personalInfo.linkedin} target="_blank" rel="noopener noreferrer">
                <FaLinkedin />
              </a>
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
}

export default App;
