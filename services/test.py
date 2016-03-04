import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		if self.request.path == "/api/v1/employees":
			self.getEmployees();
			return;
		self.set_status(400);
		self.write("Bad request.");
	
	def getEmployees(self):
		self.set_status(200);
		self.write(readEmployees());
		return;
		
def readEmployees():
	return open('employees.json').read();

application = tornado.web.Application([
(r"/api/?.*", MainHandler)
]);

application.listen(8888);
tornado.ioloop.IOLoop.instance().start()