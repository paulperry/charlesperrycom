# Charles O. Perry - Artist Portfolio Website 

A Django-based portfolio website showcasing the sculpture, jewelry, puzzles, and chairs of artist Charles O. Perry. This site has been modernized to Django 5.x with a file-based data architecture.

## Features

- **Sculpture Gallery**: Browse sculptures by style (ribbed, planar, topological, solid) or material
- **Jewelry Collection**: View pendants, earrings, pins, and other jewelry pieces
- **Puzzle Showcase**: Interactive puzzles and chess sets
- **Chair Designs**: Industrial design furniture pieces
- **Contact Forms**: Contact and newsletter subscription functionality
- **Tour & Slideshow**: Interactive map tour and slideshow presentations

## Architecture

- **Framework**: Django 5.x
- **Data Storage**: File-based CSV data (no database required)
- **Authentication**: None (public portfolio site)
- **Email**: Django SMTP integration for contact forms

## Quick Start

### Prerequisites
- Python 3.8+
- pip

### Installation

1. **Clone the repository**:
```bash
git clone <repository-url>
cd charlesperrycom
```

2. **Install dependencies**:
```bash
pip install django
```

3. **Set up environment variables** (optional):
```bash
cp .env.example .env
# Edit .env with your values
```

4. **Run the development server**:
```bash
python manage.py runserver
```

5. **Visit the site**:
   - Main site: http://localhost:8000/

## Configuration

### Environment Variables

Create a `.env` file or set environment variables:

```bash
# Required for production
DJANGO_SECRET_KEY=your-secret-key-here
DEBUG=false

# Email configuration (for contact forms)
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL=noreply@charlesperry.com
```

### Email Setup

See [EMAIL_SETUP.md](EMAIL_SETUP.md) for detailed email configuration instructions.

## Data Structure

The site uses CSV files for data storage:

- `media/sculpture/art.csv` - Sculpture database
- `media/jewelry/jewelry.csv` - Jewelry collection
- `media/puzzles/puzzles.csv` - Puzzle designs

### Adding New Items

To add new sculptures, jewelry, or puzzles:

1. Add a new row to the appropriate CSV file
2. Add images to the corresponding media directory
3. The changes will appear immediately (no database migration needed)

## Key URLs

- `/` - Homepage
- `/sculpture/` - Main sculpture gallery
- `/sculpture/style/` - Browse by style
- `/sculpture/material/` - Browse by material
- `/sculpture/slideshow/` - Slideshow presentation
- `/sculpture/tour/` - Interactive map tour
- `/jewelry/` - Jewelry collection
- `/puzzles/` - Puzzle designs
- `/chairs/` - Chair furniture
- `/bio/` - About the artist
- `/bio/contact/` - Contact form

## Development

### Running in Development

```bash
# Start development server
python manage.py runserver

# View emails in console (no SMTP needed)
# Contact forms will print to terminal
```

### File-Based Data System

The site uses CSV files instead of a traditional database:

- **Benefits**: No database setup, easy data management, version controllable
- **Data Loading**: CSV files are read on each request
- **Performance**: Suitable for small datasets (hundreds of items)
- **Legacy Models**: Django model files (`models.py`) are preserved but not used. They could be reactivated for future database integration if needed.

### Adding New Features

1. **New Data Types**: Add CSV file and create corresponding item class
2. **New Views**: Follow existing patterns in app views.py files
3. **Templates**: Extend base templates for consistent styling

## Deployment

### Production Checklist

- [ ] Generate new `DJANGO_SECRET_KEY`
- [ ] Set `DEBUG=false`
- [ ] Configure email settings
- [ ] Set up web server (nginx/Apache) for static files
- [ ] Configure HTTPS
- [ ] Set proper file permissions

### Example Production Settings

```bash
export DJANGO_SECRET_KEY="your-generated-secret-key"
export DEBUG=false
export EMAIL_HOST_USER="production-email@domain.com"
export EMAIL_HOST_PASSWORD="app-specific-password"
export DEFAULT_FROM_EMAIL="noreply@charlesperry.com"
```

## Migration History

This site was migrated from Google App Engine to modern Django:

- **Original**: GAE Python 2.7 with webapp2 framework
- **Converted**: Django 5.x with Python 3.8+
- **Database**: Migrated from GAE Datastore to CSV files
- **Authentication**: Removed (was admin-only, now public)
- **Email**: Converted from GAE Mail API to Django SMTP

## Security

- Secret key moved to environment variables
- Debug mode configurable
- No user authentication (reduced attack surface)
- File-based data (no SQL injection risk)
- Minimal dependencies
- Proper email configuration

## Performance

- **Data Loading**: CSV files loaded on each request
- **Caching**: None implemented (suitable for low-traffic portfolio site)
- **Static Files**: Served by Django in development, should use web server in production

## Browser Support

- Modern browsers (Chrome, Firefox, Safari, Edge)
- Mobile responsive design

## License

&copy; 2000-2025 Charles O. Perry. All rights reserved.

## Support

For technical issues or questions about the artist's work, use the contact form at `/bio/contact/`.
