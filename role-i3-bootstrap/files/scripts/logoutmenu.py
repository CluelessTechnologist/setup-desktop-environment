import urwid
import subprocess

# Define the actions and their corresponding commands
actions = [
    ("Lock", "lock"),
    ("Logout", "i3-msg exit"),
    ("Suspend", "lock && dbus-send --system --print-reply --dest='org.freedesktop.UPower' /org/freedesktop/UPower org.freedesktop.UPower.Suspend"),
    ("Hibernate", "lock && dbus-send --system --print-reply --dest='org.freedesktop.UPower' /org/freedesktop/UPower org.freedesktop.UPower.Hibernate"),
    ("Reboot", "dbus-send --system --print-reply --dest=org.freedesktop.login1 /org/freedesktop/login1 org.freedesktop.login1.Manager.Reboot boolean:true"),
    ("Shutdown", "dbus-send --system --print-reply --dest=org.freedesktop.login1 /org/freedesktop/login1 org.freedesktop.login1.Manager.PowerOff boolean:true"),
    ("Cancel", "exit")  # Add Cancel option
]

# Define the menu choices
menu = urwid.SimpleListWalker([
    urwid.Button(label, on_press=lambda button, cmd=command: execute_command(cmd))
    for label, command in actions
])

# Define the ListBox
listbox = urwid.ListBox(menu)

# Define the main frame
main_frame = urwid.Frame(urwid.AttrWrap(listbox, 'body'))

# Function to execute the commands
def execute_command(command):
    if command == "exit":
        raise urwid.ExitMainLoop()
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command '{command}': {e}")

# Main loop
def main():
    palette = [
        ('body', 'black', 'light gray', 'standout'),
        ('reverse', 'light gray', 'black'),
    ]

    urwid.MainLoop(main_frame, palette).run()

if __name__ == "__main__":
    main()

