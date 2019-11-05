import webapp2

form = """

    <form action="/foo">
	    <input type="" name="name"> <input type="submit" name="">
    </form>

"""


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['content-type'] = 'text/plain'
        self.response.out.write('Hello World')

    app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
