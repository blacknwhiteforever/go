import json
import random

# 50+ Unique and Fresh Unsplash Image IDs (Fashion, Tech, Aesthetic)
image_ids = [
    "photo-1515886657613-9f3515b0c78f", "photo-1539008835657-9e8e9680c956", 
    "photo-1483985988355-763728e1935b", "photo-1524504388940-b1c1722653e1", 
    "photo-1506794778202-cad84cf45f1d", "photo-1494790108377-be9c29b29330", 
    "photo-1534528741775-53994a69daeb", "photo-1517841905240-472988babdf9", 
    "photo-1529626455594-4ff0802cfb7e", "photo-1531746020798-e6953c6e8e04", 
    "photo-1500917293891-ef795e70e1f6", "photo-1524250502761-1ac6f2e30d43", 
    "photo-1517365830460-955ce3ccd263", "photo-1544005313-94ddf0286df2", 
    "photo-1508214751196-bcfd4ca60f91", "photo-1518770660439-4636190af475", 
    "photo-1526374965328-7f61d4dc18c5", "photo-1550751827-4bd374c3f58b", 
    "photo-1519389950473-47ba0277781c", "photo-1498050108023-c5249f4df085", 
    "photo-1555066931-4365d14bab8c", "photo-1611186871348-b1ce696e52c9", 
    "photo-1523275335684-37898b6baf30", "photo-1511707171634-5f897ff02aa9", 
    "photo-1583394838336-acd977736f90", "photo-1499750310107-5fef28a66643", 
    "photo-1486406146926-c627a92ad1ab", "photo-1556761175-5973dc0f32e7", 
    "photo-1522202176988-66273c2fd55f", "photo-1512413914633-b5043f4041ea", 
    "photo-1611162617474-5b21e879e113", "photo-1507679799987-c73779587ccf",
    "photo-1531297172864-822d1fe1d378", "photo-1492562080023-ab3db95bfbce",
    "photo-1521119989659-a83eee488004", "photo-1580489944761-15a19d654956",
    "photo-1507003211169-0a1dd7228f2d", "photo-1519085360753-af0119f7cbe7",
    "photo-1500648767791-00dcc994a43e", "photo-1539571696357-5a69c17a67c6",
    "photo-1497366216548-37526070297c", "photo-1524758631624-e2822e304c36",
    "photo-1555421689-491a97ff2040", "photo-1516321318423-f06f85e504b3",
    "photo-1454165804606-c3d57bc86b40", "photo-1512314889357-e157c22f938d",
    "photo-1556761175-b413da4baf72", "photo-1504384308090-c894fdcc538d",
    "photo-1487014679447-9f8336841d58", "photo-1499951360447-b19be8fe80f5"
]

tags = ["fashion", "tech", "aesthetic", "lifestyle", "portrait", "design", "style"]
titles = ["Premium Look", "Modern Tech", "Minimalist Vibe", "Street Style", "Elegant Portrait", "Dark Aesthetic", "Creative Design", "Urban Life"]

photos = []
# Loop through unique IDs to create non-duplicated entries
for i, img_id in enumerate(image_ids):
    # URL optimized for fast mobile loading
    url = f"https://images.unsplash.com/{img_id}?q=80&w=600&auto=format&fit=crop"
    
    photos.append({
        "id": f"bnw_new_{i}",
        "img": url,
        "title": f"{random.choice(titles)} {i+1}",
        "tag": random.choice(tags),
        "author": "Unsplash",
        "author_link": "https://unsplash.com"
    })

with open('photos.json', 'w') as f:
    json.dump(photos, f, indent=2)

print(f"✅ Successfully generated photos.json with {len(photos)} totally UNIQUE Unsplash images!")
