Lego MiniFigs E-commerce Webpage: http://minifigs.spookyai.com/

1. project framework. simple introduce to our project
- E-commerce about Lego MiniFigures
- Basic functions: register, browse, buy and sell mini figures

#William

2. create ERD; set up table relationships;
#William

3. Create our own API; 
- scrape from Lego website;
- use beautifulsoup to scrape these data;
- save it into Json files;
#Kevin

4. use SQL Alchemy to build tables in database;
- import our Json files; 
- create models and class, attributes, table rows;
- build relationships and join tables;
- create queries to make HTML functional; 
#Kevin

5. HTML templates
- use jinja template to extract reusable component out of HTML page. Like header, navbar and footer
So we save some time on HTML part and code complexity;

We heavily use JQuery and Ajax in our project.
It can help us to fetch data asynchronously and update html content dynamically; 
So that we can update partial content without refreshing entire page.

For example, when I click this drop down to make selection, I can get the data without refreshing the whole page, which gives better user experience;

Also, We applied JQuery to do auto completion fields like when I input in search bar, it will trigger a JS event on text change. In background the app calls the backend to get search suggestions.

Lastly, this pagination feature is also built on top of JQuery and Ajax.
When I clicked the page number, the page will anchor to the top and update accordingly;

Did some research on caching technology;
Because this can minimize latency and reduce database query times;

We decided to use memory caching in our project because our app is relatively a small scale project.

Compared to redis and memcache, memory is easier to set up without extra dependency. 
In future, we might swap out the cache backend to use redis or memcache to make cache persist when application restarts.

We used Github to collaborate with team members so that we can do our parts separately.
We learned a lesson that we should commit code change as frequently as possible after completing a small feature. Because we have accidentally discard changes during live sharing;


#Tracy 

Technology:
language: Python--backend API to interact with frontend, use MVC model;
HTML5, CSS, Javascript --frontend for visualizintg website
framework: flask
Database: MySQL--data store and import and validate;
 (Apply Flask build-in methods like flask-webforms, login, validators, Migrate to our project)
-scrape tool: beautifulsoup and Json file read, write;
-jQuerry (AJAX, API)
-SQL Alchemy
-Apply cache to minimize latency and reduce query times;
-Docker to run all the service components and AWS Hosting to deploy the project;


Future optimize project:
use redis cache;
use CDN to serve html, js script, css and images;
permanent session lifetime flask;
SSL to secure connections;


