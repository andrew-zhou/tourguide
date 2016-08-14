# tourguide
A simple web service for re-routing queries to urls and custom scripts built using [Flask](http://flask.pocoo.org/) and [Python 3](https://www.python.org/).

Consider the sample list of aliases:
```
{
  "test": "http://www.reddit.com",
  "script": "$sample_script"
}
```
Making a GET request to `/alias/test` will redirect the client to `http://www.reddit.com`.

Making a GET request to `alias/script` will run `sample_script()` in `scripts.py`.

Making a GET request to `alias/script%20foo:bar%20abc:def` (note that %20 is a space) will run `sample_script(foo: 'bar', abc: 'def')` in `scripts.py`.

## Basic Setup
Install [Python >=3.5.2](https://www.python.org/downloads/). Clone this repo and edit the `aliases.json` file with the desired list of aliases (see [Aliases](#aliases) for details). For local setup, run the following in your console:
```
pip install -r requirements.txt
export FLASK_APP=server.py
python -m flask run
```
By default, tourguide will be running on port 5000 of localhost, so a GET request to `localhost:5000/alias/<query>` will redirect to the route defined in `aliases.json` for `query`.

## Tests
The test suite is written using Python's [`unittest` module](https://docs.python.org/3.5/library/unittest.html).

To run the test suite, run the following in your console:
```
nosetests
```

## Aliases
tourguide provides a single endpoint: `GET /alias/<query>`. The query is mapped to an alias string through `aliases.json`.

Alias strings can take on two forms: traditional HTTP urls and function names. To map a query to a HTTP url, simply add an item to `aliases.json` in the form:
```
"<query>": "<http_url>"
```

Alternatively, tourguide allows for script aliases, which are function names prefixed by a dollar sign ($). When the client makes a request with a query that routes to a script alias, the server makes a call to the corresponding function inside `scripts.py`. To map a query to a function, add an item to `aliases.json` in the form:
```
"<query>": "$<function_name>"
```

You must then define and implement a function with that name in `scripts.py`. These functions should always return a `flask.redirect` object and should take in `**kwargs` as its sole parameter.

Clients can pass in keyword arguments to these functions by adding key-value pairs in the form of `<key>:<value>` to their request. Each of these pairs should be separated from other pairs and the query by whitespace. These requests should look like:
```
/alias/query key1:value1 key2:value2 key3:value3 ...
```
