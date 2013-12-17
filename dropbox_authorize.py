# Initial flow to authorize an app with dropbox.

import requests
import dropbox

app_key = 'ezbqgqbovrrha4y'
app_secret = '1mucf93bsj3m10e'

flow = dropbox.client.DropboxOAuth2FlowNoRedirect(
        app_key, app_secret)

authorize_url = flow.start()

# Have to ask the 'user' (me) to authorize linking my app 
# to my dropbox account.

# Parse the authorization code and from the request 'r'
# and return the string and assign it to the var code.
# r = requests.get(authorize_url)


# access_token, user_id = flow.finish(code)

# STORE THE ACCESS TOKEN. Authorization is only needed 
# once unless the user revokes access or reinstalls
# this app.
# client = dropbox.client.DropboxClient(access_token)

# print 'linked account: ', client.account_info()


def download_file(client):
    for file in fuji_mix_pic_folder['contents']:
        f, metadata = client.get_file_and_metadata(file['path'])
        file_name = file['path'].strip('/fuji-mix/')
        out = open('static/images/'+file_name, 'wb')
        out.write(f.read())
        out.close()
