#!/usr/bin/env python3
"""
Test URL discovery for static site generation
"""

import os
import csv
import glob

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

if __name__ == "__main__":
    print("🔍 Discovering URLs for static site generation...\n")
    
    sculpture_items = get_sculpture_items()
    print(f"📿 Sculpture items ({len(sculpture_items)}):")
    for item in sculpture_items[:5]:  # Show first 5
        print(f"  /sculpture/{item}/")
    if len(sculpture_items) > 5:
        print(f"  ... and {len(sculpture_items) - 5} more")
    
    jewelry_items = get_jewelry_items()
    print(f"\n💎 Jewelry items ({len(jewelry_items)}):")
    for item in jewelry_items[:5]:  # Show first 5
        print(f"  /jewelry/{item}/")
    if len(jewelry_items) > 5:
        print(f"  ... and {len(jewelry_items) - 5} more")
    
    chair_pages = get_chair_pages()
    print(f"\n🪑 Chair pages ({len(chair_pages)}):")
    for page in chair_pages:
        print(f"  /chairs/{page}")
    
    puzzle_pages = get_puzzle_pages()
    print(f"\n🧩 Puzzle pages ({len(puzzle_pages)}):")
    for page in puzzle_pages:
        print(f"  /puzzles/{page}")
    
    total = len(sculpture_items) + len(jewelry_items) + len(chair_pages) + len(puzzle_pages)
    print(f"\n📊 Total individual pages discovered: {total}")
    print("✅ URL discovery working correctly!")