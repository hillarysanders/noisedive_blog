# Noisedive
Simple blog app built with Flask, originally based on [flaskBlog📜](https://dogukanurker.com/flaskblog) but, er, very different by now.

# Updates, using github actions
1. Change code
2. Test locally
3. Bump version number
3. Push to main, this will automatically publish and install most recent version package
4. Restart server daemon (via website, unf), then production site will pick up new installation

# Github Actions
Current deployment github action scripts are defined in `.github/workflows/`. To run, I've set the required secrets in the github repo's [repository secrets](https://github.com/hillarysanders/noisedive_blog/settings/secrets/actions).


# Local (Assumes you're on an [Apple-Silicon] Mac)
### On a new clone or computer:
1. `cd $dir`
2. install brew if you haven't already: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
3. install asdf if you haven't already: `brew install asdf`. Then add `. /opt/homebrew/opt/asdf/libexec/asdf.sh` to your `~/.zshrc` file (NOTE: if things aren't working, consult asdf documentation, these instructions may have changed). Start a new terminal shell and `cd $dir` back to the repo.
4. install python 3.10+ with asdf if you haven't already: `asdf plugin-add python`; `asdf install python 3.11.4` (current code requires 3.10 but why not go higher).
5. set local python to this new version and confirm it's correct: `asdf local python 3.11.4`; `python3 -V`
6. install virtualenv package if you haven't already: `pip install virtualenv`
7. create virutalenv: `python3 -m  virtualenv venv`
8. activate virtualenv: `source venv/bin/activate`
9. pip install -r requirements.txt
10. Now use the "Each Time" instructions below each time.
### Each time
1. `cd $dir`
2. `source venv/bin/activate`
3. `FLASK_APP=noisedive_blog flask` run or `FLASK_DEBUG=1 ENV=development  FLASK_APP=noisedive_blog flask run --debugger`
