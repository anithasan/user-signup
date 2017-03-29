#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi

# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>User Signup Form</title>
    <style type="text/css">
        .error {
            color: red;
        }
        h1 a{
        text-decoration:none;
        }

    </style>
</head>
<body>
    <h1>
        <a href="/">Signup:</a>
    </h1>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        # a form for adding new movies
        signup_form = """

        <form action="/signup" method="post">
        <table><tr>
            <td class="label">Username:</td>
            <td><input type="text" name="Username"/></td>
            </tr>
            <tr>
            <td class="label">Password:</td>
            <td><input type="text" name="Password"/></td>
            </tr>
            <tr>
            <td class="label">Verify Password:</td>
            <td><input type="text" name="Verify_Password"/></td>
            </tr>
            <tr>
            <td class="label">Email(Optional):</td>
            <td><input type="text" name="Username"/></td>
            </tr></table>
            <input type="submit" value="Submit"/>

        </form>

        """
        content = (page_header + signup_form + page_footer)
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
