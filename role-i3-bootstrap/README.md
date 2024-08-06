## role-i3-bootstrap 
### About  
This role will setup i3 and everything needed for a good user experience (IMHO). Current supported themes are:  
* Win95
* Gruvbox

**Note:** I don't use the default keybindings for i3, also the default layout is tabbed mode in my config. I don't see the need for opening a window and not use all the space I can right away. 
### Quick start  
Make sure you have clean install of Debian or Arch. If you have a physical PC I would recommend Debian netinst for a minimal Debian install or just install ArchLinux. For a VM I would recommend a cloud image. Here are some links:  
* [Debian Network install from minimal CD](https://www.debian.org/CD/netinst/)
* [Installing Arch Linux on Proxmox using cloud image](https://wiki.archlinux.org/title/Arch_Linux_on_a_VPS#Proxmox)
* [Cloud images in Proxmox](https://gist.github.com/chrii3g/b6421dcc69cb3b7e41f2998f1150e1df)
* [A Faster Way to Create Virtual Machines with Cloud Images and virt-manager (kvm)](https://codeofconnor.com/a-faster-way-to-create-virtual-machines-with-cloud-images-and-virt-manager/)
* [Quick provisioning of Linux VM using Hyper-V on Windows](https://github.com/schtritoff/hyperv-vm-provisioning)
* [example of using Ubuntu cloud images with virtualbox](https://gist.github.com/smoser/6066204)  

When you have a clean install you can go ahead and run the playbook.  

**If your install user has sudo access with nopasswd set:**  
```
ansible-playbook -i localhost --user <your user here> play-i3-bootstrap.yml
```
**Otherwise install sshpass and run the playbook this way: [(this doesn't currently work on Arch see todo)](#broken-things--todo)**
```
ansible-playbook -i localhost --user <your user here> --ask-pass play-i3-bootstrap.yml
``` 
**The install will prompt you for the following things:**    
```
Enter the IP address or resolvable DNS name for the machine you want to setup i3 on:  
Choose system type (desktop/virtual_machine/laptop):  
Choose theme (win95/gruvbox):  
Choose keyboard layout, this is usually a two letter country code (see https://wiki.archlinux.org/title/Linux_console/Keyboard_configuration):  
```  

After the playbook has finished all you need to do is restart your machine and you should be greeted by the empttty login.
### Screenshots
#### Win95
![i3 desktop with Win95 theme, grub menu](/screenshots/role-i3-bootstrap/win95/win95_grub.jpg "i3 - Grub Win95 theme")
![i3 desktop with Win95 theme, plymouth splash](/screenshots/role-i3-bootstrap/win95/win95_plymouth.jpg "i3 - Plymouth Win95 theme")
![i3 desktop with Win95 theme, login screen](/screenshots/role-i3-bootstrap/win95/win95_lightdm.jpg "i3 - LightDM Win95 theme")
![i3 desktop with Win95 theme, two applications running](/screenshots/role-i3-bootstrap/win95/win95_desktop.jpg "i3 - Win95 theme desktop")
![i3 desktop with Win95 theme, logout menu](/screenshots/role-i3-bootstrap/win95/win95_logout.jpg "i3 - Win95 theme logout menu")
#### Gruvbox
![i3 desktop with Gruvbox theme, grub menu](/screenshots/role-i3-bootstrap/gruvbox/gruvbox_grub.jpg "i3 - Grub Gruvbox theme")
![i3 desktop with Gruvbox theme, plymouth splash](/screenshots/role-i3-bootstrap/gruvbox/gruvbox_plymouth.jpg "i3 - Plymouth Gruvbox theme")
![i3 desktop with Gruvbox theme, login screen](/screenshots/role-i3-bootstrap/gruvbox/gruvbox_lightdm.jpg "i3 - LightDM Gruvbox theme")
![i3 desktop with Gruvbox theme, two applications running](/screenshots/role-i3-bootstrap/gruvbox/gruvbox_desktop.jpg "i3 - Gruvbox theme desktop")
![i3 desktop with Gruvbox theme, logout menu](/screenshots/role-i3-bootstrap/gruvbox/gruvbox_logout.jpg "i3 - Gruvbox theme logout menu")
### Components used  
* **WM:** [i3](https://i3wm.org)
* **Bar:** [Polybar](https://github.com/polybar/polybar)
* **Terminal:** [XTerm](https://invisible-island.net/xterm/)
* **Hotkey daemon:** [sxhkd](https://git.sr.ht/~shinyzenith/swhkd)
* **Lockscreen:** [i3lock](https://github.com/i3wm/i3lock)
* **Application launcher:** [bemenu](https://github.com/Cloudef/bemenu)
* **Application menu generator:** [j4-dmenu-desktop](https://github.com/enkore/j4-dmenu-desktop)
* **Notification daemon:** [dunst](https://dunst-project.org/)
* **Login manager:** [LightDM](https://github.com/canonical/lightdm)
* **Logout menu:** Custom Python script based on ideas from [i3 FAQ](https://faq.i3wm.org/question/239/how-do-i-suspendlockscreen-and-logout.1.html)
* **track_prev_focus script:** [i3 implement window back and forth](https://www.reddit.com/r/i3wm/comments/etpjix/i_created_a_script_to_implement_window_back_and/?utm_source=share&utm_medium=web2x&context=3)
* **Battery notification daemon:** [batsignal](https://github.com/electrickite/batsignal)
* **Tool for selecting Wifi networks:** [Networkmanager-dmenu](https://github.com/firecat53/networkmanager-dmenu)

\+ many more.
### Themes & images
#### Win95 
* **i3 theme:** Modified version of [base16-windows-scheme](https://github.com/funguscolander/base16-windows-scheme)
* **GTK theme:** [Chicago95](https://github.com/grassmunk/Chicago95)
* **XTerm theme:** Hyper from [xresources-themes](https://github.com/janoamaral/Xresources-themes)
* **Polybar theme:** Custom 
* **Wallpaper:** [Green and brown plant on brown woven basket by Toa Hefitba](https://unsplash.com/photos/green-and-brown-plant-on-brown-woven-basket-p6GQoZHw_TI)
* **LightDM:** [Chicago95](https://github.com/grassmunk/Chicago95)
* **Lockscreen:** Background image from the Win95 setup
* **Grub theme:** [GRUB Windows 95 Theme](https://github.com/a1ive/grub-theme-win95)
* **Plymouth theme:** [Plymouth RetroTux Theme from Chicago95](https://github.com/grassmunk/Chicago95)
#### Gruvbox  
* **i3 theme:** Modified version of [Gruvbox material colorscheme for i3wm](https://gist.github.com/Cardoso1994/80641d652a4adcf6c8f718ebc3770ab9)
* **GTK theme:** [Gruvbox-GTK-Theme](https://github.com/Fausto-Korpsvart/Gruvbox-GTK-Theme)
* **XTerm theme:** Gruvbox dark from [gruvbox-contrib](https://github.com/morhetz/gruvbox-contrib/blob/master/xresources/gruvbox-dark.xresources)
* **Polybar theme:** Custom 
* **Wallpaper:** [forest-3](https://gruvbox-wallpapers.pages.dev/wallpapers/irl)
* **LightDM:** [Gruvbox-GTK-Theme](https://github.com/Fausto-Korpsvart/Gruvbox-GTK-Theme)
* **Lockscreen:** [Minimalism 2](https://hdqwalls.com/minimalism-2-wallpaper)
* **wlogout:** [Cozy Grubox with GTK icons](https://github.com/0bCdian/Hyprland_dotfiles/tree/Cozy_Gruvbox)
* **Grub theme:** [grub2-gruvbox](https://git.fs.lmu.de/adnan/grub2-gruvbox/-/tree/master)
* **Plymouth theme:** [Loader from adi1090x's plymouth-themes repo](https://github.com/adi1090x/plymouth-themes)
### Broken things / Todo
| Application     | Issue                                                                               | Workaround                                                                 |
|-----------------|-------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| yay (arch)      | Cannot run yay without NOPASSWD sudo option                                         | Use NOPASSWD sudo option                                                   |
| QT6 (arch)      | Some applications use QT6 now so need to add qt6ct for theming those                                         | Install and configure qt6ct yourself                                                   |
| N/A             | Virtual machine option doesn't install guest tools for other than KVM hypervisor    |                                                                            |
