#!/usr/bin/env python3
"""
Static Site Generator for Charles Perry Website
Crawls the Django application and saves static HTML files
"""

import os
import sys
import requests
from urllib.parse import urljoin, urlparse
from pathlib import Path
import time

# Base URL of your Django development server
BASE_URL = "http://localhost:8000"
OUTPUT_DIR = "static_site"

# URLs to crawl - add more as needed
URLS_TO_CRAWL = [
    "/",
    "/sculpture/",
    "/sculpture/style/",
    "/sculpture/material/",
    "/sculpture/list/",
    "/sculpture/all/",
    "/sculpture/tour/",
    "/sculpture/slideshow/",
    "/sculpture/style/ribbed/",
    "/sculpture/style/planar/",
    "/sculpture/style/topological/",
    "/sculpture/style/solid/",
    "/sculpture/material/aluminum/",
    "/sculpture/material/bronze/",
    "/sculpture/material/steel/",
    "/sculpture/material/stainlesssteel/",
    "/sculpture/material/other/",
    "/jewelry/",
    "/jewelry/pendants/",
    "/jewelry/earrings/",
    "/jewelry/pins/",
    "/jewelry/other/",
    "/puzzles/",
    "/chairs/",
    "/bio/",
    "/bio/contact/",
]

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

def download_media_files(base_url, output_dir):
    """Download media files (CSS, JS, images)"""
    media_dir = os.path.join(output_dir, "media")
    ensure_dir(media_dir)
    
    # Copy media files from Django media directory
    import shutil
    django_media = "media"
    if os.path.exists(django_media):
        print("Copying media files...")
        shutil.copytree(django_media, media_dir, dirs_exist_ok=True)
        print(f"Media files copied to {media_dir}")

def generate_static_site():
    """Main function to generate static site"""
    print(f"Generating static site from {BASE_URL}")
    print(f"Output directory: {OUTPUT_DIR}")
    
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
    
    # Crawl and save pages
    for url_path in URLS_TO_CRAWL:
        full_url = urljoin(BASE_URL, url_path)
        try:
            print(f"Crawling: {full_url}")
            response = session.get(full_url)
            response.raise_for_status()
            
            # Save the page
            save_page(url_path, response.text, OUTPUT_DIR)
            
            # Small delay to be nice to the server
            time.sleep(0.1)
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Error crawling {full_url}: {e}")
            continue
    
    # Download media files
    download_media_files(BASE_URL, OUTPUT_DIR)
    
    print(f"\n✅ Static site generated in '{OUTPUT_DIR}' directory")
    print(f"Open {OUTPUT_DIR}/index.html in your browser to view the static site")
    
    return True

if __name__ == "__main__":
    if generate_static_site():
        print("\n🎉 Static site generation completed successfully!")
    else:
        print("\n❌ Static site generation failed")
        sys.exit(1)