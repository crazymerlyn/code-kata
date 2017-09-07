#!/usr/bin/awk -f

BEGIN { min_diff = 10000; }

function abs(v) { return v > 0 ? v : -v; }

$1 ~ /^[0-9]+\./ {
    diff = abs($7 - $9);
    if (diff < min_diff) {
        min_diff = diff;
        ans = $2;
    }
}

END { print ans; }

