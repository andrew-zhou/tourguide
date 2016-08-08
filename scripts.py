from flask import redirect

# Create custom scripts here to be ran from certain aliases
# These scripts must return a redirect object from flask
# Each script should take in **kwargs as its sole parameter

def sample_script(**kwargs):
    for key, value in kwargs.items():
        print('{0}: {1}'.format(key, value))
    return redirect('http://www.google.com')
