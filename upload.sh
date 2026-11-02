#!/data/data/com.termux/files/usr/bin/bash

API_KEY="ea671002a611b7840bd420a21a42c611"
JSON_FILE="photos.json"

echo "Enter image filename (e.g., image.jpg):"
read IMG_FILE

if [ ! -f "$IMG_FILE" ]; then
    echo "Error: File '$IMG_FILE' not found!"
    exit 1
fi

echo "Uploading to ImgBB..."

# Upload image and extract direct URL
RESPONSE=$(curl -s -X POST --data-binary @"$IMG_FILE" "https://api.imgbb.com/1/upload?key=$API_KEY")
IMG_URL=$(echo "$RESPONSE" | jq -r '.data.url')

if [ "$IMG_URL" == "null" ] || [ -z "$IMG_URL" ]; then
    echo "Upload failed. Response from server:"
    echo "$RESPONSE"
    exit 1
fi

echo "Upload Successful! URL: $IMG_URL"

# Add to photos.json dynamically
echo "Enter Title for this image:"
read IMG_TITLE
echo "Enter Tag (fashion, tech, aesthetic):"
read IMG_TAG

# Create new JSON object
NEW_DATA="{\"id\": \"p$(date +%s)\", \"img\": \"$IMG_URL\", \"title\": \"$IMG_TITLE\", \"tag\": \"$IMG_TAG\", \"author\": \"BnW Team\", \"author_link\": \"#\"}"

# Use jq to append to existing array
jq ". += [$NEW_DATA]" "$JSON_FILE" > tmp.json && mv tmp.json "$JSON_FILE"

echo "Data successfully added to $JSON_FILE!"
