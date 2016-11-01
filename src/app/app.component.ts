import {Component, OnInit} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {Http, Response, RequestOptions, Headers} from '@angular/http';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  title = 'app works!';

  constructor(public http:Http) {

  }

  ngOnInit() {
    this.http.request('/')
      .subscribe((res:Response) => {
        console.log(res.headers);
        res.headers.set('Cache-Control', 'max-age=86400')
      });
  }
}
