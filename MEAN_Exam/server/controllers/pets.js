console.log('****CONTROLLERS****')
var Pet = require('../model/pet.js')
module.exports = {
   index: (req, res) => {
      console.log('***CONTROLLER-index***')
      //index - all Pets
      Pet.find().sort({ type: -1 })
         .then(allPets => {
            res.json({ pets: allPets })
         })
         .catch(err => { res.json(err) })
   },
   show: (req, res) => {
      console.log('***CONTROLLER-show***')
      petId = req.params.petId
      Pet.findOne({_id: petId})
         .then(pet => {
            res.json(pet)
         })
         .catch(err => res.json(err))
   },
   create: (req, res) => {
      console.log('***CONTROLLER-create***')
      petName = req.body.name
      newPet = req.body
      console.log(petName)
      Pet.find({ name: petName })
         .then(petFound => {
            console.log(petFound)
            if(petFound.length > 0){

               return Promise.reject({errorUnique: 'Already Chose! Please select a different pet name'})
            }
            else{
               return Pet.create(newPet)
            }
         })
         .then(petConfirm => res.json(petConfirm))
         .catch(err => res.json(err))
   },
   edit: (req, res) => {
      console.log('***CONTROLLER-edit***')

   },
   update: (req, res) => {
      console.log('***CONTROLLER-update***')
      petId = req.body._id
      petName = req.body.name
      pet = req.body
      Pet.find()
      .then(petFound => {
         uniqueTest = 
            petFound[0]["_id"] != pet._id 
         && petFound[0]["name"] == pet.name  
         && petFound.length > 0
         if( uniqueTest ){
            return Promise.reject({errorUnique: 'Already Chose! Please select a different pet name'})
         }
         else{
            Pet.update({_id: petId}, {$set: 
               {name: petName, 
                  type: pet.type, 
                  desc: pet.desc, 
                  skillOne: pet.skillOne, 
                  skillTwo: pet.skillTwo, 
                  skillThree: pet.skillThree}}, 
               {runValidators: true})
               .then(petConfirm => res.json(petConfirm))
               .catch(err => res.json(err))
            }})
            .catch(err => { res.json(err)})
   },
   destroy: (req, res) => {
      console.log('***CONTROLLER-destroy***')
      petId = req.params.petId
      Pet.remove({_id: petId})
         .then(petConfirm => {
            res.json(petConfirm)
         })
         .catch(err => res.json(err))
   },
   like: (req, res) => {
      console.log('***CONTROLLER-like***')
      petId = req.body.id
      Pet.findOne({_id: petId})
         .then(pet =>{
            newLike = pet.likes+1
            console.log(newLike)
            Pet.update({ _id: pet._id }, {$set: {likes: newLike}})
               .then(petVoteConfirm => {
                  console.log(petVoteConfirm)
               })
               .catch(err => res.json(err))
         })
         .catch(err => {res.json(err)})
   },
}
