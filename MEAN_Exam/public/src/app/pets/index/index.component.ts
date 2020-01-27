import { Component, OnInit } from '@angular/core';
import { Router, Params, ActivatedRoute } from '@angular/router';
import { HttpService } from 'src/app/http.service';

@Component({
  selector: 'app-index',
  templateUrl: './index.component.html',
  styleUrls: ['./index.component.css']
})
export class IndexComponent implements OnInit {
  allPets: {}
  constructor(
    private _router: Router,
    private _route: ActivatedRoute,
    private _httpService: HttpService
  ) { }

  ngOnInit() {
    this.getAllPets()
  }
  getAllPets(){
    let observable = this._httpService.getAllPetsSRV()
    observable.subscribe(data => {
      this.allPets = data["pets"] 
    })
  }
}
