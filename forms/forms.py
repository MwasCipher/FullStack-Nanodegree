import webapp2

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']


def valid_month(month):
    month = month.capitalize()
    if month in months:
        return month
    else:
        return None

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
