import os
import shutil


def move_files(source_path: str, dest_path: str):
    file_type_mapping = {
        "adv_cidol": {"folder": "cidol", "index": 1, "split_char": "-"},
        "adv_csprt": {"folder": "csprt", "index": 1, "split_char": "_"},
        "adv_dear": {"folder": "dear", "index": 2, "split_char": "_"},
        "adv_event": {"folder": "event", "index": 2, "split_char": "_"},
        "adv_live": {"folder": "live", "index": 2, "split_char": "_"},
        "adv_pevent": {"folder": "pevent", "index": 3, "split_char": "_"},
        "adv_pgrowth": {"folder": "pgrowth", "index": 3, "split_char": "_"},
        "adv_pstory": {"folder": "pstory", "index": 3, "split_char": "_"},
        "adv_unit": {"folder": "unit", "index": 2, "split_char": "_"}
    }

    for root, _, files in os.walk(source_path):
        for file in files:
            folder = "other"
            for prefix, config in file_type_mapping.items():
                if file.startswith(prefix):
                    folder = config["folder"]
                    parts = file.split(config["split_char"])
                    if len(parts) > config["index"]:
                        subfolder = parts[config["index"]]
                        store_path = os.path.join(dest_path, folder, subfolder)
                        break
            else:
                store_path = os.path.join(dest_path, "other")
            
            os.makedirs(store_path, exist_ok=True)
            shutil.move(os.path.join(root, file), os.path.join(store_path, file))


for file_type in ["ass", "csv"]:
    if file_type == "ass":
        source_path = ".tmp/ass"
        dest_path = "Subtitles"
    else:
        source_path = ".tmp/csv"
        dest_path = "CSV"
    move_files(source_path, dest_path)
