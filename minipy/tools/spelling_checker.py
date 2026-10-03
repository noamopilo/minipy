import requests
import click

def get_multiline_input_editor():
    instruction_text = "#type your text above. Save the file and close it to continue."
    message = click.edit(f"\n\n{instruction_text}").strip()
    
    if message:
        final_message = message.replace(instruction_text, "").strip()
        return final_message
    return ""

text = get_multiline_input_editor()

print("Original text: \n")
print(text + "\n")
print("Corrected text: \n")

url = f"https://api.languagetool.org/v2/check"
payload = {
    "text": text,
    "language": "auto",
}

try:
    response = requests.post(url, data=payload)
    response.raise_for_status()
    data = response.json()
except Exception as e:
    print("Error when calling API: {e}")


def check_spelling():
    matches = data.get("matches", [])
    
    if not matches:
        print("No errors found")
        return
    
    correct_text = text
    for match in sorted(matches, key=lambda x: x['offset'], reverse=True):
        start = match['offset']
        length = match['length']
        end = start + length
        
        bad_word = correct_text[start:end]
        
        if match.get('replacements'):
            best_suggestion = match['replacements'][0]['value']
            correct_word = f"\033[92m{best_suggestion}\033[0m"
            correct_text = correct_text[:start] + correct_word + correct_text[end:]
        else:
            bad_word = correct_text[start:end]
            correct_text = correct_text[:start] + f"\033[91m{bad_word}\033[0m" + correct_text[end:]
    print(correct_text)
    
check_spelling()