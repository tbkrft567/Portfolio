import { Component, OnInit } from '@angular/core';
import { Router, Params, ActivatedRoute } from '@angular/router';
import { HttpService } from 'src/app/http.service';

@Component({
  selector: 'app-show',
  templateUrl: './show.component.html',
  styleUrls: ['./show.component.css']
})
export class ShowComponent implements OnInit {

  petId: {};
  pet: {};
  liked: boolean;

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
      this.liked = false
  }
  showPet(petId){
    let observable = this._httpService.showPetSRV(petId)
    observable.subscribe(data => {
      console.log(data)
      this.pet = data
    })
  }
  removePet(petId){
    this.petId = petId
    let observable = this._httpService.removePetSRV(petId)
    observable.subscribe(data => {
      console.log(data)
      this.goToIndex()
    })
  }
  addLike(petId){
    this.liked = true
    this.petId = petId
    console.log(petId, this.petId)
    let observable = this._httpService.addLikeSRV(this.petId)
    observable.subscribe(data => {
      console.log(data)
    })
    this.petId = {id: this.petId}
    this.showPet(this.petId)
  }
  goToIndex(){
    this._router.navigate(['/pets','index'])
  }
}
