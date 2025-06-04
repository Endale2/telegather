import zipfile
import os
import shutil

# 1) Adjust these if your version is different.
old_wheel = os.path.join("dist", "telegather-0.1.4-py3-none-any.whl")
temp_dir = "tmp_wheel"

# 2) Remove any existing tmp_wheel folder
if os.path.isdir(temp_dir):
    shutil.rmtree(temp_dir)

# 3) Unzip the wheel into tmp_wheel/
os.makedirs(temp_dir, exist_ok=True)
with zipfile.ZipFile(old_wheel, 'r') as zin:
    zin.extractall(temp_dir)

# 4) Remove unwanted metadata lines from METADATA
meta_dir = os.path.join(temp_dir, "telegather-0.1.4.dist-info")
meta_path = os.path.join(meta_dir, "METADATA")

cleaned_lines = []
with open(meta_path, "r", encoding="utf-8") as f:
    for line in f:
        # Skip any line that starts with "License-File:" or "Dynamic:"
        if line.startswith("License-File:") or line.startswith("Dynamic:"):
            continue
        cleaned_lines.append(line)

with open(meta_path, "w", encoding="utf-8") as f:
    f.writelines(cleaned_lines)

# 5) Delete the old wheel so we don’t overwrite it accidentally later
os.remove(old_wheel)

# 6) Re-pack everything under tmp_wheel/ back into a new .whl
with zipfile.ZipFile(old_wheel, 'w', compression=zipfile.ZIP_DEFLATED) as zout:
    for root, dirs, files in os.walk(temp_dir):
        for filename in files:
            fullpath = os.path.join(root, filename)
            # Compute the archive name relative to tmp_wheel
            relpath = os.path.relpath(fullpath, temp_dir)
            zout.write(fullpath, relpath)

# 7) Clean up the temporary folder
shutil.rmtree(temp_dir)

print(f"Rebuilt wheel without License-File or Dynamic lines: {old_wheel}")
