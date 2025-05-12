import os
import argparse
import json

script_dir = os.path.dirname(os.path.abspath(__file__))
directories_file = os.path.join(script_dir, "directories.json")

defaultDirectories = [
	"~/Python Projects",
	"~/JavaScript Projects",
	"~/Expo Apps",
	"~/ReactJS Apps",
	"~/Java Projects"
]

def load_directories():
    try:
        with open(directories_file) as f:
            data = json.load(f)

            if not data:
                raise ValueError("Empty array")
            return data
    except (FileNotFoundError, json.JSONDecodeError, ValueError):
        with open(directories_file, "w") as f:
            json.dump(defaultDirectories, f, indent=4)
        return defaultDirectories

directories = load_directories()

parser = argparse.ArgumentParser(prog="pm", description="A simple manager for your projects")

parser.add_argument("-c", "--config", help="Configure your project manager", choices=["directories", "show"], nargs="?", const="show", default=None)

args = parser.parse_args()

if (args.config == "show"):
	for directory in defaultDirectories:
		print(f"{directory.replace('~/', '')}: {directories[defaultDirectories.index(directory)]}")
elif (args.config == "directories"):
	#* Create new empty directories array (list)
	print("\x1b[31m\x1b[1m-----WARNING: This will overwrite your directories.json file-----\x1b[0m\n")
	print("\x1b[33mDo not include ~/ in your directory paths, use .. for parent directories. Press Enter to keep current value\x1b[0m\n")
	new_directories = []
	for directory in defaultDirectories:
		new_directories.append(
			"~/" +
			(input( f"{directory.replace('~/', '')} [{directories[len(new_directories)]}]: " ) or directories[len(new_directories)].replace('~/', ''))
		)
	with open(directories_file, "w") as f:
		json.dump(new_directories, f)
else:
	print("\x1b[32m\x1b[1m-----Welcome to Project Manager, please select your project-----\x1b[0m\n")
	totalArray = []
	for directory in directories:
		directoryPath = os.path.expanduser(directory)
		projects = []
		try:
			projects = os.scandir(directoryPath)
			print(f"{defaultDirectories[directories.index(directory)].replace('~/', '')}:")
		except:
			print(f"\x1b[31m\x1b[1mWARNING: Could not read {directoryPath}, this directory may not exist\x1b[0m")
			exit(1)

		for project in projects:
			totalArray.append(project.path)
			print(f"\x1b[4m\x1b[96m\x1b[1m	{project.name}\x1b[0m\x1b[32m ({totalArray.index(project.path) + 1})\x1b[0m")
	chosen = input(f"[1-{len(totalArray)}]: ")
	if (int(chosen) > len(totalArray) or int(chosen) < 1):
		print("\x1b[31mInvalid input\x1b[0m")
		exit(1)
	else:
		openInCode = input(f"Open {totalArray[int(chosen) - 1].split('/')[len(totalArray[int(chosen) - 1].split('/')) - 1]} in VSCode? (y/n): ")
		if openInCode == "y":
			os.system(f"code \"{totalArray[int(chosen) - 1]}\"")
		print(f"\x1b[92mSuccessfully copied CD command to clipboard!\x1b[0m")
		os.system(f"echo 'cd \"{totalArray[int(chosen) - 1]}\"' | clip.exe")
