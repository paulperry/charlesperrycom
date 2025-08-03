# Static Site Generation

Convert your Django application to a static website that can be hosted anywhere without requiring Python or Django.

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

```
static_site/
├── index.html                    # Homepage
├── sculpture/
│   ├── index.html               # Main sculpture gallery
│   ├── style/index.html         # Browse by style
│   ├── ribbed/index.html        # Ribbed sculptures
│   ├── cantata/index.html       # Individual sculpture pages
│   └── ...
├── jewelry/
│   ├── index.html               # Jewelry collection
│   ├── pendants/index.html      # Pendants
│   └── ...
├── media/                       # All images, CSS, JS files
│   ├── sculpture/
│   ├── jewelry/
│   └── ...
└── site-index.html              # Complete page listing
```

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

## Hosting Options

Once generated, you can host the static site on:

### Free Hosting
- **GitHub Pages**: Push `static_site/` contents to gh-pages branch
- **Netlify**: Drag and drop the `static_site/` folder
- **Vercel**: Deploy the `static_site/` directory
- **Firebase Hosting**: Upload to Firebase

### Traditional Hosting
- **Any web server**: Upload files via FTP/SFTP
- **CDN**: CloudFront, CloudFlare Pages
- **Shared hosting**: Most providers support static files

## Example Deployment

### GitHub Pages
```bash
# After generating static site
cd static_site
git init
git add .
git commit -m "Static site"
git branch -M gh-pages
git remote add origin YOUR_REPO_URL
git push -u origin gh-pages
```

### Netlify
1. Generate static site: `python generate_static_advanced.py`
2. Go to [netlify.com](https://netlify.com)
3. Drag and drop the `static_site/` folder
4. Your site is live!

## Benefits of Static Site

- ✅ **No server required** - just HTML, CSS, JS
- ✅ **Fast loading** - no database queries
- ✅ **Cheap hosting** - many free options
- ✅ **High availability** - served from CDN
- ✅ **Secure** - no server-side vulnerabilities
- ✅ **Easy backup** - just copy files

## Limitations

- ❌ **No contact forms** - forms won't work without backend
- ❌ **No dynamic content** - content is frozen at generation time
- ❌ **Manual updates** - need to regenerate after changes

## Contact Form Solutions

For static sites, you can use:
- **Netlify Forms**: Built-in form handling
- **Formspree**: External form service
- **EmailJS**: Client-side email sending
- **Google Forms**: Embed Google Forms

## Updating the Static Site

When you make changes:

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