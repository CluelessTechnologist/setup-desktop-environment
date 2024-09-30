#!/bin/ksh

# Get used memory
USED_MEM=$(top -b | grep "^Memory" | awk -F: '{ print $3 }' | awk -F/ '{ print $2 }' | awk '{ print $1 }' | sed 's/M//g')
# Get free memory
FREE_MEM=$(top -b | grep "^Memory" | awk -F: '{ print $4 }' | awk '{ print $1 }' | sed 's/M//g')
# Calculate total memory
TOTAL_MEM=$(($USED_MEM + $FREE_MEM))

# Convert to GiB if total memory is over 1024 MiB
if [ "$TOTAL_MEM" -ge 1024 ]; then
    USED_MEM_GB=$(echo "scale=2; $USED_MEM / 1024" | bc | awk '{printf "%.2f", $0}')
    TOTAL_MEM_GB=$(echo "scale=2; $TOTAL_MEM / 1024" | bc | awk '{printf "%.2f", $0}')
    PERCENTAGE=$(echo "scale=0; ($USED_MEM * 100) / $TOTAL_MEM" | bc)
    echo "${USED_MEM_GB}GiB/${TOTAL_MEM_GB}GiB (${PERCENTAGE}%)"
else
    PERCENTAGE=$(echo "scale=0; ($USED_MEM * 100) / $TOTAL_MEM" | bc)
    echo "${USED_MEM}MiB/${TOTAL_MEM}MiB (${PERCENTAGE}%)"
fi
