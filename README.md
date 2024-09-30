# Desktop Environment Bootstrap with Ansible 
## About 
One of the big advantages of running Linux/BSD is having the freedom to customize your desktop. But it can be quite the burden sometimes, since a desktop consists of many components. It's easy to forget important components or settings. For the longest time I was running Ubuntu standard desktop for this reason.   

"I don't have time to configure my own custom desktop. I'll just use the standard one. Using something that most people use will guarantee a good experience."  

It's a similar rationale to people using *VSCode* over *neovim* for time saving purposes. "I don't wanna waste time learning vim, I rather just do my work without spending extra time learning keyboard shortcuts". 

I quickly changed my mind on this after installing Sway and configuring it over summer vacation. It took some time to get it right and I missed some important components at first. Like forgetting to activate swaylock after suspend, or having a nice and smooth way to connect to Wifi. I also had major frustrations with theming and getting a uniform look in both Sway, QT and GTK. It took sometime to setup just the way I wanted it but having it as a ansible role means it will be easy to replicate my setup when I want to install a new desktop. 

This repository contains ansible roles to bootstrap complete desktop environments with the defaults I use and with the basic components needed for desktop & laptop use. It doesn't contain all the scripts & keyboard shortcuts I use since they are for my personal use.  

For instructions on how to run the playbooks click the links below.
  
## Supported OSes:
* Debian 12
* Arch Linux
* OpenBSD 7.5 (specific role) 

## Roles:
* [**role-sway-bootstrap:** Bootstraps a Sway desktop, complete with theme and all necessary components.](role-sway-bootstrap/README.md)
* [**role-i3-bootstrap:** Bootstraps a i3 desktop, complete with theme and all necessary components.](role-i3-bootstrap/README.md)
* [**role-openbsd-i3-bootstrap:** Bootstraps a OpenBSD based i3 desktop, complete with theme and all necessary components.](role-openbsd-i3-bootstrap/README.md)
