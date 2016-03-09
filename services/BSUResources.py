import tornado.ioloop
import tornado.web
import json
import os

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		if self.request.path == "/api/v1/employees":
			self.getEmployees();
			return;
		self.set_status(400);
		self.write("Bad request.");
	def post(self):
		if self.request.path =="/api/vi/employees":
			self.postEmployees();
			return;
		self.write_status(400);
		self.write("Bad request.");
	
	def postEmployees(self):
		self.set_status(200);
		self.write(writeEmployess(self.request.body))
		return;
	
	def getEmployees(self):
		self.set_status(200);
		self.write(readEmployees());
		return;

def readEmployees():
	return json.dumps(data);
	
def writeEmployees(writeTo):
	employees = json.load(writeTo);
	
	return "Successful Update";

data = json.loads(open('data/employees.json').read());
static_path = os.path.join("..\static")
application = tornado.web.Application([
(r"/api/?.*", MainHandler),
(r'/(.*)', tornado.web.StaticFileHandler, {'path': static_path, "default_filename": "index.html"})
]);

application.listen(8888);
tornado.ioloop.IOLoop.instance().start()