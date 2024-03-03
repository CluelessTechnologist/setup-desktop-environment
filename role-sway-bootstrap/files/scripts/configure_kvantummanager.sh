#/bin/bash
# Check if the flag file exists
if [ -e ~/.configure_kvantummanager_script_has_run.flag ]; then
    echo "Kvantum manager configuration script has been run before. Removing the autoexec from sway config"
    sed -i '/^exec alacritty --class start-kvantummanager-config/d' ~/.config/sway/config
    rm ~/.configure_kvantummanager_script_has_run.flag
    exit 0
fi
# Create a flag file
touch ~/.configure_kvantummanager_script_has_run.flag
echo "Setting kvantum theme to gruvbox-kvantum"
sleep 3s
kvantummanager --set gruvbox-kvantum
sleep 3s
exit
