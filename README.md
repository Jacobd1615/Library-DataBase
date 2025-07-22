<div align="center">

# 📚 Library Management System

### *Professional Flask-based REST API for Modern Library Operations*

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.1.1-green?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Latest-blue?style=for-the-badge&logo=postgresql&logoColor=white)](https://postgresql.org)
[![Swagger](https://img.shields.io/badge/Swagger-API%20Docs-orange?style=for-the-badge&logo=swagger&logoColor=white)](https://swagger.io)
[![Render](https://img.shields.io/badge/Deployed%20on-Render-purple?style=for-the-badge&logo=render&logoColor=white)](https://render.com)

---

**🌐 Live Demo:** [library-database-ja0b.onrender.com](https://library-database-ja0b.onrender.com)  
**📖 API Documentation:** [Interactive Swagger Docs](https://library-database-ja0b.onrender.com/api/docs)

*A comprehensive solution for library management with modern REST API architecture, JWT authentication, and interactive documentation.*

</div>

---

## ✨ Key Features

<table>
<tr>
<td width="50%">

### 📖 **Book Management**
- ➕ Add new books with comprehensive metadata
- 🔍 Advanced search functionality by title
- 📊 Popular books ranking system
- ✏️ Update and delete operations
- 📋 Complete book catalog management

</td>
<td width="50%">

### 👥 **Member Management**
- 🔐 Secure user registration and authentication
- 🎫 JWT token-based authorization
- 👤 Profile management and updates
- � Password hashing and security
- 📧 Email-based user identification

</td>
</tr>
<tr>
<td width="50%">

### 📋 **Loan Management**
- 📚 Multi-book loan creation
- 📅 Date tracking and management
- 🔄 Dynamic book addition/removal
- � Comprehensive loan history
- 🔗 Member-book relationship tracking

</td>
<td width="50%">

### 🚀 **Production Features**
- 📊 Interactive Swagger API documentation
- �️ Rate limiting and security measures
- 🌐 Cloud deployment with PostgreSQL
- 🔄 Automatic database migrations
- 📈 Scalable architecture design

</td>
</tr>
</table>

## 🏗️ System Architecture

### 🛠️ Technology Stack

<div align="center">

| Component | Technology | Version | Purpose |
|-----------|------------|---------|---------|
| **Backend Framework** | ![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white) | 3.1.1 | Web application framework |
| **Database (Prod)** | ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=flat&logo=postgresql&logoColor=white) | Latest | Production database |
| **Database (Dev)** | ![SQLite](https://img.shields.io/badge/SQLite-07405E?style=flat&logo=sqlite&logoColor=white) | Built-in | Development database |
| **ORM** | ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=flat&logo=sqlalchemy&logoColor=white) | 2.0.41 | Object-relational mapping |
| **Authentication** | ![JWT](https://img.shields.io/badge/JWT-000000?style=flat&logo=jsonwebtokens&logoColor=white) | python-jose | Token-based auth |
| **Validation** | ![Marshmallow](https://img.shields.io/badge/Marshmallow-8A2BE2?style=flat) | Latest | Data serialization |
| **Documentation** | ![Swagger](https://img.shields.io/badge/Swagger-85EA2D?style=flat&logo=swagger&logoColor=white) | OpenAPI 2.0 | API documentation |
| **Deployment** | ![Render](https://img.shields.io/badge/Render-46E3B7?style=flat&logo=render&logoColor=white) | Cloud | Production hosting |
| **Rate Limiting** | ![Flask-Limiter](https://img.shields.io/badge/Flask_Limiter-FF6B6B?style=flat) | Latest | API protection |

</div>

### 📁 Project Architecture

```
📦 Library Management System
├── 🚀 flask_app.py              # Application entry point & server startup
├── ⚙️ config.py                 # Environment configurations (Dev/Prod)
├── 📋 requirements.txt          # Python package dependencies
├── 📦 setup.py                  # Package installation configuration
├── 📖 README.md                 # Project documentation
├── 
├── 📁 app/                      # Main application package
│   ├── 🏭 __init__.py           # Application factory pattern
│   ├── 🗄️ models.py             # SQLAlchemy database models
│   ├── 🔧 extensions.py         # Flask extensions initialization
│   │
│   ├── 📁 blueprints/           # Modular route organization
│   │   ├── 👥 member/           # Member management module
│   │   │   ├── __init__.py      # Blueprint registration
│   │   │   ├── routes.py        # Member API endpoints
│   │   │   └── schemas.py       # Member data validation
│   │   ├── 📚 book/             # Book management module
│   │   │   ├── __init__.py      # Blueprint registration
│   │   │   ├── routes.py        # Book API endpoints
│   │   │   └── schemas.py       # Book data validation
│   │   ├── 📋 loan/             # Loan management module
│   │   │   ├── __init__.py      # Blueprint registration
│   │   │   ├── routes.py        # Loan API endpoints
│   │   │   └── schemas.py       # Loan data validation
│   │   └── 🐛 debug/            # Development utilities
│   │       ├── __init__.py      # Debug blueprint
│   │       └── routes.py        # Debug endpoints
│   │
│   ├── 📁 static/               # Static assets
│   │   └── 📄 swagger.yaml      # OpenAPI documentation
│   │
│   ├── 📁 utils/                # Helper utilities
│   │   ├── __init__.py          # Utils package
│   │   └── utils.py             # Common utility functions
│   │
│   └── 📁 tests/                # Test suite
│       ├── __init__.py          # Test package
│       ├── test_member.py       # Member endpoint tests
│       ├── test_book.py         # Book endpoint tests
│       └── test_loan.py         # Loan endpoint tests
```

## 🚀 Quick Start Guide

### 📋 Prerequisites

Before you begin, ensure you have the following installed:

- ![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=flat&logo=python&logoColor=white) **Python 3.9 or higher**
- ![Git](https://img.shields.io/badge/Git-Latest-orange?style=flat&logo=git&logoColor=white) **Git version control**
- ![pip](https://img.shields.io/badge/pip-Latest-yellow?style=flat&logo=pypi&logoColor=white) **pip package manager**

### 🔧 Installation & Setup

#### **Step 1: Clone Repository**
```bash
# Clone the project repository
git clone https://github.com/Jacobd1615/Library-DataBase.git

# Navigate to project directory
cd Library-DataBase
```

#### **Step 2: Environment Setup**
```bash
# Create virtual environment (Windows)
python -m venv .venv

# Activate virtual environment
# Windows Command Prompt:
.venv\Scripts\activate
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# macOS/Linux:
source .venv/bin/activate
```

#### **Step 3: Install Dependencies**
```bash
# Install all required packages
pip install -r requirements.txt

# Verify installation
pip list
```

#### **Step 4: Environment Configuration**
```bash
# Create environment file (optional for local development)
# The app will use SQLite by default for local development
echo "SECRET_KEY=your-secret-key-here" > .env
```

#### **Step 5: Launch Application**
```bash
# Start the Flask development server
python flask_app.py

# You should see:
# * Running on http://127.0.0.1:5000
# * Debug mode: on (in development)
```

### 🌐 Access Points

Once running, access your application at:

| Service | URL | Description |
|---------|-----|-------------|
| **API Base** | `http://localhost:5000` | Main API endpoint |
| **Swagger Docs** | `http://localhost:5000/api/docs` | Interactive API documentation |
| **Health Check** | `http://localhost:5000/debug/health` | Application status |

## 📖 API Documentation

### 🗂️ Endpoint Overview

<details>
<summary><b>👥 Member Management Endpoints</b></summary>

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `POST` | `/members` | Register new member | ❌ |
| `GET` | `/members` | Retrieve all members | ❌ |
| `PUT` | `/members` | Update member profile | ✅ |
| `DELETE` | `/members` | Delete member account | ✅ |
| `POST` | `/members/login` | Authenticate & get JWT token | ❌ |

</details>

<details>
<summary><b>📚 Book Management Endpoints</b></summary>

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `POST` | `/books` | Add new book to catalog | ❌ |
| `GET` | `/books` | Retrieve all books | ❌ |
| `GET` | `/books/popular` | Get books sorted by popularity | ❌ |
| `GET` | `/books/search` | Search books by title | ❌ |
| `PUT` | `/books/{id}` | Update book information | ❌ |
| `DELETE` | `/books/{id}` | Remove book from catalog | ❌ |

</details>

<details>
<summary><b>📋 Loan Management Endpoints</b></summary>

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `POST` | `/loans` | Create new book loan | ❌ |
| `GET` | `/loans` | Retrieve all loans | ❌ |
| `GET` | `/loans/{id}` | Get specific loan details | ❌ |
| `PUT` | `/loans/{id}` | Update loan (add/remove books) | ❌ |
| `DELETE` | `/loans/{id}` | Delete loan record | ❌ |

</details>

### 🔐 Authentication System

The API uses **JWT (JSON Web Tokens)** for secure authentication. Protected endpoints require a valid token in the request header.

#### **Getting Authentication Token**
```bash
POST /members/login
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "securepassword123"
}
```

#### **Using Authentication Token**
```bash
# Include in Authorization header
curl -H "Authorization: Bearer YOUR_JWT_TOKEN" \
     -H "Content-Type: application/json" \
     https://library-database-ja0b.onrender.com/members
```

### 📊 Request/Response Examples

<details>
<summary><b>🔍 Example: Create a New Member</b></summary>

**Request:**
```bash
POST /members
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john.doe@email.com",
  "DOB": "1990-01-15",
  "password": "securepassword123"
}
```

**Response:**
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john.doe@email.com",
  "DOB": "1990-01-15",
  "password": "$2b$12$..." // hashed password
}
```

</details>

<details>
<summary><b>📚 Example: Add a New Book</b></summary>

**Request:**
```bash
POST /books
Content-Type: application/json

{
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "genre": "Classic Literature",
  "desc": "A classic American novel set in the Jazz Age"
}
```

**Response:**
```json
{
  "id": 1,
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "genre": "Classic Literature",
  "desc": "A classic American novel set in the Jazz Age"
}
```

</details>

<details>
<summary><b>📋 Example: Create Multi-Book Loan</b></summary>

**Request:**
```bash
POST /loans
Content-Type: application/json

{
  "loan_date": "2025-01-22",
  "member_id": 1,
  "book_ids": [1, 2, 3]
}
```

**Response:**
```json
{
  "id": 1,
  "loan_date": "2025-01-22",
  "member_id": 1,
  "books": [
    {
      "id": 1,
      "title": "The Great Gatsby",
      "author": "F. Scott Fitzgerald"
    },
    {
      "id": 2,
      "title": "To Kill a Mockingbird",
      "author": "Harper Lee"
    },
    {
      "id": 3,
      "title": "1984",
      "author": "George Orwell"
    }
  ]
}
```

</details>

## 💾 Database Architecture

### 📊 Entity Relationship Diagram

```
┌─────────────────┐         ┌─────────────────┐         ┌─────────────────┐
│     MEMBERS     │         │      LOANS      │         │      BOOKS      │
├─────────────────┤         ├─────────────────┤         ├─────────────────┤
│ 🔑 id (PK)      │◄────────┤ 🔑 id (PK)      │         │ 🔑 id (PK)      │
│ 👤 name         │         │ 📅 loan_date    │         │ 📖 title        │
│ 📧 email        │         │ 🔗 member_id FK │         │ ✍️ author       │
│ 🎂 DOB          │         └─────────────────┘         │ 🏷️ genre        │
│ 🔒 password     │                  │                  │ 📝 description  │
└─────────────────┘                  │                  └─────────────────┘
                                     │                           ▲
                                     │                           │
                                     ▼                           │
                            ┌─────────────────┐                  │
                            │   LOAN_BOOKS    │                  │
                            │ (Junction Table) │                  │
                            ├─────────────────┤                  │
                            │ 🔗 loan_id (FK) │──────────────────┘
                            │ 🔗 book_id (FK) │
                            └─────────────────┘
```

### 🗃️ Database Models

<details>
<summary><b>👤 Member Model</b></summary>

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `id` | Integer | Primary Key, Auto-increment | Unique member identifier |
| `name` | String(100) | Not Null | Member's full name |
| `email` | String(120) | Unique, Not Null | Email address for login |
| `DOB` | Date | Not Null | Date of birth |
| `password` | String(255) | Not Null | Hashed password |

**Relationships:**
- One-to-Many with Loans (One member can have multiple loans)

</details>

<details>
<summary><b>📚 Book Model</b></summary>

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `id` | Integer | Primary Key, Auto-increment | Unique book identifier |
| `title` | String(200) | Not Null | Book title |
| `author` | String(100) | Not Null | Author name |
| `genre` | String(50) | Not Null | Book genre/category |
| `desc` | Text | Not Null | Book description |

**Relationships:**
- Many-to-Many with Loans (One book can be in multiple loans)

</details>

<details>
<summary><b>📋 Loan Model</b></summary>

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `id` | Integer | Primary Key, Auto-increment | Unique loan identifier |
| `loan_date` | Date | Not Null | Date when loan was created |
| `member_id` | Integer | Foreign Key, Not Null | Reference to member |

**Relationships:**
- Many-to-One with Members (Multiple loans can belong to one member)
- Many-to-Many with Books (One loan can contain multiple books)

</details>

## 🛠️ Development & Testing

### 🏃‍♂️ Running the Application

#### **Development Mode**
```bash
# Activate virtual environment
.venv\Scripts\activate

# Run with debug mode enabled
python flask_app.py

# The application will start with:
# ✅ Debug mode: ON
# ✅ Auto-reload: ENABLED
# ✅ SQLite database: AUTO-CREATED
# ✅ Swagger docs: AVAILABLE
```

#### **Production Mode**
```bash
# Set production environment
export FLASK_ENV=production  # Linux/macOS
set FLASK_ENV=production     # Windows

# Run with Gunicorn (production server)
gunicorn --bind 0.0.0.0:5000 flask_app:app
```

### 🧪 Testing the API

#### **Using Swagger UI (Recommended)**
1. Navigate to `http://localhost:5000/api/docs`
2. Explore all available endpoints
3. Test requests directly in the browser
4. View response schemas and examples

#### **Using cURL Commands**
```bash
# Test API health
curl http://localhost:5000/debug/health

# Create a new member
curl -X POST http://localhost:5000/members \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Jane Smith",
    "email": "jane@example.com",
    "DOB": "1985-05-15",
    "password": "mypassword123"
  }'

# Get all books
curl http://localhost:5000/books

# Search for books
curl "http://localhost:5000/books/search?title=gatsby"
```

#### **Using Postman**
Import our Postman collection for comprehensive testing:
1. Download from: `/static/postman-collection.json` (if available)
2. Import into Postman
3. Set base URL to `http://localhost:5000`
4. Run automated test suites

### 🔒 Database Safety Features

Our application implements **advanced database protection**:

```python
# Conditional table creation prevents data loss
inspector = inspect(db.engine)
if not inspector.has_table("members"):
    db.create_all()  # Only creates if tables don't exist
    print("✅ Database tables created successfully!")
else:
    print("ℹ️ Database tables already exist - preserving data")
```

**Protection Benefits:**
- ✅ **Safe Restarts**: Data preserved when restarting application
- ✅ **Safe Deployments**: Production data maintained during updates
- ✅ **Development Safety**: Local test data won't be lost
- ✅ **Migration Ready**: Prepared for future schema changes

## 🚀 Production Deployment

### 🌐 Live Production Environment

**🔗 Production URL:** [library-database-ja0b.onrender.com](https://library-database-ja0b.onrender.com)

Our application is professionally deployed on **Render Cloud Platform** with enterprise-grade features:

| Feature | Implementation | Status |
|---------|----------------|---------|
| **Auto-Deployment** | GitHub integration | ✅ Active |
| **Database** | PostgreSQL managed service | ✅ Running |
| **SSL/HTTPS** | Automatic certificate | ✅ Secured |
| **CDN** | Global content delivery | ✅ Enabled |
| **Monitoring** | Real-time health checks | ✅ Active |

### ⚙️ Environment Configuration

#### **Production Environment Variables**
```bash
# Required for production deployment
DATABASE_URL=postgresql://username:password@host:port/database
SECRET_KEY=your-super-secret-key-for-jwt-signing
FLASK_ENV=production
```

#### **Development Environment Variables**
```bash
# Optional for local development
SECRET_KEY=dev-secret-key
DEBUG=True
DATABASE_URL=sqlite:///library.db  # Uses SQLite locally
```

### 🔄 Deployment Process

#### **Automatic Deployment (Recommended)**
1. **Push to GitHub**: Changes automatically trigger deployment
2. **Build Process**: Render installs dependencies and builds application
3. **Health Check**: Automatic verification of successful deployment
4. **Go Live**: Updated application available immediately

#### **Manual Deployment**
1. Navigate to [Render Dashboard](https://dashboard.render.com)
2. Select "Library Database" service
3. Click **"Manual Deploy"** → **"Deploy latest commit"**
4. Monitor deployment logs for success confirmation

### 🛡️ Production Security Features

- **🔐 JWT Authentication**: Secure token-based authorization
- **🚫 Rate Limiting**: API protection against abuse
- **🔒 Password Hashing**: Bcrypt encryption for user passwords
- **🌐 HTTPS Only**: All traffic encrypted in transit
- **🚪 CORS Configuration**: Controlled cross-origin access
- **📊 Request Logging**: Comprehensive audit trail

## 🤝 Contributing to the Project

We welcome contributions from developers of all skill levels! Here's how you can help improve the Library Management System:

### 📋 Contribution Guidelines

#### **🚀 Getting Started**
1. **Fork the Repository**
   ```bash
   # Click the "Fork" button on GitHub, then clone your fork
   git clone https://github.com/YOUR-USERNAME/Library-DataBase.git
   cd Library-DataBase
   ```

2. **Set Up Development Environment**
   ```bash
   # Create and activate virtual environment
   python -m venv .venv
   .venv\Scripts\activate

   # Install dependencies
   pip install -r requirements.txt
   ```

3. **Create Feature Branch**
   ```bash
   # Create a descriptive branch name
   git checkout -b feature/add-book-ratings
   git checkout -b bugfix/login-validation
   git checkout -b docs/update-api-examples
   ```

#### **💻 Development Workflow**
1. **Make Your Changes**
   - Write clean, commented code
   - Follow existing code style and patterns
   - Add tests for new functionality
   - Update documentation as needed

2. **Test Your Changes**
   ```bash
   # Run the application locally
   python flask_app.py
   
   # Test all endpoints in Swagger UI
   # Verify no existing functionality is broken
   ```

3. **Commit Your Work**
   ```bash
   # Stage your changes
   git add .
   
   # Write descriptive commit messages
   git commit -m "Add book rating system with 1-5 star validation"
   ```

4. **Submit Pull Request**
   ```bash
   # Push to your fork
   git push origin feature/your-feature-name
   
   # Create pull request on GitHub with:
   # - Clear description of changes
   # - Screenshots if UI changes
   # - Reference to any related issues
   ```

### 🎯 Areas for Contribution

<table>
<tr>
<td width="50%">

#### **🔧 Backend Enhancements**
- [ ] Add book rating system
- [ ] Implement due date tracking
- [ ] Add email notifications
- [ ] Create data export features
- [ ] Improve error handling
- [ ] Add logging system

</td>
<td width="50%">

#### **📚 Documentation**
- [ ] API usage examples
- [ ] Video tutorials
- [ ] Deployment guides
- [ ] Troubleshooting section
- [ ] Translation to other languages
- [ ] Code comments improvement

</td>
</tr>
<tr>
<td width="50%">

#### **🧪 Testing & Quality**
- [ ] Unit test coverage
- [ ] Integration tests
- [ ] Performance testing
- [ ] Security auditing
- [ ] Code quality tools
- [ ] Automated testing pipeline

</td>
<td width="50%">

#### **🌟 New Features**
- [ ] Member photo uploads
- [ ] Book cover images
- [ ] Advanced search filters
- [ ] Reporting dashboard
- [ ] Mobile-responsive frontend
- [ ] Book recommendation engine

</td>
</tr>
</table>

### 🏆 Recognition

All contributors will be:
- ✅ Listed in our **Contributors** section
- ✅ Credited in release notes
- ✅ Invited to our contributor community
- ✅ Eligible for recommendation letters

### 📞 Questions?

- 💬 **Discussions**: Use GitHub Discussions for questions
- 🐛 **Bug Reports**: Create detailed GitHub Issues
- 💡 **Feature Requests**: Share your ideas in Issues
- 📧 **Direct Contact**: Reach out via GitHub profile

---

## 📄 License & Legal

### 📜 MIT License

```
MIT License

Copyright (c) 2025 Jacob Davis

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### ⚖️ Third-Party Licenses

This project uses several open-source libraries. See individual package licenses for details:
- **Flask**: BSD-3-Clause License
- **SQLAlchemy**: MIT License  
- **PostgreSQL**: PostgreSQL License
- **JWT**: MIT License

---

## 👨‍💻 Project Team

<div align="center">

### **Jacob Dyson**
*Lead Developer & System Architect*

[![GitHub](https://img.shields.io/badge/GitHub-Jacobd1615-black?style=for-the-badge&logo=github)](https://github.com/Jacobd1615)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/jacob-davis)
[![Email](https://img.shields.io/badge/Email-Contact-red?style=for-the-badge&logo=gmail)](mailto:jacob@example.com)

*"Building robust, scalable solutions for modern library management"*

---

### 🙏 Acknowledgments

Special thanks to:
- **Flask Community** for the incredible framework
- **Render Platform** for reliable hosting
- **PostgreSQL Team** for the robust database system
- **Open Source Community** for continuous inspiration

</div>

---

<div align="center">

## 🎯 Ready to Transform Library Management?

### **🚀 Get Started Now!**

**For Users:**
[![Explore API](https://img.shields.io/badge/Explore_API-Live_Demo-green?style=for-the-badge&logo=swagger)](https://library-database-ja0b.onrender.com/api/docs)

**For Developers:**
[![Fork Repository](https://img.shields.io/badge/Fork_Repository-Contribute-blue?style=for-the-badge&logo=github)](https://github.com/Jacobd1615/Library-DataBase/fork)

**For Supporters:**
[![Star Repository](https://img.shields.io/badge/⭐_Star_Repository-Show_Support-yellow?style=for-the-badge&logo=github)](https://github.com/Jacobd1615/Library-DataBase)

---

*Built with ❤️ using Flask • Deployed on 🌐 Render • Documented with 📖 Swagger*

**© 2025 Library Management System - Revolutionizing Library Operations**

</div>
https://api.render.com/deploy/srv-d1vpi9idbo4c73fork0g?key=s3mH2RtNVcY
rnd_846s8w3Js2wYDJiw7c8bpo1NrSad