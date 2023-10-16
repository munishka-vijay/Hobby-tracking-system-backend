class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://root:hehe@localhost/userregsystem' #For connecting to MySQL DB
    SECRET_KEY = '18122022' # FOR TOKEN
    JWT_SECRET_KEY = "jwt" #for JWT
    JWT_ACCESS_TOKEN_EXPIRES = 24 #24 hrs