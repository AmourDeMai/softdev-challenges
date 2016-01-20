egrep '<div class="command">.*</div>|<div class="num-votes".*</div>' | sed -e 's/<[^>]*>//g' |  awk 'ORS = NR%2 ? FS : RS' | sed 's/^[ ]*//' | awk '{if ($NF >= 5) {NF = NF - 1; print $0;}}'
