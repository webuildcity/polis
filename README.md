Utopia City Demo - powered by the Open Source project We-Build.City
====================================

Utopia - is the Demo Instance of the Smart City Planning Platform of We-build.City [utopia.we-build.city][utopia]  


More about the OpenSource project: [we-build.city][we-build-city] or the company and services: [services.we-build.city][wbc-services]  


## How to setup your own city instance:

1. Have Python 2.7.x installed.
(1.1 brew install [GDAL][gdal] ) 
2. Clone [https://github.com/webuildcity/wbc][wbc-github] to a location of your choice.
3. Clone this repository, [https://github.com/webuildcity/utopia][utopia-github], to a location of your choice.
3.1 Rename the sub-directory "utopia" to your own "city name" i.e. "paris". 
4. Copy `/path/to/utopia/utopia/default.local.py` to `/path/to/utopia/utopia/local.py`.
5. Edit `/path/to/utopia/utopia/local.py` to match your setup. At least edit the path to the 'lib' directory within the 'wbc' repository and update the database adapter settings. For testing purposes, use the sqlite3 adapter.
6. Install the dependencies using pip `pip install -r /path/to/utopia/requirements.txt`. You might want to use a [virtualenv][virtualenv] for this.
7. Change to the `utopia` directory and execute `python manage.py migrate` to set up the database structure.
8. Use `python manage.py load-fixtures` to load test data of the administrative information about our "utopia test city" Hamburg into the database.
9. Run `python manage.py createsuperuser` to create an admin account.
10. Start the development server using `python manage.py runserver`.
11. Open a browser and go to [http://localhost:8000/][utopia-home]. A map of our "utopia test city" Hamburg should appear.
12. Use [http://localhost:8000/admin/][utopia-admin] to log in. Under *region* and *process*, districts, departments, places and publications can be added or edited.



[utopia]: http://utopia.we-build.city
[utopia-github]: https://github.com/webuildcity/utopia
[wbc-github]: https://github.com/webuildcity/wbc
[django]: https://docs.djangoproject.com/en/1.8/
[virtualenv]: https://virtualenv.pypa.io/en/latest/
[utopia-home]: http://localhost:8000/
[utopia-admin]: http://localhost:8000/admin/
[gdal]: http://www.gdal.org/
[we-build-city]: http://we-build.city
[wbc-services]: http://services.we-build.city