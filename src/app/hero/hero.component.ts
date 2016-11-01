import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-hero',
  templateUrl: './hero.component.html',
  styleUrls: ['./hero.component.css']
})

export class HeroComponent implements OnInit {
  fullImagePath: string;

  constructor() {
    this.fullImagePath = 'assets/images/hero-mountains.png'
  }

  ngOnInit() {
  }

}
