/**
* Vitesse.js
*
* @description :: TODO: You might write a short summary of how this model works and what it represents here.
* @docs        :: http://sailsjs.org/#!documentation/models
*/

module.exports = {

  attributes: {
    vitesse : { type: 'integer', required: true },
    puissance : { type: 'integer', required: true },
    distance : { type: 'integer', required: true },
    accuracy : { type: 'integer', required: true },
    score : { type: 'integer', required: true },
  }
};

