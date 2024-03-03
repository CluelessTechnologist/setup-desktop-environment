# Desktop Environment Bootstrap with Ansible 
## About 
One of the big advantages of running Linux is having the freedom to customize your desktop. But it can be quite the burden sometimes since a desktop consists of many components. It's easy to forget important components or a setting. For the longest time I was running Ubuntu standard desktop for this reason.   

"I don't have time to configure my own custom desktop. I'll just use the standard one. Using something that most people use will guarantee a good experience."  

It's a similar rationale to people using *VSCode* over *neovim* for time saving purposes. "I don't wanna waste time learning vim, I rather just do my work without spending extra time learning keyboard shortcuts". 

I quickly changed my mind on this after installing i3wm and configuring it over summer vacation. It took some time to get it right and I missed some important components at first. Like forgetting to activate swaylock after suspend, or having a nice and smooth way to connect to Wifi. I also had major frustrations with theming and getting a uniform look in both Sway, QT and GTK. It took sometime to setup just the way I wanted it but having it as a ansible role means it will be easy to replicate my setup when I want to install a new desktop. 

This repository will contain ansible roles to bootstrap a complete desktop environment with the defaults I use and with the basic components needed for desktop & laptop use.It doesn't contain all the scripts & keyboard shortcuts I use since they are for my personal use.  

Currently I only have one ansible role and that is for setting up Sway. I will soon create another role for setting up i3 for my old computers that don't support Wayland.  

For instructions on how to run the playbook for setting up Sway see the [README](role-sway-bootstrap/README.md#quick-start).
  
## Supported OSes:
* Debian 12
* Arch Linux

## Roles:
* [**role-sway-bootstrap:** Bootstraps a Sway desktop, completed with theme and all necessary components.](role-sway-bootstrap/README.md)
