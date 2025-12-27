from pathlib import Path

raw_path = input("Enter folder path: ").strip()
path = Path(raw_path)

if not path.exists() or not path.is_dir():
    print("Invalid folder path:", path)
    exit()

for item in path.iterdir():
    if item.is_file():
        ext = item.suffix[1:] or "others"
        target = path / ext
        target.mkdir(exist_ok=True)
        item.rename(target / item.name)

print("Done!")
