
# Flask Learning Journey 🚀

## PHASE 1

This repository documents my journey of learning **Flask**, one concept at a time.

I'm currently exploring backend development alongside Machine Learning to strengthen my full-stack development skills.

## 📚 Topics Covered

- ✅ Flask Installation
- ✅ Routing
- ✅ GET & POST Requests
- ✅ Forms
- ✅ Redirects
- ✅ Sessions
- ✅ Login Authentication (Basic)

## 📂 Current Project

### Basic Login System

Features:
- Login page
- Username & Password validation
- Session handling
- Redirect after successful login
- Logout functionality

Credentials:

Username: admin
Password: 123


##  Phase 2 – Flask Templates & Frontend Integration (login_1.1)

### 📚 Topics Covered

#### 📝 Jinja2 Templating
- Render dynamic HTML using `render_template()`
- Pass variables from Flask to HTML templates
- Use Jinja2 syntax:
  - `{{ }}` for variables
  - `{% %}` for control statements (loops, conditions, blocks)

#### 🏗️ Template Inheritance
- Create a reusable `base.html` layout
- Extend base templates using `{% extends %}`
- Define and override sections with `{% block %}`
- Reduce code duplication across multiple pages

#### 🌐 HTML Integration
- Organize HTML files inside the `templates/` directory
- Create multiple web pages
- Connect pages using Flask routes

#### 🎨 CSS Integration
- Serve static files from the `static/` directory
- Link CSS using:
  ```html
  <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
  ```
- Apply custom styling to Flask web pages

## 🛠 Tech Stack

- Python
- Flask

## 🎯 Goal

This repository is intended to track my Flask learning progress from beginner to advanced.

Future topics include:

- Bootstrap Integration
- SQLite Database
- User Registration
- CRUD Applications
- REST APIs
- Deployment

---

 This repository will be updated regularly as I continue learning Flask.
