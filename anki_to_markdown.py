import os
import re
import shutil
anki_media_folder = r"C:\Users\pilch\AppData\Roaming\Anki2\User 1\collection.media"
anki_exported_deck_txt = r"C:\Users\pilch\OneDrive\Desktop\Final Year with deck.txt"
decks_folder = r"C:\Users\pilch\anki_to_markdown\decks"
media_folder = r"C:\Users\pilch\anki_to_markdown\media"

# read file line by line


def copy_media_files():
    # copy media files to the output folder
    for file in os.listdir(anki_media_folder):
        if file.endswith(".png") or file.endswith(".jpg"):
            # print("copying file " + file + " to " + out_media_folder)
            shutil.copy2(os.path.join(anki_media_folder, file), media_folder)
    return

def clear_out_folder():
    # wipe the output folder
    for file in os.listdir(decks_folder):
        file_path = os.path.join(decks_folder, file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(e)
    return

def sanitize_and_fix_paths(text: str, num_of_dot_dots: int) -> str:
    """Remove quotes quirk and fix image paths."""
    # Remove double quotes from start and end if present
    if text.startswith('"') and text.endswith('"'):
        text = text[1:-1]
    
    # Fix image paths
    dot_dots = "../" * num_of_dot_dots
    text = text.replace('<img src=""', f'<img src="{dot_dots}media/').replace('.jpg""', '.jpg"')
    
    return text

def create_card_md(deck_folder: str, card_title: str, question: str, answer: str):
    with open(os.path.join(deck_folder, f"{card_title}.md"), 'a') as card_file:

        card_file.write(f"## {question}\n")

        # wrap the answer in a details tag, so it's hidden until clicked
        card_file.write("<details>\n")
        card_file.write(f"<summary><b>Reveal answer</b></summary>\n")
        card_file.write(f"{answer}\n")
        card_file.write("</details>\n")

def process_card(line: str):
    try:
        line_parts = line.split("\t")
        print(line_parts)
        if len(line_parts) < 3:
            raise ValueError("not enough values to unpack")
        deck, question, answer = line_parts[0], line_parts[1], line_parts[2]
    except ValueError as e:
        print(f"Error splitting line: {line.strip()} - {e}")
        return
    
    deck_parts = deck.split("::")
    num_of_dot_dots = len(deck_parts) + 1 # for relative pathing
    deck_folder = os.path.join(decks_folder, *deck_parts)
    os.makedirs(deck_folder, exist_ok=True)


    card_title = re.sub(r'[<>:"/\\|?*]', '', question)
    question = sanitize_and_fix_paths(question, num_of_dot_dots)
    answer = sanitize_and_fix_paths(answer, num_of_dot_dots)

    create_card_md(deck_folder, card_title, question, answer)



clear_out_folder()
copy_media_files()

with open(anki_exported_deck_txt, 'r') as file:
    lines = file.readlines()
    for line in lines:
        if line.startswith("#"):
            # metadata line, skip
            continue
        process_card(line)
       

