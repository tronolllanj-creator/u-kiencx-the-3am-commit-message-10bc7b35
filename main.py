"""WTF at 3AM: fix: typo in 'self' for make.fun."""

import os
import sys

COMMIT = "fix: typo in 'self' caused infinite loop of self-hatred"

def main():
    out_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, 'entry.txt')
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(COMMIT + '\n')

    # Assert constraints
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    stripped = content.strip()
    assert 1 <= len(stripped) <= 139, f"Invalid length: {len(stripped)}"
    
    print(f'wrote entry.txt {len(stripped)} chars')

if __name__ == '__main__':
# Runner-up considered and rejected in session: 'fix: apologize to context window for the overflow'
    main()