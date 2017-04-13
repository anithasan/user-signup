
import webapp2
import jinja2
import os

from google.appengine.ext import db

# set up jinja
template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                                autoescape = True)#escape

#standard google app engine app
# class handler inherits from webapp2
#convenience functionS
class Blog(db.Model):
    title = db.StringProperty(required = True)#constraints <500
    blog = db.TextProperty(required = True)# more than 500 characters
    created = db.DateTimeProperty(auto_now_add = True)
    last_modified = db.DateTimeProperty(auto_now = True)

class Handler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))


class MainPage(Handler):

    def get(self):
        self.render("base.html")

class BlogHandler(Handler):
    def render_front(self, title="", blog="", error=""):
        blogs = db.GqlQuery("SELECT * FROM Blog ORDER BY created DESC LIMIT 5")
        self.render("blog.html", blogs= blogs)

    def get(self):
        self.render_front()

class NewPost(Handler):

    def get(self):
        self.render("newpost.html")

    def post(self):
        title = self.request.get("title")
        blog = self.request.get("blog")

        if title and blog:
            b = Blog(title = title, blog = blog)
            b.put()
            self.redirect("/blog/"+str(b.key().id()))
        else:
            error = "We need both a title and some text!"
            self.render("newpost.html", title= title, blog = blog, error = error)

class NewBlog(Handler):
    def get(self, id):

        key = db.Key.from_path('Blog', int(id))
        blog = db.get(key)

        if not blog:
            self.error(404)
            return

        self.render("permalink.html", blog = blog)


app = webapp2.WSGIApplication([
    ('/', BlogHandler),
    ('/blog', BlogHandler),
     ('/blog/([0-9]+)', NewBlog),
    ('/blog/newpost', NewPost),
], debug=True)
