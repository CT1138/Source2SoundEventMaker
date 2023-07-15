# Soundevent Generator

The Soundevent Generator is a Python script that automates the creation of soundevent files for sound assets in the Half-Life: Alyx game. It recursively searches for .wav files in the specified directory and generates soundevent files (.vsndevts) for each folder directly under the root sounds directory. Additionally, it creates a resource manifest file (.vrman) that references the generated soundevent files.

**This script was designed for Half-Life: Alyx and may or may not work for other Source 2 Games.**

## How it Works

The Soundevent Generator script performs the following steps:

1. It recursively searches for .wav files within the specified `sounds_dir` directory.
2. For each folder directly under the root sounds directory, it creates a soundevent file (.vsndevts) in the `soundevents_dir` directory.
3. The script generates soundevent entries for each found .wav file, including the necessary metadata such as volume, spread, and file paths.
4. It creates a resource manifest file (.vrman) in the `resourcemanifests_dir` directory that references the generated soundevent files.
5. The script compiles the sound files, soundevent files, and the resource manifest using the specified `resource_compiler_path`.

## Getting Started

To use the Soundevent Generator script, follow these steps:
1. Install Python 3.x if not already installed.
2. Open the `soundevent_generator.py` file and adjust the configuration variables at the beginning of the script, such as `sounds_dir`, `soundevents_dir`, `resourcemanifests_dir`, `resource_manifest`, and `resource_compiler_path`, to match your environment.
3. Make sure the `resource_compiler_path` variable points to the correct path of the `resourcecompiler.exe` executable for Half-Life: Alyx.
4. Save the modifications.
5. Open a terminal or command prompt and navigate to the directory containing the script files.
6. Run the script by executing `python soundevent_generator.py`.
7. The script will generate the soundevent files and resource manifest, compile the sound and resource files, and provide information about the progress.
8. Once the script completes, the generated soundevent files and resource manifest will be available in the specified output directories and Valve's resourcecompiler tool will have all the compiled assets in their proper places.

**Note:** It is essential to have the correct file structure and naming conventions for your sound assets to ensure proper functionality. Refer to the script comments for more details.

## Loading addon soundevents
 
Addon soundevents are not loaded until a map is loaded in game, or the addon soundevent file is reloaded in the Asset Browser.

This means that if you launch the Workshop Tools and only open Hammer, you will find that your addon soundevents are not yet available in the soundevent picker.

 
In such cases, to load addon soundevents, do either of the following:

1. Launch the Workshop Tools and load any map by using “addon_tools_map <mapname>.”
2. Recompile and reload your <addon_name>_soundevents.vsndevts file in the Asset Browser.

These steps are only necessary if you have not yet loaded a map after launching the Workshop Tools.
Another useful way to check the existence of your addon soundevents is by entering the “snd_list_soundevents” console command into the vconsole.

## License

This project is licensed under the [MIT License](LICENSE).
