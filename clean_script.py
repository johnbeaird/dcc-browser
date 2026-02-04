import re

with open('DCC.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove all JSDoc comments (/** ... */)
content = re.sub(r'/\*\*.*?\*/', '', content, flags=re.DOTALL)

# Also remove the alert statements I added
content = content.replace('alert("Script loading...");', '')
content = content.replace('alert("init() called");', '')
content = content.replace('alert("startGame() called");', '')
content = content.replace('alert("About to call init()");', '')

with open('DCC_clean.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Created DCC_clean.html without JSDoc comments')