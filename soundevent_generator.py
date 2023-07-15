import os, subprocess, time

sounds_dir = "./sounds/"
soundevents_dir = "./soundevents/"
resourcemanifests_dir = "./resourcemanifests/"
#This should usually be <addonName>_addon_resources.vrman
resource_manifest = "sp_a2_core_addon_resources.vrman"
#MAKE SURE YOU CHANGE THIS PATH TO YOUR RESOURCECOMPILER EXECUTABLE
resource_compiler_path = r"E:\SteamLibrary\steamapps\common\Half-Life Alyx\game\bin\win64\resourcecompiler.exe"

def create_resource_manifest(soundevents_files):
    manifest = '<!-- kv3 encoding:text:version{e21c7f3c-8a33-41c5-9977-a76d3a32aa0d} format:generic:version{7412167c-06e9-4698-aff2-e63eb59037e7} -->\n'
    manifest += "{\n\tresourceManifest = \n\t[\n\t\t[\n"
    for soundevents_file in soundevents_files:
        manifest += f'\t\t\t"./soundevents/{soundevents_file}",\n'  # Corrected file path
    manifest += "\t\t],\n\t]\n}"
    return manifest

def create_soundevent_entry(filepath, foldername):
    filename = os.path.splitext(os.path.basename(filepath))[0]
    filepath = filepath.replace("\\", "/")  # Replace backslashes with slashes
    filepath = os.path.splitext(filepath)[0] + ".vsnd"  # Replace file extension to .vsnd

    if foldername == "music":
        soundevent_type = "hlvr_music_3d"
    else:
        soundevent_type = "hlvr_default_3d"
    
    entry = f'\t"{filename}" = \n\t{{\n\t\ttype = "{soundevent_type}"\n\t\tvolume = 1.0\n\t\tvolume_falloff_min = 70.0\n\t\tvolume_falloff_max = 2700.0\n\t\tvolume_fade_out = 1\n\t\tvolume_fade_in = 0\n\t\tspread_min = 30\n\t\tspread_max = 150\n\t\tvsnd_files = \n\t\t[\n\t\t\t"./sounds/{filepath}",\n\t\t]\n\t}}'
    return entry

def find_wav_files(directory):
    wav_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(".wav"):
                wav_files.append(os.path.relpath(os.path.join(root, file), start=sounds_dir))
    return wav_files

def create_soundevents_file(soundevents_path, soundevent_entries):
    with open(soundevents_path, "w") as f:
        f.write('<!-- kv3 encoding:text:version{e21c7f3c-8a33-41c5-9977-a76d3a32aa0d} format:generic:version{7412167c-06e9-4698-aff2-e63eb59037e7} -->\n')
        f.write("{\n")
        for i, entry in enumerate(soundevent_entries):
            if i > 0:
                f.write("\n")
            f.write(entry)
        f.write("\n}")

def create_soundevent_files():
    soundevents_files = []
    for root, dirs, files in os.walk(sounds_dir):
        for dir_name in dirs:
            folder_path = os.path.join(root, dir_name)
            if os.path.samefile(sounds_dir, os.path.dirname(folder_path)):
                soundevents_path = os.path.join(soundevents_dir, f"{dir_name}_soundevents.vsndevts")
                wav_files = find_wav_files(folder_path)
                soundevent_entries = []
                for file in wav_files:
                    soundevent_entries.append(create_soundevent_entry(file, dir_name))
                create_soundevents_file(soundevents_path, soundevent_entries)
                print(f"Soundevents file created successfully: {soundevents_path}")
                soundevents_files.append(os.path.relpath(soundevents_path, start=soundevents_dir))

    resource_manifest_path = os.path.join(resourcemanifests_dir, resource_manifest)
    resource_manifest_content = create_resource_manifest(soundevents_files)
    with open(resource_manifest_path, "w") as f:
        f.write(resource_manifest_content)
    print(f"Resource manifest file created successfully: {resource_manifest_path}")

    compile_sound()
    compile_soundevents()
    compile_resource_manifest()

def compile_sound():
    print("Compiling sounds")
    for root, dirs, files in os.walk(sounds_dir):
        for file in files:
            file_path = os.path.join(root, file)
            subprocess.call([resource_compiler_path, file_path])
            print(f"Sound compiled successfully: {file_path}")

def compile_soundevents():
    print("Compiling Soundevents")
    for root, dirs, files in os.walk(soundevents_dir):
        for file in files:
            file_path = os.path.join(root, file)
            subprocess.call([resource_compiler_path, file_path])
            print(f"Soundevent file compiled successfully: {file_path}")

def compile_resource_manifest():
    print("Compiling Resource Manifest")
    resource_manifest_path = os.path.join(resourcemanifests_dir, resource_manifest)
    subprocess.call([resource_compiler_path, resource_manifest_path])
    print(f"Resource manifest file compiled successfully: {resource_manifest_path}")

def main():
    start_time = time.time()  # Get the current time before starting the script

    create_soundevent_files()

    end_time = time.time()  # Get the current time after the script finishes
    execution_time = end_time - start_time  # Calculate the total execution time

    print(f"Script execution time: {execution_time} seconds")

if __name__ == "__main__":
    main()
