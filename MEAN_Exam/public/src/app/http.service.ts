import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'

@Injectable({
  providedIn: 'root'
})
export class HttpService {

  constructor( private _http: HttpClient) { }

  createPetSRV(newPet){
    return this._http.post('/app/pets/create',newPet)
  }
  getAllPetsSRV(){
    return this._http.get('/app/pets/index')
  }
  showPetSRV(petId){
    return this._http.get("/app/pets/"+petId.id+"/show")
  }
  updatePetSRV(updatePet){
    return this._http.post("/app/pets/update", updatePet)
  }
  removePetSRV(petId){
    return this._http.delete("/app/pets/"+petId+"/destroy")
  }
  addLikeSRV(petId){
    petId = {id: petId}
    return this._http.post("/app/pets/like", petId)
  }
}
