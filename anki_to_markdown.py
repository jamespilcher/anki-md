import os
import re
import shutil
anki_media_folder = r"C:\Users\pilch\AppData\Roaming\Anki2\User 1\collection.media"
anki_text = r"C:\Users\pilch\OneDrive\Desktop\Final Year with deck.txt"
out_folder = r"C:\Users\pilch\anki_to_markdown\anki_out"
out_media_folder = r"C:\Users\pilch\anki_to_markdown\media"

# read file line by line


def copy_media_files():
    # copy media files to the output folder
    for file in os.listdir(anki_media_folder):
        if file.endswith(".png") or file.endswith(".jpg"):
            # print("copying file " + file + " to " + out_media_folder)
            shutil.copy2(os.path.join(anki_media_folder, file), out_media_folder)
    return

def clear_out_folder():
    # wipe the output folder
    for file in os.listdir(out_folder):
        file_path = os.path.join(out_folder, file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(e)
    return

clear_out_folder()
copy_media_files()

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
        deck_folder = os.path.join(out_folder, *deck_parts)
        os.makedirs(deck_folder, exist_ok=True)

        if question.startswith('"') and question.endswith('"'):
            question = question[1:-1]
        if answer.startswith('"') and answer.endswith('"'):
            answer = answer[1:-1]

        card_title = re.sub(r'[<>:"/\\|?*]', '_', question)
        with open(os.path.join(deck_folder, f"{card_title}.md"), 'a') as card_file:
            dot_dots = "../" * num_of_dot_dots
            question = question.replace('<img src=""', f'<img src="{dot_dots}media/').replace('.jpg""', '.jpg"')
            answer = answer.replace('<img src=""', f'<img src="{dot_dots}media/').replace('.jpg""', '.jpg"')
            
            card_file.write(f"# {question}\n")

            # wrap the answer in a details tag, so it's hidden until clicked
            card_file.write("<details>\n")
            card_file.write(f"<summary><b>Reveal answer</b></summary>\n")
            card_file.write(f"{answer}\n")
            card_file.write("</details>\n")




with open(anki_text, 'r') as file:
    lines = file.readlines()

    for line in lines:
        # seperate the line into the question and answer using tabs (deck, question, answer)
        if line.startswith("#"):
            continue
        # Separate the line into the question and answer using tabs (deck, question, answer)
        process_card(line)
       

