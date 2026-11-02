import json
import random

# 20 High-Quality Unsplash Image IDs (Fashion, Tech, Aesthetic)
image_ids = [
    "photo-1515886657613-9f3515b0c78f", "photo-1539008835657-9e8e9680c956",
    "photo-1483985988355-763728e1935b", "photo-1523275335684-37898b6baf30",
    "photo-1494790108377-be9c29b29330", "photo-1511707171634-5f897ff02aa9",
    "photo-1550614000-4b95d858288a", "photo-1512413914633-b5043f4041ea",
    "photo-1611162617474-5b21e879e113", "photo-1518770660439-4636190af475",
    "photo-1499750310107-5fef28a66643", "photo-1486406146926-c627a92ad1ab",
    "photo-1556761175-5973dc0f32e7", "photo-1522202176988-66273c2fd55f",
    "photo-1531297172864-822d1fe1d378", "photo-1507679799987-c73779587ccf",
    "photo-1524504388940-b1c1722653e1", "photo-1506794778202-cad84cf45f1d",
    "photo-1492562080023-ab3db95bfbce", "photo-1534528741775-53994a69daeb"
]

tags = ["fashion", "tech", "aesthetic", "lifestyle", "portrait", "nature", "gadgets", "style"]
titles = ["Classic Look", "Tech Gadget", "Minimalist Vibe", "Street Style", "Elegant Portrait", "Dark Aesthetic", "Modern Design", "Urban Life"]

photos = []
for i in range(200):
    img_id = image_ids[i % len(image_ids)]
    
    # Direct Unsplash Link with 'sig' parameter to load a fresh image every time
    url = f"https://images.unsplash.com/{img_id}?q=80&w=800&auto=format&fit=crop&sig={i}"
    
    photos.append({
        "id": f"bnw_img_{i}",
        "img": url,
        "title": f"{random.choice(titles)} {i+1}",
        "tag": random.choice(tags),
        "author": "Unsplash Contributor",
        "author_link": "https://unsplash.com"
    })

with open('photos.json', 'w') as f:
    json.dump(photos, f, indent=2)

print("✅ Successfully generated photos.json with 200 Direct Unsplash images!")
