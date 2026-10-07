let taillepopudépart = 10;
let popu = [];

if(modetest == true){
	taillepopudépart = 2;
}

let chanceautoséléction = 1/2; // 1/3;

let tauxdemutation = 0.05;

let listeindexstat = [];

let mort = (indexsmort,population) => {
	// print("mort");

	//tauxdemutation = 250/popu[indexmort].fitness;
	// tauxdemutation = 0.01;
	
	let sommefitness = calcsommefitness(population); // calcule la meilleure fitness
	// print(sommefitness)

	// liste des index de guerrier et de leurs chances d'etre choisis
	let listeabaise = calclisteabaise(sommefitness,population);
	// print(listeabaise)

	let nouveau = reproduis(listeabaise, population, indexsmort);
	// print(nouveau)

	let nouveaumuté = mutation(nouveau);
	// print(nouveaumuté)

	population[indexsmort[0]][indexsmort[1]] = nouveaumuté;

	return population

}

let calcsommefitness = (liste) => { // nouvelle maniere d'écrire une fonction en ES6

	let sommefitness = 0;

	for(let i = 0; i < liste.length; i++){
		for(let j = 0; j < liste[i].length; j++){ // calcule la fitness max
			sommefitness += liste[i][j].fitness;
		}
	}

	return sommefitness
}

function calclisteabaise(sommefitness,population){
	let listeabaise = [];

	for(let i = 0; i < population.length; i++){
		for(let j = 0; j < population[i].length; j++){
			listeabaise.push([[i,j],population[i][j].fitness/sommefitness]);
		}
	}
	return listeabaise
}

function reproduis(listeabaise, listepopu, indexsmort) {

	let Pe;

	if(random() < chanceautoséléction){
		Pe = new guerrier(listepopu[indexsmort[0]][indexsmort[1]].npopu);
		index = calcavecproba(listeabaise);
		Pe.ADN = listepopu[index[0]][index[1]].ADN
		// print("auto")
	} else {
		let Ps = calc2parents(listeabaise);
		Pe = fusion(listepopu,Ps[0],Ps[1],listepopu[indexsmort[0]][indexsmort[1]].npopu);
		// print("pète sa raceeeeee");
	}
	return Pe
}

function calc2parents(listeabaise){
	
	indexa = calcavecproba(listeabaise);
	indexb = calcavecproba(listeabaise);

	let indexs = [indexa,indexb];

	return indexs;
}

function calcavecproba(listeabaise){
	let nbrandom = random();

	let somme = 0;

	let index = null;

	for(let i = 0;i < listeabaise.length;i++){ // pour chaque popu

		if(somme + listeabaise[i][1] < nbrandom){
			somme = somme + listeabaise[i][1];
		} else {// elle s'est fait élir
			index = listeabaise[i][0];
			break;
		}
	}
	if(index == null)index = listeabaise[listeabaise.length - 1][0];

	ajouteruneséléction(index);

	return index
}

function fusion(liste, indexa, indexb, npopumort){

	let Parenta = liste[indexa[0]][indexa[1]];
	let Parentb = liste[indexb[0]][indexb[1]];

	let Enfant = new guerrier(npopumort);
 
	// floor(random(0,Enfant.ADN.neurones.length));
	//let nbrandom = Enfant.ADN.neurones.length / 2;
	let nbrandom = 0;
	for(let i = 0; i < Enfant.ADN.nbneurones.length;i++){
		nbrandom += Enfant.ADN.nbneurones[i];
	}

	nbrandom = random(0,nbrandom - 1);

	let étape = 0;
	for(let i = 0;i < Enfant.ADN.neurones.length;i++){
		for(let j = 0;j < Enfant.ADN.neurones[i].length;j++){ // met chaques neurones
			if(étape < nbrandom){
				Enfant.ADN.neurones[i][j] = Parenta.ADN.neurones[i][j];
			} else {
				Enfant.ADN.neurones[i][j] = Parentb.ADN.neurones[i][j];
			}
			étape++;
		}
	}
	étape = Enfant.ADN.neurones[0].length;

	for(let i = 1; i < Enfant.ADN.neurones.length; i++) {
		for(let j = 0; j < Enfant.ADN.neurones[i].length;j++){ // chaques connections ( pour chaques neurones apres)
			for(let k = 0; k < Enfant.ADN.neurones[i][j].nbavant;k++){
				if(étape < nbrandom){
					Enfant.ADN.neurones[i - 1][k].connections[j] = Parenta.ADN.neurones[i - 1][k].connections[j];
				} else {
					Enfant.ADN.neurones[i - 1][k].connections[j] = Parentb.ADN.neurones[i - 1][k].connections[j];
				}
			}
			étape++;
		}
	}

	return Enfant
}

function mutation(individu){ // mutation a faire
	for (let i = 0; i < individu.ADN.neurones.length; i++){
		for (let j = 0; j < individu.ADN.neurones[i].length; j++){
			for(let k = 0;k < individu.ADN.neurones[i][j].connections.length;k++){
				if(random() < tauxdemutation){
					individu.ADN.neurones[i][j].connections[k] = random(-1,1);
				}
			}
		}	
	}
	return individu
}