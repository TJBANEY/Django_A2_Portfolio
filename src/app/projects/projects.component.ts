import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-projects',
  templateUrl: './projects.component.html',
  styleUrls: ['./projects.component.css']
})
export class ProjectsComponent implements OnInit {
  fullBeachImagePath: string;

  constructor() {
    this.fullBeachImagePath = '/assets/images/cleanbeachbg.png'
  }

  ngOnInit() {
  }

}
