# 서버!
from http.server import BaseHTTPRequestHandler, HTTPServer 
import logging

class MyHandler(BaseHTTPRequestHandler):
    def do_POST(self):   
      #send code 200 response  
      self.send_response(200) 
      self.send_header('Content-type','text/html')  
      self.end_headers()  
      content_length = int(self.headers['Content-Length'])
      post_data = self.rfile.read(content_length)
      logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                str(self.path), str(self.headers), post_data.decode('utf-8'))
      print('\n'+post_data.decode('utf-8')+'\n')
      
      return  

def run(server_class=HTTPServer, handler_class=MyHandler, port=8080):  
  print('http server is starting...')  
  server_address = ('', 8080)
  httpd = HTTPServer(server_address, handler_class)
  logging.info('Starting httpd...\n')
  print('http server is running...')  
  try:
    httpd.serve_forever()
  except KeyboardInterrupt:
    pass
  httpd.server_close()
  logging.info('Stopping httpd...\n')

if __name__ == '__main__':  
  run()
# 이건 서버야. 알겠어?