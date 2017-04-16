## Roba Square Website  [Robasquare.com](robasquare.com)

#### An e-commerce website developed for the college Jamia Millia Islamia. It has a blogging section as well. Built on Django 1.8 and deployed on Apache server.

Feel free to contribute to its development. In case you need any information or help mail me at msr.concordfly@gmail.com


**About Roba Square**
* An ecommerce website which sells apparels,outfits,gifts and has option for bulk orers
* It has a section for blogging also. Read blogs [here !](https://robasquare.com/blog/)
* The Apache server is secured with Let's Encrypt (for SSL certification)
* Supports social signup and online payment.

**Technologies Used**
* [Django 1.8](https://www.djangoproject.com)
* [Materialize CSS](materializecss.com/)
* JavaScript , Jquery-Ajax
* Django-Allauth
* [Instamojo](instamojo.com) for the payment gateway.

**How to make this project run on your local machine**
* Install all the requirements in a virtual environment with the command `pip install -r requirements.txt`
* `cd src`
* Migrate the database by runninig the commands `python manage.py makemigrations` and `python manage.py migrate`
* Run the server by running `python manage.py runserver`


> The `settings.py` file has been excluded in this repo because it contained private data. In case you need a similar file for knowing the configurations used, mail me at msr.concordfly@gmail.com


  
