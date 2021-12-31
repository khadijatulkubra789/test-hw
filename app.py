from flask import Flask
name = "kha"

app = Flask(__name__)
@app.route("/")
def index():
    return '''
    <!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>FreeChat</title>
	<style type="text/css">
		body {background: #77A1D3; 
background: -webkit-linear-gradient(to right, #E684AE, #79CBCA, #77A1D3); 
background: linear-gradient(to right, #E684AE, #79CBCA, #77A1D3); 
}
h1{color: #004e92;
font-family: Times;
font-size: 200%;
text-align: center;  }
h2{
	color: #114e92;
font-family: Times;
}
p {color: #004e92;
font-family: Times;
font-size: 120%;
text-align: center;
 }
li{
	color:  #41295a ;
font-family: Times;
font-size: 100%;
} 

	</style>
</head>
<body>
<h1>FreeChat</h1>
<br>
<p>FreeChat is an app for texting (SMS, MMS) and chat (RCS). <br>Message anyone from anywhere with the reliability of texting <br> and the richness of chat. Stay in touch with friends and family,<br> send group texts, and share your favorite pictures, GIFs, emoji,<br> stickers, videos and audio messages.<br></p>
<h1 style="text-align: left;">Features</h1>
<ul>
<li style="text-align: justify;">
<h2><strong> Chat features (RCS)<br /></strong></h2>
On supported carriers, you can send and receive messages over Wi-Fi or your data network, see when friends are typing or when they have read your message, share images and videos in high quality, and more.</li>
<li style="text-align: justify;">
<h2><strong>Clean, intuitive, and comfortable design<br /></strong></h2>
Instant notifications, smart replies and a fresh new design make communicating faster and more fun. With dark mode, you can use Messages comfortably in low-light situations.</li>
<li style="text-align: justify;">
<h2><strong>Easy sharing<br /></strong></h2>
Select or take pictures and videos directly from the app and share easily. You can even send audio messages to your contacts.</li>
<li style="text-align: justify;">
<h2><strong>Powerful search</strong></h2>
<br />Now you can find more of the content shared in your conversations: tap on the search icon and select a specific contact to see your messaging history with them and all the photos, videos, addresses or links you shared with each other.</li>
</ul>
</body>
</html>
    '''

@app.route("/login")
def login():
    return '''<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Login</title>
	<style type="text/css"> 
body {background: #77A1D3; 
background: -webkit-linear-gradient(to right, #E684AE, #79CBCA, #77A1D3); 
background: linear-gradient(to right, #E684AE, #79CBCA, #77A1D3); 
}
h1{color: #004e92;
font-family: sans-serif;
font-size: 200%;
text-align: center;  }
p {color: #004e92;
font-family: sans-serif;
font-size: 120%;
text-align: center; }

label {color:  #41295a ;
font-family: sans-serif;
font-size: 100%;
padding: 10px;
margin-left: 40%;}
input {border: 1px solid;
border-radius: 5px;
padding: 5px;
margin-top: 10px; 
margin-left: 40%;}
button { background-color: steelblue;
	font-family: sans-serif;
font-size: 100%;
	border: 1px solid;
border-radius: 5px;
padding: 5px;
margin-top: 10px; 
}
</style>
</head>
<body>
<form>
    <h1>Login</h1>
    <label for="email"><b>Email</b></label>
    <br>
    <input type="text" placeholder="Enter Email" name="email" required>
	<br>
    <label for="psw"><b>Password</b></label>
    <br>
    <input type="password" placeholder="Enter Password" name="psw" required>
    <label>
      <input type="checkbox" checked="checked" name="remember"> Remember me
    </label>
	<br>
    <p>By logging in you agree to our <a href="#" style="color:dodgerblue">Terms & Privacy</a>.</p>
      <button type="button" class="cancelbtn">Cancel</button>
      <button type="submit" class="signupbtn">Login</button>
</form>
</body>
</html>'''

@app.route("/signup")
def signup():
    return '''<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>SignUp</title>
	<style type="text/css"> 
body {background: #77A1D3; 
background: -webkit-linear-gradient(to right, #E684AE, #79CBCA, #77A1D3); 
background: linear-gradient(to right, #E684AE, #79CBCA, #77A1D3); 
}
h1{color: #004e92;
font-family: sans-serif;
font-size: 200%;
text-align: center;  }
p {color: #004e92;
font-family: sans-serif;
font-size: 120%;
text-align: center; }

label {color:  #41295a ;
font-family: sans-serif;
font-size: 100%;
padding: 10px;
margin-left: 35%;}
input {border: 1px solid;
border-radius: 5px;
padding: 5px;
margin-top: 10px; 
margin-left: 35%;}
button { background-color: steelblue;
	font-family: sans-serif;
font-size: 100%;
	border: 1px solid;
border-radius: 5px;
padding: 5px;
margin-top: 10px; 
}
</style>
</head>
<body>
<form>
    <h1>Sign Up</h1>
    <p>Please fill in this form to create an account.</p>
    <label for="fname"><b>First Name</b></label>
    <br>
    <input type="text" placeholder="Enter First Name" name="fname" required>
    <br>
    <label for="lname"><b>Last Name</b></label>
    <br>
    <input type="text" placeholder="Enter Last Name" name="lname" required>
    <br>
    <label for="DOB"><b>Date of Birth</b></label>
    <br>
    <input type="date" name="DOB" required>
    <br>
    <label for="email"><b>Email</b></label>
    <br>
    <input type="text" placeholder="Enter Email" name="email" required>
	<br>
    <label for="psw"><b>Password</b></label>
    <br>
    <input type="password" placeholder="Enter Password" name="psw" required>
	<br>
    <label for="psw-repeat"><b>Repeat Password</b></label>
    <br>
    <input type="password" placeholder="Repeat Password" name="psw-repeat" required>
    <br>
    <label>
      <input type="checkbox" checked="checked" name="remember"> Remember me
    </label>
	<br>
    <p>By creating an account you agree to our <a href="#" style="color:dodgerblue">Terms & Privacy</a>.</p>
      <button type="button" class="cancelbtn">Cancel</button>
      <button type="submit" class="signupbtn">Sign Up</button>
</form>
</body>
</html>
'''
