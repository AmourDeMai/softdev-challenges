cut -d ":" -f 4 | sed '/^$/d' | tr "," "\n" | sort | uniq -c|sort -r
