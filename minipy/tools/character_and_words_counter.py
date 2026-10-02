import click

def get_multiline_input_editor():
    instruction_text = "#type your text above. Save the file and close it to continue."
    message = click.edit(f"\n\n{instruction_text}")
    
    if message:
        final_message = message.replace(instruction_text, "").strip()
        return final_message
    return ""

def count_characters(text):
    characters = 0
    for i in text:
        characters += 1
    
    return characters
        

def count_words(text):
    words_count = len(text.split())
    return words_count

input("Press Enter to open the text editor...")
text = get_multiline_input_editor()
choice = input("What do you want to do with this text, count characters (c), count words (w), count both (b): ").strip().lower()

if choice == "c":
    counted_characters = count_characters(text)
    print(f"Character: {counted_characters}")
elif choice == "w":
    counted_words = count_words(text)
    print(f"Words: {counted_words}")
elif choice == "b":
    counted_characters = count_characters(text)
    counted_words = count_words(text)
    print(f"Character: {counted_characters}")
    print(f"Words: {counted_words}")
else:
    print("Not a valid choice")

    
    
