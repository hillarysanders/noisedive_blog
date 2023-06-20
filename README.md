# Noisedive
Simple blog app built with Flask, originally based on [flaskBlog📜](https://dogukanurker.com/flaskblog).

# Updates, using github actions
1. Change code
2. Test locally
3. Bump version number
3. Push to main, this will automatically publish and install most recent version package
4. Restart server daemon (via website, unf), then production site will pick up new installation

# Local
1. `cd $dir`
2. `source .venv/bin/activate`
3. `FLASK_APP=noisedive_blog flask` run or `FLASK_DEBUG=1 ENV=development  FLASK_APP=noisedive_blog flask run --debugger`
