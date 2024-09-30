#!/bin/ksh

# Previous states to avoid redundant notifications
prev_charger_status=""
prev_battery_warning=false

while true; do
    # Get the current charger status and battery percentage
    charger_status=$(apm -a)
    battery_percentage=$(apm -l)

    # Determine if the charger is connected or disconnected
    if [ "$charger_status" -eq 1 ]; then
        status="CHG"
    else
        status="DCHG"
    fi

    # Send a notification if the charger state changes
    if [ "$charger_status" != "$prev_charger_status" ]; then
        if [ "$status" = "CHG" ]; then
            notify-send "Charger Status" "Charger Connected. Battery: $battery_percentage%"
        else
            notify-send "Charger Status" "Charger Disconnected. Battery: $battery_percentage%"
        fi
    fi

    # Warn if the battery is below 10%
    if [ "$battery_percentage" -lt 10 ] && [ "$prev_battery_warning" = false ]; then
        notify-send "Battery Warning" "Battery is low: $battery_percentage%"
        prev_battery_warning=true
    elif [ "$battery_percentage" -ge 10 ]; then
        prev_battery_warning=false
    fi

    # Update the previous charger status
    prev_charger_status="$charger_status"

    # Wait for 60 seconds before checking again
    sleep 60
done
