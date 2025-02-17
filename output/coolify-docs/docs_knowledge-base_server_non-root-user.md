Skip to content
Menu
On this page
# Non-root user ​
You could have a server with a non-root user that will manage your resources instead of the root user.
For this to work, you need to set up the server correctly.
Caution
**This is an experimental feature.**
## Requirements ​
  * The non-root user needs to have the SSH key added to the server.
  * Sudos permissions for the non-root user.


## Sudo permissions ​
You need to add the following lines to the `/etc/sudoers` file:
bash```
# Allow the your-non-root-user to run commands as root without a password
your-non-root-user ALL=(ALL) NOPASSWD: ALL
```

This will allow the non-root user to any command as root without a password. Note: you need to replace "your-non-root-user" with your user.
Caution
This is not the most secure way to set up a non-root user, but we will improve this in the future, by adding more granular permissions on binaries.
