#!/bin/bash

export NODE_TLS_REJECT_UNAUTHORIZED=0

AUTH="elastic:LIrp1J5ryZ9=oBgfzhro"
HOST="localhost:9200"
INDEXES=("authors_data" "book_links" "books_data_bis" "meta_collections_indice" "password_resets" "sessions" "user_collections" "user_likes" "users")

for index in "${INDEXES[@]}"; do
  echo "Dumping $index..."
  elasticdump \
    --input="https://${AUTH}@${HOST}/${index}" \
    --output="${index}.json" \
    --type=data \
    --limit=10000 \
    --concurrency=2
done
