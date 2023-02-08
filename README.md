# Mock Code Challenge Bundler

This is a tool developed to make it easier to bundle mock code challenges (or real ones) for the Flatiron School program.

## Getting Started

Begin by cloning down and renaming this repository to whatever you'd prefer.

Move your designated code challenge repository into the top level of this directory and rename the sub-directory to `code-challenge`. For example, clone the `ramen-rater-mock-cc` repository into here and run `mv ramen-rater-mock-cc code-challenge`. You can also rename the code challenge as you clone it, for example `git clone ramen-rater-mock-cc code-challenge`.


Execute `python3 bin/create.py` or `./bin/create.py` and it should automatically bundle the code challenge for you. This will remove it as a `git` repo.

From there you can use your own zipping tool to properly zip the directory and distribute to students via slack or canvas.

## Troubleshooting

Be sure that you've renamed the code challenge directory for students to `code-challenge` and that it's seated next to the `bin` directory.

The `code-challenge` directory needs to be a repository initialized with `git`.

During the bundling process, the git remote is removed and the main branch renamed to `main` from `master` if it wasn't before. This functionality is intentional.
