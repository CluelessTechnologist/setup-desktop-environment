# grub2-gruvbox
Grub2 theme based on [gruvbox](https://github.com/morhetz/gruvbox).

Forked from a [grub2 solarized theme](https://github.com/Xyr0s1gn/grub2-solarized-dark).


 How To:
======

 1. Unzip
 2. Go to unzipped folder
 3. in terminal run the command **`sudo ./install.sh`**
 4. Follow the messages
 5. Reboot

or you can do this manually:
----

 1. Unzip and copy the theme folder to **`/boot/grub2/themes/gruvbox`**
 2. add (or edit existing lines) this to **`/etc/default/grub`**:

 `GRUB_THEME=/boot/grub2/themes/gruvbox/theme.txt`

 3. update your grub:

 `grub-mkconfig -o /boot/grub/grub.cfg`

 4. Done!

