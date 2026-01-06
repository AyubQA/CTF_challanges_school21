#!/bin/bash
# Puzzle script - reverse engineer to find the flag
# The script applies transformations to input string

input="$1"

# Step 1: Base64 encode
step1=$(echo -n "$input" | base64)

# Step 2: Reverse string
step2=$(echo -n "$step1" | rev)

# Step 3: Hex encode
step3=$(echo -n "$step2" | xxd -p -c 0)

# Step 4: Rot13
step4=$(echo -n "$step3" | tr 'A-Za-z' 'N-ZA-Mn-za-m')

# Step 5: Reverse again
step5=$(echo -n "$step4" | rev)

echo "Result: $step5"
echo ""
echo "Your task: Given the result, find the original input (flag)"
echo "Hint: Apply transformations in reverse order!"

