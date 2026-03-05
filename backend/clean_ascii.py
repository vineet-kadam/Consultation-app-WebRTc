import os
import re

def clean_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Replace non-ASCII characters with ASCII equivalents or remove them
    # Especially common separators and icons
    replacements = {
        '──': '--',
        '—': '-',
        '–': '-',
        '→': '->',
        '✅': '[OK]',
        '❌': '[ERR]',
        '📋': '[INFO]',
        '📝': '[LOG]',
        '🔌': '[CONN]',
        '🎙': '[MIC]',
        '⚠️': '[WARN]',
        'ℹ️': '[INFO]',
    }
    
    for old, new in replacements.items():
        content = content.replace(old, new)
    
    # Generic non-ASCII removal for any remaining characters in comments
    # Replaces any non-ASCII character with a space if it's outside the standard ASCII range
    content = re.sub(r'[^\x00-\x7F]', ' ', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

root_dir = r'd:\Medical-Consultation-App-main(1)\Integrated-Medical-Consultation-app\backend\consultation'

for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith('.py'):
            filepath = os.path.join(root, file)
            print(f"Cleaning {filepath}...")
            clean_file(filepath)

print("Cleanup complete.")
