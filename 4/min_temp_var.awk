BEGIN { min = 1000; }

NF > 10 && $1 ~ /^[0-9]+/ {
    if (min > $2 - $3) {
        min = $2 - $3;
        ans = $1;
    }
}

END { print ans }

