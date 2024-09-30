import urwid
import subprocess

# Define the actions and their corresponding commands
actions = [
    ("Lock", "i3lock -t -i .cache/lockscreen.png"),
    ("Logout", "i3-msg exit"),
    ("Suspend", "doas /usr/sbin/zzz"),
    ("Hibernate", "doas /usr/sbin/zzz"),
    ("Reboot", "doas /sbin/reboot"),
    ("Shutdown", "doas /sbin/halt -p"),
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

