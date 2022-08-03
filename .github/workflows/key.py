
import requests
import os
def main():
  API_KEY = os.environ.get("APIKEY")
  if not API_KEY:
    raise RuntimeError("API_KEY env var and or secret is not set!")
  KEY_ID = os.environ.get("KEYID")
  if not KEY_ID:
    raise RuntimeError("KEY_ID env var and or secret is not set!")
  key =  {
      "api_key": str(API_KEY)
      "key_id": str(KEY_ID)
      }
  url_var = 'http://localhost/user/credentials/cdis/access_token'
  token = (requests.post(url_var, json=key).json())['access_token']
  write_in_string = "TOKEN={}".format(token)
  env_file = os.getenv('GITHUB_ENV')
  with open(env_file, "a") as myfile:
    myfile.write(write_in_string)
  
  return token

if __name__ == '__main__':
  main()
