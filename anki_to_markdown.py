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

def wipe_anki_out():
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

wipe_anki_out()
copy_media_files()



with open(anki_text, 'r') as file:
    lines = file.readlines()

    for line in lines:
        # seperate the line into the question and answer using tabs (deck, question, answer)
        if line.startswith("#"):
            continue
        # Separate the line into the question and answer using tabs (deck, question, answer)
        try:
            line_parts = line.split("\t")
            if len(line_parts) < 3:
                raise ValueError("not enough values to unpack")
            deck, question, answer = line_parts[0], line_parts[1], "".join(line_parts[2:])
        except ValueError as e:
            print(f"Error splitting line: {line.strip()} - {e}")
            continue

        # mkdir for the deck
        # make list of deck names split from ::
        deck_parts = deck.split("::")

        deck_folder = os.path.join(out_folder, *deck_parts)
        os.makedirs(deck_folder, exist_ok=True)


        # write the question and answer to a markdown file

        question_sanitised = re.sub(r'[<>:"/\\|?*]', '_', question)
        if question.startswith('"'):
            question = question[1:-1]
        if answer.startswith('"'):
            answer = answer[1:-2]


        with open(os.path.join(deck_folder, f"{question_sanitised}.md"), 'a') as question_file:
            # search for '<src=" and replace with 'src=""media/' in both question and answer
            question = question.replace('<img src=""', '<img src=""../media/')
            answer2 = answer.replace('<img src=""', '<img src=""../media/')

            question_file.write(f"# {question}\n")
            question_file.write(f"{answer2}\n")

