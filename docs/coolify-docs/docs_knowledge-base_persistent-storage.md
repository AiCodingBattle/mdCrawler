Skip to content
Menu
On this page
# Persistent Storage ​
You could add persistent storage to your resources, so you can preserve your data between deployments.
This persistent storage could be different in different types of Destinations.
## Docker Engine ​
If you are using Docker Engine, persistent storage could be a `volume` or a `bind mount` (a file/directory from the host system - your server).
### Volume ​
To create a volume, you need to define:
  * `Name` of the volume.
  * `Destination Path` where the volume will be mounted inside the container.


Caution
The base directory inside the container is `/app`. So if you need to store your files under `storage` directory, you need to define `/app/storage` as the destination path.
Tip
To prevent storage overlapping between resources, Coolify automatically adds the resource's UUID to the volume name.
### Bind Mount ​
To create a bind mount, you need to define:
  * `Name` of the volume, which will be used as a reference.
  * `Source Path` from the host system. **No docker volume created in this case.**
  * `Destination Path` where the volume will be mounted inside the container.


Caution
The base directory inside the container is `/app`. So if you need to store your files under `storage` directory, you need to define `/app/storage` as the destination path.
Caution
Share file between more than one container? **NOT RECOMMENDED.**
If you mount the same file to more than one container, you will need to make sure that the proper file locking mechanism is implemented in your resources.
