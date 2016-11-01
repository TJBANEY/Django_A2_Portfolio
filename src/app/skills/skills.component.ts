import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-skills',
  templateUrl: './skills.component.html',
  styleUrls: ['./skills.component.css']
})
export class SkillsComponent implements OnInit {
  info: string;
  skills_list: any = {
    'python': 'Python is probably my strongest skill. I vehemently promote this awesome easy to read, beautifully written code as the backend language of choice, and have worked on more than 12 web apps whose server side was written in python, …and a battleship script !',
    'node': 'I typically only use node.js for package management, and requiring dependencies into my gulpfile for task running, however I am familiar with the server side language, and  have also played around with the Express framework in the past.',
    'angular2': 'This site is completely done in Angular2. I have been teaching myself Angular2 for the past couple of months, even attending a conference to prepare myself for the stable release and all its glory. I also have experience creating applications with Angular.',
    'django': "I have been professionally creating and contributing to content managed Django applications using the Pycharm IDE since February of 2016 at Mill Creek Software. I also have experience in Flask, and creating RESTful APIs with Django’s REST Framework.",
    'responsive': 'I am skilled in creating responsive web applications using bootstrap and media queries to create smooth style transitions between multiple screen sizes.',
    'basics': 'I have strong foundations in all the basics of web dev such as CSS3, HTML5, and EcmaScript5. I also use LESS to create well organized stylesheets, and can use JQuery for anything from page animations to asynchronous backend calls and functions.',
    'bootstrap': 'A lot of the web apps I contribute to use bootstrap to create smooth responsive, mobile first designs.',
    'bower': 'Some development tools that I can use include, but aren’t limited to: NPM, and Bower as package managers, Gulp as a task runner, PyCharm, Atom, and Sublime for IDEs and Text Editing, Bitbucket, Github, Slack, Photoshop, and Postman for API testing.',
    'treehouse': 'I have a Python tech degree from Treehouse, an online coding tutorial site. The degree is a projected 12 month course consisting of 22 lessons, 72 quizzes, over 200 challenges, and 12 required projects.',
    'phoenix': 'I attended the University of Phoenix …. In Phoenix in June of 2015, where I received certification for an immersive 3 month course in front end web development called RockIT Bootcamp. The course taught front end skills like CSS, HTML, and client/server-side Javascript.'
  };

  constructor() { }

  ngOnInit() {
  }

  showSkillInfo(event) {
    this.info = this.skills_list[event];
  }

}
