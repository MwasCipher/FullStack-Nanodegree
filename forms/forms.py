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

month_abbreviations = dict((m[:3].lower(), m) for m in months)


def valid_month(month):
    month = month.capitalize()
    if month in months:
        return month
    else:
        return None


form = """
    <form action="/foo">
	    <label>Month</label> <input type="text" name="month">
	    <label>Day</label><input type="" name="day">
	    <label>Year</label><input type="" name="year"> <br>
	    <input type="submit" name="">
    </form>

"""


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['content-type'] = 'text/plain'
        self.response.out.write('Hello World')

    app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
