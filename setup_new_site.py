#!/usr/bin/env python3
"""
Setup script for new modern website
Copies content from static_site and creates additional pages
"""

import os
import shutil
from pathlib import Path

def ensure_dir(path):
    """Ensure directory exists"""
    os.makedirs(path, exist_ok=True)

def setup_new_site():
    """Setup the new modern website"""
    print("🚀 Setting up modern Charles O. Perry website...")
    
    # Create directory structure
    directories = [
        'new_site/sculpture',
        'new_site/jewelry', 
        'new_site/puzzles',
        'new_site/chairs',
        'new_site/bio',
        'new_site/css',
        'new_site/js'
    ]
    
    for directory in directories:
        ensure_dir(directory)
    
    # Copy media files from static_site if it exists
    if os.path.exists('static_site/media'):
        print("📁 Copying media files...")
        if os.path.exists('new_site/media'):
            shutil.rmtree('new_site/media')
        shutil.copytree('static_site/media', 'new_site/media')
        print("✅ Media files copied")
    else:
        print("⚠️  static_site/media not found - run generate_static_advanced.py first")
        
        # Copy from Django media directory as fallback
        if os.path.exists('media'):
            print("📁 Copying from Django media directory...")
            if os.path.exists('new_site/media'):
                shutil.rmtree('new_site/media')
            shutil.copytree('media', 'new_site/media')
            print("✅ Media files copied from Django directory")
    
    # Copy HTML files from static_site if available
    if os.path.exists('static_site'):
        print("📄 Copying HTML content...")
        
        # Copy sculpture pages
        if os.path.exists('static_site/sculpture'):
            shutil.copytree('static_site/sculpture', 'new_site/sculpture', dirs_exist_ok=True)
        
        # Copy jewelry pages
        if os.path.exists('static_site/jewelry'):
            shutil.copytree('static_site/jewelry', 'new_site/jewelry', dirs_exist_ok=True)
            
        # Copy puzzle pages
        if os.path.exists('static_site/puzzles'):
            shutil.copytree('static_site/puzzles', 'new_site/puzzles', dirs_exist_ok=True)
            
        # Copy chair pages
        if os.path.exists('static_site/chairs'):
            shutil.copytree('static_site/chairs', 'new_site/chairs', dirs_exist_ok=True)
            
        # Copy bio pages
        if os.path.exists('static_site/bio'):
            shutil.copytree('static_site/bio', 'new_site/bio', dirs_exist_ok=True)
        
        print("✅ HTML content copied")
    else:
        print("⚠️  static_site directory not found")
        print("   Run 'python generate_static_advanced.py' first to generate content")
    
    print(f"\n🎉 New modern website setup complete!")
    print(f"📁 Location: new_site/")
    print(f"🌐 Open new_site/index.html in your browser to view")
    
    # Check what was created
    if os.path.exists('new_site/index.html'):
        print("\n📋 Created files:")
        print("  ✅ index.html (modern homepage)")
        print("  ✅ css/main.css (modern styling)")
        print("  ✅ js/main.js (interactive features)")
        
        if os.path.exists('new_site/media'):
            media_count = sum([len(files) for _, _, files in os.walk('new_site/media')])
            print(f"  ✅ media/ ({media_count} files)")
        
        if os.path.exists('new_site/sculpture'):
            print("  ✅ sculpture/ (gallery pages)")
        if os.path.exists('new_site/jewelry'):
            print("  ✅ jewelry/ (collection pages)")
            
    return True

if __name__ == "__main__":
    if setup_new_site():
        print("\n✨ Setup completed successfully!")
        print("\nTo view the new website:")
        print("1. Open new_site/index.html in your browser")
        print("2. Or serve with: python -m http.server 8080 --directory new_site")
    else:
        print("\n❌ Setup failed")
        exit(1)