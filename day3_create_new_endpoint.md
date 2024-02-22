**                CREATING NEW ENDPOINT IN OUR FLASK APPLICATION
* Creating an endpoint is nothing but creating a api,create an endpoint named as 
"greeting" in flask our flask application.
   add the below python code in method() portion in your flask application(app.py)
  *      @app.route('/greeting')
  
         def greeting():
  
         return 'Welcome to my flask application'
* Run your flask application after adding new endpoint  
               
  *           SYNTAX : python app.py
* result:  

   *          Serving Flask app 'app'
  
              Debug mode: on

              Running on all addresses (0.0.0.0)

              Running on http://127.0.0.1:5000

              Running on http://172.20.10.3:5000

              Press CTRL+C to quit

              Restarting with stat

              Debugger is active!

              Debugger PIN: 601-377-110

* once flask application is started we should call any one of the above IP_ADDRESS into web browser
 
* copy IP_ADDRESS( 172.20.10.3:5000/greeting ) and paste in url field of any webapplication
  
* If everything goes right you can see the greeting displayed in you web application as below
        
  *     " Welcome to my flask application "