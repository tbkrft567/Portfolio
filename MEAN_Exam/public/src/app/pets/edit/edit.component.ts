import { Component, OnInit } from '@angular/core';
import { Router, Params, ActivatedRoute } from '@angular/router';
import { HttpService } from 'src/app/http.service';

@Component({
  selector: 'app-edit',
  templateUrl: './edit.component.html',
  styleUrls: ['./edit.component.css']
})
export class EditComponent implements OnInit {

  petId: {}
  pet: {}
  updatePetObj: {}
  error: {}
  validationError: {}
  constructor(
    private _router: Router,
    private _route: ActivatedRoute,
    private _httpService: HttpService
  ) { }

  ngOnInit() {
    this._route.params.subscribe((params: Params) => {
      this.petId = { id: params["petId"] }
    })
    this.showPet(this.petId)
}
showPet(petId){
  let observable = this._httpService.showPetSRV(petId)
  observable.subscribe(data => {
    this.pet = data
  })
}
updatePet(){
  let observable = this._httpService.updatePetSRV(this.pet)
  observable.subscribe(data => {
    if("errorUnique" in data){
      this.error = data
      this.validationError = undefined
    }
    else{
      // console.log(data)
      if("errors" in data){
        console.log("Error Found")
        this.error = undefined
        this.validationError = data["errors"]
      }
      else{
        console.log("Pet Updated!")
        // this.newPet = { name: "", type: "", desc: "", skillOne: "", skillTwo: "", skillThree: "" }
        this.petId = {id: this.pet["_id"]}
        this.goToDetail(this.petId)
      }
    }
  })
}
goToDetail(petId){
  this._router.navigate(['/pets',petId.id,'show'])
}
}
