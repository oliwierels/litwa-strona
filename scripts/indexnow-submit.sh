#!/usr/bin/env bash
# Praneša nurodytus URL adresus (arba numatytąjį pagrindinių puslapių rinkinį) IndexNow
# paslaugai (Bing / Yandex / Seznam).
#
# Naudojimas:  ./scripts/indexnow-submit.sh [url1 url2 ...]
# Paleiskite po kiekvieno diegimo į produkciją.
#
# PRIEŠ PIRMĄ PALEIDIMĄ: sugeneruokite savo IndexNow raktą ir įkelkite jį kaip
# https://33bots.lt/<RAKTAS>.txt (failo turinys — tas pats raktas).
KEY="${INDEXNOW_KEY:-}"
HOST="33bots.lt"

if [ -z "$KEY" ]; then
  echo "Nustatykite INDEXNOW_KEY aplinkos kintamąjį arba įrašykite raktą į šį skriptą." >&2
  exit 1
fi

URLS=("$@")
if [ ${#URLS[@]} -eq 0 ]; then
  URLS=(
    "https://33bots.lt/"
    "https://33bots.lt/humanoidinio-roboto-nuoma.html"
    "https://33bots.lt/robotas-renginiui.html"
    "https://33bots.lt/robotas-parodoms.html"
    "https://33bots.lt/robotas-konferencijai.html"
    "https://33bots.lt/kainos.html"
    "https://33bots.lt/video-realizacijos.html"
    "https://33bots.lt/blog.html"
    "https://33bots.lt/robotu-nuoma-vilnius.html"
    "https://33bots.lt/robotu-nuoma-kaunas.html"
  )
fi

LIST=$(printf '"%s",' "${URLS[@]}"); LIST="[${LIST%,}]"
curl -s -X POST "https://api.indexnow.org/indexnow" \
  -H "Content-Type: application/json; charset=utf-8" \
  -d "{\"host\":\"$HOST\",\"key\":\"$KEY\",\"keyLocation\":\"https://$HOST/$KEY.txt\",\"urlList\":$LIST}" \
  -w "\nHTTP %{http_code}\n"
