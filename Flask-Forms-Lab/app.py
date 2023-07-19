from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "MariaIsTheBest"
password = "hello123"



@app.route('/',methods=['GET','POST'])  # '/' for the default page
def login():
	if request.method =='POST': 
		username1=request.form['username']
		password1=request.form['password']
		if password1 == password and username==username1:
			return redirect(url_for('home'))
		else:
			return render_template('login.html')
	else:
		return render_template('login.html')


facebook_friends=["majd","katya","joelle", "Razi", "doaa", "waseem"]
@app.route('/home')
def home():
    return render_template('home.html' , facebook_friends=facebook_friends)

@app.route('/friend_axists/<string:name>' , methods=['GET', 'POST'])
def hello_name_route(name):
	return render_template('friend_exists.html' , methods=['GET', 'POST'] , facebook_friends=facebook_friends , name = name)



 

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True )