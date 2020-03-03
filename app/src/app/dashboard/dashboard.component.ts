import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Data } from '../data';


@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {

  title = 'app';
  data: Data[];
  url = 'http://localhost:4000/results';
  year = [];
  count = [];

  public lineChartData: Array<any> = [
    {data: this.count, label: 'Python Language'},
  ];
  public lineChartLabels: Array<any> = this.year;
  public lineChartOptions: any = {
    responsive: true
  };
  public lineChartColors: Array<any> = [
    {
      backgroundColor: 'rgba(148,159,177,0.2)',
      borderColor: 'rgba(148,159,177,1)',
      pointBackgroundColor: 'red',
      pointBorderColor: 'red',
      pointHoverBackgroundColor: '#fff',
      pointHoverBorderColor: 'rgba(148,159,177,0.8)'
    }
  ];
  public lineChartLegend: Boolean = true;
  public lineChartType: String = 'line';

  constructor(private httpClient: HttpClient) { }

  ngOnInit(): void {
    this.httpClient.get(this.url).subscribe((res: Data[]) => {
      this.data = res.filter(r => {
        return r.name === 'Python';
      });
      this.data.forEach(y => {
        this.year.push(y.year);
        this.count.push(y.count);
      });
    });
  }
  
  
  
}
