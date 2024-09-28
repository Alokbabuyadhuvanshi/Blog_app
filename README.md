

---

# Blog_app

**Blog_app** is a web application built using Django, HTML, and CSS that allows users to create, edit, and manage blog posts.
The application includes features like user authentication, post creation, editing, deletion, and viewing. Users can also 
view posts of other users.

# ckeckout the demonstration [video](https://drive.google.com/file/d/15mXRau-jYz3z980YsvYTWyooZzfvNhxX/view?usp=sharing)

## Features

- **User Authentication**
  - User registration, login, and logout functionality.
  - Profile management for users.
  
- **Blog Management**
  - Create, edit, and delete blog posts.
  - View a list of all blog posts.
  - View individual blog post details.

- **Responsive Design**
  - The application is styled using CSS to ensure responsiveness and user-friendly navigation on different devices.

## Requirements

- Python 3.12 or later
- Django 5.1 or later
- SQLite3 (default database for Django)
- HTML, CSS

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Alokbabuyadhuvanshi/Blog_app.git
   cd Blog_app
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

6. **Open the application**:
   - Visit `http://127.0.0.1:8000/` in your web browser.

## Project Structure

```plaintext
Blog_app/
│
├── blog_app/               # Project configuration folder
│   ├── __pycache__/        # Compiled Python files
│   ├── asgi.py             # ASGI configuration
│   ├── settings.py         # Django settings for the project
│   ├── urls.py             # URL routing for the project
│   ├── wsgi.py             # WSGI configuration for deployment
│   └── __init__.py         # Project initialization file
│
├── core/                   # Main application folder containing views, models, etc.
│   ├── __pycache__/        # Compiled Python files
│   ├── migrations/         # Database migration files
│   ├── templates/          # HTML templates
│   ├── admin.py            # Admin panel configurations
│   ├── apps.py             # App configuration
│   ├── forms.py            # Forms used in the app
│   ├── models.py           # Database models
│   ├── tests.py            # Automated tests
│   ├── urls.py             # URL routing for the core app
│   ├── views.py            # View functions
│   └── __init__.py         # App initialization file
│
├── media/images/           # Directory for user-uploaded images
│
├── static/                 # Static files (CSS, images, etc.)
│
├── templates/              # Base templates for the entire project
│
├── db.sqlite3              # SQLite database file
│
├── manage.py               # Django management script
│
├── requirements.txt        # Python dependencies
│
└── .gitignore              # Git ignore file
```

## Usage

- **Register a new user**:
  - Click on "Sign Up" and fill out the registration form.
  
- **Login**:
  - After registration, log in with your credentials to access the blog management features.

- **Create a new blog post**:
  - Navigate to "Create Post" and fill out the form to publish a new blog entry.

- **Edit or delete posts**:
  - Manage your posts from the dashboard where you can edit or delete them.

## Contributing

If you would like to contribute to the project, please fork the repository and submit a pull request. Contributions are
welcome!

## Contact

For any queries, please contact:

- **Alok Babu**  
  - Email: alokbabuyadhuvanshi@gmail.com
  - LinkedIn: [Alok Babu](https://www.linkedin.com/in/alok-babu-8a7619269)
  - GitHub: [Alok Babu](https://github.com/Alokbabuyadhuvanshi)

---

