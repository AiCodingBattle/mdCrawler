Skip to main content
An **OutSystems** Company →
Version: v7
On this page
When creating unit tests within your application, it is a best practice to create mocks for any external dependency to the unit that is under test. This includes Capacitor plugins that your component or service is using.
Most mocking libraries create mocks by taking an object and wrapping it in a JavaScript proxy so calls to the methods on that object can be examined and the return values of the methods can be controlled. Capacitor plugins, however, are implemented within the JavaScript layer as proxies. Creating a proxy of a proxy is not supported and fails. Manual mocks can be used to circumvent this issue.
## Manual Mocks​
Manual mocks allow the user to easily stub the functionality of an entire JavaScript module. As a result, when the tests do an `import { Storage } from '@capacitor/storage'`, instead of loading the real `Storage` JavaScript proxy object, the tests would load something like this:
```
exportconst Storage ={asyncget(data:{ key:string}):Promise<{ value:string|undefined}>{return{ value:undefined};},asyncset(data:{ key:string; value:string}):Promise<void>{},asyncclear():Promise<void>{},};
```

Since this is a plain JavaScript object and not a proxy object, it is very easy to spy on. Also, since it is a mock it does not try to make any native calls. This makes the use of manual mocks an ideal choice to use when testing code that uses Capacitor plugins.
### Jest​
The Jest testing framework has manual mocks built in to it. Create a `__mocks__/@capacitor` folder at the root of your project, and Jest will automatically load files from there rather than from `node_modules`.
For example, let's say you have the following directory structure:
```
.|+- __mocks__| || +- @capacitor|  ||  +- storage.ts|  +- toast.ts...+- src
```

Your tests will use the stubs defined in `storage.ts` and `toast.ts` rather than the real `@capacitor/storage` and `@capacitor/toast` plugins from `node_modules`.
### Jasmine​
The Jasmine testing framework does not include the concept of "manual mocks" but we can easily simulate this through the use of TypeScript path mapping.
First, create the same directory structure at the root level of your project just like you would for the Jest example.
Angular projects (the most common scenario in which you would be using Jasmine as a testing framework) include a `tsconfig.spec.json` file that extends the `tsconfig.json` base configuration when unit tests are being executed. Modify this file to extend any `paths` mapping you may have at the base level.
For example, if your `tsconfig.json` file contains the following `paths` mapping:
```
"paths":{"@app/*":["src/app/*"],"@env/*":["src/environments/*"]},
```

Then update your `tsconfig.spec.json` file to include those paths plus any you would like to use for the unit tests:
```
"paths":{"@app/*":["src/app/*"],"@env/*":["src/environments/*"],"@test/*":["test/*"],"@capacitor/*":["__mocks__/@capacitor/*"]}
```

Now when the unit tests are compiled, `import { Storage } from '@capacitor/storage';` will use the stub file under `__mocks__/@capacitor` rather than the real one in `node_modules`.
**Note:** the `paths` object is replaced entirely rather than being merged, so if you have any paths defined at in `tsconfig.json` they _must_ also be included in `tsconfig.spec.json`.
## Mocking the Stubs​
With the manual mocks in place, the tests can now be written to mock and spy on the method calls in all of the usual ways.
### Jest​
```
it("gets the first and last name",async()=>{  Storage.get = jest.fn().mockImplementation(async(data:{ key:string}):Promise<{ value:string}>=>{return data.key ==="firstName"?{ value:"Jimmy"}: data.key ==="lastName"?{ value:"Simms"}:{ value:"unknown"};});const w =mount(Home);awaitflushPromises();expect(w.vm.firstName).toEqual("Jimmy");expect(w.vm.lastName).toEqual("Simms");});it("clears the storage",()=>{const button = wrapper.findComponent('[data-testid="clear"]');  Storage.clear = jest.fn().mockResolvedValue(undefined);  button.trigger("click");expect(Storage.clear).toHaveBeenCalledTimes(1);});
```

### Jasmine​
```
it("gets the first and last name",async()=>{spyOn(Storage,'get');(Storage.get asany).withArgs({ key:'firstName'}).and.returnValue(Promise.resolve({ value:'Jason'}));(Storage.get asany).withArgs({ key:'lastName'}).and.returnValue(Promise.resolve({ value:'Jones'}));  fixture.detectChanges();await fixture.whenRenderingDone();expect(component.firstName).toEqual('Jason');expect(component.lastName).toEqual('Jones');});it('clears the storage',()=>{spyOn(Storage,'clear');click(clear.nativeElement);  fixture.detectChanges();expect(Storage.clear).toHaveBeenCalledTimes(1);});
```

## Examples​
  * Mocking Capacitor Plugins in Jasmine
  * Mocking Capacitor Plugins in Jest


## Contents
  * Manual Mocks
    * Jest
    * Jasmine
  * Mocking the Stubs
    * Jest
    * Jasmine
  * Examples


Edit this page![](https://images.prismic.io/ionicframeworkcom/d3d3f7a3-023b-4cdf-93af-84674f623818_portals+ad.png?auto=compress,format&rect=0,0,280,200&w=280&h=200)
Micro Frontends for any React Native, Android, or iOS mobile apps.
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=802059049&_biz_u=ed6d98ad223740ddbf99774ce8c4ab02&_biz_l=https%3A%2F%2Fcapacitorjs.com%2Fdocs%2Fguides%2Fmocking-plugins&_biz_t=1739811931961&_biz_i=Capacitor%20Documentation&_biz_n=44&rnd=25451&cdn_o=a&_biz_z=1739811931962)
