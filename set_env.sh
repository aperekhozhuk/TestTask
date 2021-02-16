grep -v "^#" .env | while read -r line; do export "$line"; done
