"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Requests(Controller):
    def __init__(self, action):
        super(Requests, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.

            self.load_model('WelcomeModel')
        """
        self.load_model('User')
        self.load_model('Request')

    def index(self): #new 
        """ 
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_all_users()
        """
        if "id" in session:
            message = "hi user" + str(session['id'])
            data = self.models['User'].user_info_by_id(session['id'])
            print session['id']

        return self.load_view('index.html', message = message, data=data)

    def home(self, id):
        return



    def add(self):
        print "hello"
        item={

            'description':request.form['description'],
            'helpee':request.form['helpee_name'],
            # 'photo':request.form['event_photo'],
            'latt':request.form['latt'],
            'long':request.form['long'],
            'intersection':request.form['intersection'],
            'user_id':session['id']
        }
        # print item
        self.models['Request'].create_request(item)
        return redirect ('/')

        # return redirect('Users/home/{}'.format(session['id']))

    # def remove(self, friendship_id):
    #     self.models['Friendship'].remove_friend(friendship_id)
    #     return redirect ('/Users/home/{}'.format(int(session['id'])))





    