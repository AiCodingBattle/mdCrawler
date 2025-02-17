Skip to content
Menu
On this page
# Adding a new service template to Coolify ​
Services in Coolify are templates made from normal docker-compose files with some added Coolify magic.
INFO
See Coolify's docker-compose specs to learn more about Coolify's magic and how to benefit from generated variables and storage handling. Please use this magic when submitting your PR to make the merging process smoother.
  1. Add metadata
At the top of your `docker-compose` file, add the following metadata:
yaml```
# documentation: https://docs.example.com/
# slogan: A brief description of your service.
# tags: tag1,tag2,tag3
# logo: svgs/your-service.svg
# port: 1234
```

     * `documentation`: Link to the service's official documentation
     * `slogan`: A short description of the service
     * `tags`: Comma-separated list for better searchability
     * `logo`: Path to the service's logo (see step 3)
     * `port`: The main entrypoint port of the service


Caution
Always specify a port, as Caddy Proxy cannot automatically determine the service's port.
  1. Create the docker-compose file
Below the metadata, add your docker-compose configuration. Use Coolify's environment variable magic here.
Example:
yaml```
version: '3.8'
services:
 app:
  image: your-service-image:tag
  environment:
   - DATABASE_URL=${COOLIFY_DATABASE_URL}
  volumes:
   - ${COOLIFY_VOLUME_APP}:/data
```

  2. Add a logo
     * Create or obtain an SVG logo for your service (strongly preferred format)
     * If SVG is unavailable, use a high-quality.webp or JPG as a last resort
     * Add the logo file to the `svgs` folder in the Coolify repository
     * The logo filename should match the docker-compose service name exactly 
       * For example, if your service name is `wordpress`, your logo should be `wordpress.svg` and the final path then is `svgs/wordpress.svg` use this path in the `logo` metadata.
  3. Test your template
Use the `Docker Compose` deployment option in Coolify to test your template. This process mimics the one-click service deployment.
  4. Submit a Pull Request
Once your template works correctly:
     * Open a PR
     * Add your new `<service>.yaml` compose file under `/templates/compose`
     * Include the logo file in the `svgs` folder


INFO
Coolify uses a parsed version of the templates for deployment.
## Request a new service ​
If there's a service template you'd like to see in Coolify:
  1. Search GitHub discussions for existing requests.
  2. If the service has been requested, upvote it. If not, create a new request.


