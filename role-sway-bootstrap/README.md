## role-sway-bootstrap 
### About  
This role will setup sway and everything needed for a good user experience (IMHO). Current supported themes are:  
* Win95
* Gruvbox

**Note:** I don't use the default keybindings for Sway, check out the [reference card](/role-sway-bootstrap/files/help/sway%20-%20Reference%20Card.html) to see what keybindings I use. Also the default layout is tabbed mode in my config. I don't see the need for opening a window and not use all the space I can right away. 
### Quick start  
Make sure you have clean install of Debian or Arch. If you have a physical PC I would recommend Debian netinst for a minimal Debian install or just install ArchLinux. For a VM I would recommend a cloud image. Here are some links:  
* [Debian Network install from minimal CD](https://www.debian.org/CD/netinst/)
* [Installing Arch Linux on Proxmox using cloud image](https://wiki.archlinux.org/title/Arch_Linux_on_a_VPS#Proxmox)
* [Cloud images in Proxmox](https://gist.github.com/chriswayg/b6421dcc69cb3b7e41f2998f1150e1df)
* [A Faster Way to Create Virtual Machines with Cloud Images and virt-manager (kvm)](https://codeofconnor.com/a-faster-way-to-create-virtual-machines-with-cloud-images-and-virt-manager/)
* [Quick provisioning of Linux VM using Hyper-V on Windows](https://github.com/schtritoff/hyperv-vm-provisioning)
* [example of using Ubuntu cloud images with virtualbox](https://gist.github.com/smoser/6066204)  

When you have a clean install you can go ahead and run the playbook.  

**If your install user has sudo access with nopasswd set:**  
```
ansible-playbook -i localhost --user <your user here> play-sway-bootstrap.yml
```
**Otherwise install sshpass and run the playbook this way: [(this doesn't currently work on Arch see todo)](#broken-things--todo)**
```
ansible-playbook -i localhost --user <your user here> --ask-pass play-sway-bootstrap.yml
``` 
**The install will prompt you for the following things:**    
```
Enter the IP address or resolvable DNS name for the machine you want to setup sway on:  
Choose system type (desktop/virtual_machine/laptop):  
Choose theme (win95/gruvbox):  
Choose keyboard layout, this is usually a two letter country code (see https://wiki.archlinux.org/title/Linux_console/Keyboard_configuration):  
```  

After the playbook has finished all you need to do is restart your machine and you should be greeted by Ly login or TTY. If Ly doesn't start you just logon to TTY and type "sway" and the desktop should load up. [(this is a bug that I have added to my Todo)](#broken-things--todo)
### Screenshots
#### Win95
![Sway desktop with Win95 theme, login screen](/screenshots/win95/win95_ly_prompt.jpg "Sway - Ly Win95 theme")
![Sway desktop with Win95 theme, two applications running](/screenshots/win95/win95_desktop.jpg "Sway - Win95 theme desktop")
![Sway desktop with Win95 theme, logout menu](/screenshots/win95/win95_logout.jpg "Sway - Win95 theme logout menu")
#### Gruvbox
![Sway desktop with Gruvbox theme, login screen](/screenshots/gruvbox/gruvbox_ly.jpg "Sway - Ly Gruvbox theme")
![Sway desktop with Gruvbox theme, two applications running](/screenshots/gruvbox/gruvbox_desktop.jpg "Sway - Gruvbox theme desktop")
![Sway desktop with Gruvbox theme, logout menu](/screenshots/gruvbox/gruvbox_logout.jpg "Sway - Gruvbox theme logout menu")
### Components used  
* **WM:** [Sway](https://swaywm.org)
* **Bar:** [Waybar](https://github.com/Alexays/Waybar)
* **Terminal:** [Alacritty](https://alacritty.org/)
* **Hotkey daemon:** [SWHKD](https://git.sr.ht/~shinyzenith/swhkd)
* **Lockscreen:** [swaylock](https://github.com/swaywm/swaylock)
* **Application launcher:** [bemenu](https://github.com/Cloudef/bemenu)
* **Application menu generator:** [j4-dmenu-desktop](https://github.com/enkore/j4-dmenu-desktop)
* **Notification daemon:** [dunst](https://dunst-project.org/)
* **Login manager:** [ly](https://github.com/fairyglade/ly)
* **Logout menu:** [wlogout](https://github.com/ArtsyMacaw/wlogout)
* **track_prev_focus script:** [Sway implement window back and forth](https://www.reddit.com/r/swaywm/comments/etpjix/i_created_a_script_to_implement_window_back_and/?utm_source=share&utm_medium=web2x&context=3)
* **Battery notification daemon:** [batsignal](https://github.com/electrickite/batsignal)
* **GUI for configuring displays:** [wdisplays](https://github.com/artizirk/wdisplays)
* **Tool for selecting Wifi networks:** [Networkmanager-dmenu](https://github.com/firecat53/networkmanager-dmenu)

\+ many more.
### Themes & images
#### Win95 
* **Sway theme:** Modified version of [base16-windows-scheme](https://github.com/funguscolander/base16-windows-scheme)
* **GTK theme:** [Chicago95](https://github.com/grassmunk/Chicago95)
* **Alacritty theme:** Hyper from [alacritty-theme](https://github.com/alacritty/alacritty-theme)
* **Waybar theme:** Modified version of [Waybar Win95](https://www.reddit.com/r/unixporn/comments/18af8fv/sway_waybar_my_windows95_inspired_theme)
* **Wallpaper:** [Green and brown plant on brown woven basket by Toa Hefitba](https://unsplash.com/photos/green-and-brown-plant-on-brown-woven-basket-p6GQoZHw_TI)
* **Lockscreen:** Background image from the Win95 setup
* **wlogout:** Custom
#### Gruvbox  
* **Sway theme:** Modified version of [Gruvbox material colorscheme for i3wm](https://gist.github.com/Cardoso1994/80641d652a4adcf6c8f718ebc3770ab9)
* **GTK theme:** [Gruvbox-GTK-Theme](https://github.com/Fausto-Korpsvart/Gruvbox-GTK-Theme)
* **Alacritty theme:** Gruvbox material from [alacritty-theme](https://github.com/alacritty/alacritty-theme)
* **Waybar theme:** Modified version of [gruvy gruvbox](https://www.reddit.com/r/unixporn/comments/rhi6m6/sway_wayland_with_gruvy_gruvbox)
* **Wallpaper:** [forest-3](https://gruvbox-wallpapers.pages.dev/wallpapers/irl)
* **Lockscreen:** [Minimalism 2](https://hdqwalls.com/minimalism-2-wallpaper)
* **wlogout:** [Nord theme](https://gist.github.com/exdeniz/dea6b4817b8d35cecb8f21a13c6e7aa6)
### Broken things / Todo
| Application     | Issue                                                                               | Workaround                                                                 |
|-----------------|-------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| Ly              | Sometimes when booting Ly is not visible in TTY1                                    | Logon to TTY and start Sway manually                                       |
| Ly              | When upgrading Ly the systemd file that contains the theme is wiped to the defaults |                                                                            |
| Kvantum Manager | Gruvbox: Seems to be no way to set kvantum theme using CLI or conf file             | I have a script starting at first boot that sets the theme using the "GUI" |
| wlogout         | Gruvbox: Current theme for wlogout is Nord based and not Gruvbox                    |                                                                            |
| Grub            | Need to rice Grub to match the themes                                               |                                                                            |
| yay (arch)      | Cannot run yay without NOPASSWD sudo option                                         | Use NOPASSWD sudo option                                                   |
| N/A             | Virtual machine option doesn't install guest tools for other than KVM hypervisor    |                                                                            |
