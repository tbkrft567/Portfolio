console.log('****MODELS****')
var mongoose = require('mongoose')
//var uniqueValidator = require('mongoose-unique-validator')
const PetSchema = new mongoose.Schema(
   {
      name: {type: String, minlength: [3, "Sry, name must be 3 chars"]},
      type: {type: String, minlength: [3, "Sry, animal type must be 3 chars"]},
      desc: {type: String, minlength: [3, "Sry, description must be 3 chars"]},
      skillOne: String,
      skillTwo: String,
      skillThree: String,
      likes: {type: Number, default: 0},
   })
//UserSchema.plugin(uniqueValidator, { message: "This item must be UNIQUE*/*/*/*/*/" })
const Pet = mongoose.model('Pet', PetSchema);
module.exports = Pet