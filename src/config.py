class DevConfig():
    DEBUG = True

config = {
    'development': DevConfig,
    #'MONGO_URI': 'mongodb://localhost:27017/registraduria'
    'MONGO_URI':'mongodb+srv://yaneth:yaneth@cluster0.wintjaq.mongodb.net/?retryWrites=true&w=majority'
}