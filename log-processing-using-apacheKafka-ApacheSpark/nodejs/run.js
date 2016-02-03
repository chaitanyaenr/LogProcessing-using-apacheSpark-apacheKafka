var httpd= require('http');
var fs=require('fs');
httpd.createServer(function(req,res)
{
        res.writeHead(200, {'Content-Type' : 'text/plain'});
        res.end("Serving content A web server is an information technology that processes requests via HTTP, the basic network protocol used to distribute information on the World Wide Web. The term can refer either to the entire computer system, an appliance, or specifically to the software that accepts and supervises the HTTP requests");
}).listen(8112);
console.log('webserver started on 8112');

