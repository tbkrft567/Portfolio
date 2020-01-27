import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { HttpService } from 'src/app/http.service';

@Component({
  selector: 'app-new',
  templateUrl: './new.component.html',
  styleUrls: ['./new.component.css']
})

export class NewComponent implements OnInit {
  newPet: {}
  error: {}
  validationError: {}

  constructor(
      private _router: Router,
      private _route: ActivatedRoute,
      private _httpService: HttpService
  ) { }

  ngOnInit() {
    this.newPet = { name: "", type: "", desc: "", skillOne: "", skillTwo: "", skillThree: "" }
  }
  createPet(){
    let observable = this._httpService.createPetSRV(this.newPet)
    observable.subscribe(data => {
      if("errorUnique" in data){
        this.error = data
        this.validationError = undefined
      }
      else{
        console.log(data)
        if("errors" in data){
          console.log("Error Found")
          this.error = undefined
          this.validationError = data["errors"]
        }
        else{
          console.log("Pet Updated!")
          // this.newPet = { name: "", type: "", desc: "", skillOne: "", skillTwo: "", skillThree: "" }
          this.goToIndex()
        }
      }
    })
  }
  goToIndex(){
    this._router.navigate(['/pets','index'])
  }
}
