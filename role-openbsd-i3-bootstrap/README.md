## role-openbsd-i3-bootstrap 
### About  
This role will setup i3 and everything needed for a good user experience (IMHO). Current supported themes are:  
* Win95
* Gruvbox

**Note:** I don't use the default keybindings for i3, also the default layout is tabbed mode in my config. I don't see the need for opening a window and not use all the space I can right away. 
  
Please remember that this role is written by a Linux user trying OpenBSD for the first time, mostly for fun as a experiment on how much configuration would be interchangeable between Linux & OpenBSD. If I were to run OpenBSD as my main OS I would probably opt for other software since some of these applications don't have native OpenBSD support. But overall I'm pretty happy with the result, this means that I could move over to OpenBSD and my desktop would mostly look & behave the same as on Linux.

### Quick start  
Make sure you have clean install of OpenBSD. This is how I usually install OpenBSD:
1. Download the ISO from a [mirror](https://www.openbsd.org/ftp.html). ([cd75.iso](https://cdn.openbsd.org/pub/OpenBSD/7.5/amd64/cd75.iso) is what I use)
2. Boot the ISO and follow the install instructions. (don't forget to install with X support)

In case you get stuck see the official installation guide:

* [OpenBSD Installation Guide](https://www.openbsd.org/faq/faq4.html)


When the installation has been completed you need to install Python and configure doas for the playbook to work:
```
su
pkg_add python
echo "permit $(who -m | awk '{print $1}') as root" >> /etc/doas.conf
```

**Run the playbook:**  
  

*(requires [sshpass](https://stackoverflow.com/questions/42835626/ansible-to-use-the-ssh-connection-type-with-passwords-you-must-install-the-s))*

```
ansible-playbook -i localhost --user <your user here> --ask-pass --ask-become-pass play-openbsd-i3-bootstrap.yml
``` 
  

**The install will prompt you for the following things:**    
```
Enter the IP address or resolvable DNS name for the machine you want to setup i3 on:  
Choose system type (desktop/virtual_machine/laptop):  
Choose theme (win95/gruvbox):  
Choose keyboard layout, this is usually a two letter country code (see https://wiki.archlinux.org/title/Linux_console/Keyboard_configuration):  
```  

After the playbook has finished you should be greeted by the xenodm login screen.
### Screenshots
#### Win95
![i3 desktop with Win95 theme, login screen](/screenshots/role-openbsd-i3-bootstrap/win95/win95_xenodm.jpg "i3 - Xenodm Win95 theme")
![i3 desktop with Win95 theme, two applications running](/screenshots/role-openbsd-i3-bootstrap/win95/win95_desktop.jpg "i3 - Win95 theme desktop")
![i3 desktop with Win95 theme, logout menu](/screenshots/role-openbsd-i3-bootstrap/win95/win95_logout.jpg "i3 - Win95 theme logout menu")
#### Gruvbox
![i3 desktop with Gruvbox theme, login screen](/screenshots/role-openbsd-i3-bootstrap/gruvbox/gruvbox_xenodm.jpg "i3 - Xenodm Gruvbox theme")
![i3 desktop with Gruvbox theme, two applications running](/screenshots/role-openbsd-i3-bootstrap/gruvbox/gruvbox_desktop.jpg "i3 - Gruvbox theme desktop")
![i3 desktop with Gruvbox theme, logout menu](/screenshots/role-openbsd-i3-bootstrap/gruvbox/gruvbox_logout.jpg "i3 - Gruvbox theme logout menu")
### Components used  
* **WM:** [i3](https://i3wm.org)
* **Bar:** [Polybar](https://github.com/polybar/polybar)
* **Terminal:** [XTerm](https://invisible-island.net/xterm/)
* **Hotkey daemon:** [sxhkd](https://git.sr.ht/~shinyzenith/swhkd)
* **Lockscreen:** [i3lock](https://github.com/i3wm/i3lock)
* **Application launcher:** [rofi](https://github.com/davatorium/rofi)
* **Notification daemon:** [dunst](https://dunst-project.org/)
* **Login manager:** [xenodm](https://why-openbsd.rocks/fact/xenodm/)
* **Logout menu:** Custom Python script based on ideas from [i3 FAQ](https://faq.i3wm.org/question/239/how-do-i-suspendlockscreen-and-logout.1.html)
* **track_prev_focus script:** [i3 implement window back and forth](https://www.reddit.com/r/i3wm/comments/etpjix/i_created_a_script_to_implement_window_back_and/?utm_source=share&utm_medium=web2x&context=3)
* **Battery notification daemon:** Custom ksh script 

\+ many more.
### Themes & images
#### Win95 
* **i3 theme:** Modified version of [base16-windows-scheme](https://github.com/funguscolander/base16-windows-scheme)
* **GTK theme:** [Chicago95](https://github.com/grassmunk/Chicago95)
* **XTerm theme:** Hyper from [xresources-themes](https://github.com/janoamaral/Xresources-themes)
* **Polybar theme:** Custom 
* **Wallpaper:** [Green and brown plant on brown woven basket by Toa Hefitba](https://unsplash.com/photos/green-and-brown-plant-on-brown-woven-basket-p6GQoZHw_TI)
* **xenodm:** Custom with the help from [TuM'Fatig's blog post](https://www.tumfatig.net/2019/customizing-openbsd-xenodm/)
* **Lockscreen:** Background image from the Win95 setup
#### Gruvbox  
* **i3 theme:** Modified version of [Gruvbox material colorscheme for i3wm](https://gist.github.com/Cardoso1994/80641d652a4adcf6c8f718ebc3770ab9)
* **GTK theme:** [Gruvbox-GTK-Theme](https://github.com/Fausto-Korpsvart/Gruvbox-GTK-Theme)
* **QT5ct theme:** [gruvbox-qt6ct](https://github.com/giuji/gruvbox-qt6ct)
* **XTerm theme:** Gruvbox dark from [gruvbox-contrib](https://github.com/morhetz/gruvbox-contrib/blob/master/xresources/gruvbox-dark.xresources)
* **Polybar theme:** Custom 
* **Wallpaper:** [forest-3](https://gruvbox-wallpapers.pages.dev/wallpapers/irl)
* **xenodm:** Custom with the help from [TuM'Fatig's blog post](https://www.tumfatig.net/2019/customizing-openbsd-xenodm/). OpenBSD artwork from [atlas-ark](https://www.reddit.com/r/openbsd/comments/mz9qll/after_a_lot_of_requests_i_made_a_openbsd/)
* **Lockscreen:** [Minimalism 2](https://hdqwalls.com/minimalism-2-wallpaper)
### QT Themeing on OpenBSD
AFAIK Kvantum is not available on OpenBSD so I had to use a qt5ct stylesheet for the Gruvbox theme instead. In my experience the Gruvbox Kvantum theme is better for getting a uniform look on all QT apps but this can work too. Originally I got a white background in [Dolphin](https://apps.kde.org/dolphin/) (the file manager), but I fixed this by setting a hardcoded background color in `.config/kdeglobals`. Might not be a big deal and Dolphin is a bit bloated so you probably would like to run something else like [PCManFM-Qt](https://github.com/lxqt/pcmanfm-qt) which works with the qt5ct theme out of the box anyways.
### Default shell 
For this role I decided to change the default shell to [zsh](https://www.zsh.org/). I normally just run the default shell but I couldn't live with [ksh](https://man.openbsd.org/ksh.1) as my default shell since I felt I was missing some features from bash, so I opted for trying zsh for the first time. The config is not too bloated I hope.
