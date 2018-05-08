Homework 11: Add Search and GIS Computatibilty to Elegant Props
====

TODO: properties App Search
----

Useful reference: https://github.com/rmedinahu/cs350lab12/blob/master/README.md

Add a search form to the property app that allows a user to query the **description** attribute of all property listings. Form should return all properties that contain at least one occurrence of the query in the description.

TODO: properties App Search by Geolocation
----

Add a search form to the property app that allows a user to query those properties that are within range of a user inputted address and user inputted number of miles. For example, retrieve all properties that are within 200 miles of 1314 chavez st., las vegs, nm.

Useful reference: https://github.com/rmedinahu/cs350lab12/blob/master/README.md

* Please study Lab 12 to understand how to use Geopy to compute distance between two Location objects.

### 7. You can use the same template created in step 3 above as long as your view (step 5) creates the same template variable used in the previous search component.

### 10. Add two unit tests to properties/tests.py. The tests should test the two views you created above. The key test is to count the number of properties stored in the context variable that stores the results of each query. See the following example in the lab12 repository for a guide. Note that you will have to construct a query parameter string relevant to your forms.

https://github.com/rmedinahu/cs350lab12/blob/master/geoquery/tests.py

## Done.