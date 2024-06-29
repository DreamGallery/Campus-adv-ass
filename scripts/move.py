import os
import shutil
from pathlib import Path


def format_store(filename: str, store_path: str) -> str:
    if filename.endswith(".txt"):
        txt_path = os.path.join(store_path, "txt")
        Path(txt_path).mkdir(parents=True, exist_ok=True)
        return txt_path
    elif filename.endswith(".ass"):
        ass_path = os.path.join(store_path, "ass")
        Path(ass_path).mkdir(parents=True, exist_ok=True)
        return ass_path


def move_files(source_path: str = ".tmp", dest_path: str = "Subtitles"):
    for root, _, files in os.walk(source_path):
        for file in files:
            if file.startswith("adv_cidol"):
                idol_name = file.split("-")[1]
                store_path = os.path.join(dest_path, "cidol", idol_name)
                final_path = format_store(file, store_path)
                shutil.move(os.path.join(root, file), os.path.join(final_path, file))
            elif file.startswith("adv_csprt"):
                store_path = os.path.join(dest_path, "csprt", file.split("_")[1])
                final_path = format_store(file, store_path)
                shutil.move(os.path.join(root, file), os.path.join(final_path, file))
            elif file.startswith("adv_dear"):
                idol_name = file.split("_")[2]
                store_path = os.path.join(dest_path, "dear", idol_name)
                final_path = format_store(file, store_path)
                shutil.move(os.path.join(root, file), os.path.join(final_path, file))
            elif file.startswith("adv_event"):
                event_id = file.split("_")[2]
                store_path = os.path.join(dest_path, "event", event_id)
                final_path = format_store(file, store_path)
                shutil.move(os.path.join(root, file), os.path.join(final_path, file))
            elif file.startswith("adv_live"):
                idol_name = file.split("_")[2]
                store_path = os.path.join(dest_path, "live", idol_name)
                final_path = format_store(file, store_path)
                shutil.move(os.path.join(root, file), os.path.join(final_path, file))
            elif file.startswith("adv_pevent"):
                idol_name = file.split("_")[3]
                store_path = os.path.join(dest_path, "pevent", idol_name)
                final_path = format_store(file, store_path)
                shutil.move(os.path.join(root, file), os.path.join(final_path, file))
            elif file.startswith("adv_pgrowth"):
                idol_name = file.split("_")[3]
                store_path = os.path.join(dest_path, "pgrowth", idol_name)
                final_path = format_store(file, store_path)
                shutil.move(os.path.join(root, file), os.path.join(final_path, file))
            elif file.startswith("adv_pstory"):
                idol_name = file.split("_")[3]
                store_path = os.path.join(dest_path, "pstory", idol_name)
                final_path = format_store(file, store_path)
                shutil.move(os.path.join(root, file), os.path.join(final_path, file))
            elif file.startswith("adv_unit"):
                episode = file.split("_")[2]
                store_path = os.path.join(dest_path, "unit", episode)
                final_path = format_store(file, store_path)
                shutil.move(os.path.join(root, file), os.path.join(final_path, file))
            else:
                store_path = os.path.join(dest_path, "other")
                final_path = format_store(file, store_path)
                shutil.move(os.path.join(root, file), os.path.join(final_path, file))


move_files()
