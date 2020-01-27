console.log('****ROUTES****')
const pets = require('../controllers/Pets.js')
const path = require('path')
module.exports = function(app){
   app.get('/app/pets/index', (req, res) => {
      console.log('***ROUTE-index***')
      pets.index(req, res)
   })
   app.get('/app/pets/:petId/show', (req, res) => {
      console.log('***ROUTE-show***')
      pets.show(req, res)
   })
   app.post('/app/pets/create', (req, res) => {
      console.log('***ROUTE-create***')
      pets.create(req, res)
   })
   app.get('/app/pets/edit', (req, res) => {
      console.log('***ROUTE-edit***')
      pets.edit(req, res)
   })
   app.post('/app/pets/update', (req, res) => {
      console.log('***ROUTE-update***')
      pets.update(req, res)
   })
   app.delete('/app/pets/:petId/destroy', (req, res) => {
      console.log('***ROUTE-destroy***')
      pets.destroy(req, res)
   })
   app.post('/app/pets/like', (req, res) => {
      console.log('***ROUTE-like***')
      pets.like(req, res)
   })
   app.all("*", (req,res,next) => { 
      console.log('***ROUTE-catchAll***')
      res.sendFile(path.resolve("./public/dist/public/index.html")) 
   })
}