import webapp2
import re
import cgi

# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>User Signup Form</title>

</head>
<body>

"""
# a form for adding new movies
signup_form = """
<h1>Signup</h1>
<form method="post">
<table><tr>
    <td class="label">Username:</td>
    <td><input type="text" name="username" value=""/></td>
    <td class="error">
    <label style="color:red;">{error_username}</label>
      </td>
    </td>

    </td>

    </tr>
    <tr>
    <td class="label">Password:</td>
    <td><input type="password" name="password" value=""/></td>
    <td class="error">
    <label style="color:red;">{error_password}</label>
      </td>
    </tr>
    <tr>
    <td class="label">Verify Password:</td>
    <td><input type="password" name="verify"/></td>
    <td class="error">
    <label style="color:red;">{error_verify}</label>
      </td>
    </tr>
    <tr>
    <td class="label">Email(Optional):</td>
    <td><input type="text" name="email"/></td>
    <td class="error">
    <label style="color:red;">{error_email}</label>
      </td>

    </tr></table>
    <input type="submit" value="Submit"/>

</form>

"""
# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return USER_RE.match(username)

PASS_RE = re.compile("^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

EMAIL_RE = re.compile("^[\S]+@[\S]+.[\S]+$")
def valid_email(email):
    return not email or EMAIL_RE.match(email)

class MainHandler(webapp2.RequestHandler):

    def helper(self, user_name="", user_password="", match_password="",user_email=""):
    #string substitution
        self.response.write(signup_form.format(error_username= user_name,
                              error_password= user_password,
                              error_verify= match_password,
                              error_email= user_email))

    def get(self):
        self.helper()

    def post(self):
        have_error = False
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')


        params = dict(username = username, email = email)

        user_name=""
        user_password=""
        match_password=""
        user_email=""

        if not valid_username(username):
            user_name = "That's not a valid username."
            have_error = True

        if not valid_password(password):
            user_password = "That wasn't a valid password."
            have_error = True
        elif password != verify:
            match_password = "Your password didn't match."
            have_error = True

        if not valid_email(email):
            user_email = "Thats not a valid email"
            have_error = True

        if have_error:
            self.response.write(signup_form.format(error_username= user_name,
                              error_password= user_password,
                              error_verify= match_password,
                              error_email= user_email
                              ))
        else:
            self.redirect("/welcome?username="+username)

class Welcome(webapp2.RequestHandler):
   def get(self):
        username = self.request.get('username')
        if valid_username(username):
             self.response.write(welcome.format(username = username))

#html for welcome page
welcome = """
<!DOCTYPE html>

<html>
<head>
    <title>
    User Signup
    </title>
</head>

<body>
<h2>Welcome, {username}!</h2>
</body>
</html>
"""
#def Welcome(webapp2.RequestHandler):

app = webapp2.WSGIApplication([
('/', MainHandler),
('/welcome', Welcome)
], debug=True)
