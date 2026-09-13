#!/usr/bin/env bash
#
# Tailwind arkuso kompiliavimas 33bots.lt.
#
# Perdarytu dizainu paremti puslapiai (pagrindinis, parduotuvė, diegimai) naudoja
# assets-redesign.css. Šis skriptas jį sukompiluoja ir kiekviename puslapyje pažymi
# paties arkuso turinio kontroline suma — versijos numeris pasikeičia lygiai tada,
# kai pasikeičia išvaizda, todėl naršyklė niekada nepateikia seno arkuso iš talpyklos.
#
# NAUDOJIMAS
#     python3 build_all.py && ./buduj.sh
#
# Pridėjus naują perdaryto dizaino puslapį, įrašykite jį į tailwind.config.js —
# kitaip jo klasės nepateks į arkušą ir puslapis liks be stilių.

set -euo pipefail
cd "$(dirname "$0")"

echo "Kompiliuoju stilių arkušą…"
npx --yes tailwindcss@3.4.17 \
  -c tailwind.config.js \
  -i tw-input.css \
  -o assets-redesign.css \
  --minify

VERSIJA=$(md5sum assets-redesign.css | cut -c1-8)

echo "Arkušas: $(du -h assets-redesign.css | cut -f1), versija ${VERSIJA}"

PUSLAPIAI=$(grep -rl 'assets-redesign\.css' --include='*.html' . | grep -v '^\./templates/' | sed 's|^\./||' | sort)
for PUSLAPIS in ${PUSLAPIAI}; do
  sed -i -E "s|href=\"assets-redesign\.css(\?v=[^\"]*)?\"|href=\"assets-redesign.css?v=${VERSIJA}\"|g" "${PUSLAPIS}"
  echo "  ${PUSLAPIS} → $(grep -o 'href="assets-redesign\.css[^"]*"' "${PUSLAPIS}" | head -1)"
done
