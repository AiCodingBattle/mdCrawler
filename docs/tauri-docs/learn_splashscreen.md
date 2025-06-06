Skip to content
# Splashscreen
In this lab we’ll be implementing a basic splashscreen functionality in a Tauri app. Doing so is quite straight forward, a splashscreen is effectively just a matter of creating a new window that displays some contents during the period your app is doing some heavy setup related tasks and then closing it when setting up is done.
## Prerequisites
## Steps
  1. ##### Install dependencies and run the project
Before you start developing any project it’s important to build and run the initial template, just to validate your setup is working as intended.
Show solution
```

# Make sure you're in the right directory
cdsplashscreen-lab
# Install dependencies
pnpminstall
# Build and run the app
pnpmtauridev

```

![Successful run of the created template app.](https://v2.tauri.app/_astro/step_1._Ugp-O91_2riBWF.webp)
  2. ##### Register new windows in `tauri.conf.json`
The easiest way of adding new windows is by adding them directly to `tauri.conf.json`. You can also create them dynamically at startup, but for the sake of simplicity lets just register them instead. Make sure you have a window with the label `main` that’s being created as a hidden window and a window with the label `splashscreen` that’s created as being shown directly. You can leave all other options as their defaults, or tweak them based on preference.
Show solution
src-tauri/tauri.conf.json```

{
"windows": [
{
"label": "main",
"visible": false
},
{
"label": "splashscreen",
"url": "/splashscreen"
}
]
}

```

  3. ##### Create a new page to host your splashscreen
Before you begin you’ll need to have some content to show. How you develop new pages depend on your chosen framework, most have the concept of a “router” that handles page navigation which should work just like normal in Tauri, in which case you just create a new splashscreen page. Or as we’re going to be doing here, create a new `splashscreen.html` file to host the contents.
What’s important here is that you can navigate to a `/splashscreen` URL and be shown the contents you want for your splashscreen. Try running the app again after this step!
Show solution
/splashscreen.html```

<!doctypehtml>
<htmllang="en">
<head>
<metacharset="UTF-8" />
<linkrel="stylesheet"href="/src/styles.css" />
<metaname="viewport"content="width=device-width, initial-scale=1.0" />
<title>Tauri App</title>
</head>
<body>
<divclass="container">
<h1>Tauri used Splash!</h1>
<divclass="row">
<h5>It was super effective!</h5>
</div>
</div>
</body>
</html>

```

![The splashscreen we just created.](https://v2.tauri.app/_astro/step_3.Cjc3aTae_fcnHV.webp)
  4. ##### Start some setup tasks
Since splashscreens are generally intended to be used for the sake of hiding heavy setup related tasks, lets fake giving the app something heavy to do, some in the frontend and some in the backend.
To fake heavy setup in the frontend we’re going to be using a simple `setTimeout` function.
The easiest way to fake heavy operations in the backend is by using the Tokio crate, which is the Rust crate that Tauri uses in the backend to provide an asynchronous runtime. While Tauri provides the runtime there are various utilities that Tauri doesn’t re-export from it, so we’ll need to add the crate to our project in order to access them. This is a perfectly normal practice within the Rust ecosystem.
Don’t use `std::thread::sleep` in async functions, they run cooperatively in a concurrent environment not in parallel, meaning that if you sleep the thread instead of the Tokio task you’ll be locking all tasks scheduled to run on that thread from being executed, causing your app to freeze.
Show solution
```

# Run this command where the `Cargo.toml` file is
cdsrc-tauri
# Add the Tokio crate
cargoaddtokio
# Optionally go back to the top folder to keep developing
# `tauri dev` can figure out where to run automatically
cd..

```

src/main.ts```

// These contents can be copy-pasted below the existing code, don't replace the entire file!!
// Utility function to implement a sleep function in TypeScript
functionsleep(seconds:number):Promise<void> {
returnnewPromise(resolve=>setTimeout(resolve,seconds*1000));
}
// Setup function
asyncfunctionsetup() {
// Fake perform some really heavy setup task
console.log('Performing really heavy frontend setup task...')
awaitsleep(3);
console.log('Frontend setup task complete!')
// Set the frontend task as being completed
invoke('set_complete', {task: 'frontend'})
}
// Effectively a JavaScript main function
window.addEventListener("DOMContentLoaded", ()=> {
setup()
});

```

/src-tauri/src/lib.rs```

// Import functionalities we'll be using
use std::sync::Mutex;
use tauri::async_runtime::spawn;
use tauri::{AppHandle, Manager, State};
use tokio::time::{sleep, Duration};
// Create a struct we'll use to track the completion of
// setup related tasks
struct SetupState {
frontend_task: bool,
backend_task: bool,
}
// Our main entrypoint in a version 2 mobile compatible app
#[cfg_attr(mobile, tauri::mobile_entry_point)]
pubfnrun() {
// Don't write code before Tauri starts, write it in the
// setup hook instead!
tauri::Builder::default()
// Register a `State` to be managed by Tauri
// We need write access to it so we wrap it in a `Mutex`
.manage(Mutex::new(SetupState {
frontend_task:false,
backend_task:false,
}))
// Add a command we can use to check
.invoke_handler(tauri::generate_handler![greet, set_complete])
// Use the setup hook to execute setup related tasks
// Runs before the main loop, so no windows are yet created
.setup(|app| {
// Spawn setup as a non-blocking task so the windows can be
// created and ran while it executes
spawn(setup(app.handle().clone()));
// The hook expects an Ok result
Ok(())
})
// Run the app
.run(tauri::generate_context!())
.expect("error while running tauri application");
}
#[tauri::command]
fngreet(name: String) -> String {
format!("Hello {name} from Rust!")
}
// A custom task for setting the state of a setup task
#[tauri::command]
asyncfnset_complete(
app: AppHandle,
state: State<'_, Mutex<SetupState>>,
task: String,
) -> Result<(), ()> {
// Lock the state without write access
letmutstate_lock=state.lock().unwrap();
matchtask.as_str() {
"frontend"=>state_lock.frontend_task =true,
"backend"=>state_lock.backend_task =true,
_=>panic!("invalid task completed!"),
}
// Check if both tasks are completed
ifstate_lock.backend_task &&state_lock.frontend_task {
// Setup is complete, we can close the splashscreen
// and unhide the main window!
letsplash_window=app.get_webview_window("splashscreen").unwrap();
letmain_window=app.get_webview_window("main").unwrap();
splash_window.close().unwrap();
main_window.show().unwrap();
}
Ok(())
}
// An async function that does some heavy setup task
asyncfnsetup(app: AppHandle) -> Result<(), ()> {
// Fake performing some heavy action for 3 seconds
println!("Performing really heavy backend setup task...");
sleep(Duration::from_secs(3)).await;
println!("Backend setup task completed!");
// Set the backend task as being completed
// Commands can be ran as regular functions as long as you take
// care of the input arguments yourself
set_complete(
app.clone(),
app.state::<Mutex<SetupState>>(),
"backend".to_string(),
)
.await?;
Ok(())
}

```

  5. ##### Run the application
You should now see a splashscreen window pop up, both the frontend and backend will perform their respective heavy 3 second setup tasks, after which the splashscreen disappears and the main window is shown!


## Discuss
##### Should you have a splashscreen?
In general having a splashscreen is an admittance of defeat that you couldn’t make your app load fast enough to not need one. In fact it tends to be better to just go straight to a main window that then shows some little spinner somewhere in a corner informing the user there’s still setup tasks happening in the background.
However, with that said, it can be a stylistic choice that you want to have a splashscreen, or you might have some very particular requirement that makes it impossible to start the app until some tasks are performed. It’s definitely not _wrong_ to have a splashscreen, it just tends to not be necessary and can make users feel like the app isn’t very well optimized.
© 2025 Tauri Contributors. CC-BY / MIT
