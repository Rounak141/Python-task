
import os
import shutil

source_folder = "image"
destination_folder = "organized_images"

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

count = 0

for filename in os.listdir(source_folder):
    if filename.lower().endswith(".jpg"):
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)

        shutil.move(source_path, destination_path)
        count += 1


print("\n========== FILE ORGANIZER ==========")
print(f"Source folder      : {source_folder}")
print(f"Destination folder : {destination_folder}")

if count > 0:
    print(f"Files moved        : {count}")
    print("Status             : Success")
    
else:
    print("Files moved        : 0")
    print("Status             : No JPG files found")

print("====================================")

p=(input("write 'open' for show organized_images folder: "))
if p == "open":
    print("\nSaved files in organized_images:")

    saved_files = os.listdir(destination_folder)

    if saved_files:
        for filename in saved_files:
                print(filename)
    else:
            print("No files found.")

elif p != "open":
        print("ok ")
