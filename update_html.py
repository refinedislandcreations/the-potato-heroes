import os
import re

def process_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # 1. Update image extensions
    replacements = [
        ('background-potato.png', 'background-potato.webp'),
        ('forgotten-greek-salad.jpeg', 'forgotten-greek-salad.webp'),
        ('banana-malt.jpeg', 'banana-malt.webp'),
        ('apple-tart.jpeg', 'apple-tart.webp'),
        ('potato1.jpg', 'potato1.webp')
    ]
    for old, new in replacements:
        content = content.replace(old, new)

    # 2. Update favicon in head.html
    if 'head.html' in filepath:
        old_favicon = '<link rel="icon" href="{{ \'/assets/images/favicon.png\' | relative_url }}" />'
        new_favicon = '<link rel="icon" type="image/png" sizes="32x32" href="{{ \'/assets/images/favicon-32x32.png\' | relative_url }}" />\n<link rel="icon" type="image/png" sizes="192x192" href="{{ \'/assets/images/favicon-192x192.png\' | relative_url }}" />'
        content = content.replace(old_favicon, new_favicon)

    # 3. Add loading="lazy" decoding="async" to img tags
    # We will use a regex to find all <img ...> tags.
    # We skip adding lazy if it already has loading=
    # We also skip adding lazy to hero/loader images.
    
    # Eager classes/IDs or source patterns to skip
    eager_patterns = [
        'class="absolute inset-0 h-full w-full object-cover"', # typical hero backgrounds
        'id="hero',
        'entry-screen__logo',
        'loader__logo',
        'brand-panel__image',
        'logo-potato-heroes.svg' # navbar logos usually shouldn't be lazy
    ]

    def img_replacer(match):
        img_tag = match.group(0)
        
        # If it already has loading=, leave it alone
        if 'loading=' in img_tag:
            return img_tag
            
        # Check if it should be eager
        for pattern in eager_patterns:
            if pattern in img_tag:
                return img_tag
                
        # Insert loading="lazy" decoding="async" right after <img
        return img_tag.replace('<img', '<img loading="lazy" decoding="async"', 1)

    content = re.sub(r'<img[^>]+>', img_replacer, content)

    with open(filepath, 'w') as f:
        f.write(content)

# Traverse directory
for root, dirs, files in os.walk('.'):
    if '_site' in root or '.git' in root or 'node_modules' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            process_file(os.path.join(root, file))

print("HTML files updated.")
