import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.less']
})
export class DashboardComponent implements OnInit {
  years = [ '2019', '2018' ];
  selectedYear = '2020';
  constructor(private httpClient: HttpClient) { }

  ngOnInit(): void {
    
  }
}
