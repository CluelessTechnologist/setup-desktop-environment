import os
import random

def get_mount_points():
    df_output = os.popen("df -k").read().strip().splitlines()[1:]
    mount_points = []

    for line in df_output:
        parts = line.split()
        if len(parts) >= 6:
            mount_point = parts[5]
            size_kb = int(parts[1])
            used_kb = int(parts[2])
            free_space_kb = int(parts[3])
            # We append used space in KB to sort by most used space.
            mount_points.append((mount_point, size_kb, used_kb, free_space_kb))
    
    # Sort by used space (third element in tuple) in descending order
    mount_points.sort(key=lambda x: x[2], reverse=True)

    return mount_points[:3]

def format_space(free_space_kb):
    if free_space_kb >= 1048576:  # 1 GB in KB
        free_space = free_space_kb / 1048576.0
        unit = "GB"
    else:
        free_space = free_space_kb / 1024.0
        unit = "MB"
    
    return f"{free_space:.2f}{unit}"

def main():
    top_mounts = get_mount_points()
    selected_mount = random.choice(top_mounts)
    
    mount_point = selected_mount[0]
    free_space_kb = selected_mount[3]  # free space in KB
    formatted_space = format_space(free_space_kb)

    print(f"{mount_point} Free: {formatted_space}")

if __name__ == "__main__":
    main()
