#!/usr/bin/env python3
import sys, os

if __name__ == "__main__":
    if os.path.exists('code-challenge/') and os.path.exists('code-challenge/.git'):
        print("Creating bundle file...")
        os.system("cd code-challenge && git branch -M main && git remote remove origin && git bundle create ../code-challenge.bundle HEAD main")
        print("Removing unbundled files...")
        os.system("rm -rf code-challenge")
        print("Removing template files")
        os.system("rm -rf README.md .git ./bin/create.py")
        print("Code challenge ready!")
    else:
        print("No git initialized 'code-challenge' directory found...")
