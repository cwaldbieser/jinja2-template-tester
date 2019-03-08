
Jinja2 Template Tester
======================

Test jinja2 templates.

Example:

.. code:: shell

    $ cat test.json

    {
        "givenName": ["Carl"],
        //"displayName": ["Carl"],
        "sn": ["Waldbieser"],
        "netid": ["waldbiec"]
    }
    $ cat test.jinja2 

    GN : {{data.givenName | first}}
    PFN: {{data.displayName | first}}
    SN : {{data.sn | first}}
    UID: {{data.netid | first}}
    $ pipenv run ./jinja2test.py ./test.json ./test.jinja2 

    GN : Carl
    PFN: 
    SN : Waldbieser
    UID: waldbiec
    waldbiec@waldbiec-Latitude-7490:~/git-repos/jinja2-test$ 

