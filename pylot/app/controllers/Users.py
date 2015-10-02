"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.

            self.load_model('WelcomeModel')
        """
        self.load_model('User')
        # self.load_model('Friendship')

    """ This is an example of a controller method that will load a view for the client """


    def create(self):
        reg_info = {
            'first_name':request.form['first_name'].capitalize(),
            'last_name':request.form['last_name'].capitalize(), 
            'username':request.form['username'].capitalize(), 
            'email':request.form['email'], 
            'password':request.form['password'], 
        }

        created_status = self.models['User'].create_user(reg_info)

        if created_status['status'] == True:
            session['id'] = created_status['user']['id']
            # session['name'] = created_status['user']['name']
            return redirect("/")
        else:
            for message in created_status['errors']:
                flash (message, 'regis_errors')
        return redirect('/')
        
        


    def login(self):
        # session.pop('id')
        log_info ={
            'email':request.form['email'],
            'password':request.form['password']
        }
        login_attemp = self.models['User'].login(log_info)
        if login_attemp['status'] == True:
            session['id'] = login_attemp['user']['id']
            print session['id']
            return redirect ("/Users/home/{}".format(login_attemp['user']['id']))
        else:
            flash(login_attemp['message'])
        return redirect('/')


    def logout(self):
        session.pop('id')
        return redirect('/')









