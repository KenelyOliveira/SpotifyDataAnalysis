import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { map, catchError, tap } from 'rxjs/operators';

const endpoint = 'http://localhost:4193/api/';
const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type':  'application/json',
    
  })
};

@Injectable({providedIn:'root'})
export class RestService {

  private extractData(res: Response) {
    let body = res;
    return body || { };
  }

  getArtists(date): Observable<any> {
    return this.http.get(endpoint + 'artists/'+ date).pipe(
      map(this.extractData)
    );
  }

  constructor(private http: HttpClient) { }
}
