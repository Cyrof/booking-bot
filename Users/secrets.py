# import libraries
import base64
import pickle
import os

# file class to create and store user obj into a secret json file


class File():
    def __init__(self):
        self.__wfile = open('./Users/secrets.pkl', 'wb')
        self.__rfile = open('./Users/secrets.pkl', 'rb')

    # write data into secret file
    def write_dict(self, data):
        # json_string = json.dumps(data)
        # json.dump(json_string, self.__wfile)
        # self.__wfile.close()
        # self.__wfile.write(str(data))
        # self.__wfile.close()
        pickle.dump(data, self.__wfile)
        self.__wfile.close()

    # read data from secret file

    def read(self):
        data = pickle.load(self.__rfile)
        self.__rfile.close()
        return data

# user class to contain and store user data


class User(File):
    def __init__(self, username, password):
        self.__username = self.encode(username)
        self.__password = self.encode(password)

    # define basic representation of the obj
    def tostring(self):
        return ("Username : %s\nPassword : %s\n" % (self.__username, self.__password))

    # create encoding & decode function
    def encode(self, data):
        data_byte = data.encode('ascii')
        encoded_msg = base64.b64encode(data_byte)
        encoded_msg = encoded_msg.decode('ascii')
        return encoded_msg

    def decode(self, data):
        data = data.encode('ascii')
        decoded_msg = base64.b64decode(data)
        og_data = decoded_msg.decode('ascii')
        return og_data

    # getter setter functions for username & password
    def get_uname(self):
        return self.decode(self.__username)

    def get_pass(self):
        return self.decode(self.__password)

    def set_uname(self, username):
        self.__username = self.encode(username)

    def set_pass(self, password):
        self.__password = self.encode(password)
    



if __name__ == "__main__":
    user = User('cyrof', '12345')
    user_dict = {"user": user}
    file = File()

    file.write_dict(user_dict)
    data = file.read()
    print(data)
