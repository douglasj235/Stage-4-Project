import os

import jinja2
import webapp2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
								autoescape = True)

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
		items = self.request.get_all("comments")
		concepts = [['Understanding of Servers', 'A browser speaks to the server through http to request documents.  There are two types of classifications of responses that a server will do.  Static and Dynamic.  Static is pre written files images that the server will return.  Dynamic requests are responses built on the fly by a program called web applications that is running.  Most content online is dynamic today.  Web application is a program that generates content that a browser requests (ex. Facebook page, blog pages, and google search results). Two commonly used methods for a request-response between a client and server are: GET and POST. GET requests data from a specified resource.  POST submits data to be processed to a specified resource.'],
					['Importance of Validating Input', 'Verify the user input. When you get an input error, render form again.  Should always include an error message.'],
					['HTML Templates and Abstraction', 'A template library is a library to build complicate strings.  Jinja2 is a template library that is built into Google App Engine.']]
					
		self.render("HTML_Notes.html", items = items, concepts = concepts)
				
		
app = webapp2.WSGIApplication([('/', MainPage)], debug=True)				