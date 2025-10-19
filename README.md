# Blogged - Django Blog Application

A modern, full-featured blog application built with Django 5.2.7 and deployed on Render.

🌐 **Live Demo**: [https://blogged-vrd6.onrender.com](https://blogged-vrd6.onrender.com)

## Features

- 📝 Create, read, update, and delete blog posts
- 💬 Comment system for reader engagement
- 📧 Contact form for visitor inquiries
- 🎨 Clean and responsive design
- 🔐 Admin panel for content management
- 🚀 Production-ready deployment on Render

## Tech Stack

- **Backend**: Django 5.2.7
- **Database**: PostgreSQL (production), SQLite (development)
- **Server**: Gunicorn
- **Static Files**: WhiteNoise
- **Hosting**: Render
- **Version Control**: Git/GitHub

## Project Structure

```
blogged/
├── blog/                   # Main blog application
│   ├── models.py          # Database models (Post, Comment)
│   ├── views.py           # View functions
│   ├── urls.py            # URL routing
│   ├── forms.py           # Forms for contact and comments
│   ├── admin.py           # Admin panel configuration
│   └── templates/         # HTML templates
│       └── blog/
│           ├── base.html
│           ├── index.html
│           ├── detail.html
│           └── contact.html
├── blogged/               # Project configuration
│   ├── settings.py        # Django settings
│   ├── urls.py            # Main URL configuration
│   └── wsgi.py            # WSGI configuration
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── Procfile              # Render deployment configuration
└── .env.example          # Environment variables template
```

## Local Development Setup

### Prerequisites

- Python 3.12+
- pip
- virtualenv (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/khalludi03/blogged.git
   cd blogged
   ```

2. **Create and activate virtual environment**
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your configuration
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

8. **Run the development server**
   ```bash
   python manage.py runserver
   ```

9. **Access the application**
   - Homepage: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Deployment to Render

### Prerequisites

- GitHub account
- Render account (free tier works)
- PostgreSQL database on Render

### Deployment Steps

1. **Push code to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Create PostgreSQL Database on Render**
   - Go to [Render Dashboard](https://dashboard.render.com/)
   - Click "New" → "PostgreSQL"
   - Name: `blogged-db`
   - Plan: Free
   - Copy the "Internal Database URL"

3. **Create Web Service on Render**
   - Click "New" → "Web Service"
   - Connect your GitHub repository
   - Configure:
     - **Name**: blogged
     - **Environment**: Python
     - **Build Command**: 
       ```bash
       pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput
       ```
     - **Start Command**: 
       ```bash
       gunicorn blogged.wsgi:application
       ```

4. **Set Environment Variables**
   Add these in Render's Environment tab:
   - `DJANGO_SECRET_KEY`: Generate a secure random string
   - `DJANGO_DEBUG`: `False`
   - `DATABASE_URL`: Paste your PostgreSQL Internal Database URL

5. **Deploy**
   - Click "Create Web Service"
   - Wait for deployment to complete
   - Visit your app at the provided URL

### Post-Deployment

To create an admin user on Render (free tier without shell access):

Temporarily update the Build Command to include:
```bash
pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput && echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'your-strong-password')" | python manage.py shell
```

Then revert to the normal build command after deployment.

## Environment Variables

Create a `.env` file for local development:

```env
DJANGO_SECRET_KEY=your-secret-key-here
DJANGO_DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

For production (Render):

```env
DJANGO_SECRET_KEY=your-production-secret-key
DJANGO_DEBUG=False
DATABASE_URL=postgres://user:password@host:port/database
```

## Usage

### Admin Panel

1. Access the admin panel at `/admin/`
2. Log in with your superuser credentials
3. Create new blog posts
4. Manage comments
5. View contact form submissions

### Blog Posts

- Posts are displayed on the homepage
- Click any post to view full details
- Readers can leave comments (if enabled)

### Contact Form

- Accessible at `/contact/`
- Visitors can send messages
- Submissions are stored in the database

## Development

### Running Tests

```bash
python manage.py test
```

### Making Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Creating a New App

```bash
python manage.py startapp app_name
```

## Dependencies

- Django==5.2.7
- gunicorn==23.0.0
- whitenoise==6.11.0
- dj-database-url==3.0.1
- psycopg[binary]==3.2.10

See `requirements.txt` for the complete list.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

**Khalludi**
- GitHub: [@khalludi03](https://github.com/khalludi03)

## Acknowledgments

- Django documentation and community
- Render for hosting
- All contributors and users

## Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check the [Django documentation](https://docs.djangoproject.com/)
- Review [Render deployment docs](https://render.com/docs/deploy-django)

---

⭐ If you find this project helpful, please consider giving it a star!
