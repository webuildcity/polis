Polis City Demo - powered by the Open Source project We-Build.City
====================================

Polis - is the Demo Instance of the Smart City Planning Platform of We-build.City [polis.we-build.city][polis]  


More about the OpenSource project: [we-build.city][we-build-city] or the company and services: [services.we-build.city][wbc-services]  


## How to setup your own city instance:

1. Have Python 2.7.x installed.
(1.1 brew install [GDAL][gdal] ) 
2. Clone [https://github.com/webuildcity/wbc][wbc-github] to a location of your choice.
3. Clone this repository, [https://github.com/webuildcity/polis][polis-github], to a location of your choice.
3.1 Rename the sub-directory "polis" to your own "city name" i.e. "paris". 
4. Make a copy of your local settings:
4.1 Copy `/path/to/polis/city/default.local.py` to `/path/to/polis/city/local.py`.
4.2 Edit `/path/to/polis/city/local.py` to match your setup. 

4.3 Edit the path to the 'wbc' library directory within the 'wbc' repository and update the database adapter settings. For testing purposes, use the sqlite3 adapter.
4.4 Edit the `HAYSTACK_CONNECTIONS` block, edit the name of the index.

7. Install the dependencies using pip `pip install -r /path/to/city/requirements.txt`. You might want to use a [virtualenv][virtualenv] for this.
8. Change to the home-directory of the city repository and execute `python manage.py migrate` to set up the database structure.

9. Use `python manage.py load-fixtures` to load test data of the administrative information about our "polis test city" Hamburg into the database.
10. Run `python manage.py createsuperuser` to create an admin account.
11. Start the development server using `python manage.py runserver`.
12. Open a browser and go to [http://localhost:8000/][polis-home]. A map of our "polis test city" Hamburg should appear.
13. Use [http://localhost:8000/admin/][polis-admin] to log in. Under *region* and *process*, districts, departments, places and publications can be added or edited.



[polis]: http://polis.we-build.city
[polis-github]: https://github.com/webuildcity/polis
[wbc-github]: https://github.com/webuildcity/wbc
[django]: https://docs.djangoproject.com/en/1.8/
[virtualenv]: https://virtualenv.pypa.io/en/latest/
[polis-home]: http://localhost:8000/
[polis-admin]: http://localhost:8000/admin/
[gdal]: http://www.gdal.org/
[we-build-city]: http://we-build.city
[wbc-services]: http://services.we-build.city
