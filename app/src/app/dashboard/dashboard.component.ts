import { Component, OnInit } from '@angular/core';
import { RestService } from '../rest.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.less']
})
export class DashboardComponent implements OnInit {
  years = [ '2019', '2018' ];
  selectedYear = '2020';
  
  artists:any = [];
  constructor(private rest:RestService) { }

  ngOnInit(): void {
    this.getArtists();
  }

  getArtists() {
    this.artists = [];
    this.rest.getArtists('52-2019').subscribe((data: {}) => {
      console.log(data);
      this.artists = data;
    });
  }
}
