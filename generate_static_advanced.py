#!/usr/bin/env python3
"""
Advanced Static Site Generator for Charles Perry Website
Dynamically discovers and crawls all pages including individual items
"""

import os
import sys
import requests
from urllib.parse import urljoin, urlparse
from pathlib import Path
import time
import re
from bs4 import BeautifulSoup
import csv
import glob

# Base URL of your Django development server
BASE_URL = "http://localhost:8000"
OUTPUT_DIR = "static_site"

def ensure_dir(path):
    """Ensure directory exists"""
    os.makedirs(path, exist_ok=True)

def save_page(url, content, output_dir):
    """Save HTML content to file"""
    parsed = urlparse(url)
    path = parsed.path
    
    # Convert URL path to file path
    if path == "/" or path == "":
        file_path = os.path.join(output_dir, "index.html")
    elif path.endswith("/"):
        file_path = os.path.join(output_dir, path.strip("/"), "index.html")
    else:
        file_path = os.path.join(output_dir, path.strip("/") + ".html")
    
    # Ensure directory exists
    ensure_dir(os.path.dirname(file_path))
    
    # Write HTML content
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Saved: {file_path}")
    return file_path

def get_sculpture_items():
    """Get all sculpture items from CSV"""
    items = []
    csv_path = "media/sculpture/art.csv"
    if os.path.exists(csv_path):
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get('key_name'):
                    items.append(row['key_name'])
    return items

def get_jewelry_items():
    """Get all jewelry items from CSV"""
    items = []
    csv_path = "media/jewelry/jewelry.csv"
    if os.path.exists(csv_path):
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get('key_name'):
                    items.append(row['key_name'])
    return items

def get_chair_pages():
    """Get chair pages from templates directory"""
    chair_templates = glob.glob("templates/chairs/*.html")
    pages = []
    for template in chair_templates:
        filename = os.path.basename(template)
        if filename != 'index.html':  # Skip index page
            page_name = filename.replace('.html', '')
            pages.append(page_name)
    return pages

def get_puzzle_pages():
    """Get puzzle pages from templates directory"""
    puzzle_templates = glob.glob("templates/puzzles/*.html")
    pages = []
    for template in puzzle_templates:
        filename = os.path.basename(template)
        if filename != 'index.html':  # Skip index page
            page_name = filename.replace('.html', '')
            pages.append(page_name)
    return pages

def generate_urls():
    """Generate comprehensive list of URLs to crawl"""
    urls = [
        # Main pages
        "/",
        "/sculpture/",
        "/sculpture/style/",
        "/sculpture/material/",
        "/sculpture/list/",
        "/sculpture/all/",
        "/sculpture/tour/",
        "/sculpture/slideshow/",
        
        # Sculpture by style
        "/sculpture/style/ribbed/",
        "/sculpture/style/planar/",
        "/sculpture/style/topological/",
        "/sculpture/style/solid/",
        
        # Sculpture by material
        "/sculpture/material/aluminum/",
        "/sculpture/material/bronze/",
        "/sculpture/material/steel/",
        "/sculpture/material/stainlesssteel/",
        "/sculpture/material/other/",
        
        # Jewelry pages
        "/jewelry/",
        "/jewelry/pendants/",
        "/jewelry/earrings/",
        "/jewelry/pins/",
        "/jewelry/other/",
        
        # Other sections
        "/puzzles/",
        "/chairs/",
        "/bio/",
        "/bio/contact/",
    ]
    
    # Add individual sculpture pages
    sculpture_items = get_sculpture_items()
    for item in sculpture_items:
        urls.append(f"/sculpture/{item}/")
    
    # Add individual jewelry pages
    jewelry_items = get_jewelry_items()
    for item in jewelry_items:
        urls.append(f"/jewelry/{item}/")
    
    # Add individual chair pages
    chair_pages = get_chair_pages()
    for page in chair_pages:
        urls.append(f"/chairs/{page}")
    
    # Add individual puzzle pages
    puzzle_pages = get_puzzle_pages()
    for page in puzzle_pages:
        urls.append(f"/puzzles/{page}")
    
    print(f"Generated {len(urls)} URLs to crawl")
    print(f"  - Sculpture items: {len(sculpture_items)}")
    print(f"  - Jewelry items: {len(jewelry_items)}")
    print(f"  - Chair pages: {len(chair_pages)}")
    print(f"  - Puzzle pages: {len(puzzle_pages)}")
    
    return urls

def copy_media_files(output_dir):
    """Copy media files to static site"""
    import shutil
    
    media_dir = os.path.join(output_dir, "media")
    django_media = "media"
    
    if os.path.exists(django_media):
        print("Copying media files...")
        if os.path.exists(media_dir):
            shutil.rmtree(media_dir)
        shutil.copytree(django_media, media_dir)
        print(f"✅ Media files copied to {media_dir}")
    else:
        print("⚠️  No media directory found")

def generate_static_site():
    """Main function to generate static site"""
    print(f"🚀 Generating static site from {BASE_URL}")
    print(f"📁 Output directory: {OUTPUT_DIR}")
    
    # Create output directory
    ensure_dir(OUTPUT_DIR)
    
    session = requests.Session()
    
    # Test if server is running
    try:
        response = session.get(BASE_URL)
        response.raise_for_status()
        print("✅ Django server is running")
    except requests.exceptions.RequestException as e:
        print(f"❌ Error: Cannot connect to {BASE_URL}")
        print("Make sure Django server is running with: python manage.py runserver")
        return False
    
    # Generate URLs to crawl
    urls_to_crawl = generate_urls()
    
    # Crawl and save pages
    successful = 0
    failed = 0
    
    for i, url_path in enumerate(urls_to_crawl, 1):
        full_url = urljoin(BASE_URL, url_path)
        try:
            print(f"[{i}/{len(urls_to_crawl)}] Crawling: {url_path}")
            response = session.get(full_url)
            
            if response.status_code == 404:
                print(f"⚠️  404 Not Found: {url_path}")
                failed += 1
                continue
                
            response.raise_for_status()
            
            # Save the page
            save_page(url_path, response.text, OUTPUT_DIR)
            successful += 1
            
            # Small delay to be nice to the server
            time.sleep(0.05)
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Error crawling {full_url}: {e}")
            failed += 1
            continue
    
    # Copy media files
    copy_media_files(OUTPUT_DIR)
    
    # Generate index of all pages
    generate_site_index(OUTPUT_DIR, urls_to_crawl)
    
    print(f"\n📊 Crawling completed:")
    print(f"   ✅ Successful: {successful}")
    print(f"   ❌ Failed: {failed}")
    print(f"   📁 Output: {OUTPUT_DIR}/")
    print(f"\n🎉 Static site generated successfully!")
    print(f"Open {OUTPUT_DIR}/index.html in your browser")
    
    return True

def generate_site_index(output_dir, urls):
    """Generate a site index page"""
    index_content = """<!DOCTYPE html>
<html>
<head>
    <title>Charles O. Perry - Site Index</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        h1 { color: #333; }
        ul { list-style-type: none; padding: 0; }
        li { margin: 5px 0; }
        a { color: #0066cc; text-decoration: none; }
        a:hover { text-decoration: underline; }
        .section { margin: 20px 0; }
    </style>
</head>
<body>
    <h1>Charles O. Perry - Static Site Index</h1>
    <p>This static site contains the following pages:</p>
    
    <div class="section">
        <h2>Main Sections</h2>
        <ul>
"""
    
    # Categorize URLs
    main_pages = [url for url in urls if url.count('/') <= 2 and not any(x in url for x in ['style/', 'material/'])]
    
    for url in sorted(main_pages):
        if url == "/":
            index_content += f'            <li><a href="index.html">Home</a></li>\n'
        else:
            link = url.strip('/').replace('/', '/index') + ('.html' if not url.endswith('/') else '/index.html')
            index_content += f'            <li><a href="{link}">{url}</a></li>\n'
    
    index_content += """        </ul>
    </div>
    
    <p><em>Generated by Charles Perry Static Site Generator</em></p>
</body>
</html>"""
    
    with open(os.path.join(output_dir, 'site-index.html'), 'w') as f:
        f.write(index_content)
    
    print("📋 Generated site-index.html")

if __name__ == "__main__":
    # Check if requests and beautifulsoup4 are available
    try:
        import requests
        from bs4 import BeautifulSoup
    except ImportError as e:
        print("❌ Missing required packages. Install with:")
        print("pip install requests beautifulsoup4")
        sys.exit(1)
    
    if generate_static_site():
        print("\n🎉 Static site generation completed successfully!")
    else:
        print("\n❌ Static site generation failed")
        sys.exit(1)