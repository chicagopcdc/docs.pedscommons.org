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

# Setup local DEV env with Windows
- bash
- sudo apt-get update
- sudo apt install python3.8-venv
- python3 -m venv env
- source env/bin/activate
- pip3 install -r requirements.txt

# Run local DEV env
- source env/bin/activate
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
- If EMAILLIST doesn't exists create a new repository secret **not** an enviorment secret
- put **'None'** for default email or add alternative email address 

## Adding API Key and Key ID
The API request requires three redentials (Request URL, API key, & key ID) to complete a access token request. These three credentials will be stored in Github Secrets. To add or change them the instructions are as follows:
- Go to settings
- on the left click the 'Secrets' tab
- select action
- go to the secret 
- either edit or create a new secret
  - Must be named REQUESTURL, APIKEY and KEYID
- put in corrisponding credentials
  - credentials can be gathered by going to the profile page and clicking the orange get API key button
  - further explanation at [here](https://gen3.org/resources/user/using-api/#credentials-to-send-api-requests)
 
## Running Workflows and Actions Locally
Use this [link](https://formulae.brew.sh/formula/act) for refernce
- install correct version of Homebrew for your device [here](https://brew.sh/)
- download Act extension using:
  - `brew install act`
- test actions using act

