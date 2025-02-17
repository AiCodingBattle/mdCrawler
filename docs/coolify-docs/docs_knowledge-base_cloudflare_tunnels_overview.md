Skip to content
Menu
On this page
# Cloudflare Tunnels ​
Cloudflare Tunnels ↗ allow you to securely expose your local server or applications to the internet without opening ports on your router.
This makes them a great option for hosting projects on devices like old laptops or Raspberry Pis.
## Why Use Cloudflare Tunnels? ​
  * No need to open or forward ports on your device to the public internet.
  * Simplifies routing and DNS configuration.
  * Supports exposing a single application or multiple services.
  * Hides your server's IP address by routing traffic through a Cloudflare Tunnel, showing only your domain.
  * Works even if you have a dynamic IP (or) no public IP at all.
  * Eliminates the hassle of managing and setting up SSL certificates.


## When Not to Use Cloudflare Tunnels? ​
  * If you prefer direct access to your server without a proxy layer.
  * If you're concerned about routing traffic through Cloudflare's servers.
  * If you rely on additional firewall tools, as Cloudflare Tunnels bypass all firewall rules.
  * If you need SSL certificates trusted by entities other than Cloudflare.


## Ways to Use Cloudflare Tunnels with Coolify ​
You can set up Cloudflare Tunnels with Coolify in several ways, depending on your needs. Below are the available options, each linked to a detailed guide for easy setup:
  1. All Resources -> Use a tunnel for all resources deployed through Coolify. This is the **easiest** and **most recommended** way for beginners.
  2. Single Resource -> Use a tunnel for a single resource deployed through Coolify.
  3. Server SSH Access -> Securely connect your server to Coolify using a domain through Cloudflare Tunnel.
  4. Full HTTPS/TLS -> Setup always-on **HTTPS** for all domains and subdomains. Normally, Coolify uses **HTTP** while Cloudflare manages **HTTPS**. If certain apps require **HTTPS** directly on Coolify.


Tip:
It’s highly recommended to go with the first option All Resources if you're new to Coolify and Cloudflare Tunnels, as it’s much easier to set up and manage.
