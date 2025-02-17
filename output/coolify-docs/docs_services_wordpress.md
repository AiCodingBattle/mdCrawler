Skip to content
Menu
On this page
![Wordpress](https://raw.githubusercontent.com/logo/wordpress/caefc9aa315eafcf8687804564a11a9c5a77a561/images/logo.svg)
## What is Wordpress? ​
Wordpress is a free and open-source content management system written in PHP and paired with a MySQL/MariaDB database. It is used for creating websites, blogs, and applications.
## Links ​
  * The official website ›
  * GitHub ›


## FAQ ​
### How to increase the upload size limit? ​
You can increase the upload size limit by following these steps:
  1. Open the `.htaccess` file through Coolify's Terminal (or through SSH, and docker exec -ti `container_id` /bin/sh)
  2. Add the following lines to the end of the file with `vi` or `nano`:


php```
# END WordPress - this line already exists in the file
php_value upload_max_filesize 256M
php_value post_max_size 256M
php_value max_execution_time 300
php_value max_input_time 300
```

  1. Save and close the file.
  2. Reload the website in your browser. The changes should be applied automatically.


### How to Fix a Redirection Loop in WordPress? ​
If your WordPress site is stuck in a redirection loop, follow these steps to resolve the issue:
Access the .htaccess file:
  1. Open the `.htaccess` file through Coolify's Terminal (or through SSH, and docker exec -ti `container_id` /bin/sh)
  2. Navigate to the WordPress root directory and locate the .htaccess file. Edit the .htaccess file:


```
<IfModule mod_setenvif.c>
 SetEnvIf X-Forwarded-Proto "^https$" HTTPS
</IfModule>
```

  1. Save and close the file.
  2. Reload the website in your browser. The changes should be applied automatically.


