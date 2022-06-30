# chicagopcdc.github.io
Repository of PCDC Documentation

Built with mkdocs material

Publish using `mkdocs gh-deploy`

# Dev Process
1. Create your feature branch out of dev
2. Make the necessary changes 
3. Test locally with `mkdocs serve` and/or `mkdocs build`
4. Once satified with the changes submit a PR to the `dev` branch

# Setup local DEV env
- python -m venv env
- source env/bin/activate
- pip install -r requirements.txt
- `mkdocs serve` to run it locally


# Release Process
1. Once the `dev` branch has reached the expected state make a PR to `main`
2. 

## Email Notifications
Document update emails default to lgraglia@bsd.uchicago.edu
Instructions to change email address:
- Go to settings
- on the left click the 'Secrets' tab
- select action
- go to the secret called EMAILLIST
- put 'None' for default email or add alternative email address 