from flask import Flask, request, jsonify, render_template, render_template, url_for, session, redirect
import json
from six.moves.urllib.parse import urlencode

from models import setup_db, User, Contact, Interaction
from auth import setup_auth, requires_auth, AUTH0_CLIENT_ID, AUTH0_CALLBACK_URL, AUTH0_CLIENT_SECRET

app = Flask(__name__)
setup_db(app)
auth0 = setup_auth(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return auth0.authorize_redirect(redirect_uri=AUTH0_CALLBACK_URL)

'''
Login --> callback /interactions
    attempt to access page without login --> Back to login

/interactions:
    GET 
        - returns all interactions ordred by date
        - returns list of contact names (not a priority)
        - paginate to help with loading
    POST
        - search
            - query interactions db inside of notes column
        - add contact
            - get form args
                - contact name
                - contact frequency (this will need to be some sort of popup or something)
        - add interaction
            - get form args
                - contact name
                - timestamp
                - method
                - duration
                - notes (multi-line --> use <textarea> in the <form> also use javascript to alter dimensions of area)
            - find contact id
            - use user id
            - add user to session
            


'''

@app.route('/callback')
def callback_handling():
    # Handles response from token endpoint
    auth0.authorize_access_token()
    resp = auth0.get('userinfo')
    userinfo = resp.json()

    # Store the user information in flask session.
    session['jwt_payload'] = userinfo
    session['profile'] = {
        'user_id': userinfo['sub'],
        'name': userinfo['name'],
        'picture': userinfo['picture'],
        'email': userinfo['email']
    }
    # return jsonify({
    #     "success": True,
    #     "profile": jsonify(session['profile'])
    # })
    
    # return redirect('/dashboard')
    return redirect(url_for('interactions'))

@app.route('/dashboard')
@requires_auth
def dashboard():
    return render_template('dashboard.html',
                           userinfo=session['profile'],
                           userinfo_pretty=json.dumps(session['jwt_payload'], indent=4))

@app.route('/logout')
def logout():
    # Clear session stored data
    session.clear()
    # Redirect user to logout endpoint
    params = {'returnTo': url_for('index', _external=True), 'client_id': AUTH0_CLIENT_ID}
    return redirect(auth0.api_base_url + '/v2/logout?' + urlencode(params))

@app.route('/interactions')
@requires_auth
def interactions():
    return render_template('interactions.html')