## PWA

The first thing in PWA is to make `manifest.json` and serve it to browser to make it 
understand that its a mobile friendly web app.

## Hello PWA 

Here are the list of docs found helpful while doing PWA.

### What a service worker can do:-

* **Improve performance of your application/site**
Caching resources (files) will make content load faster under most network conditions.

* **Make your app "offline-first"**
Using the Fetch API inside a service worker, we can intercept network requests and then modify the response with content other than the requested resource.

* **Act as the base for advanced features**
Service workers provide the starting point for features that make web applications work like native apps. Some of these features are:

    * **Notifications API:**
    A way to display and interact with notifications using the operating system's native notification system.
    * **Push API:**
    An API that enables your app to subscribe to a push service and receive push messages. 
    * **Background Sync API:**
    Lets you defer actions until the user has stable connectivity.
    * **Channel Messaging API:**
    Lets web workers and service workers communicate with each other and with the host application. Examples of this API       include new content notification and updates that require user interaction.


## Service workers are also intended to be used for such things as:

* Background data synchronization
* Responding to resource requests from other origins
* Receiving centralized updates to expensive-to-calculate data such as geolocation or gyroscope, so multiple pages can make  use of one set of data
* Client-side compiling and dependency management of CoffeeScript, less, CJS/AMD modules, etc. for dev purposes
* Hooks for background services
* Custom templating based on certain URL patterns
* Performance enhancements, for example pre-fetching resources that the user is likely to need in the near future, such as the next few pictures in a photo album.
