# Static Site for https://charlesperry.com

This is the converted Django application to a static website that can be hosted anywhere without requiring Python or Django.

## Quick Start

### 1. Install Required Packages

```bash
pip install requests beautifulsoup4
```

### 2. Start Django Server

```bash
python manage.py runserver
```

### 3. Generate Static Site

In a new terminal window:

```bash
# Basic version (predefined pages only)
python generate_static.py

# Advanced version (discovers all pages automatically)
python generate_static_advanced.py
```

## Output

The static site will be generated in the `static_site/` directory:

## Features

### Basic Generator (`generate_static.py`)
- ✅ Crawls predefined important pages
- ✅ Downloads all media files
- ✅ Simple and fast
- ✅ Good for testing

### Advanced Generator (`generate_static_advanced.py`)
- ✅ **Automatically discovers all pages** from CSV data
- ✅ Crawls every individual sculpture and jewelry item
- ✅ Generates comprehensive site index
- ✅ Better error handling and progress reporting
- ✅ Complete static site with all content

## Hosting 

Once generated, you can host the static site GitHub Pages.

## Contact Form Solutions

For static sites, you can use:
- **Formspree**: External form service
- **EmailJS**: Client-side email sending
- **Google Forms**: Embed Google Forms

## Updating the Static Site

When you make changes, operate in the django5 branch and:

1. Update CSV data or templates
2. Start Django server: `python manage.py runserver`
3. Regenerate: `python generate_static_advanced.py`
4. Upload new `static_site/` contents to your host

## Troubleshooting

### "Cannot connect to server"
- Make sure Django server is running on http://localhost:8000
- Check that all required packages are installed

### "404 errors during generation"
- Some URLs might not exist - this is normal
- Check CSV data for invalid `key_name` values

### "Missing media files"
- Ensure `media/` directory exists with images
- Check file permissions

### "Broken links in static site"
- Static site uses relative paths
- Test locally by opening `static_site/index.html`

## Performance Tips

- The advanced generator can create 100+ pages
- Large CSV files will generate more pages
- Generation takes 1-2 minutes for full site
- Use basic generator for quick testing