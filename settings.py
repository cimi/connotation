import ConfigParser

config = ConfigParser.ConfigParser()
config.read('settings.cfg')

print config.get('Algorithm', 'name')
print config.get('Corpus', 'name')
print config.get('Data', 'name')
