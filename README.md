import { Component } from '@angular/core';

@Component({
  selector: 'app-your-component',
  templateUrl: './your-component.component.html',
  styleUrls: ['./your-component.component.css']
})
export class YourComponent {

  constructor() {}

  showAlert(): void {
    const confirmation = confirm('Shall I proceed?');
    if (confirmation) {
      alert('Thank you');
    }
  }
}
