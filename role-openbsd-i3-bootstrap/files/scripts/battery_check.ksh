#!/bin/ksh

# Get the charger status
charger_status=$(apm -a)
# Get the battery percentage
battery_percentage=$(apm -l)

# Determine if the battery is charging or discharging
if [ "$charger_status" -eq 1 ]; then
    echo "BAT CHG: $battery_percentage%"
elif [ "$charger_status" -eq 0 ]; then
    echo "BAT DCHG: $battery_percentage%"
else
    echo "Battery status unknown"
fi
