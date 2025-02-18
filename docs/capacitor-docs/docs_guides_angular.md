Skip to main content
An **OutSystems** Company →
Version: v7
On this page
## NgZone​
Capacitor plugin event listeners run outside of Angular's `NgZone` execution context. Contain handler logic within an `NgZone.run` block to ensure Angular's change detection is triggered:
```
constructor(private ngZone: NgZone){}asyncngOnInit(){ Network.addListener("networkStatusChange",(status)=>{this.ngZone.run(()=>{// This code will run in Angular's execution contextthis.networkStatus = status.connected ?"Online":"Offline";});});}
```

## Contents
  * NgZone


Edit this page![](https://images.prismic.io/ionicframeworkcom/50ede1c5-d69d-4c9d-bf0d-4c9ab7c14724_doc-ad-appflow.png?auto=compress,format&rect=0,0,280,200&w=280&h=200)
Mobile CI/CD made easy. Build, publish, and update from the cloud.
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=802059049&_biz_u=ed6d98ad223740ddbf99774ce8c4ab02&_biz_l=https%3A%2F%2Fcapacitorjs.com%2Fdocs%2Fguides%2Fangular&_biz_t=1739811926374&_biz_i=Capacitor%20Documentation&_biz_n=34&rnd=284380&cdn_o=a&_biz_z=1739811926374)
