#!/bin/bash

API_KEY="ea671002a611b7840bd420a21a42c611"
JSON_FILE="photos.json"

# Unsplash Image URLs (Direct High-Res Links)
URLS=(
  "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?w=800"
  "https://images.unsplash.com/photo-1539008835657-9e8e9680c956?w=800"
  "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=800"
  "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=800"
  "https://images.unsplash.com/photo-1483985988355-763728e1935b?w=800"
  "https://images.unsplash.com/photo-1550614000-4b95d858288a?w=800"
)

# Titles and Tags
TITLES=("Classic Street Fashion" "Elegant White Dress" "Minimalist Watch" "Aesthetic Portrait" "Shopping Day" "Black & White Fashion")
TAGS=("fashion" "fashion" "tech" "aesthetic" "fashion" "fashion")

echo "[" > $JSON_FILE

for i in "${!URLS[@]}"; do
    echo "Downloading: ${TITLES[$i]}..."
    curl -sL "${URLS[$i]}" -o "temp_img.jpg"
    
    echo "Uploading to ImgBB..."
    RESPONSE=$(curl -s -X POST --data-binary @"temp_img.jpg" "https://api.imgbb.com/1/upload?key=$API_KEY")
    
    # Extract the direct image URL from ImgBB response
    IMG_URL=$(echo "$RESPONSE" | jq -r '.data.url')
    
    if [ "$IMG_URL" == "null" ] || [ -z "$IMG_URL" ]; then
        echo "Failed to upload ${TITLES[$i]}"
    else
        echo "Success! Link: $IMG_URL"
        # Create JSON entry
        echo "  {" >> $JSON_FILE
        echo "    \"id\": \"bnw_$i\"," >> $JSON_FILE
        echo "    \"img\": \"$IMG_URL\"," >> $JSON_FILE
        echo "    \"title\": \"${TITLES[$i]}\"," >> $JSON_FILE
        echo "    \"tag\": \"${TAGS[$i]}\"," >> $JSON_FILE
        echo "    \"author\": \"Unsplash via ImgBB\"," >> $JSON_FILE
        echo "    \"author_link\": \"#\"" >> $JSON_FILE
        # Add comma if not the last item
        if [ $i -lt $((${#URLS[@]} - 1)) ]; then
            echo "  }," >> $JSON_FILE
        else
            echo "  }" >> $JSON_FILE
        fi
    fi
    
    # Clean up temp image
    rm temp_img.jpg
done

echo "]" >> $JSON_FILE
echo "✅ All images uploaded and saved to $JSON_FILE!"
