from configparser import ConfigParser

def config(filename='database.ini', section='postgresql'):
    # create parser
    parser = ConfigParser()
    
    # read config file
    parser.read(filename)
    
    db ={}
    # if the database has sections
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    # else raise an error
    else:
        raise Exception('Section {} is not found in the file {}'.format(section, filename))
    
    return db
    
config()