# Flask_Blogging

'''bash
'''bash
(Flask_Bag) rakesh@rakesh-ThinkPad-L440:~/Desktop/Flaskkk/Flask_Blogging$ python
Python 3.7.11 (default, Jul 27 2021, 14:32:16) 
[GCC 7.5.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from flask_bcrypt import  Bcrypt
>>> bcrypt = Bcrypt()
>>> bcrypt.generate_password_hash('testing')
b'$2b$12$xHgvlY9BA2aPNeKAb4keEeF.4M1YC5COAw7VBCoVt7ll/JCDeZNNK'
>>> bcrypt.generate_password_hash('testing').decode('utf-8')
'$2b$12$89pngNYjxStuUk61cZwmxefBcCpY96npyE/HiRNz/saH6YubTF5lC'
>>> bcrypt.generate_password_hash('testing').decode('utf-8')
'$2b$12$R67L.K9Scng3fLxpH3AY1u.XDP7pRU6uOCnsk2mYYP.19HkZeJ7z2'
>>> hashed_pw = bcrypt.generate_password_hash('testing').decode('utf-8')
>>> bcrypt.check_password_hash(hashed_pw,'password')
False
>>> bcrypt.check_password_hash(hashed_pw,'testing')
True
>>> 

'''